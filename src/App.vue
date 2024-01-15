<template>
  <div id="app">
    <component :is="currentPage" @change-page="changePage" />
  </div>
</template>

<script>
import Home from "./Home.vue";
import Contact from "./Contact.vue";
import Demo from "./Demo.vue";

export default {
  data() {
    return {
      currentPage: "home",
    };
  },
  components: {
    Home,
    Contact,
    Demo,
  },
  methods: {
    changePage(page) {
      this.currentPage = page;
    },
  },
};
</script>

<style>
/* Add your styles here if needed */
</style>