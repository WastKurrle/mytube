<script setup lang="ts">
  import { ref } from "vue";
  import { useCommentStore } from "@/stores/commentStore";
  import  { useAuthenticatedStore } from "@/stores/authenticated";
  import type { Comment } from "@/assets/interfaces";

  const props = defineProps(['video'])

  // stores
  const commentStore = useCommentStore()
  const authenticatedStore = useAuthenticatedStore()

  const video = ref(props.video)

  const commentMessage = ref('')
  const postComment = async () => {
      const comment:Comment = {
        message:commentMessage.value,
        video:video.value.id,
        user:authenticatedStore.user.id
      }

      const postedComment = await commentStore.postComment(comment)
      commentMessage.value = ''
      await commentStore.getPostedComment(postedComment.id, video.value.id)
  }
</script>

<template>
  <div class="mx-auto mt-3">
    <p class="text-white font-light mb-3">{{ video.commentsCount }} comments</p>
    <form @submit.prevent="postComment" v-if="authenticatedStore.authenticated">
      <div class="relative">
        <textarea placeholder="Add Comment..." class="bg-input text-white w-full
        resize-none focus:outline-none
        border-t-0 border-r-0 border-l-0 border-b-2
        border-gray-300 focus:border-blue-500 py-2 pl-2" v-model="commentMessage"
        required
        >
        </textarea>
        <div class="absolute bottom-0 left-0 h-1 bg-blue-500"></div>
      </div>
      <button type="submit" class="bg-blue-500 text-white rounded-lg mt-2 px-4 py-2 hover:bg-blue-600">Comment</button>
    </form>
  </div>

</template>

<style scoped>
  .bg-input {
    background-color: #0F0F0F;
  }
</style>