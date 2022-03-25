<template>
  <b-container fluid="sm">
    <b-jumbotron header="Login">
      <h2>Username:</h2>
      <b-row class="username_input">
            <b-col sm="5">
              <b-form-input
                sm="auto"
                id="input-1"
                v-model="form.username"
                type="name"
                placeholder="Username"
                required
              ></b-form-input>
            </b-col>
          </b-row>
        <h2>Password:</h2>
          <b-row class="password_input">
            <b-col sm="5">
              <b-form-input
                sm="auto"
                id="input-2"
                v-model="form.password"
                type="name"
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
                type="cancel"
                @click="returnToday"
                >Create User</b-button
              >
            </b-col>
          </b-row>
    </b-jumbotron>
  </b-container>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      form: {
        username_input: '',
        password_input: '',
      },
    };
  },
  methods: {
    onSubmit(event) {
      event.preventDefault();
      const payload = {
        name: this.form.username_input,
        subcategory_id: this.form.password_input,
      };
      this.login(payload);
    },
    login(payload) {
      const path = 'http://localhost:5000/login';
      axios
        .post(path, payload)
        .then(() => {
          console.log('User logged in');
          // do something after login
        })
        .catch((error) => {
          console.log(error);
          this.getTasks();
          this.$router.push('/error');
        });
    },
  },
};
</script>
