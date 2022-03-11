import Vue from 'vue';
import Router from 'vue-router';
import Ping from '../components/Ping.vue';
import CreateEvent from '../components/CreateEvent.vue';
import CreateTask from '../components/CreateTask.vue';
import Today from '../components/Today.vue';
import Success from '../components/Success.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/ping',
      name: 'Ping',
      component: Ping,
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
      component: Today,
    },
    {
      path: '/success',
      name: 'Success',
      component: Success,
    }, 
  ],
});
