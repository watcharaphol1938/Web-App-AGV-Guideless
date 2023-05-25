<template>
  <div>
    <div class="container mt-4">
      <form @submit.prevent="updateArticle">
        <input
          type="text"
          class="form-control"
          placeholder="please enter title"
          v-model="title"
        />
        <br />
        <textarea
          rows="10"
          class="form-control"
          placeholder="please enter body"
          v-model="body"
        ></textarea>
        <button class="btn btn-success mt-4">Update Article</button>
      </form>
      <div
        v-if="error"
        class="alert alert-warning alert-dismissible fade show mt-5"
        role="alert"
      >
        <strong>{{ error }}</strong>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    id: {
      type: [Number, String],
      required: true,
    },
  },
  data() {
    return {
      title: null,
      body: null,
      error: null,
    };
  },
  methods: {
    updateArticle() {
      if (!this.title || !this.body) {
        this.error = "Please add all fields";
      } else {
        fetch(`http://127.0.0.1:5000/update/${this.id}/`, {
          method: "PUT",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ title: this.title, body: this.body }),
        })
          .then((resp) => resp.json())
          .then(() => {
            this.$router.push({ name: "home" });
          })
          .catch((error) => {
            console.log(error);
          });
      }
    },
  },
  beforeRouteEnter(to, from, next) {
    if (to.params.id !== undefined) {
      fetch(`http://127.0.0.1:5000/get/${to.params.id}/`, {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      })
        .then((resp) => resp.json())
        .then((data) => {
          return next((vm) => ((vm.title = data.title, vm.body = data.body)));
        })
        .catch((error) => {
          console.log(error);
        });
    } else {
      return next();
    }
  },
};
</script>

<style></style>
