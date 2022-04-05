<template>
  <v-col id="today-view" sm="3" md="3">
    <v-card class="rounded-lg pt-3" style="overflow: hidden">
      <v-sheet id="today-card" class="rounded-lg pt-3 mt-n7" height="93vh">
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
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      focus: '',
      today_day: new Date().toISOString().split('T')[0],
      today_events_tasks: [],
    };
  },
  methods: {
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
    getEventColor(event) {
      return event.color;
    },
    setToday() {
      this.focus = '';
    },
    updateToday() {
      const path = 'api/eventsAndTasksWithParams';
      const currDate = new Date(this.today_day);
      const start = currDate;
      const end = currDate;
      const bodyParameters = {
        start_time: start,
        end_time: end,
        user: this.$store.getters.user.user,
      };
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
