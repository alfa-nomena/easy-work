<script setup>
  import HeaderComponent from './components/HeaderComponent.vue'
  import JobListComponent from './components/Jobs/JobListComponent.vue';
</script>
<template>
  <div>
    <HeaderComponent/>
    <router-view></router-view>
  </div>
</template>

<style lang="scss">

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
<script>
  export default {
    name: 'App',
    components: [HeaderComponent, JobListComponent],
  }
</script>
