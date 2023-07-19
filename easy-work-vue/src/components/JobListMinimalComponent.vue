<script setup>
import JobListCardComponent from './JobListCardComponent.vue'
import PaginationComponent from './PaginationComponent.vue'
</script>

<template>
    <section class="features">
		<div v-if="jobs" class="container container-fluid">
			<JobListCardComponent class="card" v-for="(job,i) in jobs" :key="i" :job="job"></JobListCardComponent>
		</div>
		<div v-else>No data found</div>
		<PaginationComponent :next="next" :previous="previous" @click_next="fetch_jobs(next)" @click="fetch_jobs(previous)"></PaginationComponent>
	</section>
</template>

<script>
export default {
    name: 'JobListComponent',
    components: [JobListCardComponent, PaginationComponent],
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
		async fetch_jobs(url){
			let response = await fetch(url)
			let data = await response.json()
			let results = data.results
			results.forEach(job => {
				switch (job.type.toLowerCase()){
					case 'full time':
					job.class_type='success'
					break
					case 'part time':
					job.class_type='danger'
					break
				}
			})
			this.jobs=results
			this.next = data.next
			this.previous = data.previous
		}
    }
}
</script>

<style scoped>
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