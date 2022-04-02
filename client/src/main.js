import axios from 'axios';
import Vue from 'vue';
import Vuex from 'vuex';
import VueCookies from 'vue-cookies';
import App from './App.vue';
import router from './router';
import vuetify from './plugins/vuetify';

Vue.use(Vuex);
Vue.use(VueCookies);

Vue.config.productionTip = false;

axios.defaults.auth = {
  username: '',
  password: '',
};

const store = new Vuex.Store({
  state: {
    user: {},
    isLoggedIn: false,
  },
  getters: {
    isLoggedIn: (state) => state.isLoggedIn,
    user: (state) => state.user,
  },
  actions: {
    async registerUser({ dispatch }, user) {
      await axios.post('api/auth/register', user);
      await dispatch('fetchUser');
    },
    async loginUser({ dispatch }, user) {
      console.log('in loginuser');
      await axios.post('api/auth/login', user).then((response) => {
        console.log(response);
      });
      await dispatch('fetchUser');
    },
    async fetchUser({ commit }) {
      await axios.get('api/auth/user')
        .then(({ data }) => {
          console.log(data);
          commit('setUser', data);
        });
    },
    async logoutUser({ commit }) {
      await axios.post('api/auth/logout');
      commit('logoutUserState');
    },
  },
  mutations: {
    setUser(state, user) {
      state.isLoggedIn = true;
      state.user = user;
    },
    logoutUserState(state) {
      state.isLoggedIn = false;
      state.user = {};
    },
  },
});

new Vue({
  router,
  store,
  vuetify,
  render: (h) => h(App),
}).$mount('#app');

const COOKIE_EXPIRED_MSG = 'Token has expired';
axios.interceptors.response.use((response) => (response), async (error) => {
  const errorMessage = error.response.data.msg;
  const err = error;
  switch (err.response.status) {
    case 401:
      if (!err.config.retry && errorMessage === COOKIE_EXPIRED_MSG) {
        err.config.retry = true;
        axios.defaults.xsrfCookieName = 'csrf_refresh_token';
        await axios.post('/refresh_token');
        axios.defaults.xsrfCookieName = 'csrf_access_token';
        return axios(err.config);
      }
      break;
    case 404:
      this.$router.push('/error');
      break;
    default:
      break;
  }
  return error.response;
});
