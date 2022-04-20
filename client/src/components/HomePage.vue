<template>
  <v-container fluid class="orange lighten-5 fill-height">
    <v-row id="content" class="wrap justify-center">
      <today-component :today=today_day></today-component>

      <v-col class="hidden-xs-only" id="calendar-view" sm="8" md="8">
        <v-card class="rounded-lg pt-3" style="overflow:hidden">
        <v-sheet height="8vh">
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
            <v-spacer></v-spacer>
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
            <v-spacer></v-spacer>
            <v-toolbar-title class="justify-center" v-if="$refs.calendar">
              {{ $refs.calendar.title }}
            </v-toolbar-title>
            <v-spacer></v-spacer>
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
            <v-spacer></v-spacer>
          </v-toolbar>
        </v-sheet>
        <v-sheet height="81.5vh">
          <v-calendar
            ref="calendar"
            v-model="focus"
            color="primary"
            :events="events"
            :event-color="getEventColor"
            :type="type"
            @click:event="showEvent"
            @click:date="showDay"
            @change="updateRange"
          ></v-calendar>
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
        <v-fab-transition>
          <v-btn
            v-show="!hidden"
            v-if="fab"
            v-model="fab"
            color="red darken-2"
            dark
            fab
            elevation="10"
          >
            <v-icon>mdi-close</v-icon>
          </v-btn>
          <v-btn x-large rounded color="green darken-2" dark
            v-else
            v-model="fab"
            elevation="10"
            height=56
          >
            <v-icon class="mr-2">mdi-plus</v-icon>
            Create New
          </v-btn>
        </v-fab-transition>
      </template>
      <v-tooltip nudge-left="6" :disabled="tooltipsDisabled" left color="blue"
      :value="tooltips">
        <template>
          <v-btn
            fab
            color="blue"
            dark
            small
            @click="goToCreateTask"
            slot="activator"
          >
            <v-icon>mdi-checkbox-marked-circle-plus-outline</v-icon>
          </v-btn>
        </template>
        <span>Create Task</span>
      </v-tooltip>
      <v-tooltip nudge-left="6" :disabled="tooltipsDisabled" left color="purple"
      :value="tooltips">
        <template>
          <v-btn
            fab
            small
            dark
            @click="goToCreateEvent"
            color="purple"
            slot="activator"
          >
            <v-icon>mdi-calendar</v-icon>
          </v-btn>
        </template>
        <span>Create Event</span>
      </v-tooltip>
    </v-speed-dial>
  </v-container>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      events: [],
      focus: '',
      type: 'month',
      today_day: new Date(new Date().getTime() - (new Date().getTimezoneOffset() * 60 * 1000)).toISOString().split('T')[0],
      today_events_tasks: [],
      fab: false,
      tooltips: true,
      tooltipsDisabled: false,
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
    showEvent({ event }) {
      console.log(event.event);
      if (typeof event.event !== 'undefined') {
        this.$router.push({ name: 'ShowEvent', query: { event_id: event.event } });
      }
    },
    showDay(dayTime) {
      this.today_day = dayTime.date;
    },
    updateRange({ start, end }) {
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

/* .fab-text-custom {
  position: absolut;
  right: 50px;
  background-color: rgba(0, 0, 0, 0.5);
  padding: 10px;
  box-shadow: 0px 3px 5px -1px rgba(0, 0, 0, 0.2), 0px 6px 10px 0px rgba(0, 0, 0, 0.14),
  0px 1px 18px 0px rgba(0, 0, 0, 0.12);
  border-radius: 2px;
} */

/*
#calendar-view {
  height: 100vh;
  border: 5px solid blue;
}
*/
</style>
