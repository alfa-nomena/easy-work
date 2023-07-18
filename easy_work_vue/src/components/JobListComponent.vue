<template>
    <section class="features">
			<div class="container" v-if="jobs">
				<div class="col-md-4 col-sm-4" v-for="(job, i) in jobs" :key="i">
					<div class="features-content">
						<span class="box1"><span aria-hidden="true" class="icon-dial"></span></span>
						<h3>{{job.title}}</h3>
						<p>{{ job.description }}</p>
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
        this.jobs = data
      })
      .catch(
        error=>alert(error)
      )
    }
}
</script>