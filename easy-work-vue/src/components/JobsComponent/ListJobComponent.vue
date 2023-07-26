<template>
    <div class="companies">
        <JobListDisplayComponent v-for="(job,i) in jobs" :key="i" :job="job"/>
    </div>
</template>

<script setup>
    import JobListDisplayComponent from './JobListDisplayComponent.vue'
</script>
<script>
export default {
    name: 'ListJobComponent',
    props: ['jobs'],
    components: [JobListDisplayComponent],
    updated(){
        this.jobs.forEach(job => {
            job.class_type = job.type.toLowerCase().split(' ').join('-')
            job.enterprise_display.picture = job.enterprise_display.picture===null?require('../../assets/img/unknown.jpg'):'http://127.0.0.1:8000'+job.enterprise_display.picture
        });
    }
}
</script>