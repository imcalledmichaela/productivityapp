<template>
  <v-container fluid class="blue lighten-5 fill-height">
    <v-row class="wrap justify-center">
      <today-component></today-component>
      
      <v-col md="8" sm="8">
        <v-card class="rounded-lg pt-3" height="91vh" style="overflow-y:scroll">
          <v-row>
            <v-col>
              <v-card-title class="ml-6 mb-3 mt-5 display-2 font-weight-bold"
                >{{ task.name }}</v-card-title>
            </v-col>
          </v-row>

          <v-row class="subcategory justify-center">
            <v-col sm="1" md="1" class="my-auto">
              <v-card-subtitle class="font-weight-bold">
                Subcategory:
              </v-card-subtitle>
            </v-col>

            <v-col sm="8" md="8" class="my-auto">
              <v-card-subtitle>{{ task.subcategory }}</v-card-subtitle>
            </v-col>
          </v-row>

          <v-row class="date justify-center">
            <v-col sm="1" md="1" class="my-auto">
              <v-card-subtitle class="font-weight-bold">
                Date:
              </v-card-subtitle>
            </v-col>

            <v-col sm="8" md="8" class="my-auto">
              <v-card-subtitle>{{ task.date }}</v-card-subtitle>
            </v-col>
          </v-row>

          <v-row class="start_time justify-center">
            <v-col sm="1" md="1" class="my-auto">
              <v-card-subtitle class="font-weight-bold">
                Start Time:
              </v-card-subtitle>
            </v-col>

            <v-col sm="8" md="8" class="my-auto">
              <v-card-subtitle>{{ task.start_time }}</v-card-subtitle>
            </v-col>
          </v-row>

          <v-row class="end_time justify-center">
            <v-col sm="1" md="1" class="my-auto">
              <v-card-subtitle class="font-weight-bold">
                End Time:
              </v-card-subtitle>
            </v-col>

            <v-col sm="8" md="8" class="my-auto">
              <v-card-subtitle>{{ task.end_time }}</v-card-subtitle>
            </v-col>
          </v-row>

          <v-row class="details justify-center">
            <v-col sm="1" md="1" class="my-auto">
              <v-card-subtitle class="font-weight-bold">
                Details:
              </v-card-subtitle>
            </v-col>

            <v-col sm="8" md="8" class="my-auto">
              <v-card-subtitle>{{ task.details }}</v-card-subtitle>
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
      task_id: this.$router.params.task_id,
      task: {},
    };
  },
  methods: {
    getTask() {
      const path = `api/getTaskById/${this.task_id}`;
      axios
        .get(path)
        .then((res) => {
          this.task = res.data.data.task;
          console.log(res)
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  create() {
    this.getTask();
  }
};
</script>
