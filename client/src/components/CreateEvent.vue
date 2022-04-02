<template>
  <div>
    <v-container class="align-items:center">
      <v-form @submit="onSubmit" v-if="show">
        <v-card>
          <v-card-title>Create Event</v-card-title>
          <v-row class="name">
            <v-col sm="3">
              <v-card-text>Event Name:</v-card-text>
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
              <v-card-text>Subcategory:</v-card-text>
            </v-col>
            <v-col sm="9">
              <v-select
              v-model="form.subcategory"
              :items="subcategories"
              label="Select Subcategory"
              require
              outlined
            ></v-select>
            </v-col>
          </v-row>

          <v-row class="date" style="padding-top: 15px">
            <v-col sm="3">
              <v-card-text>Date:</v-card-text>
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
              <v-card-text>Start Time:</v-card-text>
            </v-col>

            <v-col sm="3">
              <v-menu
                v-model="menu3"
                :close-on-content-click="false"
                :nudge-right="40"
                transition="scale-transition"
                offset-y
                min-width="auto"
              >
              <template v-slot:activator="{ on, attrs }">
                  <v-text-field
                    v-model="form.start_time"
                    label="Select Start Time"
                    prepend-icon="mdi-clock-time-four-outline"
                    readonly
                    v-bind="attrs"
                    v-on="on"
                  ></v-text-field>
                </template>
                <v-time-picker
                  v-model="form.start_time"
                  header-color="primary"
                  @input="menu3 = false"></v-time-picker>
              </v-menu>
            </v-col>

            <!--End Time-->
            <v-col sm="2">
              <v-card-text>End Time:</v-card-text>
            </v-col>

            <v-col sm="3">
              <v-menu
                v-model="menu4"
                :close-on-content-click="false"
                :nudge-right="40"
                transition="scale-transition"
                offset-y
                min-width="auto"
              >
              <template v-slot:activator="{ on, attrs }">
                  <v-text-field
                    v-model="form.end_time"
                    label="Select End Time"
                    prepend-icon="mdi-clock-time-four-outline"
                    readonly
                    v-bind="attrs"
                    v-on="on"
                  ></v-text-field>
                </template>
                <v-time-picker
                  v-model="form.end_time"
                  header-color="primary"
                  @input="menu4 = false"></v-time-picker>
              </v-menu>
            </v-col>
          </v-row>

          <v-row class="location" style="padding-top: 15px">
            <v-col sm="3">
              <v-card-text>Location:</v-card-text>
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
              <v-card-text id="input-group-7" label-for="input-7">Details:</v-card-text>
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
      const path = 'api/events';
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
      const path = 'api/events';
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
      const path = 'api/subcategoriesNameId';
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
