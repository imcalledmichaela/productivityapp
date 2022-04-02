<template>
  <v-container fluid class="orange lighten-5 fill-height">
    <v-row class="wrap">
      <v-col md="5" sm="7" class="ma-auto">
        <v-card class="rounded-lg pt-3">
          <v-form @submit="onSubmit" v-if="show">
            <v-row>
              <v-col sm="10" md="10" class="ma-auto">
                <v-card-title class="ml-n5 mb-3 mt-5 display-2 font-weight-bold"
                  >Create User</v-card-title
                >
              </v-col>
            </v-row>
            <v-row class="name">
              <v-col sm="10" md="10" class="ma-auto">
                <v-text-field
                  class="rounded-lg"
                  id="input-1"
                  v-model="form.name"
                  label="Enter name"
                  outlined
                  required
                ></v-text-field>
              </v-col>
            </v-row>

            <v-row class="email">
              <v-col sm="10" md="10" class="ma-auto">
                <v-text-field
                  class="mt-n5 rounded-lg"
                  id="input-3"
                  v-model="form.email"
                  label="Enter email"
                  outlined
                  required
                ></v-text-field>
              </v-col>
            </v-row>

            <v-row class="username">
              <v-col sm="10" md="10" class="ma-auto">
                <v-text-field
                  class="mt-n5 rounded-lg"
                  id="input-2"
                  v-model="form.username"
                  label="Enter username"
                  outlined
                  required
                ></v-text-field>
              </v-col>
            </v-row>

            <v-row class="password">
              <v-col sm="10" md="10" class="ma-auto">
                <v-text-field
                  class="mt-n5 rounded-lg"
                  id="input-4"
                  type="password"
                  v-model="form.password"
                  label="Enter password"
                  outlined
                  required
                ></v-text-field>
              </v-col>
            </v-row>

            <v-row>
              <v-card-actions class="ma-auto mt-n5 mb-5">
                <v-col class="justify-start">
                  <v-btn plain @click="returnLogin" color="red">Cancel</v-btn>
                </v-col>
                <v-col class="justify-end">
                  <v-btn type="submit" color="blue" dark variant="primary"
                    >Create</v-btn
                  >
                </v-col>
              </v-card-actions>
            </v-row>
          </v-form>
        </v-card>
      </v-col>
    </v-row>
    <v-row>
      <v-col md="5" sm="7" class="mt-10 ma-auto">
        <v-card class="mt-3" header="Form Data Result">
          <pre class="m-0">{{ form }}</pre>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
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
      show: false,
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
    ...mapActions(['registerUser', ['/registerUser']]),
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
        if (this.$store.state.isLoggedIn) {
          this.$router.push('/home');
        } else {
          console.log('authenticationfailed');
          this.$router.push('/login');
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
