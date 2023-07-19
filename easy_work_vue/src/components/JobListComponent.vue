<template>
    <section class="features">
			<div v-if="jobs" class="container container-fluid">
        <div class="card" v-for="(job,i) in jobs" :key="i">
          <div class="logo">
            <img :src="job.enterprise_display.picture" :alt="job.enterprise_display.name">
          </div>
          <div class="card-body">
          </div>
          <div class="job-type">
            <div>
              <button class="btn" :class="'btn-'+job.class_type">{{ job.type }}</button>
            </div>
          </div>
        </div>
      </div>
      <div v-else>
        No data found
      </div>
      <nav>
        <ul class="pagination">
          <li v-if="previous" class="page-item">
            <a class="page-link" :href="previous" @click.prevent="fetch_jobs(previous)">Previous</a>
          </li>
          <li v-if="next" class="page-item">
            <a class="page-link" :href="next" @click.prevent="fetch_jobs(next)">Next</a>
          </li>
        </ul>
      </nav>
		</section>
</template>

<script>


export default {
    name: 'JobListComponent',
    data(){
        return {
            jobs: [],
            next: null,
            previous: null
        }
    },
    mounted() {
      this.fetch_jobs('http://127.0.0.1:8000/api/jobs')
      
    },
    methods:{
      fetch_jobs(url){
      fetch(url)
      .then(res=>res.json())
      .then(data => {
        if (data.results){
          data.results.forEach(job => {
            switch (job.type.toLowerCase()){
              case 'full time':
                job.class_type='success'
                break
              case 'part time':
                job.class_type='danger'
                break
            }
          })
          this.jobs=data.results
          this.next = data.next
          this.previous = data.previous
        }
      })
      .catch(
        error=>alert(error)
      )
    }
  }
}
</script>

<style scoped>
.card{
  /* width: 30%;
  height: 50%; */
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  width: 100%;
  height: 150px;
  margin: 10px;
  border: 0;
  padding: 10px;
  background-color: antiquewhite;
}
.container{
  display: flex;
  flex-wrap: wrap;
  align-items: flex-start;
  justify-content: center;
}
.features{
  display: flex;
  justify-content: center;
  flex-direction: column;
}
nav{
  margin: auto
}
</style>