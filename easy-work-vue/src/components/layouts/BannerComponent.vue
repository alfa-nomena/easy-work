<template>
    <section class="main-banner">
        <div class="container">
            <div class="caption">
                <h2>Find your dream job</h2>
                <form>
                    <fieldset>
                        <div class="col-md-4 col-sm-4 no-pad">
                            <input type="text" class="form-control border-right" placeholder="Enterprise name | Job title" />
                        </div>
                        <div class="col-md-3 col-sm-3 no-pad">
                            <select class="selectpicker border-right">
                                <option value="" selected disabled hidden>Experiences</option>
                                <option value="">Any</option>
                                <option v-for="exp in experience_periods" :key="exp[0]">{{ exp[0].charAt(0).toUpperCase() + exp[0].slice(1) }} ({{ exp[1] }})</option>
                            </select>
                        </div>
                        <div class="col-md-3 col-sm-3 no-pad">
                            <select class="selectpicker">
                                <option value="" disabled selected hidden>Sectors</option>
                                <option value="">Any</option>
                                <option v-for="sector in sectors" :key="sector.id">{{ sector.title }}</option>
                            </select>
                        </div>
                        <div class="col-md-2 col-sm-2 no-pad">
                            <input type="submit" class="btn seub-btn" value="submit" />
                        </div>
                    </fieldset>
                </form>
            </div>
        </div>
    </section>
</template>
<script>
    export default {
        name: 'BannerComponent',
        data(){
            return {
                sectors: [],
                experience_periods: []
            }
        },
        async mounted(){
            this.experience_periods = await( await fetch('http://127.0.0.1:8000/api/experience-periods/')).json()
            this.sectors = await( await fetch('http://127.0.0.1:8000/api/sectors/')).json()
        }
    }
</script>
<style scoped>
    .main-banner{
        background: #242c36 url(../../assets/img/banner.jpeg) no-repeat;
    }
</style>