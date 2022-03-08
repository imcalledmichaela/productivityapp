<template>
  <div>
  <b-container>
    <b-form @submit="onSubmit" v-if="show">
    <b-row class="name">
        <b-col sm="3">
     <label id="input-group-1" label-for="input-1" >Event Name:</label>
      </b-col>
      <b-col sm="9">
        <b-form-input sm="auto"
          id="input-1"
          v-model="form.name"
          type="name"
          placeholder="Enter event name"
          required
        ></b-form-input>

      </b-col>
    </b-row>

    <b-row class="subcategory">
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

    <b-row class="date">
      <b-col sm="3">
        <label id="input-group-3" label-for="input-3">Date:</label>
      </b-col>
      <b-col sm="9">
        <b-form-datepicker
          id="input-3"
          v-model="form.date"
          required
        ></b-form-datepicker>
      </b-col>
    </b-row>

    <b-row class="start_time">
      <b-col sm="3">
        <label id="input-group-4" label-for="input-4">Start Time:</label>
      </b-col>
      <b-col sm="9">
        <b-form-timepicker
            id="input-4"
            v-model="form.start_time"
            locale="en"
            placeholder="Enter Start Time:"
            required
        ></b-form-timepicker>
      </b-col>
    </b-row>

    <b-row class="end_time">
      <b-col sm="3">
        <label id="input-group-5" label-for="input-5">End Time:</label>
      </b-col>
      <b-col sm="9">
        <b-form-timepicker
            id="input-5"
            v-model="form.end_time"
            locale="en"
            placeholder="Enter End Time:"
            required
        ></b-form-timepicker>
      </b-col>
    </b-row>

    <b-row class="location">
      <b-col sm="3">
        <label id="input-group-6" label-for="input-6">Location:</label>
      </b-col>
      <b-col sm="9">
        <b-form-input
          id="input-6"
          v-model="form.location"
          type="location"
          placeholder="Enter location"
          required
        ></b-form-input>
      </b-col>
    </b-row>

    <b-row class="details">
      <b-col sm="3">
        <label id="input-group-7" label-for="input-7">Details</label>
      </b-col>
      <b-col sm="9">
        <b-form-textarea
          id="input-7"
          v-model="form.details"
          placeholder="Enter details"
        ></b-form-textarea>
      </b-col>
    </b-row>

      <b-button type="submit" variant="primary">Submit</b-button>
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
        start_time: '',
        end_time: '',
        location: '',
        details: '',
      },
      subcategories: [{ text: 'Select One', value: null }, this.getSubcategories()],
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
        start_time: this.form.start_time,
        end_time: this.form.end_time,
        location: this.form.location,
        details: this.form.details,
      };
      this.addEvent(payload);
      this.initForm();
    },
    getEvents() {
      const path = 'http://localhost:5000/events';
      axios.get(path)
        .then((res) => {
          this.events = res.data.name;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    addEvent(payload) {
      const path = 'http://localhost:5000/events';
      axios.post(path, payload)
        .then(() => {
          this.getEvents();
        })
        .catch((error) => {
          console.log(error);
          this.getEvents();
        });
    },
    getSubcategories() {
      const path = 'http://localhost:5000//subcategoriesNameId';
      axios.get(path)
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
      this.form.start_time = '';
      this.form.end_time = '';
      this.form.location = '';
      this.form.details = '';
    },
  },
};
</script>
