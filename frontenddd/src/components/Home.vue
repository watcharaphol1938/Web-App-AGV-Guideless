<template>
  <h1>Home</h1>
</template>

<script>
export default {
  methods: {
    getArticles() {
      fetch('http://127.0.0.1:5000/get', {
        methods:"GET",
        headers: {
          "Content-Type" : "application/json"
        }
      })
      .then(resp => resp.json)
      .then(data => {
        console.log(data);
      })
      .catch(error => {
        console.log(error);
      })
    }
  },
  created() {
    this.getArticles()
  }
}
</script>

<style>

</style>