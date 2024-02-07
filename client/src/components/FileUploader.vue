<template>
  <div>
    <h1>Upload your JSON files</h1>
    <input type="file" id="millennium-falcon" @change="handleFileUpload($event, 'millennium-falcon')">
    <input type="file" id="empire" @change="handleFileUpload($event, 'empire')">
    <button @click="calculateOdds">Calculate Odds</button>
    <div v-if="result">
      <p>The odds of the Millennium Falcon saving the galaxy is: {{ result.probability }}</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      millenniumFalcon: null,
      empire: null,
      result: null,
    };
  },
  methods: {
    handleFileUpload(event, fileKey) {
      this[fileKey] = event.target.files[0];
    },
    calculateOdds() {
      const formData = new FormData();
      formData.append('millennium-falcon', this['millennium-falcon']);
      formData.append('empire', this['empire']);

      axios.post('http://localhost:5000/calculateOdds', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      })
      .then(response => {
        this.result = response.data;
      })
      .catch(error => {
        console.error('There was an error!', error.response);
      });
    }
  }
}
</script>

<style scoped>
/* Add your styles here */
</style>


