<template>
    <div v-if="job" class="container">
        <div class="header">
            <div class="logo">
                <img :src="job.enterprise_display.picture" :alt="job.title">
            </div>
            <div class="detail">
                <h2>{{ job.title }}</h2>
                <p>
                    <i class="uil uil-calendar-alt"></i> {{ job.date_posted }} 
                    | <i class="uil uil-building"></i> {{ job.enterprise_display.name }}
                    | <i class="uil uil-file-info-alt"></i> {{ job.contract }}
                    | <i class="uil uil-clock"></i> {{ job.type }}
                    | <i class="uil uil-map-marker"></i> {{ job.location }}
                </p>
            </div>
        </div>
        
        
        
         {{ job }}
    </div>
    <div v-else>No job found</div>
</template>
<script>
    export default {
        data(){
            return {
                job: null
            }
        },
        created(){
            this.fetch_job()
        },
        methods: {
            async fetch_job(){
                const params = this.$route.params
                const url = `http://127.0.0.1:8000/api/enterprises/${params.enterprise_id}/jobs/${params.job_id}`
                this.job  = await (await fetch(url)).json()
            }
        }
    }
</script>
<style scoped>
    img{
        width: 250px;
        height: 250px;
        position: relative;
        right: 20px
    }
    *{
        text-align: left;
    }
    .detail{
        padding: 20px;
        margin: 20px
    }
    .header{
        display: flex;
        flex-direction: row;
        margin-bottom: 20px;
    }
    .container{
        margin-top: 20px;
    }
</style>