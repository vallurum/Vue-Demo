<script>

export default {
  // reactive state
  data() {
    return {
      count: 0
    }
  },

  // functions that mutate state and trigger updates
  methods: {
    increment() {
      this.count++
    }
  },

  // lifecycle hooks
  mounted() {
    console.log(`The initial count is ${this.count}.`)
  }
}
</script>

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
    <a-button @click="increment">Demo</a-button >
    <a-button @click="increment">Count is: {{ count }}</a-button >

  </div>
  
</template>