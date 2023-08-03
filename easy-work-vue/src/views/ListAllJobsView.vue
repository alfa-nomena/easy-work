<template>
    <section class="jobs">
        <div class="container">
            <div class="row heading">
                <h2>All jobs</h2>
                <p>Find your dream job in these jobs</p>
            </div>
            <ListJobComponent :jobs="jobs"/>
            <PaginationComponent :next="next" @click_next="get_jobs(next)"/>
        </div>
    </section>
</template>

<script setup>
import ListJobComponent from '../components/JobsComponent/ListJobComponent.vue'
import PaginationComponent from '@/components/layouts/PaginationComponent.vue';
</script>
<script>
export default {
    name: 'HomeView',
    components: [ ListJobComponent, PaginationComponent],
    data(){
        return {
            jobs:[],
            next: null
        }
    },
    async mounted(){
        this.get_jobs('http://127.0.0.1:8000/api/jobs')
    },
    methods: {
        async get_jobs(url){
            url +=url.includes('?')?'&':'?'
            url += new URLSearchParams(this.$route.query)
            const data = await (await fetch(url)).json()
            this.jobs = this.jobs.concat(data.results)
            this.next = data.next
        },
    }
}
</script>
<style scoped>
nav{
    display: flex;
    justify-content: space-around;
}
</style>