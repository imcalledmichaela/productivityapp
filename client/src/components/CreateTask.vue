<template>
  <v-container fluid class="blue lighten-5 fill-height">
    <v-row class="wrap">
      <v-col md="7" sm="7" class="ma-auto">
        <v-card id="today-card" class="rounded-lg pt-3">
          <v-form @submit="onSubmit" v-if="show">
            <v-row>
              <v-col>
                <v-card-title class="ml-6 mb-3 mt-5 display-2 font-weight-bold"
                  >Create Task</v-card-title
                >
              </v-col>
            </v-row>

            <v-row class="name justify-center">
              <v-col sm="1" md="1" class="my-auto">
                <v-icon class="ma-auto" x-large>
                  mdi-pencil
                </v-icon>
              </v-col>

              <v-col sm="8" md="8" class="my-auto">
                <v-text-field
                  id="input-1"
                  v-model="form.name"
                  placeholder="Enter Task Name"
                  required
                ></v-text-field>
              </v-col>
            </v-row>

            <v-row class="subcategory justify-center">
              <v-col sm="1" md="1">
                <v-icon class="mt-2" x-large>
                  mdi-format-list-bulleted-type
                </v-icon>
              </v-col>

              <v-col sm="8" md="8">
                <v-select
                  v-model="form.subcategory"
                  :items="subcategories"
                  placeholder="Select Subcategory"
                  require
                  filled
                ></v-select>
              </v-col>
            </v-row>

            <v-row class="date justify-center mt-n4">
              <v-col sm="1" md="1">
                <v-icon class="mt-2" x-large> mdi-calendar </v-icon>
              </v-col>

              <v-col sm="8" md="8">
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
                      readonly
                      filled
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

            <v-row class="duration justify-center mt-n4">
              <v-col sm="1" md="1">
                <v-icon class="mt-2" x-large> mdi-timer-cog-outline </v-icon>
              </v-col>

              <v-col sm="8" md="8">
                <v-text-field
                  id="input-1"
                  v-model="form.duration"
                  placeholder="Enter Duration in Minutes"
                  filled
                  required
                ></v-text-field>
              </v-col>
            </v-row>

            <v-row class="start_time justify-center mt-n4">
              <v-col sm="1" md="1">
                <v-icon class="mt-2" x-large>
                  mdi-clock-time-four-outline
                </v-icon>
              </v-col>

              <v-col sm="8" md="8">
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
                      filled
                      readonly
                      v-bind="attrs"
                      v-on="on"
                    ></v-text-field>
                  </template>
                  <v-time-picker
                    v-model="form.start_time"
                    header-color="primary"
                    @input="menu3 = false"
                  ></v-time-picker>
                </v-menu>
              </v-col>
            </v-row>

            <v-row class="details justify-center mt-n4">
              <v-col sm="1" md="1">
                <v-icon class="mt-2" x-large>
                  mdi-clipboard-edit-outline
                </v-icon>
              </v-col>

              <v-col sm="8" md="8">
                <v-textarea
                  id="input-7"
                  v-model="form.details"
                  placeholder="Enter Details"
                  filled
                ></v-textarea>
              </v-col>
            </v-row>

            <v-row class="mt-n5">
              <v-card-actions class="ma-auto">
                <v-col class="justify-start">
                  <v-btn type="cancel" plain @click="returnHome" color="red"
                    >Cancel</v-btn
                  >
                </v-col>

                <v-col class="justify-end">
                  <v-btn type="submit" color="blue" dark variant="primary"
                    >Submit</v-btn
                  >
                </v-col>
              </v-card-actions>
            </v-row>
          </v-form>
        </v-card>
      </v-col>
    </v-row>

    <v-row>
      <v-col md="7" sm="7" class="ma-auto">
        <v-card class="mt-3" header="Form Data Result">
          <pre class="m-0">{{ form }}</pre>
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
        user_id: this.$store.getters.user.user,
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
      const path = 'api/tasks';
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
      const path = 'api/tasks';
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
    initForm() {
      this.form.name = '';
      this.form.subcategory_id = null;
      this.form.date = '';
      this.form.duration = '';
      this.form.start_time = '';
      this.form.details = '';
    },

    returnHome() {
      this.$router.push('/home');
    },
  },
};
</script>
