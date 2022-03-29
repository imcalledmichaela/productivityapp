<template>
  <div>
    <v-container fluid="md">
      <v-form @submit="onSubmit" v-if="show">
        <v-card>
          <v-card-title>Create Task</v-card-title>
          <v-row class="name">
            <v-col sm="3">
              <label id="input-group-1" label-for="input-1">Task Name:</label>
            </v-col>
            <v-col sm="9">
              <v-text-field
                sm="auto"
                id="input-1"
                v-model="form.name"
                placeholder="Enter Task Name"
                required
              ></v-text-field>
            </v-col>
          </v-row>

          <v-row class="subcategory" style="padding-top: 15px">
            <v-col sm="3">
              <label id="input-group-2" label-for="input-2">Subcategory:</label>
            </v-col>
            <v-col sm="9">
              <v-form-select
                id="input-2"
                v-model="form.subcategory"
                :options="subcategories"
                require
              ></v-form-select>
            </v-col>
          </v-row>

          <v-row class="date" style="padding-top: 15px">
            <v-col sm="3">
              <label id="input-group-3" label-for="input-3">Date:</label>
            </v-col>

            <v-col sm="4">
              <v-menu
                v-model="menu2"
                :close-on-content-click="false"
                :nudge-right="40"
                transition="scale-transition"
                offset-y
                min-width="auto"
              >
                <template v-slot:activator="{ on, attrs }">
                  <v-text-field
                    v-model="form.date"
                    label="Select Date"
                    prepend-icon="mdi-calendar"
                    readonly
                    v-bind="attrs"
                    v-on="on"
                  ></v-text-field>
                </template>
                <v-date-picker
                  v-model="form.date"
                  @input="menu2 = false"
                ></v-date-picker>
              </v-menu>
            </v-col>
          </v-row>

          <v-row class="duration" style="padding-top: 15px">
            <v-col sm="3">
              <label id="input-group-5" label-for="input-5">Duration:</label>
            </v-col>
            <v-col sm="4">
              <v-text-field
                sm="auto"
                id="input-1"
                v-model="form.duration"
                placeholder="Enter Duration in Minutes"
                required
              ></v-text-field>
            </v-col>
          </v-row>

          <v-row class="start_time" style="padding-top: 15px">
            <v-col sm="3">
              <label id="input-group-4" label-for="input-4">Start:</label>
            </v-col>

            <v-col sm="4">
              <v-form-timepicker
                v-model="form.start_time"
                placeholder="Enter Time"
                locale="en-US"
              ></v-form-timepicker>
            </v-col>
          </v-row>

          <v-row class="details" style="padding-top: 15px">
            <v-col sm="3">
              <label id="input-group-6" label-for="input-6">Details</label>
            </v-col>
            <v-col sm="9">
              <v-form-textarea
                id="input-7"
                v-model="form.details"
                placeholder="Enter details"
              ></v-form-textarea>
            </v-col>
          </v-row>
          <v-row style="padding-top: 15px">
            <v-col sm="5"> </v-col>
            <v-col sm="1">
              <v-btn type="submit" variant="primary">Submit</v-btn>
            </v-col>
            <v-col sm="1">
              <v-btn
                type="cancel"
                @click="returnToday"
                style="background-color: red"
                >Cancel</v-btn
              >
            </v-col>
            <v-col sm="5"> </v-col>
          </v-row>
        </v-card>
      </v-form>

      <v-card class="mt-3" header="Form Data Result">
        <pre class="m-0">{{ form }}</pre>
      </v-card>
    </v-container>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  APP_URL: process.env.VUE_APP_URL,
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
        user_id: 1,
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
      const path = `${this.$APP_URL}/tasks`;
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
      const path = `${this.$APP_URL}/tasks`;
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
      const path = `${this.$APP_URL}/subcategoriesNameId`;
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
