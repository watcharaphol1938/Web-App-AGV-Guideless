<template>
  <!-- <nav class="navbar">
    <div class="container">
      <img :src="picture" width="189" height="68">
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item">
            <router-link class="btn" aria-current="page" to="/">Home</router-link>
          </li>
          <li class="nav-item">
            <router-link class="btn" to="/create">Create</router-link>
          </li>
        </ul>
      </div>
    </div>
  </nav> -->
  <div>
    <nav class="navbar">
      <!-- 21 -->
      <img :src="picture" width="100" height="40">
      <img class="icon" :src="icon" width="20" height="20">
      <!-- <ul class="nav">
        <li>
          <router-link class="btn" to="/">Dashboard</router-link>
        </li>
        <li class="nav">
          <router-link class="btn" to="/">Analytics</router-link>
        </li>
        <li class="nav">
          <router-link class="btn" to="/">Report</router-link>
        </li>
        <li class="nav">
          <router-link class="btn" to="/">Alarm History</router-link>
        </li>
        <li class="nav">
          <router-link class="btn" to="/">Setting</router-link>
        </li>
        <li class="nav">
          <router-link class="btn" to="/">User</router-link>
        </li>
      </ul> -->
    </nav>
  </div>
</template>

<script>
export default {
  name: 'Navbar',
  data() {
    return {
      picture: "https://th.bing.com/th/id/R.6df47b8ac32b46b15cc91f3d3eceea77?rik=23YbV2UZ1Fys0Q&riu=http%3a%2f%2fwww.densocorp-na.com%2fwp-content%2fthemes%2fsemantic%2fimages%2fdenso-logo.png&ehk=CNmR9%2fJhwqF9kdMKNeDurA1Tm%2fl9JiPb64pWZDj7CrE%3d&risl=&pid=ImgRaw&r=0",
      icon: "https://www.pinclipart.com/picdir/big/181-1812493_menu-white-menu-button-png-clipart.png"
    }
  }
};
</script>

<style>
img {
  margin-bottom: 5px;
  margin-left: 25px;
  background: lightgray;
}
.icon {
  margin-right: 1100px;
}
.navbar {
  background: lightgray;
}
.nav {
  margin-left: 500px;
  background-color: lightgray;
  color: black;
  border-radius: 8px solid #555555;
}
</style>
