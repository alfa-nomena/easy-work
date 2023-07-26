<script setup>
    import NavigationComponent from './components/layouts/NavigationComponent.vue';
    import FooterComponent from './components/layouts/FooterComponent.vue';
</script>
<template>
    <main>
        <NavigationComponent />
        <router-view></router-view>
        <FooterComponent />
    </main>
</template>
<script>
  export default {
    name: 'App',
    components: [NavigationComponent, FooterComponent]
  }
</script>