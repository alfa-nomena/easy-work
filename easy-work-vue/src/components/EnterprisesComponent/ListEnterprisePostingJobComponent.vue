<script setup>
    import ListEnterpriseComponent from './ListEnterpriseComponent.vue'
</script>
<template>
    <div class="row heading">
        <h2>Enterprises</h2>
        <p>Enterprises that posted the latest job</p>
    </div>
    <ListEnterpriseComponent :enterprises="enterprises" /> 
</template>
<script>
    export default {
        name: 'ListEnterprisePostingJobComponent',
        components: [ListEnterpriseComponent],
        data(){
            return {
                enterprises:[]
            }
        },
        async mounted(){
            const data = await (await fetch('http://127.0.0.1:8000/api/enterprises')).json()
            this.enterprises = data.results
        }
    }
</script>