<template>
    <section class="counter">
        <div class="container">
            <div class="col-md-3 col-sm-3">
                <div class="counter-text">
                    <span aria-hidden="true" class="icon-briefcase"></span>
                    <h3>1000</h3>
                    <p>Jobs Posted</p>
                </div>
            </div>
            
            <div class="col-md-3 col-sm-3">
                <div class="counter-text">
                    <span class="box1"><span aria-hidden="true" class="icon-expand"></span></span>
                    <h3>207</h3>
                    <p>All Companies</p>
                </div>
            </div>
            
            <div class="col-md-3 col-sm-3">
                <div class="counter-text">
                    <span class="box1"><span aria-hidden="true" class="icon-profile-male"></span></span>
                    <h3>700+</h3>
                    <p>Total Members</p>
                </div>
            </div>
            
        </div>
    </section>
</template>
<script>
    export default {
        name: 'CounterComponent'
    }
</script>
<style scoped>
    .container{
        display: flex;
        justify-content: space-evenly;
    }
</style>