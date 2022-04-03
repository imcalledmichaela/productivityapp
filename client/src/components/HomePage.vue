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
      events: [],
    };
  },
  methods: {
    getEvents() {
      const path = 'api/events';
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
