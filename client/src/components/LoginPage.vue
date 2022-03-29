<template>
  <v-container class="align-items:center">
    <v-form @submit="onSubmit">
      <v-card>
        <v-card-title>Login</v-card-title>
        <v-row class="username">
          <v-col sm="3">
              <v-card-text>Username:</v-card-text>
            </v-col>
              <v-col sm="5">
                <v-text-field
                  sm="auto"
                  id="input-1"
                  v-model="form.username"
                  placeholder="Username"
                  required
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row class="password">
              <v-col sm="3">
              <v-card-text>Password:</v-card-text>
            </v-col>
              <v-col sm="5">
                <v-text-field
                  sm="auto"
                  id="input-2"
                  v-model="form.password"
                  type="password"
                  placeholder="Password"
                  required
                ></v-text-field>
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
      </v-card>
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
