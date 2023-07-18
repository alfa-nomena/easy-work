<template>
    <section class="features">
			<div class="container" v-if="jobs">
        <div class="card" v-for="(job, i) in jobs" :key="i">
          <div class="card-body">
            <h5 class="card-title">{{ job.title }}</h5>
            <h6 class="card-subtitle mb-2 text-muted">{{ job.type }} {{ job.contract }}</h6>
            <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
            <a href="#" class="card-link">Card link</a>
            <a href="#" class="card-link">Another link</a>
          </div>
        </div>
			</div>
      <div v-else>
        No data found
      </div>
		</section>
</template>

<script>

export default {
    name: 'JobListComponent',
    data(){
        return {
            jobs: []
        }
    },
    mounted() {
      fetch('http://127.0.0.1:8000/api/jobs')
      .then(res=>res.json())
      .then(data => {
        console.log(data)
        if (data.results){
          this.jobs=data.results
        }
      })
      .catch(
        error=>alert(error)
      )
    }
}
</script>

<style scoped>
.card{
  width: 30%;
  margin: 10px;
  height: 50%;
  border: 0;
  background-color: antiquewhite;
}
.container{
  display: flex;
  flex-wrap: wrap;
  align-items: flex-start;
  justify-content: center;
}
</style>