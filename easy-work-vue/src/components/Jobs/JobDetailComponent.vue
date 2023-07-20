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
                    | <i class="uil uil-building"></i> {{ job.enterprise_display.title }}
                    | <i class="uil uil-file-info-alt"></i> {{ job.contract }}
                    | <i class="uil uil-clock"></i> {{ job.type }}
                    | <i class="uil uil-map-marker"></i> {{ job.location }}
                </p>
                <p class="skills">
                    <span class="skill" v-for="skill in job.skill_set" :key="skill.id">{{ skill.title }} {{ console.log(skill) }}</span>
                </p>
            </div>
        </div>
        <div class="body">
            <div class="about">
                <h2>About the enterprise</h2>
                <p>{{ job.enterprise_display.description }}</p>
            </div>
            <h2>Missions</h2>
            <ul class="mission">
                <li v-for="role in job.role_set" :key="role.id">{{ role.title }}</li>
            </ul>
            <h2>Profil</h2>
            <ul class="mission">
                <li v-for="profil in job.profil_set" :key="profil.id">{{ profil.title }}</li>
            </ul>
            <div class="">
                <button class="btn btn-primary">Apply</button>
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
    .skills{
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: flex-start;
        flex-wrap: wrap;
    }
    span.skill{
        color: #fff;
        padding: 4px 10px;
        background-color: #a4b9db;
        margin: 5px;
        border-radius: 10px;
        text-align: center;
        font-weight: 600;
    }
    .body h2{
        color: #f7021b
    }
    ul{
        list-style: none;
    }
    .apply{
        display: flex;
        justify-content: flex-end;
        flex-direction: row;
        width: 100%;
    }
</style>