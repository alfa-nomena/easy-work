<template>
    <div class="row heading">
        <h2>Find Popular Jobs</h2>
        <p>Candidates that are being active lastely.</p>
    </div>
    <ListJobComponent :jobs="jobs" /> 
</template>
<script setup>
    import ListJobComponent from './ListJobComponent.vue'
</script>
<script>
    export default {
        name: 'ListLatestJobComponent',
        components: [ListJobComponent],
        data(){
            return {
                jobs:[]
            }
        },
        async mounted(){
            const data = await (await fetch('http://127.0.0.1:8000/api/jobs')).json()
            this.jobs = data.results
        }
    }
</script>