<template>
  <v-container fluid class="orange lighten-5 fill-height">
    <v-row id="content" class="justify-center">
      <v-col id="today-view" sm="3" md="3">
        <v-sheet id="today-card" class="rounded-lg pt-3" height="100vh">
          <v-calendar color="primary" type="day">
            <template v-slot:day-header="{ present }">
              <template v-if="present" class="text-center"> Today </template>
            </template>

            <template v-slot:day-body="{ date, week }">
              <div
                class="v-current-time"
                :class="{ first: date === week[0].date }"
                :style="{ top: nowY }"
              ></div>
            </template>

            <!--
            <template v-slot:interval="{ hour }">
              <div class="text-center">{{ hour }} o'clock</div>
            </template>
            -->
          </v-calendar>
        </v-sheet>
      </v-col>

      <v-col id="calendar-view" sm="8" md="8">
        <v-card id="calendar-card" class="rounded-lg pt-3"> </v-card>
        <v-calendar
          ref="calendar"
          v-model="focus"
          color="primary"
          :events="events"
          :event-color="getEventColor"
          :type="month"
          @click:event="showEvent"
          @click:more="viewDay"
          @click:date="viewDay"
          @change="updateRange"
        ></v-calendar>
        <v-menu
          v-model="selectedOpen"
          :close-on-content-click="false"
          :activator="selectedElement"
          offset-x
        >
          <v-card
            color="grey lighten-4"
            min-width="350px"
            flat
          >
            <v-toolbar
              :color="selectedEvent.color"
              dark
            >
              <v-btn icon>
                <v-icon>mdi-pencil</v-icon>
              </v-btn>
              <v-toolbar-title v-html="selectedEvent.name"></v-toolbar-title>
              <v-spacer></v-spacer>
              <v-btn icon>
                <v-icon>mdi-heart</v-icon>
              </v-btn>
              <v-btn icon>
                <v-icon>mdi-dots-vertical</v-icon>
              </v-btn>
            </v-toolbar>
            <v-card-text>
              <span v-html="selectedEvent.details"></span>
            </v-card-text>
            <v-card-actions>
              <v-btn
                text
                color="secondary"
                @click="selectedOpen = false"
              >
                Cancel
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-menu>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      subcategories: [this.getSubcategories()],
      selectedEvent: {},
      selectedElement: null,
      selectedOpen: false,
      events: [],
    };
  },
  methods: {
    getEvents(start, end) {
      const path = 'api/events';
      const bodyParameters = {
        start_time: start,
        end_time: end,
        user: this.$store.getters.user.user,
      };
      axios
        .get(path, bodyParameters)
        .then((res) => {
          console.log(res.data.data.events);
          this.events = res.data.data.events;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    getSubcategories() {
      const path = 'api/subcategories';
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
    getCurrentTime() {
      return this.cal
        ? this.cal.times.now.hour * 60 + this.cal.times.now.minute
        : 0;
    },
    scrollToTime() {
      const time = this.getCurrentTime();
      const first = Math.max(0, time - (time % 30) - 30);

      this.cal.scrollToTime(first);
    },
    updateTime() {
      setInterval(() => this.cal.updateTimes(), 60 * 1000);
    },
    fetchEvents() {},
    getEventColor() {},
    setToday() {},
  },
  created() {
    this.getEvents();
    this.getSubcategories();
  },
  getEventColor(event) {
    return event.color;
  },
  setToday() {
    this.focus = '';
  },
  prev() {
    this.$refs.calendar.prev();
  },
  next() {
    this.$refs.calendar.next();
  },
  showEvent({ nativeEvent, event }) {
    const open = () => {
      this.selectedEvent = event;
      this.selectedElement = nativeEvent.target;
      requestAnimationFrame(() => requestAnimationFrame(() => this.selectedOpen = true));
    };
    if (this.selectedOpen) {
      this.selectedOpen = false;
      requestAnimationFrame(() => requestAnimationFrame(() => open()));
    } else {
      open();
    }
    nativeEvent.stopPropagation();
  },
  updateRange({ start, end }) {
    const min = new Date(`${start.date}T00:00:00`);
    const max = new Date(`${end.date}T23:59:59`);
    this.getEvents(min, max);
  },
};
</script>

<style scoped>
#today-card {
  height: 100%;
}

#calendar-card {
  height: 100vh;
}

/*
#calendar-view {
  height: 100vh;
  border: 5px solid blue;
}
*/
</style>
