import {createRouter, createWebHistory} from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ListAllJobsView from '../views/ListAllJobsView.vue'
import ListAllEnterprisesView from '../views/ListAllEnterprisesView.vue'
import DetailJobView from '../views/DetailJobView.vue'
import DetailEnterpriseView from '../views/DetailEnterpriseView.vue'



const routes = [
    {
        path: '',
        name: 'HomeView',
        component: HomeView,
    },
    {
        path: '/jobs',
        name: 'ListAllJobsView',
        component: ListAllJobsView,
    },
    {
        path: '/enterprises/:enterprise_id/jobs/:job_id',
        name: 'DetailJobView',
        component: DetailJobView
    },
    {
        path: '/enterprises',
        name: 'ListAllEnterprisesView',
        component: ListAllEnterprisesView
    },
    {
        path: '/enterprises/:enterprise_id',
        name: 'DetailEnterpriseView',
        component: DetailEnterpriseView
    },
]
const router = createRouter({
    history: createWebHistory(process.env.BASE_URL), routes,
    scrollBehavior : (to, from, savedPosition) =>{
        return {top: 0}
    }
})
export default router