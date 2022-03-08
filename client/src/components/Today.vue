<template>
  <div class="container">
    <b-jumbotron header="Today">
    <div class="row">
      <div class="col-sm-10">
        <h1>Events</h1>
        <!--<hr><br><br>
        <button type="button" class="btn btn-success btn-sm">Add Event</button>
        <br><br>-->
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
      </div>
    </div>
    <div class="row">
      <div class="col-sm-10">
        <h1>Tasks</h1>
        <!-- <hr><br><br>
        <button type="button" class="btn btn-success btn-sm">Add Task</button>
        <br><br> -->
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Name</th>
              <th scope="col">Subcategory</th>
              <th scope="col">Date</th>
              <th scope="col">Duration</th>
              <th scope="col">Start Time</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(task, index) in tasks" :key="index">
              <td>{{ task.name }}</td>
              <td>{{ task.subcategory }}</td>
              <td>{{ task.date }}</td>
              <td>{{ task.duration }}</td>
              <td>{{ task.start_time }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    </b-jumbotron>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      events: [],
      tasks: [],
      subcategories: [this.getSubcategories()],
    };
  },
  methods: {
    getEvents() {
      const path = 'http://localhost:5000/events';
      axios.get(path)
        .then((res) => {
          console.log(res.data.data.events)
          this.events = res.data.data.events;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    getTasks() {
      const path = 'http://localhost:5000/tasks';
      axios.get(path)
        .then((res) => {
          console.log(res.data.data.tasks)
          this.tasks = res.data.data.tasks;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    getSubcategories() {
      const path = "http://localhost:5000//subcategoriesNameId";
      axios
        .get(path)
        .then((res) => {
          const subcat = res.data.data.subcategories;
          this.subcategories = Object.keys(subcat).map((k) => subcat[k]);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  created() {
    this.getEvents();
    this.getTasks();
    this.getSubcategories();
  },
};
</script>