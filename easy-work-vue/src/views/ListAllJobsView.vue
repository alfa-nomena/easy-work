<template>
    <section class="jobs">
        <div class="container">
            <div class="row heading">
                <h2>All jobs</h2>
                <p>Find your dream job in these jobs</p>
            </div>
            <ListJobComponent :jobs="jobs"/>
            <nav>
                <ul class="pagination">
                    <li v-if="previous" class="page-item" @click.prevent="get_jobs(previous)">
                        <a class="page-link" :href="previous">Previous</a>
                    </li>
                    <li v-if="next" class="page-item" @click.prevent="get_jobs(next)">
                        <a class="page-link" :href="next">Next</a>
                    </li>
                </ul>
            </nav>
        </div>
    </section>
</template>

<script setup>
import ListJobComponent from '../components/JobsComponent/ListJobComponent.vue'
</script>
<script>
export default {
    name: 'HomeView',
    components: [ ListJobComponent],
    data(){
        return {
            jobs:[],
            next: null,
            previous: null
        }
    },
    async mounted(){
        this.get_jobs('http://127.0.0.1:8000/api/jobs')
    },
    methods: {
        async get_jobs(url){
            const data = await (await fetch(url)).json()
            this.jobs = data.results
            this.next = data.next
            this.previous = data.previous
        }
    }
}
</script>
<style scoped>
nav{
    display: flex;
    justify-content: space-around;
}
</style>