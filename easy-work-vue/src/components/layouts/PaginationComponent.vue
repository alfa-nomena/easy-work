<template>
    <nav>
        <ul class="pagination">
            <!-- <li v-if="previous" class="page-item">
                <router-link @click.prevent="click_previous" class="page-link" :to="previous">Pevious</router-link>
            </li> -->
            <li v-if="next" class="page-item">
                <router-link @click.prevent="click_next" class="page-link" :to="next">Next</router-link>
            </li>
        </ul>
    </nav>
</template>

<script>
    export default {
        name: 'PaginationComponent',
        props: ['previous', 'next'],
        methods: {
            click_next(){
                this.$emit('click_next')
            },
            // click_previous(){
            //     this.$emit('click_previous')
            // }
        }
    }
</script>