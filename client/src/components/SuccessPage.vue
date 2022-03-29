<template>
  <div>
    <v-container md="auto">
      <v-jumbotron header="Success!">
        <button
          type="button"
          @click="returnToday()"
          class="btn btn-success btn-sm"
        >
          Continue
        </button>
      </v-jumbotron>
    </v-container>
  </div>
</template>

<script>
export default {
  methods: {
    returnToday() {
      this.$router.push('/today');
    },
  },
};
</script>
