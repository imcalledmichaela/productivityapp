<template>
  <div>
    <b-container md="auto">
        <b-jumbotron header="Success!">
            <button type="button" @click="returnToday()" class="btn btn-success btn-sm">Continue</button>
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
