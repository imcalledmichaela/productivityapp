<template>
  <v-container fluid class="blue lighten-5 fill-height">
    <v-row class="wrap justify-center">
      <today-component></today-component>
      <v-col md="8" sm="8">
        <v-card class="rounded-lg pt-3" height="91vh" style="overflow-y:scroll">
          <v-row>
            <v-col>
              <v-card-title class="ml-6 mb-3 mt-5 display-2 font-weight-bold"
                >{{ event.name }}</v-card-title>
            </v-col>
          </v-row>

          <v-row class="subcategory justify-center">
            <v-col sm="2" md="2" class="my-auto">
              <v-card-subtitle class="font-weight-bold">
                Subcategory:
              </v-card-subtitle>
            </v-col>

            <v-col sm="8" md="8" class="my-auto">
              <v-card-subtitle>{{ event.subcategory }}</v-card-subtitle>
            </v-col>
          </v-row>

          <v-row class="date justify-center">
            <v-col sm="2" md="2" class="my-auto">
              <v-card-subtitle class="font-weight-bold">
                Date:
              </v-card-subtitle>
            </v-col>

            <v-col sm="8" md="8" class="my-auto">
              <v-card-subtitle>{{ event.date }}</v-card-subtitle>
            </v-col>
          </v-row>

          <v-row class="start_time justify-center">
            <v-col sm="2" md="2" class="my-auto">
              <v-card-subtitle class="font-weight-bold">
                Start Time:
              </v-card-subtitle>
            </v-col>

            <v-col sm="8" md="8" class="my-auto">
              <v-card-subtitle>{{ event.start_time }}</v-card-subtitle>
            </v-col>
          </v-row>

          <v-row class="end_time justify-center">
            <v-col sm="2" md="2" class="my-auto">
              <v-card-subtitle class="font-weight-bold">
                End Time:
              </v-card-subtitle>
            </v-col>

            <v-col sm="8" md="8" class="my-auto">
              <v-card-subtitle>{{ event.end_time }}</v-card-subtitle>
            </v-col>
          </v-row>

          <v-row class="location justify-center">
            <v-col sm="2" md="2" class="my-auto">
              <v-card-subtitle class="font-weight-bold">
                Location:
              </v-card-subtitle>
            </v-col>

            <v-col sm="8" md="8" class="my-auto">
              <v-card-subtitle>{{ event.location }}</v-card-subtitle>
            </v-col>
          </v-row>

          <v-row class="details justify-center">
            <v-col sm="2" md="2" class="my-auto">
              <v-card-subtitle class="font-weight-bold">
                Details:
              </v-card-subtitle>
            </v-col>

            <v-col sm="8" md="8" class="my-auto">
              <v-card-subtitle>{{ event.details }}</v-card-subtitle>
            </v-col>
          </v-row>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      event: {},
      event_id: this.$route.query.event_id,
    };
  },
  methods: {
    getEvent() {
      const path = `api/event/${this.event_id}`;
      axios
        .get(path)
        .then((res) => {
          this.event = res.data.data.event;
          console.log(res);
        })
        .catch((error) => {
          console.log(error);
        });
    },
    deleteEvent() {
      const path = `api/event/${this.event_id}`;
      axios
        .delete(path)
        .then((res) => {
          console.log(res);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  mounted() {
    this.getEvent();
  },
};
</script>
