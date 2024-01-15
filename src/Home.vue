<template>
      

    <div  :style="{ 
          height: '663.27px',
          width:'1396.36px',
          alignItems: 'center',
          display: 'flex',
          flexDirection: 'column',
          justifyContent: 'center'}"
    >
    <a-image
    :width="400"
    src="https://www.design911.co.uk/uploads/D911-logo-private.png"
    />
    <a-button @click="showDemoPage">Demo</a-button >
  </div>
  
  </template>
  
  <script>
  export default {
    methods: {
      showContactPage() {
        this.$emit("change-page", "contact");
      },
      showDemoPage() {
        this.$emit("change-page", "Demo");
      },
    },
  };
  </script>
  