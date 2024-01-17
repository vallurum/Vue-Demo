<template>
    <div>
      <a-button @click="showHomePage"><- Home</a-button>
      
      <h2>Meghana Valluru</h2>
      <a-button @click="downloadFile">Donwload</a-button>
    </div>
  </template>
  
  <script>
  export default {
    methods: {
      showHomePage() {
        this.$emit("change-page", "home");
      },

      async downloadFile() {
      const url = 'http://localhost:5000/download-docx';  // Adjust the URL based on your Flask server setup

      // Create a hidden link to trigger the download
      const link = document.createElement('a');
      link.href = url;
      link.download = 'file.docx';
      link.style.display = 'none';
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
      }
    },
  };
  </script>
  