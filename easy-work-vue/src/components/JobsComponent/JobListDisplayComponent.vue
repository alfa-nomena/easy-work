<template>
    <div class="company-list">
        <div class="row">
            <div class="col-md-2 col-sm-2">
                <div class="company-logo">
                    <img :src="job.enterprise_display.picture" class="img-responsive" :alt="'Logo '+job.enterprise_display.title" />
                </div>
            </div>
            <div class="col-md-8 col-sm-8">
                <div class="company-content">
                    <h3>{{job.title}}</h3>
                    <p><span class="company-name"><i class="fa fa-briefcase"></i>{{job.enterprise_display.title}}</span><span class="company-location"><i class="fa fa-map-marker"></i> {{job.address}}</span><span class="package"><i class="fa fa-money"></i>{{ job.contract }}</span></p>
                </div>
            </div>
            <div class="col-md-2 col-sm-2">
                <router-link :to="`enterprises/${job.enterprise_display.id}/jobs/${job.id}`" class="btn view-job">View Job</router-link>
            </div>
        </div>
    </div>
</template>
<script>
    export default {
        name: 'JobListDisplayComponent',
        props: ['job'],
    }
</script>