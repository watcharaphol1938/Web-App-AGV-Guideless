<template>
  <div class="home">
    <!-- <img alt="Vue logo" src="../assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/> -->

    <!-- home -->
    <!-- <p ref="p">My name is {{ name }} and my age is {{ age }}</p> -->
    <!-- <p>My name is {{ name }} and my age is {{ age }}</p>
    <button @click="handleClick">click here</button>
    <button @click="age++">add 1 to age</button>
    <input type="text" v-model="name"> -->

    <!-- <h1>Home</h1>
    <h2>Refs</h2>
    <p>{{ ninjaOne.name }} - {{ ninjaOne.age }}</p>
    <button @click="updateNinjaOne">Update ninja one</button>

    <p>{{ ninjaTwo.name }} - {{ ninjaTwo.age }}</p>
    <button @click="updateNinjaTwo">Update ninja two</button> -->

    <!-- <h1>Home</h1>
    <p>{{ name }}</p> -->

    <!-- <h1>Home</h1>
    <input type="text" v-model="search">
    <p>search : {{ search }}</p> -->
    <!-- <div v-for="name in names" :key="name">{{ name }}</div> -->
    <!-- <div v-for="name in matchingNames" :key="name">{{ name }}</div>
    <button @click="handleClick">stop watching</button> -->

    <!-- <h1>Home</h1> -->
    <!-- <PostList :posts="posts" /> -->
    <!-- <PostList v-if="showPosts" :posts="posts" />
    <button @click="showPosts = !showPosts">toggle posts</button>
    <button @click="posts.pop()">delete a post</button> -->

    <h1>Home</h1>
    <div v-if="error">{{ error }}</div>
    <div v-if="posts.length">
      <PostList :posts="posts" />
    </div>
    <div v-else>Loading...</div>
    <!-- <PostList :posts="posts" /> -->
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'
// import { ref, reactive } from 'vue'
import PostList from '../components/PostList.vue'
import getPosts from '../composables/getPosts'

export default {
  name: "HomeView",
  components: {
    // HelloWorld
    PostList
  },
  setup() {
    // console.log('setup')
    // console.log(this)

    // const p = ref(null)
    // const p = ref("test");
    // console.log(p, p.value);
    // let name = "Frodo"
    // let age = 25
    // let name = ref("Frodo")
    // let age = ref(25)

    // const handleClick = () => {
    //   // console.log('click here')
    //   // console.log(p, p.value);
    //   // p.value.classList.add("test");
    //   // p.value.textContent = "hello";
    //   name.value = 'Sam'
    //   age.value = 30
    // }
    // return { name, age, handleClick, p }
    // return { name, age, handleClick}

    // const ninjaOne = ref({ name: 'Gandaft', age: 45 })
    // const ninjaTwo = reactive({ name: 'Pippins', age: 20 })

    // const updateNinjaOne = () => {
    //   ninjaOne.value.age = 88
    // }

    // const updateNinjaTwo = () => {
    //   ninjaTwo.age = 12
    // }
    // return { ninjaOne, updateNinjaOne, ninjaTwo, updateNinjaTwo }

    // const name = computed(() => {
    //   return 'Gimly'
    // })
    // return { name }

    // const search = ref('')
    // const names = ref(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])

    // const stopWatch = watch(search, () => {
    //   console.log('watch function ran')
    // })

    // const stopWatchEffect = watchEffect(() => {
    //   console.log('watchEffect function ran', search.value)
    // })

    // const matchingNames = computed(() => {
    //   return names.value.filter((name) => name.includes(search.value))
    // })

    // const handleClick = () => {
    //   stopWatch()
    //   stopWatchEffect()
    // }
    // return { names , search, matchingNames, handleClick }

    // const posts = ref([
    //   // { title: 'Eufa champions league', body: 'semi-final', id: 1 },
    //   // { title: 'Eufa Europa league', body: 'quater-final', id: 2 },
    // ])
    // const error = ref(null)
    // const load = async () => {
    //   try {
    //     let data = await fetch('http://localhost:3000/posts')
    //     // console.log(data)
    //     if (!data.ok) {
    //       throw Error('no data available')
    //     }
    //     posts.value = await data.json()
    //   } catch (err) {
    //     error.value = err.message
    //     console.log(error.value)
    //   }
    // }
    // load()

    // const showPosts = ref(true)
    // return { posts, showPosts }

    const { posts, error, load } = getPosts()
    load()

    return { posts, error }
  }
  // data() {
  //   return {
  //     score: 5
  //   }
  // }
  // created() {
  //   console.log('created')
  // },
  // mounted() {
  //   console.log('mounted')
  // }
  // data() {
  //   return {
  //     age: 40
  //   }
  // }
};
</script>
