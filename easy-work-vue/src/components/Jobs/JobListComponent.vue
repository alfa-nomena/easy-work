<script setup>
import JobListCardComponent from './JobListCardComponent.vue'
import PaginationComponent from '../PaginationComponent.vue'
</script>

<template>
    <section class="features">
		<div v-if="jobs" class="container container-fluid">
			<JobListCardComponent class="card" v-for="(job,i) in jobs" :key="i" :job="job"></JobListCardComponent>
		</div>
		<div v-else>No data found</div>
		<PaginationComponent v-if="next || previous" :next="next" :previous="previous" @click_next="fetch_jobs(next)" @click="fetch_jobs(previous)"></PaginationComponent>
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
    async created() {
		await this.fetch_jobs('http://localhost:8000/api/jobs')
    },
	updated(){
		console.log(this.jobs)
		console.log('next: ',this.next)
		console.log('previous: ',this.previous)
	},
    methods:{
		async fetch_jobs(url){
			if (url){
				const data = await (await fetch(url)).json()
				const results = data.results
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
				this.jobs= results
				this.next = data.next
				this.previous = data.previous
			}
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
  background-color: #dcdcdc;
}
nav{
  margin: auto
}
</style>