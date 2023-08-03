<template>
    <div class="companies">
        <JobListDisplayComponent v-for="job in jobs" :key="job.id" :job="job"/>
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
            if (job.enterprise_display.picture===null){
                job.enterprise_display.picture = require('../../assets/img/unknown.jpg')
            }
        });
    }
}
</script>