import Vue from 'vue';
import App from './App.vue';
import TodayComponent from './components/TodayComponent.vue';
import router from './router';
import vuetify from './plugins/vuetify';
import store from './store';
import NavigationDrawer from './components/NavigationDrawer.vue';

Vue.config.productionTip = false;
Vue.component('today-component', TodayComponent);
Vue.component('navigation-drawer', NavigationDrawer);

new Vue({
  router,
  store,
  vuetify,
  render: (h) => h(App),
}).$mount('#app');
