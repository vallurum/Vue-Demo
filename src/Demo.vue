<script>
import Contact from "./Demo.vue";

export default {
  // reactive state
  data() {
    return {
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
         height: '700px',
         display: 'flex',
         flexDirection: 'column',
         alignItems: 'center',
         justifyContent: 'space-around'
        }"
        >
        <a-button @click="showHomePage">Home</a-button >

        <div >
          <div><b :style="{color:'#eb6a2e' }">Tech :</b> </div>
          <div><b :style="{color:'#eb6a2e' }">Front End tools:</b> Antd, Vue, Vite</div>
          <div><b :style="{color:'#eb6a2e' }">Backend tools: </b> Python, Flask</div>
          <div><b :style="{color:'#eb6a2e' }">Required: </b> Node.js</div>
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