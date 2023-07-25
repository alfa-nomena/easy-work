<template>
    <div v-if="job" class="container">
        <div class="header">
            <div class="logo">
                <img :src="job.enterprise_display.picture" :alt="job.title">
            </div>
            <div class="detail">
                <h2>{{ job.title }} | <span>{{ job.enterprise_display.title }}</span></h2>
                <p>
                    <i class="uil uil-calendar-alt"></i> {{ job.date_posted }} 
                    | <i class="uil uil-file-info-alt"></i> {{ job.contract }}
                    | <i class="uil uil-clock"></i> {{ job.type }}
                    | <i class="uil uil-map-marker"></i> {{ job.location }}
                </p>
                <p class="skills">
                    <span class="skill" v-for="skill in job.skill_set" :key="skill.id">{{ skill.title }}</span>
                </p>
            </div>
        </div>
        <div class="body">
            <div class="about">
                <h2><i class="uil uil-building"></i> About the enterprise</h2>
                <p>{{ job.enterprise_display.description }}</p>
            </div>
            <h2><i class="uil uil-clipboard-notes"></i>Responsibilities</h2>
            <ul class="list">
                <li v-for="role in job.role_set" :key="role.id"><i class="uil uil-check-circle"></i> {{ role.title }}</li>
            </ul>
            <h2><i class="uil uil-file-info-alt"></i>Minimum qualifications</h2>
            <ul class="list">
                <li v-for="profil in job.profil_set" :key="profil.id"><i class="uil uil-check-circle"></i> {{ profil.title }}</li>
            </ul>
            <div class="buttons">
                <button class="btn btn-dark"><i class="uil uil-file-bookmark-alt"></i>Save</button>
                <button class="btn btn-dark"><i class="uil uil-fast-mail"></i>Follow recruiter</button>
                <button class="btn btn-dark"><i class="uil uil-message"></i>Apply</button>
            </div>
        </div>
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
        right: 20px;
        padding: 20px;;
    }
    *{
        text-align: left;
    }
    .detail{
        padding: 20px;
        margin: 20px
    }
    .detail h2{
        color: #404b4d;
        font-weight: 700
    }
    .detail h2 span{
        font-weight: 600;
    }
    .header{
        display: flex;
        flex-direction: row;
        margin-bottom: 20px;
        border-bottom: 2px solid #999;
    }
    .container{
        margin: auto;
        padding: 40px;
        background-color: #fff;
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
    li .uil{
        color: #f7021b
    }
    .list li{
        margin: 20px 0;
    }
    h2 .uil{
        color: #242c36;
        margin-right: 20px;
    }
    .buttons{
        display: flex;
        align-items: center;
        justify-content: flex-end;
        padding: 10px
    }
    .buttons .btn{
        margin: 10px 20px;
        font-size: 1.2em;
        font-weight: 600;
    }
    .buttons .btn:hover{
        background-color: #353d47;
    }
</style>