<template>
  <nav class="navbar navbar-expand-lg bg-body-tertiary">
    <div class="container">
      <!-- <a class="navbar-brand" href="#">Navbar</a> -->
      <!-- <router-link class="navbar-brand text-style" to="/">Flask and Vue</router-link> -->
      <img :src="picture" width="189" height="68">
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarNav"
        aria-controls="navbarNav"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav ms-auto">
          <li class="nav-item mx-2">
            <!-- <a class="nav-link active" aria-current="page" href="#">Home</a> -->
            <router-link class="btn" aria-current="page" to="/">Home</router-link>
          </li>
          <li class="nav-item mx-2">
            <!-- <a class="nav-link" href="#">Features</a> -->
            <router-link class="btn" to="/create">Create</router-link>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'Navbar',
  data() {
    return {
      picture: "https://th.bing.com/th/id/R.6df47b8ac32b46b15cc91f3d3eceea77?rik=23YbV2UZ1Fys0Q&riu=http%3a%2f%2fwww.densocorp-na.com%2fwp-content%2fthemes%2fsemantic%2fimages%2fdenso-logo.png&ehk=CNmR9%2fJhwqF9kdMKNeDurA1Tm%2fl9JiPb64pWZDj7CrE%3d&risl=&pid=ImgRaw&r=0",
    }
  }
};
</script>

<style>
.text-style {
  font-size: 30px !important;
  font-family: fantasy !important;
  color: brown !important;
}
.navbar {
  background: gray;
}
</style>
