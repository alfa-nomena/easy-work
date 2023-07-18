<script setup>
  import HeaderComponent from './components/HeaderComponent.vue'
</script>
<template>
  <HeaderComponent/>
  <JobListComponentVue/>
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
import JobListComponentVue from './components/JobListComponent.vue'
  export default {
    name: 'App',
    components: [HeaderComponent, JobListComponentVue],
    data(){
      return {
        candidates: []
      }
    }
  }
</script>
