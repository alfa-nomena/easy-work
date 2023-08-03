<template>
    <section class="enterprises">
        <div class="container">
            <div class="row heading">
                <h2>All enterprises</h2>
                <p>Find your dream enterprise in these enterprises</p>
            </div>
            <ListEnterpriseComponent :enterprises="enterprises"/>
            <nav>
                <ul class="pagination">
                    <li v-if="previous" class="page-item" @click.prevent="get_enterprises(previous)">
                        <a class="page-link" :href="previous">Previous</a>
                    </li>
                    <li v-if="next" class="page-item" @click.prevent="get_enterprises(next)">
                        <a class="page-link" :href="next">Next</a>
                    </li>
                </ul>
            </nav>
        </div>
    </section>
</template>

<script setup>
import ListEnterpriseComponent from '../components/EnterprisesComponent/ListEnterpriseComponent.vue'
</script>
<script>
export default {
    name: 'ListAllEnterprisesView',
    components: [ ListEnterpriseComponent],
    data(){
        return {
            enterprises:[],
            next: null,
            previous: null
        }
    },
    async mounted(){
        this.get_enterprises('http://127.0.0.1:8000/api/enterprises')
    },
    methods: {
        async get_enterprises(url){
            const data = await (await fetch(url)).json()
            this.enterprises = this.enterprises.concat(data.results)
            this.next = data.next
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