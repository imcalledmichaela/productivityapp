import axios from 'axios';
import BootstrapVue from 'bootstrap-vue';
import Vue from 'vue';
import Vuex from 'vuex';
import VueCookies from 'vue-cookies';
import App from './App.vue';
import router from './router';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';

Vue.use(BootstrapVue);
Vue.use(Vuex);
Vue.use(VueCookies);
Vue.prototype.$APP_URL = process.env.VUE_APP_URL;

Vue.config.productionTip = false;

axios.defaults.baseURL = process.env.VUE_APP_AUTH_URL;
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
      await axios.post('/register', user);
      await dispatch('fetchUser');
    },
    async loginUser({ dispatch }, user) {
      console.log('in loginuser');
      await axios.post('/login', user).then((response) => {
        console.log(response);
        console.log(Object.keys(response.headers));
      });
      await dispatch('fetchUser');
    },
    async fetchUser({ commit }) {
      await axios.get('/user')
        .then(({ data }) => commit('setUser', data));
    },
    async logoutUser({ commit }) {
      await axios.post('/logout');
      commit('logoutUserState');
    },
    isValidJwt(jwt) {
      if (!jwt || jwt.split('.'.length < 3)) {
        return false;
      }
      const data = JSON.parse(atob(jwt.split('.')[1]));
      const exp = new Date(data.exp * 1000); // JS deals with dates in milliseconds since epoch
      const now = new Date();
      return now < exp;
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
      this.$router.push('/404');
      break;
    default:
      break;
  }
  return error.response;
});

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount('#app');
