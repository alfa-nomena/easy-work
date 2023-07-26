<template>
    <div class="companies" v-if="enterprises">
        <EnterpriseListDisplayComponent v-for="enterprise in enterprises" :key="enterprise.id" :enterprise="enterprise"/>
    </div>
    <div v-else>Loading Enterprises</div>
</template>

<script setup>
    import EnterpriseListDisplayComponent from './EnterpriseListDisplayComponent.vue'
</script>
<script>
export default {
    name: 'ListEnterpriseComponent',
    props: ['enterprises'],
    components: [EnterpriseListDisplayComponent],
    updated(){
        this.enterprises.forEach(enterprise => {
            enterprise.picture = enterprise.picture===null?require('../../assets/img/unknown.jpg'):'http://127.0.0.1:8000'+enterprise.picture
        });
    },
    mounted(){
        console.log(this.enterprises)
    }
}
</script>