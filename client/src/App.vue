<template>
  <v-app>
    <v-navigation-drawer
      app
      v-model="drawer"
      temporary
      width="325"
      color="green lighten-5"
      v-if="this.$store.getters.user.isLoggedIn"
    >
      <v-list
      rounded>
      <v-list-item>
        <v-list-item-title
        class="text-h5 text-center font-weight-bold">
        Categories</v-list-item-title>
      </v-list-item>

      <v-list-group
        :value="true"
        v-for="(category, i) in categories"
        :key="i"
        v-model="categoriesActive[i]"
      >
        <template v-slot:activator>
          <v-list-item-title v-text="category.name"></v-list-item-title>
        </template>
        <v-list-item-group
          :value="true"
          v-for="(subcategory, j) in category.subcategories"
          :key="j"
          no-action
          subgroup
        >
            <v-card :color="subcategory.color"
            dark
            width="275"
            height="30"
            class="ml-5 rounded-lg"
            >
              <v-list-text
              v-text="subcategory.name"
              class="font-weight-bold ml-3 text-h6">
              </v-list-text>
            </v-card>
        </v-list-item-group>
      </v-list-group>
    </v-list>
      <template absolute class="justify-end">
        <div class="pa-2">
          <v-btn color="blue darken-2" dark block @click="showCategoryView">
            Create Category
          </v-btn>
        </div>
        <div class="pa-2">
        <v-btn color="green darken-2" dark block @click="showSubcategoryView">
            Create Subcategory
          </v-btn>
      </div>
      </template>
    </v-navigation-drawer>

    <v-app-bar
      app
      color="deep-purple accent-2"
      dense
      v-if="this.$store.getters.user.isLoggedIn"
    >
      <v-app-bar-nav-icon
        color="white"
        @click.stop="drawer = !drawer"
      ></v-app-bar-nav-icon>

      <v-spacer></v-spacer>

      <v-img
        class="mx-auto logo"
        src="@/assets/Planit_Logo_white.png"
        @click="returnHome"
        max-height="60"
        max-width="75"
        containu
      ></v-img>

      <v-spacer></v-spacer>

      <v-menu
        bottom
        min-width="200px"
        rounded
        offset-y
      >
        <template v-slot:activator="{ on }">
          <v-btn icon x-large v-on="on">
            <v-btn icon>
              <v-icon color="white">mdi-account-circle</v-icon>
            </v-btn>
          </v-btn>
        </template>
        <v-card>
          <v-list-item-content class="justify-center">
            <div class="mx-auto text-center">
              <h3>{{ user.name }}</h3>
              <p class="text-caption mt-1">
                {{ user.email }}
              </p>
              <v-divider class="my-3"></v-divider>
              <v-btn depressed rounded text> Edit Account </v-btn>
              <v-divider class="my-3"></v-divider>
              <div class="text-center">
                <v-dialog v-model="dialog" width="500">
                  <template v-slot:activator="{ on, attrs }">
                    <v-btn color="red lighten-2" dark v-bind="attrs" v-on="on">
                      Logout
                    </v-btn>
                  </template>
                  <v-card>
                    <v-card-title class="text-h5 grey lighten-2">
                      Confirm Logout?
                    </v-card-title>
                    <v-divider></v-divider>

                    <v-card-actions>
                      <v-spacer></v-spacer>
                      <v-btn color="primary" text @click="logout()">
                        Yes
                      </v-btn>
                      <v-btn color="primary" text @click="dialog = false">
                        No
                      </v-btn>
                    </v-card-actions>
                  </v-card>
                </v-dialog>
              </div>
            </div>
          </v-list-item-content>
        </v-card>
      </v-menu>
    </v-app-bar>

    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
import axios from 'axios';
import { mapActions } from 'vuex';

export default {
  name: 'App',

  data: () => ({
    drawer: false,
    user: {},
    categories: [],
    categoriesActive: [],
    dialog: false,
    //
  }),
  methods: {
    returnHome() {
      this.$router.push('/home');
    },
    getUser() {
      const path = `api/user/${this.$store.getters.user.user}`;
      axios
        .get(path)
        .then((res) => {
          if (res.status === 200) {
            this.user = res.data.data.user;
            console.log(this.user);
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
    ...mapActions(['logoutUser']),
    async logout() {
      await this.logoutUser();
      this.dialog = false;
      this.$router.push('/login');
    },
    getCategoriesByUserId() {
      const path = `api/getCategoryByUserId/${this.$store.getters.user.user}`;
      axios
        .get(path)
        .then((res) => {
          if (res.status === 200) {
            this.categories = res.data.data.categories;
            for (let i = 0; i < this.categories.length; i += 1) {
              this.categoriesActive[i] = false;
            }
            console.log(res);
            console.log(this.categoriesActive);
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
    showCategoryView() {
      this.$router.push('/createcategory');
    },
    showSubcategoryView() {
      this.$router.push('/createsubcategory');
    },
  },
  created() {
    this.getUser();
    this.getCategoriesByUserId();
  },
};
</script>

<style scoped>
.logo {
  cursor: pointer;
}
</style>
