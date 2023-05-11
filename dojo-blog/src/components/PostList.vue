<template>
  <div>
    <div class="post-list">
        <div v-for="post in posts" :key="post.id">
            <!-- <h3>{{ post.title }}</h3> -->
            <SinglePost :post="post"/>
        </div>
    </div>
  </div>
</template>

<script>
import { onMounted, onUnmounted, onUpdated } from 'vue'
import SinglePost from '../components/SinglePost.vue'
export default {
    props: ['posts'],
    components: { SinglePost },
    setup(props) {
        // console.log(prop.posts)
        onMounted(() => console.log('component mounted'))
        onUnmounted(() => console.log('component unmounted'))
        onUpdated(() => console.log('component updated'))
    },
    mounted() {
        console.log('mounted using options api')
    }
}
</script>

<style>

</style>