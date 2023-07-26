<template>
    <div class="company-list">
        <div class="row">
            <div class="col-md-2 col-sm-2">
                <div class="company-logo">
                    <img :src="enterprise.picture" class="img-responsive" :alt="'Logo '+enterprise.title" />
                </div>
            </div>
            <div class="col-md-8 col-sm-8">
                <div class="company-content">
                    <h3>{{enterprise.title}}</h3>
                    <p><span class="company-name"><i class="fa fa-briefcase"></i>{{enterprise.title}}</span><span class="company-location"><i class="fa fa-map-marker"></i> {{enterprise.address}}</span><span class="package"><i class="fa fa-money"></i>{{ enterprise.contract }}</span></p>
                </div>
            </div>
            <div class="col-md-2 col-sm-2">
                <router-link :to="`enterprises/${enterprise.id}`" class="btn view-job">View enterprise</router-link>
            </div>
        </div>
    </div>
</template>
<script>
    export default {
        name: 'EnterpriseListDisplayComponent',
        props: ['enterprise'],
        mounted(){
            console.log(this.enterprise)
        }
    }
</script>