<script setup>
  import HeaderComponent from './components/layouts/HeaderComponent.vue'
  import JobListComponent from './components/Jobs/JobListComponent.vue';
</script>
<template>
  <div>
    <HeaderComponent/>
    <router-view></router-view>
  </div>
</template>

<style lang="scss" scoped>

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
div{
  background: #ddd;
}
</style>
<script>
  export default {
    name: 'App',
    components: [
      HeaderComponent, 
      JobListComponent
    ],
  }
</script>
