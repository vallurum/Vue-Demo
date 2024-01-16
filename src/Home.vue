<template>
      

    <div  :style="{ 
          height: '551px',
          width:'708px',
          alignItems: 'center',
          display: 'flex',
          flexDirection: 'column',
          justifyContent: 'center'}"
    >
    <a-image
    :width="400"
    src="https://www.design911.co.uk/uploads/D911-logo-private.png"
    />

    <div :style="{ 
          display: 'flex',
          flexDirection: 'row',
          gap: '30px'
          }"
    >
      <a-button @click="showDemoPage">Demo</a-button >
      <a-button @click="showContactPage">Contact</a-button >
    </div>
    
      
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

<style >
    .ant-btn-default{
      background-color: #eb6a2e !important;
      color: white !important;
    }
    .ant-btn-default:hover{
      background-color: #eb6a2e !important;
      color: white !important;
      border-color: #eb6a2e !important;
    }
    .ant-table-column-sorter-up.active .ant-table-column-sorter-down.active{
      color: #eb6a2e !important;
    }
</style>
  
