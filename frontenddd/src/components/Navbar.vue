<template>
  <nav class="navbar navbar-expand-lg bg-body-tertiary">
    <div class="container">
      <!-- <a class="navbar-brand" href="#">Navbar</a> -->
      <router-link class="navbar-brand text-style" to="/">Flask and Vue</router-link>
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
            <router-link class="btn btn-primary" aria-current="page" to="/">Home</router-link>
          </li>
          <li class="nav-item">
            <!-- <a class="nav-link" href="#">Features</a> -->
            <router-link class="btn btn-success" to="/create">Features</router-link>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
export default {};
</script>

<style>
.text-style {
  font-size: 30px !important;
  font-family: fantasy !important;
  color: brown !important;
}
</style>
