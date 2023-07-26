<template>
    <section class="profile-detail" v-if="job && job.enterprise_display">
        <div class="container">
            <div class="col-md-12">
                <div class="row">
                    <div class="basic-information">
                        <div class="col-md-3 col-sm-3">
                        <img :src="job.enterprise_display.picture" :alt="job.title" class="img-responsive">
                        </div>
                        <div class="col-md-9 col-sm-9">
                            <div class="profile-content">
                                    <h2>{{ job.title }}<span>{{ job.enterprise_display.title }}</span></h2>
                                    <ul class="information">
                                        <li v-if="job.enterprise_display.address"><span>Address:</span>{{ job.enterprise_display.address}}</li>
                                        <li><span>Employee:</span>{{ job.enterprise_display.size }}</li>
                                        <li><span>Mail:</span>{{ job.enterprise_display.email || '-'}}</li>
                                        <li v-if="job.enterprise_display.date_founded">
                                            <span>From:</span>{{ job.enterprise_display.date_founded}}</li>
                                    </ul>
                                </div>
                            </div>
                        <ul class="social">
                            <li v-for="skill in job.skill_set" :key="skill.id"><span class="google"><i class="fa uil uil-plus-circle"></i>{{ skill.title }}</span></li>
                        </ul>
                        <div class="panel panel-default" v-if="job.enterprise_display.description">
                            <div class="panel-heading">
                                <i class="fa fa-user fa-fw"></i> About Microsoft
                            </div>
                                                
                            <div class="panel-body">
                            <p>{{ job.enterprise_display.description }}</p>	
                            </div>
                        </div>
                        
                        <div class="panel panel-default">
                            <div class="panel-heading">
                                <i class="fa fa-leaf fa-fw"></i> Responsibilities:
                            </div>
                                                
                            <div class="panel-body">
                            <p>Rapid growth since incorporation has triggered a chain of products, acquisitions and partnerships beyond Google's core search engine (Google Search).</p>	
                            <ul>
                                <li v-for="role in job.role_set" :key="role.id">{{ role.title }}</li>
                            </ul>
                            </div>
                        </div>
                        
                        <div class="panel panel-default">
                            <div class="panel-heading">
                                <i class="fa fa-coffee fa-fw"></i> Minimum qualifications:
                            </div>
                            <div class="panel-body">
                            <p>Rapid growth since incorporation has triggered a chain of products.</p>	
                            <ul>
                                <li v-for="profil in job.profil_set" :key="profil.id">{{ profil.title }}</li>
                            </ul>
                            </div>
                        </div>
                        

                    </div>
                </div>
            </div>
        </div>
    </section>
</template>


<script>
export default {
    name: 'DetailJobView',
    data(){
        return {
            job: {}
        }
    },
    async mounted(){
        const url = `http://127.0.0.1:8000/api/enterprises/${this.$route.params.enterprise_id}/jobs/${this.$route.params.job_id}`
        const job = await (await fetch(url)).json()
        job.class_type = job.type.toLowerCase().split(' ').join('-')
        job.enterprise_display.picture = job.enterprise_display.picture ?'http://127.0.0.1:8000'+job.enterprise_display.picture:require('../assets/img/unknown.jpg')
        this.job = job
    }
}
</script>
<style scoped>

.social li{
    border: 1px solid #d6201f;
    display: inline-block;
    padding: 4px 5px;
    border-radius: 50px;
    margin: 10px;
}
.social li .uil{
    font-size: 1.3em;
}
.social li:hover{
    border: 1px solid #ddd;
    background-color: #fff;
    color: #d6201f;
    padding: 6px 8px;
    cursor:not-allowed;
}
.social{
    display: flex;
    justify-content: space-evenly;
    flex-wrap: wrap;
}
</style>