<template>
  <v-container fluid class="orange lighten-5 fill-height">
    <v-alert
      v-if="show"
      color="red"
      type="error"
      outlined
      dark
      class="ma-auto"
    >
      {{ alert_message }}
    </v-alert>
    <v-row class="wrap">
      <v-col md="5" sm="7" class="ma-auto">
        <v-card class="rounded-lg pt-3">
          <v-card-title class="mb-3 justify-center display-3 font-weight-bold"
            >Login</v-card-title
          >
          <v-form @submit="onSubmit">
            <v-row class="username">
              <v-col sm="8" md="8" class="ma-auto">
                <v-text-field
                  class="rounded-lg"
                  id="input-1"
                  v-model="form.username"
                  label="Username"
                  outlined
                  required
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row class="password">
              <v-col sm="8" md="8" class="ma-auto">
                <v-text-field
                  class="mt-n5 rounded-lg"
                  id="input-2"
                  v-model="form.password"
                  type="password"
                  label="Password"
                  outlined
                  required
                ></v-text-field>
              </v-col>
            </v-row>

            <v-row>
              <v-card-actions class="ma-auto mt-n5 mb-5">
                <v-col class="justify-start">
                  <v-btn plain color="blue" @click="goRegister"
                    >Create User</v-btn
                  >
                </v-col>
                <v-col class="justify-end">
                  <v-btn color="green" dark type="submit" variant="primary"
                    >Login</v-btn
                  >
                </v-col>
              </v-card-actions>
            </v-row>
          </v-form>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';

export default {
  // APP_URL: process.env.VUE_APP_URL,
  data() {
    return {
      form: {
        username: '',
        password: '',
      },
      show: false,
      alert_message: '',
    };
  },
  computed: {
    ...mapGetters(['user', ['/user']]),
    user: {
      get() {
        return this.$store.user;
      },
      set(user) {
        return user;
      },
    },
  },
  methods: {
    onSubmit(event) {
      event.preventDefault();
      const payload = {
        username: this.form.username,
        password: this.form.password,
      };
      this.login(payload);
      this.initForm();
    },
    ...mapActions(['loginUser', ['/loginUser']]),
    ...mapActions(['logoutUser', ['/logoutUser']]),
    async login(payload) {
      // const path = `${this.$APP_URL}/login`;
      // axios
      //   .post(path, payload)
      //   .then(() => {
      //     console.log('User logged in');
      //     // do something after login
      //   })
      //   .catch((error) => {
      //     console.log(error);
      //     this.getTasks();
      //     this.$router.push('/error');
      //   });
      console.log(payload);
      await this.loginUser(payload).then(() => {
        if (this.$store.state.isLoggedIn) {
          this.$router.push('/home');
        } else {
          console.log('authenticationfailed');
          this.$router.push('/login');
          this.user = {
            username: null,
            password: null,
          };
          this.show = true;
          this.alert_message = 'Unable to log in! Please check credentials again!';
        }
      });
    },
    goRegister() {
      this.$router.push('/register');
    },
    initForm() {
      this.form.username = '';
      this.form.password = '';
    },
  },
  async mounted() {
    console.log('hello');
    await this.logoutUser();
  },
};
</script>
