<template>
  <div>
    <v-container class="align-items:center">
      <v-form @submit="onSubmit" v-if="show">
        <v-card>
          <v-card-title>Create Event</v-card-title>
          <v-row class="name">
            <v-col sm="3">
              <label id="input-group-1" label-for="input-1">Event Name:</label>
            </v-col>
            <v-col sm="9">
              <v-text-field
                sm="auto"
                id="input-1"
                v-model="form.name"
                placeholder="Enter event name"
                required
              ></v-text-field>
            </v-col>
          </v-row>

          <v-row class="subcategory" style="padding-top: 15px">
            <v-col sm="3">
              <label id="input-group-2" label-for="input-2">Subcategory:</label>
            </v-col>
            <v-col sm="9">
              <v-text-field
                id="input-2"
                v-model="form.subcategory"
                :options="subcategories"
                require
              ></v-text-field>
            </v-col>
          </v-row>

          <v-row class="date" style="padding-top: 15px">
            <v-col sm="3">
              <label id="input-group-3" label-for="input-3">Date:</label>
            </v-col>

            <v-col sm="9">
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

          <v-row class="time" style="padding-top: 15px">
            <!--Start Time-->
            <v-col sm="3">
              <label id="input-group-4" label-for="input-4">Start:</label>
            </v-col>

            <v-col sm="4">
               <v-time-picker
                v-model="form.start_time"
                type="month"
                width="290"
                class="ml-4"
              ></v-time-picker>
            </v-col>
          </v-row>

          <v-row class="location" style="padding-top: 15px">
            <v-col sm="3">
              <label id="input-group-6" label-for="input-6">Location:</label>
            </v-col>
            <v-col sm="9">
              <v-text-field
                id="input-6"
                v-model="form.location"
                placeholder="Enter location"
                required
              ></v-text-field>
            </v-col>
          </v-row>

          <v-row class="details" style="padding-top: 15px">
            <v-col sm="3">
              <label id="input-group-7" label-for="input-7">Details</label>
            </v-col>
            <v-col sm="9">
              <v-textarea
                id="input-7"
                v-model="form.details"
                placeholder="Enter details"
              ></v-textarea>
            </v-col>
          </v-row>
          <v-row style="padding-top: 15px">
            <v-col sm="5"> </v-col>
            <v-col sm="1">
              <v-btn type="submit" variant="primary">Submit</v-btn>
            </v-col>
            <v-col sm="1">
              <v-btn type="cancel" @click="returnToday" style="bg-color: red"
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
        start_time: this.form.start_time,
        end_time: this.form.end_time,
        location: this.form.location,
        details: this.form.details,
      };

      this.addEvent(payload);
      this.initForm();
    },
    getEvents() {
      const path = `${this.$APP_URL}/events`;
      axios
        .get(path)
        .then((res) => {
          this.events = res.data.name;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    addEvent(payload) {
      const path = `${this.$APP_URL}/events`;
      axios
        .post(path, payload)
        .then(() => {
          this.getEvents();
          this.$router.push('/success');
        })
        .catch((error) => {
          console.log(error);
          this.getEvents();
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
    printSuccess() {},
    initForm() {
      this.form.name = '';
      this.form.subcategory_id = null;
      this.form.date = '';
      this.form.start_time = '';
      this.form.end_time = '';
      this.form.location = '';
      this.form.details = '';
    },

    returnToday() {
      this.$router.push('/today');
    },
  },
};
</script>
