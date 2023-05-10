<template>
  <!-- <img alt="Vue logo" src="./assets/logo.png">
  <HelloWorld msg="Welcome to Your Vue.js App"/> -->
  <h1>Reaction timer</h1>
  <button @click="start" :disabled="isPlaying">play</button>
  <Block v-if="isPlaying" :delay="delay" @end="endGame" />
  <!-- <p v-if="showResults">Reaction time: {{ score }} ms</p> -->
  <Results v-if="showResults" :score="score" />
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
import Block from './components/Block.vue'
import Results from './components/Results.vue'

export default {
  name: 'App',
  components: {
    // HelloWorld
    Block, Results
  },
  data() {
    return {
      isPlaying : false,
      delay : null,
      score: null,
      showResults: false
    }
  },
  methods: {
    start() {
      this.delay = 2000 + Math.random() * 5000
      this.isPlaying = true
      this.showResults = false
      // console.log(this.delay)
    },
    endGame(reactionTime) {
      this.score = reactionTime
      this.isPlaying = false
      this.showResults = true
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  /* color: #2c3e50; */
  color: #444;
  margin-top: 60px;
}
button {
  background: #0faf87;
  color: white;
  border: none;
  padding: 8px 16px;
  border-radius: 4px;
  font-size: 16px;
  letter-spacing: 1px;
  cursor: pointer;
  margin: 10px;
}
button[disabled] {
  opacity: 0.2;
  cursor: not-allowed;
}
</style>
