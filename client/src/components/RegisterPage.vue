<template>
  <div>
    <b-container fluid="md">
      <b-form @submit="onSubmit" v-if="show">
        <b-jumbotron header="Create User">
          <b-row class="name">
            <b-col sm="3">
              <label id="input-group-1" label-for="input-1">Name:</label>
            </b-col>
            <b-col sm="9">
              <b-form-input
                sm="auto"
                id="input-1"
                v-model="form.name"
                placeholder="Enter name"
                required
              ></b-form-input>
            </b-col>
          </b-row>

          <b-row class="username" style="padding-top: 15px">
            <b-col sm="3">
              <label id="input-group-2" label-for="input-6">Username:</label>
            </b-col>
            <b-col sm="9">
              <b-form-input
                id="input-2"
                v-model="form.username"
                placeholder="Enter username"
                required
              ></b-form-input>
            </b-col>
          </b-row>

          <b-row class="email" style="padding-top: 15px">
            <b-col sm="3">
              <label id="input-group-3" label-for="input-3">Email:</label>
            </b-col>
            <b-col sm="9">
              <b-form-input
                id="input-3"
                v-model="form.email"
                placeholder="Enter email"
                required
              ></b-form-input>
            </b-col>
          </b-row>

          <b-row class="password" style="padding-top: 15px">
            <b-col sm="3">
              <label id="input-group-4" label-for="input-4">Password:</label>
            </b-col>
            <b-col sm="9">
              <b-form-input
                id="input-4"
                type="password"
                v-model="form.password"
                placeholder="Enter password"
              ></b-form-input>
            </b-col>
          </b-row>
          <b-row style="padding-top: 15px">
            <b-col sm="5"> </b-col>
            <b-col sm="1">
              <b-button type="submit" variant="primary">Create</b-button>
            </b-col>
            <b-col sm="1">
              <b-button
                @click="returnLogin"
                style="background-color: red"
                >Cancel</b-button
              >
            </b-col>
            <b-col sm="5"> </b-col>
          </b-row>

        </b-jumbotron>
      </b-form>

      <b-card class="mt-3" header="Form Data Result">
        <pre class="m-0">{{ form }}</pre>
      </b-card>
    </b-container>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  APP_URL: process.env.VUE_APP_URL,
  data() {
    return {
      form: {
        name: '',
        username: '',
        email: '',
        password: '',
      },
      show: true,
    };
  },
  methods: {
    onSubmit(event) {
      event.preventDefault();
      const payload = {
        name: this.form.name,
        username: this.form.username,
        email: this.form.email,
        password: this.form.password,
      };

      this.addUser(payload);
      this.initForm();
    },
    getUsers() {
      const path = `${this.$APP_URL}:5000/users`;
      axios
        .get(path)
        .then((res) => {
          this.users = res.data.name;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    addUser(payload) {
      const path = `${this.$APP_URL}:5000/users`;
      axios
        .post(path, payload)
        .then(() => {
          this.getUsers();
          this.$router.push('/success');
        })
        .catch((error) => {
          console.log(error);
          this.getUsers();
          this.$router.push('/error');
        });
    },
    initForm() {
      this.form.name = '';
      this.form.username = '';
      this.form.email = '';
      this.form.password = '';
    },

    returnLogin() {
      this.$router.push('/login');
    },
  },
};
</script>
