<template>
    <div>
        <div class="logo">
            <img :src="job.enterprise_display.picture_url" :alt="job.enterprise_display.name">
        </div>
        <div class="card-body"></div>
        <div class="job-type">
            <div>
                <button class="btn" :class="'btn-'+job.class_type">{{ job.type }}</button>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'JobListCardComponent',
    props: ['job'],

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
</style>