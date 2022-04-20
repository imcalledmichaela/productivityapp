<template>
  <v-app>
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

      <v-menu bottom min-width="200px" rounded offset-y>
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

    <v-navigation-drawer
      app
      v-model="drawer"
      width="325"
      color="green lighten-5"
      v-if="this.$store.getters.user.isLoggedIn"
      temporary
    >
      <div v-html="this.getCategoriesByUserId()"></div>
      <!--Heading-->
      <v-list-item>
        <v-list-item-content>
          <v-list-item-title class="text-h5 text-center font-weight-bold">
            Categories
          </v-list-item-title>
        </v-list-item-content>
      </v-list-item>

      <!--Categories List-->
      <v-list expand nav>
        <v-list-group
        v-for="(category, index) in categories"
        :key="index"
        v-model="categoriesActive[index]">

        <!--Categories Title-->
        <template v-slot:activator>
          <v-list-item-action class="align-self-start">
            <v-tooltip right>
              <template v-slot:activator="{ on, attrs }">
                <v-btn
                fab
                rounded
                x-small
                v-bind="attrs"
                v-on="on"
                @click="enableCreateSubcategory(index)"
                >
                  <v-icon>mdi-plus</v-icon>
                </v-btn>
              </template>
            <span>Create Subcategory</span>
            </v-tooltip>
          </v-list-item-action>

          <!--Title-->
          <v-list-item-content>
            <v-list-item-title v-text="category.name">
            </v-list-item-title>
          </v-list-item-content>
        </template>

      <v-form
      @submit="onSubmitSubCategory"
      v-if="createSubcategoryActive[index]">
      <v-list-item>
        <v-list-item-content>
          <v-text-field
          label="Enter Subcategory Name"
          v-model="subcategoryForm.name"
          class="rounded-lg mb-0"
          required
          solo
          >
          </v-text-field>
        </v-list-item-content>

          <v-list-item-action class="mt-n4">
            <v-tooltip left>
              <template v-slot:activator="{ on, attrs }">
                <v-btn
                fab
                rounded
                x-small
                v-bind="attrs"
                v-on="on"
                type="submit"
                color="green"
                dark
                >
                  <v-icon>mdi-check</v-icon>
                </v-btn>
              </template>
            <span>Create</span>
            </v-tooltip>
          </v-list-item-action>
        </v-list-item>
      </v-form>

          <!--Subcategory Cards-->
          <v-list-item-group
            :value="true"
            v-for="(subcategory, j) in category.subcategories"
            :key="j"
            no-action
            subgroup
            >
            <v-card
              :color="subcategory.color"
              dark
              width="275"
              height="30"
              class="ml-5 rounded-lg"
            >
              <v-card-title
                v-text="subcategory.name"
                class="font-weight-bold pt-0"
              >
              </v-card-title>
            </v-card>
          </v-list-item-group>
        </v-list-group>
      </v-list>

      <!--Create Category Field-->
      <v-form
      @submit="onSubmit"
      v-if="this.createCategoryButton">
      <v-list-item>
        <v-list-item-content>
          <v-text-field
          label="Enter Category Name"
          v-model="categoryForm.name"
          class="rounded-lg"
          required
          solo>
          </v-text-field>
        </v-list-item-content>

          <v-list-item-action class="mt-n4">
            <v-tooltip left>
              <template v-slot:activator="{ on, attrs }">
                <v-btn
                fab
                rounded
                x-small
                v-bind="attrs"
                v-on="on"
                type="submit"
                color="green"
                dark
                >
                  <v-icon>mdi-check</v-icon>
                </v-btn>
              </template>
            <span>Create</span>
            </v-tooltip>
          </v-list-item-action>
      </v-list-item>
      </v-form>

      <!--Create Category Button-->
      <template v-slot:append>
        <div class="pa-2">
          <v-btn class="rounded-lg" block dark
          color="blue" @click="enableCreateCategory">
            Create Category
          </v-btn>
        </div>
      </template>
    </v-navigation-drawer>

    <v-content>
      <router-view />
    </v-content>
  </v-app>
</template>

<script>
import axios from 'axios';
import { mapActions } from 'vuex';

export default {
  name: 'App',

  data() {
    return {
      drawer: false,
      user: {},
      categories: [],
      categoriesActive: [],
      createSubcategoryActive: [],
      dialog: false,
      createCategoryButton: false,
      categoryForm: {
        name: '',
      },
      subcategoryForm: {
        name: '',
        category: '',
        color: '',
      },
    };
  },
  methods: {
    onSubmit(event) {
      event.preventDefault();
      if (this.categoryForm.name !== '') {
        const payload = {
          name: this.categoryForm.name,
          user_id: this.$store.getters.user.user,
        };
        this.addCategory(payload);
      } else {
        this.$router.push('/error');
      }
    },
    onSubmitSubCategory(event) {
      event.preventDefault();
      if (this.subcategoryForm.name !== '') {
        const payload = {
          name: this.subcategoryForm.name,
          category_id: this.subcategoryForm.category,
          color: 'blue',
        };
        this.addSubcategory(payload);
      } else {
        this.$router.push('/error');
      }
    },
    addCategory(payload) {
      const path = 'api/categories';
      axios
        .post(path, payload)
        .then(() => {
          this.getCategoriesByUserId();
          this.createCategoryButton = false;
        })
        .catch((error) => {
          console.log(error);
          this.$router.push('/error');
        });
    },
    addSubcategory(payload) {
      const path = 'api/subcategories';
      axios
        .post(path, payload)
        .then(() => {
          this.getCategoriesByUserId();
        })
        .catch((error) => {
          console.log(error);
          this.$router.push('/error');
        });
    },
    initForm() {
      this.categoryForm.name = '';
      this.subcategoryForm.name = '';
    },
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
            if (this.categoriesActive.length === 0) {
              for (let i = 0; i < this.categories.length; i += 1) {
                this.categoriesActive[i] = false;
                this.createSubcategoryActive[i] = false;
              }
            }
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
    enableCreateCategory() {
      this.createCategoryButton = !this.createCategoryButton;
    },
    enableCreateSubcategory(index) {
      if (this.createSubcategoryActive[index] === false) {
        this.createSubcategoryActive[index] = true;
        this.subcategoryForm.category = this.categories[index].category_id;
        console.log('in enable create subcategory - setting subcategoryform category');
        console.log(this.subcategoryForm.category);
      } else {
        this.createSubcategoryActive[index] = false;
      }
      console.log('createSubcategoryActive array');
      console.log(this.createSubcategoryActive);
    },
    toggleCategoriesActive(index) {
      this.categoriesActive[index] = !this.categoriesActive[index];
    },
  },
  mounted() {
    this.getUser();
    this.getCategoriesByUserId();
  },
  computed: {
    /*
    showCreateSubcategoryActive(index) {
      return this.createSubcategoryActive[index];
    },
    */
  },
};
</script>

<style scoped>
.logo {
  cursor: pointer;
}
</style>
