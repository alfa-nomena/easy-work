<template>
    	<BannerComponent />
		<CounterComponent />
        <section class="jobs">
            <div class="container">
                <ListLatestJobComponent />
                <router-link to="/jobs" class="btn brows-btn">Brows All Jobs</router-link>
            </div>
        </section>
        <section class="enterprises">
            <div class="container">
                <ListEnterprisePostingJobComponent />
                <router-link to="/enterprises" class="btn brows-btn">Browse All Enterprises</router-link>
            </div>
        </section>
</template>

<script setup>
    import CounterComponent from '../components/layouts/CounterComponent.vue'
    import BannerComponent from '../components/layouts/BannerComponent.vue'
    import ListLatestJobComponent from '../components/JobsComponent/ListLatestJobComponent.vue'
    import ListEnterprisePostingJobComponent from '../components/EnterprisesComponent/ListEnterprisePostingJobComponent.vue'
</script>
<script>
    export default {
        name: 'HomeView',
        components: [BannerComponent, ListLatestJobComponent, CounterComponent, ListEnterprisePostingJobComponent]
    }
</script>