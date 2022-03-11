<template>
  <div>
    <b-container md="auto">
        <b-jumbotron header="Error! Please try again">
            <button type="button" @click="returnToday()" class="btn btn-success btn-sm">Return to Today</button>
        </b-jumbotron>

    </b-container>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  methods: {
    returnToday() {
        this.$router.push('/today');
    }
  },
};
</script>
