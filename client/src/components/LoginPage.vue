<template>
  <b-container fluid="sm">
    <b-form @submit="onSubmit">
      <b-jumbotron header="Login">
        <h2>Username:</h2>
        <b-row class="username">
              <b-col sm="5">
                <b-form-input
                  sm="auto"
                  id="input-1"
                  v-model="form.username"
                  placeholder="Username"
                  required
                ></b-form-input>
              </b-col>
            </b-row>
          <h2>Password:</h2>
            <b-row class="password">
              <b-col sm="5">
                <b-form-input
                  sm="auto"
                  id="input-2"
                  v-model="form.password"
                  type="password"
                  placeholder="Password"
                  required
                ></b-form-input>
              </b-col>
            </b-row>

          <b-row style="padding-top: 15px">
              <b-col sm="1">
                <b-button type="submit" variant="primary">Login</b-button>
              </b-col>
              <b-col sm="2">
                <b-button
                  @click="goRegister"
                  >Create User</b-button
                >
              </b-col>
            </b-row>
      </b-jumbotron>
    </b-form>
  </b-container>
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
    };
  },
  computed: {
    ...mapGetters([
      'user', ['/user'],
    ]),
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
    ...mapActions([
      'loginUser', ['/loginUser'],
    ]),
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
        if (this.user.isLoggedIn) {
          this.$router.push('/today');
        } else {
          console.log('authenticationfailed');
          this.user = {
            username: null,
            password: null,
          };
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
};
</script>
