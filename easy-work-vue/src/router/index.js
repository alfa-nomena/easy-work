import {createRouter, createWebHistory} from 'vue-router'
import JobListComponent from '../components/Jobs/JobListComponent.vue';
import JobDetailComponent from '../components/Jobs/JobDetailComponent.vue'

const routes = [
    {
        path: '/jobs/',
        name: 'JobListComponent',
        component: JobListComponent,
    },
    {
        path: '/enterprises/:enterprise_id/jobs/:job_id',
        name: 'JobDetail',
        component: JobDetailComponent
    }
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL), routes
})
export default router