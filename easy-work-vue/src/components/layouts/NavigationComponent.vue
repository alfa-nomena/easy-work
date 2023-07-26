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
                            <a href="#" class="dropdown-toggle" data-toggle="dropdown">Browse</a>
                            <ul class="dropdown-menu animated fadeOutUp" style="display: none; opacity: 1;">
                                <li class="active"><a href="browse-job.html">Browse Jobs</a></li>
                                <li><a href="company-detail.html">Job Detail</a></li>
                                <li><a href="resume.html">Resume Detail</a></li>
                            </ul>
                        </li>
                    </ul>
            </div><!-- /.navbar-collapse -->
        </div>   
    </nav>
</template>
<script>
    export default {
        name: 'NavigationComponent'
    }
</script>