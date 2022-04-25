<template>
  <v-container fluid class="blue lighten-5 fill-height">
    <v-row class="wrap justify-center">
      <today-component></today-component>

      <v-col md="8" sm="8">
        <v-form @submit="onSubmit" v-if="show">
          <v-card
              class="rounded-lg pt-3"
              height="91vh"
              style="overflow-y: scroll"
          >
            <v-row>
              <v-col>
                <v-card-title
                  class="ml-6 mb-3 mt-5 display-2 font-weight-bold"
                ><v-text-field
                  id="input-1"
                  v-model="form.name"
                ></v-text-field>
                </v-card-title>
              </v-col>
              <v-btn
                  class="mt-9 mr-11 pa-0"
                  @click="returnHome"
                  min-width=0
                  height=36
                  width=36
                  color="red"
                  dark
                >
                <v-icon>mdi-close</v-icon>
              </v-btn>
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
        </v-form>
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
        start_time: '',
        end_time: '',
        location: '',
        details: '',
      },
      subcategories: [
        { text: 'Select One', value: null },
        this.getSubcategories(),
      ],
      event: {},
      event_id: this.$route.query.event_id,
      show: true,
      fab: false,
      menu2: false,
      menu3: false,
      menu4: false,
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
        start_time: this.form.start_time,
        end_time: this.form.end_time,
        location: this.form.location,
        details: this.form.details,
      };

      this.saveChanges(payload);
      this.initForm();
    },
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
    saveChanges(payload) {
      const path = 'api/events';
      axios
        .post(path, payload)
        .then(() => {
          this.getEvent();
          this.$router.push('/success');
        })
        .catch((error) => {
          console.log(error);
          this.getEvent();
          this.$router.push('/error');
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
    getSubcategories() {
      const path = `api/subcategoriesNameId/${this.$store.getters.user.user}`;
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
    returnHome() {
      this.$router.push('/home');
    },
  },
  mounted() {
    this.getEvent();
  },
};
</script>
