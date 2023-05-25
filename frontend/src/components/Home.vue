<template>
  <div>
    <!-- <h1>Home</h1> -->
    <div class="container mt-5">
      <div v-for="article in articles" :key="article.id">
      <!-- <h3>{{ article.title }}</h3>
      <p>{{ article.body }}</p>
      <p>{{ article.date }}</p> -->

      <router-link class="link-style" :to="{name: 'articledetails', params:{id:article.id}}">
        <h3>{{ article.title }}</h3>
        <hr/>
      </router-link>
    </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      articles: [],
    }
  },
  methods: {
    getArticles() {
      fetch('http://127.0.0.1:5000/get', {
        method:"GET",
        headers: {
          "Content-Type" : "application/json"
        }
      })
      .then(resp => resp.json())
      .then(data => {
        // console.log(data);
        this.articles.push(...data)
      })
      .catch(error => {
        console.log(error)
      })
    }
  },
  created() {
    this.getArticles()
  }
}
</script>

<style>
.link-style {
  font-weight: bold;
  color: black;
  text-decoration: none;
}
.link-style-hover {
  color: gray;
  text-decoration: none;
}
</style>