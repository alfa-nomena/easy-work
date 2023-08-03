<template>
    <nav>
        <ul class="pagination">
            <li v-if="next" class="page-item">
                <a @click.prevent="click_next" class="page-link">Next</a>
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
        }
    }
</script>