<template>
  <div>
    <v-container>
      <v-row id="content">
        <v-col id="today-view" sm="3">
          <v-row class="fill-height">
            <v-col>
              <v-sheet height="64">
                <v-toolbar flat>
                  <v-btn
                    outlined
                    class="mr-4"
                    color="grey darken-2"
                    @click="setToday"
                  >
                    Today
                  </v-btn>
                  <v-btn fab text small color="grey darken-2" @click="prev">
                    <v-icon small> mdi-chevron-left </v-icon>
                  </v-btn>
                  <v-btn fab text small color="grey darken-2" @click="next">
                    <v-icon small> mdi-chevron-right </v-icon>
                  </v-btn>
                  <v-toolbar-title v-if="$refs.calendar">
                    {{ $refs.calendar.title }}
                  </v-toolbar-title>
                  <v-spacer></v-spacer>
                </v-toolbar>
              </v-sheet>
              <v-sheet height="100%">
                <v-calendar
                  ref="calendar"
                  v-model="focus"
                  color="primary"
                  type="category"
                  category-show-all
                  :categories="subcategories"
                  :events="events"
                  :event-color="getEventColor"
                  @change="fetchEvents"
                ></v-calendar>
              </v-sheet>
            </v-col>
          </v-row>
        </v-col>

        <v-col id="calendar-view">
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      subcategories: [this.getSubcategories()],
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
    getSubcategories() {
      const path = `${this.$APP_URL}:5000/subcategories`;
      axios
        .get(path)
        .then((res) => {
          console.log(res.data.data.subcategories);
          this.subcategories = res.data.data.subcategories;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    fetchEvents() {
    },
    getEventColor() {
      
    },
    setToday() {

    },
  },
  created() {
    this.getEvents();
    this.getSubcategories();
  },
};
</script>

<style scoped>
#today-view {
  height: 100vh;
  overflow-y: scroll;
  border: 5px solid red;
}

#calendar-view {
  height: 100vh;
  border: 5px solid blue;
}
</style>
