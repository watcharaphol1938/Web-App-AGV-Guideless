<template>
  <div class="home">
    <!-- <img alt="Vue logo" src="../assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/> -->

    home
    <p>My name is {{ name }} and my age is {{ age }}</p>
    <button @click="handleClick">click here</button>
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'
import {ref} from 'vue'

export default {
  name: 'HomeView',
  // components: {
  //   // HelloWorld
  // }
  setup() {
    // console.log('setup')
    console.log(this)

    const p = ref(null)
    let name = 'Frodo'
    let age = 25

    const handleClick = () => {
      console.log('click here')
    }
    return {name, age, handleClick}
  },
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
}
</script>
