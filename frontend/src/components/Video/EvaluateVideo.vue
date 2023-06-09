<script setup lang="ts">
    import { ref, onMounted, computed } from 'vue';
    import { useAuthenticatedStore } from '@/stores/authenticated';
    import { useEvaluateStore } from '@/stores/evaluateStore';
    import router from "@/router";

    const props = defineProps(['video'])

    // stores
    const authenticatedStore = useAuthenticatedStore()
    const evaluateStore = useEvaluateStore()

    const video = ref(props.video)

    const userEvaluateStatus = ref()
    const videoEvaluate = ref({
        likes: 0,
        dislikes: 0
    })


    // returns the fontawesome classes for the like button depends on the evaluation status (like, dislike)
    const likeIcon = computed(() => {
        if (userEvaluateStatus.value === '0') {
            return ['fas', 'thumbs-up']; // fa-solid thumbs-up icon
        } else {
            return ['far', 'thumbs-up']; // fa-regular thumbs-up icon
        }
    });

    // returns the fontawesome classes for the dislike button depends on the evaluation status (like, dislike)
    const dislikeIcon = computed(() => {
        if (userEvaluateStatus.value === '1') {
            return ['fas', 'thumbs-down']; // fa-solid thumbs-down icon
        } else {
            return ['far', 'thumbs-down']; // fa-regular thumbs-down icon
        }
    });

    // Handles the like button click if the user is authenticated
    const likeVideo = async () => {
        if (authenticatedStore.authenticated) {
          await evaluateStore.likeVideo(String(video.value.id), userEvaluateStatus.value)
          userEvaluateStatus.value = await evaluateStore.checkUserVideoEvaluation(String(video.value.id))

          await evaluationCount()
        } else {
          router.push({name: 'login'})
        }
    }

    // Handles the dislike button click if the user is authenticated
    const dislikeVideo = async () => {
        if (authenticatedStore.authenticated) {
          await evaluateStore.dislikeVideo(String(video.value.id), userEvaluateStatus.value)
          userEvaluateStatus.value = await evaluateStore.checkUserVideoEvaluation(String(video.value.id))

          await evaluationCount()
        } else {
          router.push({name: 'login'})
        }
    }

    // counts the likes and dislikes from the video
    const evaluationCount = async () => {
        const result = await evaluateStore.getVideoEvaluationCount(video.value.id)

        videoEvaluate.value.likes = result.likes
        videoEvaluate.value.dislikes = result.dislikes
    }

    const loaded = ref(false)

    onMounted(async () => {
        if (authenticatedStore.authenticated) {
            userEvaluateStatus.value = await evaluateStore.checkUserVideoEvaluation(String(video.value.id))
        }

        await evaluationCount()
        loaded.value = true
    })
</script>

<template>
    <div v-if="loaded" class="mt-3">
        <div class="p-3 rounded-3xl button-bg w-56 layout-buttons md:w-64">
            <div>
                <button @click="likeVideo"><font-awesome-icon :icon="likeIcon" class="text-lg mr-3 md:text-2xl"/></button>
                <span class="text-sm md:text-lg">{{ videoEvaluate.likes }}</span>
            </div>
            <div>
                <button @click="dislikeVideo"><font-awesome-icon :icon="dislikeIcon" class="text-lg mr-3 md:text-2xl"/></button>
                <span class="text-sm md:text-lg">{{ videoEvaluate.dislikes }}</span>
            </div>
        </div>
    </div>
</template>

<style scoped>
    .button-bg {
        background-color: #3F3F3F;
    }

    .layout-buttons {
        display: flex;
        justify-content: space-between;
    }
</style>
