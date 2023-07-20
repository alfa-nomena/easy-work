<template>
    <nav>
        <ul class="pagination">
            <li v-if="previous" class="page-item" @click.prevent="click_previous">
                <a class="page-link" :href="previous">Pevious</a>
            </li>
            <li v-if="next" class="page-item" @click.prevent="click_next">
                <a class="page-link" :href="next">Next</a>
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
            click_previous(){
                this.$emit('click_previous')
            }
        }
    }
</script>