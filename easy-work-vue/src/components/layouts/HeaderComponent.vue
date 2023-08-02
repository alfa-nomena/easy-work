<template>
  <nav>
    <div>
      <router-link to="/jobs/">
        <img src="../../assets/logo-header.png" alt="">
      </router-link>
    </div>
    <ul class="nav nav-tabs">
      <li v-for="(nav,i) in navs" :key="i" class="nav-item" @click.self="click_nav_button(nav)">
        <router-link :to="nav.url" class="nav-link" :class="{'nav-link':nav.is_active}">{{ nav.display_text }}</router-link> 
      </li>
    </ul> 
  </nav>
</template>

<script>
export default {
  name: 'HeaderComponent',
  data(){
    return {
      navs: [
        {
          url: '/jobs/',
          is_active: true,
          display_text: 'Home',
        },
        {
          url: '/jobs/',
          is_active: false,
          display_text: 'Companies',
        },
        {
          url: '/jobs/',
          is_active: false,
          display_text: 'Candidates',
        },
        {
          url: '/jobs/',
          is_active: false,
          display_text: 'Jobs',
        }
        ,
        {
          url: '/jobs/',
          is_active: false,
          display_text: 'Login',
        }
      ]
    }
  },
  methods: {
    click_nav_button(el){
      this.navs.forEach(nav=>{
        nav.is_active=false
      })
      el.is_active=true
      console.log(el)
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
nav{
  height: 80px;
  padding: 10px;
  display: flex;
  align-items: flex-start;
  flex-direction: row;
  justify-content: space-between;
  border-bottom: 1px solid #6b797c ;
}
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
  display: flex;
  flex-wrap: nowrap;

}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #6b797c;
}
.nav-link:hover{
  color: #da0833
}
.nav-tabs{
  border: 0;
}
</style>
