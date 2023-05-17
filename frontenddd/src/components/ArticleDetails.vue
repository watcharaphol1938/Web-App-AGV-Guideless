<template>
  <div>
    <div class="container mt-5">
      <h2>{{ article.title }}</h2>
      <p class="mt-3">{{ article.body }}</p>
      <h6>Date : {{ article.date }}</h6>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      article: {}
    }
  },
  props: {
    id: {
      type: [Number, String],
      required: true
    }
  },
  methods: {
    getArticleData() {
      fetch(`http://127.0.0.1:5000/get/${this.id}/`, {
        methods: "GET",
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
        .catch(error => {
          console.log(error);
        });
    }
  },
  created() {
    this.getArticleData();
  }
};
</script>

<style>
</style>