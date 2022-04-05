<template>
  <v-container fluid class="orange lighten-5 fill-height">
    <v-row id="content" class="justify-center">
      <v-col id="today-view" sm="3" md="3">
        <v-card class="rounded-lg pt-3" style="overflow:hidden">
        <v-sheet id="today-card" class="rounded-lg pt-3 mt-n7" height="98vh">
          <v-calendar
            ref="today_calendar"
            color="primary"
            type="day"
            :now="today_day"
            :events="today_events_tasks"
            :event-color="getEventColor"
            @change="updateToday"
          >
          </v-calendar>
        </v-sheet>
        </v-card>
      </v-col>

      <v-col id="calendar-view" sm="8" md="8">
        <v-card class="rounded-lg pt-3" style="overflow:hidden">
        <v-sheet height="10vh">
          <v-toolbar
            flat
          >
            <v-btn
              outlined
              class="mr-4"
              color="grey darken-2"
              @click="setToday"
            >
              Today
            </v-btn>
            <v-btn
              fab
              text
              small
              color="grey darken-2"
              @click="prev"
            >
              <v-icon small>
                mdi-chevron-left
              </v-icon>
            </v-btn>
            <v-btn
              fab
              text
              small
              color="grey darken-2"
              @click="next"
            >
              <v-icon small>
                mdi-chevron-right
              </v-icon>
            </v-btn>
            <v-toolbar-title v-if="$refs.calendar">
              {{ $refs.calendar.title }}
            </v-toolbar-title>
            <v-spacer></v-spacer>
          </v-toolbar>
        </v-sheet>
        <v-sheet height="85vh">
          <v-calendar
            ref="calendar"
            v-model="focus"
            color="primary"
            :events="events"
            :event-color="getEventColor"
            :type="type"
            @click:event="showEvent"
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
                <v-card-subtitle>Description:</v-card-subtitle>
                <v-card-text>{{selectedEvent.details}}</v-card-text>
                <v-card-subtitle>Location:</v-card-subtitle>
                <v-card-text>{{selectedEvent.location}}</v-card-text>
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
        </v-sheet>
        </v-card>
      </v-col>
    </v-row>
    <v-speed-dial
      class="mr-5 mb-5"
      v-model="fab"
      absolute
      bottom
      right
      slide-y-reverse-transition
    >
      <template v-slot:activator>
        <v-btn
          v-model="fab"
          color="green darken-2"
          dark
          fab
        >
          <v-icon v-if="fab">
            mdi-close
          </v-icon>
          <v-icon v-else>
            mdi-plus
          </v-icon>
        </v-btn>
      </template>
      <v-btn
        fab
        dark
        small
        @click="goToCreateTask"
        color="blue"
      >
        <v-icon>mdi-checkbox-marked-circle-plus-outline</v-icon>
      </v-btn>
      <v-btn
        fab
        small
        dark
        @click="goToCreateEvent"
        color="purple"
      >
        <v-icon>mdi-calendar</v-icon>
      </v-btn>
    </v-speed-dial>
  </v-container>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      selectedEvent: {},
      selectedElement: null,
      selectedOpen: false,
      events: [],
      focus: '',
      type: 'month',
      today_day: new Date(new Date().getTime() - (new Date().getTimezoneOffset()*60*1000)).toISOString().split('T')[0],
      today_events_tasks: [],
    };
  },
  methods: {
    getEvents(start, end) {
      const path = 'api/eventsWithParams';
      const bodyParameters = {
        start_time: start,
        end_time: end,
        user: this.$store.getters.user.user,
      };
      axios
        .post(path, bodyParameters)
        .then((res) => {
          this.events = res.data.data.events;
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
        console.log(this.selectedEvent);
        console.log(this.today_events_tasks);
        console.log(this.events);
        this.selectedElement = nativeEvent.target;
        requestAnimationFrame(() => requestAnimationFrame(() => {
          this.selectedOpen = true;
        }));
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
      console.log(start.date);
      const min = start.date;
      const max = end.date;
      this.getEvents(min, max);
    },
    goToCreateTask() {
      this.$router.push('/createtask');
    },
    goToCreateEvent() {
      this.$router.push('/createevent');
    },
    updateToday() {
      console.log('in update toda');
      console.log(this.today_day);
      const path = 'api/eventsAndTasksWithParams';
      const bodyParameters = {
        start_time: this.today_day,
        end_time: this.today_day,
        user: this.$store.getters.user.user,
      };
      console.log(bodyParameters);
      axios
        .post(path, bodyParameters)
        .then((res) => {
          console.log(res);
          this.today_events_tasks = res.data.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
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
