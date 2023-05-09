<template>
  <!-- <img alt="Vue logo" src="./assets/logo.png">
  <HelloWorld msg="Welcome to Your Vue.js App"/> -->

  <!-- <h1>Vue App</h1> -->

  <h1>{{ title }}</h1>
  <p>Welcome...</p>

  <teleport to=".modals" v-if="showModal">
    <!-- <Modal :header="header" :text="text" theme="sale" @close="toggleModal" /> -->
    <!-- <Modal theme="sale" @close="toggleModal"> -->
    <Modal theme="" @close="toggleModal">
      <template v-slot:links>
        <a href="#">sign up</a>
        <a href="#">more info</a>
      </template>
      <h1>Sign up for the Giveaway</h1>
      <p>content</p>
      <a href=""></a>
    </Modal>
  </teleport>

  <!-- <div v-if="showModal"> -->
    <!-- <Modal :header="header" :text="text" theme="sale" @close="toggleModal" /> -->
    <!-- <Modal theme="sale" @close="toggleModal"> -->
    <!-- <Modal theme="" @close="toggleModal">
      <template v-slot:links>
        <a href="#">sign up</a>
        <a href="#">more info</a>
      </template>
      <h1>Sign up for the Giveaway</h1>
      <p>content</p>
      <a href=""></a>
    </Modal>
  </div> -->

  <teleport to=".modals" v-if="showModalTwo">
    <!-- <Modal :header="header" :text="text" theme="sale" @close="toggleModal" /> -->
    <!-- <Modal theme="sale" @close="toggleModal"> -->
    <Modal @close="toggleModal">
      <h1>Sign up for newsletter</h1>
      <p>update!!!</p>
      <a href=""></a>
    </Modal>
  </teleport>

  <!-- <button @click="toggleModal">open modal</button> -->
  <button @click.shift="toggleModal">open modal (alt)</button>
  <button @click.shift="toggleModalTwo">open modal</button>

  <!-- <Modal header="Sign up for the Giveaway" text="content" /> -->
  <!-- <Modal header="['Meta', 4]" text="content" /> -->

  <!-- <input type="text" ref="name">
  <button @click="handleClick">click here</button> -->
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'

import Modal from "./components/Modal.vue";

export default {
  name: "App",
  components: {
    Modal,
  },

  // components: {
  //   HelloWorld
  // }

  data() {
    return {
      title: "Google",
      // header: 'Sign up for the Giveaway',
      // text: 'content',
      showModal: false,
      showModalTwo: false,
    };
    // },
    // methods: {
    //   handleClick() {
    //     console.log(this.$refs.name)
    //     this.$refs.name.classList.add('active')
    //     this.$refs.name.focus()
    //   }
  },
  methods: {
    toggleModal() {
      this.showModal = !this.showModal;
    },
    toggleModalTwo() {
      this.showModalTwo = !this.showModalTwo;
    },
  },
};
</script>

<style>
#app #modals{
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
h1 {
  border-bottom: 1px solid #ddd;
  display: inline-block;
  padding-bottom: 10px;
}
</style>
