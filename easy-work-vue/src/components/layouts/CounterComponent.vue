<template>
    <section class="counter">
        <div class="container">
            <div class="col-md-3 col-sm-3">
                <div class="counter-text">
                    <span aria-hidden="true" class="icon-briefcase"></span>
                    <h3>{{count_jobs}}</h3>
                    <p>Jobs Posted</p>
                </div>
            </div>
            
            <div class="col-md-3 col-sm-3">
                <div class="counter-text">
                    <span class="box1"><span aria-hidden="true" class="icon-expand"></span></span>
                    <h3>{{count_enterprises}}</h3>
                    <p>All Companies</p>
                </div>
            </div>
            
            <div class="col-md-3 col-sm-3">
                <div class="counter-text">
                    <span class="box1"><span aria-hidden="true" class="icon-profile-male"></span></span>
                    <h3>{{count_candidates}}</h3>
                    <p>Total Members</p>
                </div>
            </div>
            
        </div>
    </section>
</template>
<script>
    export default {
        name: 'CounterComponent',
        data(){
            return {
                count_jobs:0,
                count_candidates:0,
                count_enterprises: 0,
            }
        },
        async mounted(){
            this.count_candidates = await( await fetch('http://127.0.0.1:8000/api/candidates/count')).json()
            this.count_enterprises = await( await fetch('http://127.0.0.1:8000/api/enterprises/count')).json()
            this.count_jobs = await( await fetch('http://127.0.0.1:8000/api/jobs/count')).json()
        }
    }
</script>
<style scoped>
    .container{
        display: flex;
        justify-content: space-evenly;
    }
</style>