<script>
import Contact from "./Demo.vue";

export default {
  // reactive state
  data() {
    return {
      data: null,
      columns:[
        {
          title: 'Model',
          dataIndex: 'title',
          key: 'title',
        },
        {
          title: 'Seats',
          dataIndex: 'Seats',
          key: 'Seats',
        },
        {
          title: 'Price',
          dataIndex: 'Price',
          key: 'Price',
        },
      ]
    }
  },



  // functions that mutate state and trigger updates
  methods: {
    increment() {
    },
    showHomePage() {
        this.$emit("change-page", "Home");
      },
    showDemoPage() {
      this.$emit("change-page", "Demo");
    },
  },

  // lifecycle hooks
  mounted() {
    fetch("http://127.0.0.1:5000/getData")
        .then(response => response.json())
        .then(data => {
          this.data = data;
          //console.log(data);
        })
        .catch(error => {
          console.error("Error fetching data:", error);
        });

  }
}
</script>

<template>
  
  
    <a-button @click="showHomePage">Home</a-button >

    <a-table :columns="columns" :data-source="data" />
  
</template>