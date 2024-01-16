<script>
import Contact from "./Demo.vue";

export default {
  // reactive state
  data() {
    return {
      colorValue:50,
      data: [],
      columns:[
        {
          title: 'Model',
          dataIndex: 'title',
          key: 'title',
        },
        {
          title: 'Fuel type',
          dataIndex: 'Fuel type',
          key: 'Fuel type',
          filters: [
            { text: 'Petrol', value: 'Petrol' },
            { text: 'Diesel', value: 'Diesel' },
          ],
          onFilter: (value, record) => record["Fuel type"].indexOf(value) === 0,
        },
        {
          title: 'Seats',
          dataIndex: 'Seats',
          key: 'Seats',
          sorter: (a, b) => a.Seats - b.Seats,
        },
        {
          title: 'Price',
          dataIndex: 'Price',
          key: 'Price',
          sorter: (a, b) => a.Price - b.Price,
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
    getColor() {
      // You can customize this method to generate a color based on your requirements
      return `rgba(235, 106, 46, ${this.colorValue*0.01})`;
    },
    handleChangeSlider(value){
      this.colorValue = value;
    }
    
  },

  // lifecycle hooks
  mounted() {
    fetch("http://127.0.0.1:5000/getData")
        .then(response => response.json())
        .then(data => {

          data.forEach(element => {

            console.log(element.title != null && element.Seats != null && element.Price != null);
            
            if(element.Seats != '' ){
              this.data.push(element)
            }
          });
          console.log(data);
        })
        .catch(error => {
          console.error("Error fetching data:", error);
        });

  }
}
</script>

<style>
    .ant-slider-horizontal{
      width:  500px !important;
    }
</style>

<template>
  
    <div
        :style="{ 
          display: 'flex',
          flexDirection: 'row',
          width: '100%',
          height: '100%'
         }"
    >
    
      <div
        :style="{ 
         width: '40%',
         height: '551px',
         display: 'flex',
         flexDirection: 'column',
         alignItems: 'center',
         justifyContent: 'space-around'
        }"
        >
        <a-button @click="showHomePage">Home</a-button >

        <div>
          <p>Try to change opacity</p>
          <a-slider v-model="colorValue" :min="50" :max="100" :autofocus="true" @afterChange="handleChangeSlider" />
        </div>  
          
        
        <div >
          <div><b :style="{color:getColor() }">Tech :</b> </div>
          <div><b :style="{color:getColor() }">Front End tools:</b> Antd, Vue, Vite</div>
          <div><b :style="{color:getColor() }">Backend tools: </b> Python, Flask</div>
          <div><b :style="{color:getColor() }">Required: </b> Node.js</div>
          <div><b :style="{color:getColor() }">Effort: </b> 10 hrs</div>
        </div>

      </div>
      <div
      :style="{ 
         width: '58%',
         height: '100%',
        
        }"
      >
        <a-table :columns="columns" :data-source="data" />
      </div>
      
    </div>


    
  
</template>
