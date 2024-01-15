<template>
    <div>
      <h1>Contact Page</h1>
      <p>This is the contact page.</p>
      <button @click="showHomePage">Go to Home</button>
    </div>
  </template>
  
  <script>
  export default {
    methods: {
      showHomePage() {
        this.$emit("change-page", "home");
      },
    },
  };
  </script>
  