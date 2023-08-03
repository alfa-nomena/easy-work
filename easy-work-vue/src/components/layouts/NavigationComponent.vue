<template>
    <nav class="navbar navbar-default navbar-sticky bootsnav">
        <div class="container">      
            <!-- Start Header Navigation -->
            <div class="navbar-header">
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#navbar-menu">
                    <i class="fa fa-bars"></i>
                </button>
                <router-link class="navbar-brand" to="/"><img src="../../assets/img/logo.png" class="logo" alt=""></router-link>
            </div>
            <!-- End Header Navigation -->

            <!-- Collect the nav links, forms, and other content for toggling -->
            <div class="collapse navbar-collapse" id="navbar-menu">
                <ul class="nav navbar-nav navbar-right" data-in="fadeInDown" data-out="fadeOutUp">
                        <li><router-link to="/">Home</router-link></li> 
                        <li><a href="login.html">Login</a></li>
                        <li><a href="companies.html">Companies</a></li> 
                        <li class="dropdown">
                            <a href="#" class="dropdown-toggle" data-toggle="dropdown">Sectors</a>
                            <ul class="dropdown-menu animated fadeOutUp" style="display: none; opacity: 1;" v-if="sectors" id="sectors">
                                <li v-for="(sector,i) in sectors" :key="i">
                                    <a :href="sector.href" :key="sector.id">
                                        {{ sector.title }}
                                    </a>
                                </li>
                            </ul>
                        </li>
                    </ul>
            </div><!-- /.navbar-collapse -->
        </div>   
    </nav>
</template>
<script>
    export default {
        name: 'NavigationComponent',
        data(){
            return {
                sectors: []
            }
        },
        methods:{
            href_sector(sector){
                return this.$router.resolve({
                    name: 'ListAllJobsView',
                    query: {
                        sector: sector.title,
                    }
                }).href
            }
        },
        async mounted(){
            const sectors = await( await fetch('http://127.0.0.1:8000/api/sectors/')).json()
            sectors.forEach(sector=>{
                sector.href = this.href_sector(sector)
            })
            this.sectors = sectors
        }
    }
</script>
<style scoped>
    #sectors{
        max-height: 400px;
        overflow: auto;
    }
</style>