<template>
  <div>
    <b-container>
      <b-row id="content">
        <b-col
          id="today-view"
          sm="3"
        >
          <b-row class="event-table">
        <b-col sm="12" stickyColumn="true">
          <table class="table table-hover">
            <thead>
              <tr>
                <th scope="col">Name</th>
                <th scope="col">Subcategory</th>
                <th scope="col">Date</th>
                <th scope="col">Start Time</th>
                <th scope="col">End Time</th>
                <th scope="col">Location</th>
                <th></th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(event, index) in events" :key="index">
                <td>{{ event.name }}</td>
                <td>{{ event.subcategory }}</td>
                <td>{{ event.date }}</td>
                <td>{{ event.start_time }}</td>
                <td>{{ event.end_time }}</td>
                <td>{{ event.location }}</td>
              </tr>
            </tbody>
          </table>
        </b-col>
      </b-row>
        </b-col>

        <b-col id="calendar-view" sm="9">
          <b-row> This is the calendar pane </b-row>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      events: [],
    };
  },
  methods: {
    getEvents() {
      const path = `${this.$APP_URL}:5000/events`;
      axios
        .get(path)
        .then((res) => {
          console.log(res.data.data.events);
          this.events = res.data.data.events;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  created() {
    this.getEvents();
  },
};

</script>

<style scoped>
#today-view {
    height: 400px;
    border: 5px solid red;
    overflow-y: scroll;
}

#calendar-view {
    height: 400px;
    border: 5px solid blue;
}
</style>
