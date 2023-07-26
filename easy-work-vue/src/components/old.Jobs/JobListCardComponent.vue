<template>
    <router-link :to="`/enterprises/${job.enterprise_display.id}/jobs/${job.id}`" @click="apply(job)">
        <div class="logo">
            <img :src="'http://127.0.0.1:8000' + job.enterprise_display.picture || '#'" :alt="job.enterprise_display.name">
        </div>
        <div class="card-body">
            <h2><i class="uil uil-clipboard"></i>{{ job.title }}</h2>
            <h3>
                <i class="uil uil-building"></i>{{ job.enterprise_display.name }}
                <i class="uil uil-map-marker"></i>{{ job.type }}
                <i class="uil uil-file-check"> </i>{{ job.contract }}
            </h3>
            <p>Posted : {{ job.date_posted }}</p>
        </div>
        <div class="apply">
            <button class="btn btn-danger">Apply</button>
        </div>
    </router-link>
</template>

<script>
export default {
    name: 'JobListCardComponent',
    props: ['job'],
    methods: {
        apply(job){
            this.$emit('apply-job', job)
        }
    }

}
</script>
<style scoped>
h3, h2{
    padding: 0;
    margin: 0;
    box-sizing: border-box;
    font-family: 'Arial Narrow Bold', sans-serif;
}
h2{
    font-size: 1.4rem;
    font-weight: 400;
    border-bottom: 1px solid #999;
}
h3{
    font-size: 1rem;
    font-weight: 550;
}
.card-body{
    padding: 0;
    padding: 0 15px
}
.card{
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  width: 90%;
  height: 100px;
  margin: 10px;
  border: 0;
  padding: 10px;
  background-color: #eee;
  border-radius: 0;
}
.card:hover{
    background-color: #fff;
}
img{
    width: 100px;
    height: 100%;
    padding: 5px 0;
}
.logo{
    border-right: 1px solid #999 ;
    padding-right: 5px;
    width: 120px
}
.apply{
    display: flex;
    align-items: center;
}
button{
    background-color: #da0833;
}
a{
    text-decoration: none;
}
</style>