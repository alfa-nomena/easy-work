<template>
    <nav>
        <ul class="pagination">
            <li v-if="previous" class="page-item">
                <a class="page-link" @click.prevent="click_previous">Pevious</a>
            </li>
            <li v-if="next" class="page-item">
                <a class="page-link" @click.prevent="click_next">Next</a>
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