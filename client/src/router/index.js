import Vue from 'vue';
import Router from 'vue-router';
import PingPage from '../components/PingPage.vue';
import CreateEvent from '../components/CreateEvent.vue';
import CreateTask from '../components/CreateTask.vue';
import TodayPage from '../components/TodayPage.vue';
import SuccessPage from '../components/SuccessPage.vue';
import ErrorPage from '../components/ErrorPage.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/ping',
      name: 'Ping',
      component: PingPage,
    },
    {
      path: '/createEvent',
      name: 'CreateEvent',
      component: CreateEvent,
    },
    {
      path: '/createTask',
      name: 'CreateTask',
      component: CreateTask,
    },
    {
      path: '/today',
      name: 'Today',
      component: TodayPage,
    },
    {
      path: '/success',
      name: 'Success',
      component: SuccessPage,
    },
    {
      path: '/error',
      name: 'Error',
      component: ErrorPage,
    },
  ],
});
