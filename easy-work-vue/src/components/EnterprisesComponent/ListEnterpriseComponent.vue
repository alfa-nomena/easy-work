<template>
    <div class="companies">
        <EnterpriseListDisplayComponent v-for="enterprise in enterprises" :key="enterprise.id" :enterprise="enterprise"/>
    </div>
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
            if (enterprise.picture===null){
                enterprise.picture = require('../../assets/img/unknown.jpg')
            }
        })
    }
}
</script>