<template>
  <div>
    <v-container class="align-items:center">
      <v-card>
        <v-card-title>Success!</v-card-title>
        <v-btn
          type="button"
          @click="returnToday()"
          class="btn btn-success btn-sm"
        >
          Continue
        </v-btn>
      </v-card>
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
