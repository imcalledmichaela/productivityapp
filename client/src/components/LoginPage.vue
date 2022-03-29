<template>
  <v-container fluid="sm">
    <v-form @submit="onSubmit">
      <v-jumbotron header="Login">
        <h2>Username:</h2>
        <v-row class="username">
              <v-col sm="5">
                <v-form-input
                  sm="auto"
                  id="input-1"
                  v-model="form.username"
                  placeholder="Username"
                  required
                ></v-form-input>
              </v-col>
            </v-row>
          <h2>Password:</h2>
            <v-row class="password">
              <v-col sm="5">
                <v-form-input
                  sm="auto"
                  id="input-2"
                  v-model="form.password"
                  type="password"
                  placeholder="Password"
                  required
                ></v-form-input>
              </v-col>
            </v-row>

          <v-row style="padding-top: 15px">
              <v-col sm="1">
                <v-btn type="submit" variant="primary">Login</v-btn>
              </v-col>
              <v-col sm="2">
                <v-btn
                  @click="goRegister"
                  >Create User</v-btn
                >
              </v-col>
            </v-row>
      </v-jumbotron>
    </v-form>
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
