<template>
  <div>
    <b-container fluid="md">
      <b-form @submit="onSubmit" v-if="show">
        <b-jumbotron header="Create Task">
          <b-row class="name">
            <b-col sm="3">
              <label id="input-group-1" label-for="input-1">Task Name:</label>
            </b-col>
            <b-col sm="9">
              <b-form-input
                sm="auto"
                id="input-1"
                v-model="form.name"
                type="name"
                placeholder="Enter Task Name"
                required
              ></b-form-input>
            </b-col>
          </b-row>

          <b-row class="subcategory" style="padding-top: 15px">
            <b-col sm="3">
              <label id="input-group-2" label-for="input-2">Subcategory:</label>
            </b-col>
            <b-col sm="9">
              <b-form-select
                id="input-2"
                v-model="form.subcategory"
                :options="subcategories"
                require
              ></b-form-select>
            </b-col>
          </b-row>

          <b-row class="date" style="padding-top: 15px">
            <b-col sm="3">
              <label id="input-group-3" label-for="input-3">Date:</label>
            </b-col>

            <b-col sm="4">
              <b-form-datepicker
                v-model="form.date"
                placeholder="Enter date"
                :date-format-options="{
                  weekday: 'short',
                  year: '2-digit',
                  month: '2-digit',
                  day: '2-digit',
                }"
              >
              </b-form-datepicker>
            </b-col>
          </b-row>

          <b-row class="duration" style="padding-top: 15px">
            <b-col sm="3">
              <label id="input-group-5" label-for="input-5">Duration:</label>
            </b-col>
            <b-col sm="4">
              <b-form-input
                sm="auto"
                id="input-1"
                v-model="form.duration"
                type="name"
                placeholder="Enter Duration in Minutes"
                required
              ></b-form-input>
            </b-col>
          </b-row>

          <b-row class="start_time" style="padding-top: 15px">
            <b-col sm="3">
              <label id="input-group-4" label-for="input-4">Start:</label>
            </b-col>

            <b-col sm="4">
              <b-form-timepicker
                v-model="form.start_time"
                placeholder="Enter Time"
                locale="en-US"
              ></b-form-timepicker>
            </b-col>
          </b-row>

          <b-row class="details" style="padding-top: 15px">
            <b-col sm="3">
              <label id="input-group-6" label-for="input-6">Details</label>
            </b-col>
            <b-col sm="9">
              <b-form-textarea
                id="input-7"
                v-model="form.details"
                placeholder="Enter details"
              ></b-form-textarea>
            </b-col>
          </b-row>
          <b-row style="padding-top: 15px">
            <b-col sm="5"> </b-col>
            <b-col sm="1">
              <b-button type="submit" variant="primary">Submit</b-button>
            </b-col>
            <b-col sm="1">
              <b-button
                type="cancel"
                @click="returnToday"
                style="background-color: red"
                >Cancel</b-button
              >
            </b-col>
            <b-col sm="5"> </b-col>
          </b-row>
        </b-jumbotron>
      </b-form>

      <b-card class="mt-3" header="Form Data Result">
        <pre class="m-0">{{ form }}</pre>
      </b-card>
    </b-container>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      form: {
        name: '',
        subcategory: '',
        date: '',
        duration: '',
        start_time: '',
        details: '',
      },
      subcategories: [
        { text: 'Select One', value: null },
        this.getSubcategories(),
      ],
      show: true,
    };
  },
  methods: {
    onSubmit(event) {
      event.preventDefault();
      const payload = {
        name: this.form.name,
        subcategory_id: this.form.subcategory,
        date: this.form.date,
        duration: Number(this.form.duration),
        start_time: this.form.start_time,
        details: this.form.details,
      };
      this.addTask(payload);

      // this.$router.push('/success');
      // this.initForm();
    },
    getTasks() {
      const path = process.env.VUE_APP_URL + ':5000/tasks';
      axios
        .get(path)
        .then((res) => {
          this.tasks = res.data.name;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    addTask(payload) {
      const path = process.env.VUE_APP_URL + ':5000/tasks';
      axios
        .post(path, payload)
        .then(() => {
          this.getTasks();
          this.$router.push('/success');
        })
        .catch((error) => {
          console.log(error);
          this.getTasks();
          this.$router.push('/error');
        });
    },
    getSubcategories() {
      const path = process.env.VUE_APP_URL + ':5000/subcategoriesNameId';
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
    initForm() {
      this.form.name = '';
      this.form.subcategory_id = null;
      this.form.date = '';
      this.form.duration = '';
      this.form.start_time = '';
      this.form.details = '';
    },

    returnToday() {
      this.$router.push('/today');
    },
  },
};
</script>
