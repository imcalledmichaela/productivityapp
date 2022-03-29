<template>
  <div>
    <v-container fluid="md">
      <v-form @submit="onSubmit" v-if="show">
        <v-jumbotron header="Create User">
          <v-row class="name">
            <v-col sm="3">
              <label id="input-group-1" label-for="input-1">Name:</label>
            </v-col>
            <v-col sm="9">
              <v-form-input
                sm="auto"
                id="input-1"
                v-model="form.name"
                placeholder="Enter name"
                required
              ></v-form-input>
            </v-col>
          </v-row>

          <v-row class="username" style="padding-top: 15px">
            <v-col sm="3">
              <label id="input-group-2" label-for="input-6">Username:</label>
            </v-col>
            <v-col sm="9">
              <v-form-input
                id="input-2"
                v-model="form.username"
                placeholder="Enter username"
                required
              ></v-form-input>
            </v-col>
          </v-row>

          <v-row class="email" style="padding-top: 15px">
            <v-col sm="3">
              <label id="input-group-3" label-for="input-3">Email:</label>
            </v-col>
            <v-col sm="9">
              <v-form-input
                id="input-3"
                v-model="form.email"
                placeholder="Enter email"
                required
              ></v-form-input>
            </v-col>
          </v-row>

          <v-row class="password" style="padding-top: 15px">
            <v-col sm="3">
              <label id="input-group-4" label-for="input-4">Password:</label>
            </v-col>
            <v-col sm="9">
              <v-form-input
                id="input-4"
                type="password"
                v-model="form.password"
                placeholder="Enter password"
              ></v-form-input>
            </v-col>
          </v-row>
          <v-row style="padding-top: 15px">
            <v-col sm="5"> </v-col>
            <v-col sm="1">
              <v-btn type="submit" variant="primary">Create</v-btn>
            </v-col>
            <v-col sm="1">
              <v-btn
                @click="returnLogin"
                style="background-color: red"
                >Cancel</v-btn
              >
            </v-col>
            <v-col sm="5"> </v-col>
          </v-row>

        </v-jumbotron>
      </v-form>

      <v-card class="mt-3" header="Form Data Result">
        <pre class="m-0">{{ form }}</pre>
      </v-card>
    </v-container>
  </div>
</template>

<script>
// import axios from 'axios';
import { mapActions, mapGetters } from 'vuex';

export default {
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
  computed: {
    ...mapGetters({
      authUser: '/user',
    }),
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
    ...mapActions([
      'registerUser', ['/registerUser'],
    ]),
    // getUsers() {
    //   const path = `${this.$APP_URL}/users`;
    //   axios
    //     .get(path)
    //     .then((res) => {
    //       this.users = res.data.name;
    //     })
    //     .catch((error) => {
    //       console.log(error);
    //     });
    // },
    async addUser(payload) {
      // const path = `${this.$APP_URL}/users`;
      // axios
      //   .post(path, payload)
      //   .then(() => {
      //     this.getUsers();
      //     this.$router.push('/success');
      //   })
      //   .catch((error) => {
      //     console.log(error);
      //     this.getUsers();
      //     this.$router.push('/error');
      //   });
      await this.registerUser(payload).then(() => {
        if (this.authUser.authenticated) {
          this.$router.push('/today');
        } else {
          this.user = {
            username: null,
            password: null,
          };
        }
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
