<script setup lang="ts">
  import { ref } from 'vue'
  import { useCommentStore } from "@/stores/commentStore";

  // stores
  const commentStore = useCommentStore()

  const closeButton = ref()

  const submitDelete = async () => {
    await commentStore.deleteComment()
    removeComment()
    closeButton.value.click()
  }

  const removeComment = () => {
    const index = commentStore.comments.findIndex(comment => comment.id === commentStore.selectedComment.id)
    commentStore.comments.splice(index, 1)
  }

</script>

<template>
  <div>
    <!-- Modal -->
    <div
        data-te-modal-init
        class="fixed top-0 left-0 z-[1055] hidden h-full w-full overflow-y-auto overflow-x-hidden outline-none"
        id="deleteComment"
        data-te-backdrop="static"
        data-te-keyboard="false"
        tabindex="-1"
        aria-labelledby="staticBackdropLabel"
        aria-hidden="true">
      <div
          data-te-modal-dialog-ref
          class="pointer-events-none relative w-auto translate-y-[-50px] opacity-0 transition-all duration-300 ease-in-out min-[576px]:mx-auto min-[576px]:mt-7 min-[576px]:max-w-[500px]">
        <div
            class="min-[576px]:shadow-[0_0.5rem_1rem_rgba(#000, 0.15)] pointer-events-auto relative flex w-full flex-col rounded-md border-none bg-white bg-clip-padding text-current shadow-lg outline-none dark:bg-neutral-600">
          <div
              class="flex flex-shrink-0 items-center justify-between rounded-t-md border-b-2 border-neutral-100 border-opacity-100 p-4 dark:border-opacity-50">
            <h5
                class="text-xl font-medium leading-normal text-neutral-800 dark:text-neutral-200"
                id="exampleModalLabel">
              Delete Comment
            </h5>
            <button
                type="button"
                class="box-content rounded-none border-none hover:no-underline hover:opacity-75 focus:opacity-100 focus:shadow-none focus:outline-none"
                data-te-modal-dismiss
                aria-label="Close">
              <svg
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke-width="1.5"
                  stroke="currentColor"
                  class="h-6 w-6">
                <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    d="M6 18L18 6M6 6l12 12" />
              </svg>
            </button>
          </div>
          <div data-te-modal-body-ref class="relative p-4" v-if="commentStore.selectedComment != undefined">
            <div class="text-center">
              <font-awesome-icon icon="fa-solid fa-triangle-exclamation" class="text-3xl mb-3"/>

              <p>Do you want to delete the comment?</p>

              <div class="mt-3">
                <button
                    type="button"
                    class="bg-red-700 p-3 rounded-md w-28 hover:bg-red-800 mr-3"
                    @click="submitDelete"
                >Delete</button>
                <button
                    type="button"
                    class="bg-gray-700 p-3 rounded-md w-28 hover:bg-gray-800 mr-3"
                    data-te-modal-dismiss
                    data-te-ripple-init
                    data-te-ripple-color="light"
                >Cancel</button>
              </div>
            </div>
          </div>
          <div
              class="flex flex-shrink-0 flex-wrap items-center justify-end rounded-b-md border-t-2 border-neutral-100 border-opacity-100 p-4 dark:border-opacity-50">
            <button
                type="button"
                class="inline-block rounded bg-primary-100 px-6 pt-2.5 pb-2 text-xs font-medium uppercase leading-normal text-primary-700 transition duration-150 ease-in-out hover:bg-primary-accent-100 focus:bg-primary-accent-100 focus:outline-none focus:ring-0 active:bg-primary-accent-200"
                data-te-modal-dismiss
                data-te-ripple-init
                data-te-ripple-color="light"
                ref="closeButton"
            >
              Close
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>

</style>