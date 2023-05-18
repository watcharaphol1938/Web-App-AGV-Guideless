<template>
  <div>
    <div class="container mt-5">
      <h2>{{ article.title }}</h2>
      <p class="mt-3">{{ article.body }}</p>
      <h6>Date : {{ article.date }}</h6>

      <router-link :to="{name:'articleedit', params:{id:article.id}}" class="btn btn-success mt-3">Update</router-link>

      <button class="btn btn-danger mx-3 mt-3" @click="deleteArticle">Delete</button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      article: {},
    };
  },
  props: {
    id: {
      type: [Number, String],
      required: true,
    },
  },
  methods: {
    deleteArticle() {
      fetch(`http://127.0.0.1:5000/delete/${this.id}/`, {
        method: "DELETE",
        headers: {
          "Content-Type": "application/json",
        },
      })
        .then(() => {
          this.$router.push({name: 'home'})
        })
        .catch((error) => {
          console.log(error);
        });
    },
    getArticleData() {
      fetch(`http://127.0.0.1:5000/get/${this.id}/`, {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      })
        .then((resp) => resp.json())
        .then((data) => {
          // console.log(data);
          //   this.articles.push(...data);
          this.article = data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  created() {
    this.getArticleData();
  },
};
</script>

<style>
</style>