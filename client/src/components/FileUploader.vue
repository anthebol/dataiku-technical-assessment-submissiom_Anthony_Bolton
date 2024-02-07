<template>
  <div class="star-wars-container" :style="backgroundImageStyle">
    <div class="content">
      <h1 class="title">Millennium Falcon Odds Calculator</h1>
      <div class="file-upload-section">
        <h2>Navigation Data of the Millennium Falcon</h2>
        <input type="file" id="millennium-falcon" @change="handleFileUpload($event, 'millenniumFalcon')">
      </div>
      <div class="file-upload-section">
        <h2>Empire and Bounty Hunters Data</h2>
        <input type="file" id="empire" @change="handleFileUpload($event, 'empire')">
      </div>
      <button @click="calculateOdds" class="calculate-button">Calculate Odds</button>
      <div v-if="validationMessage" class="validation-message">
        <p>{{ validationMessage }}</p>
      </div>
      <div v-if="result" class="result">
        <p>The odds of the Millennium Falcon saving the galaxy is: {{ result.probability }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import millenniumFalconImage from '@/assets/millennium-falcon.jpg';

export default {
  data() {
    return {
      millenniumFalcon: null,
      empire: null,
      result: null,
      validationMessage: '',
    };
  },
  computed: {
    backgroundImageStyle() {
      return {
        backgroundImage: `url(${millenniumFalconImage})`
      };
    }
  },
  methods: {
    handleFileUpload(event, fileKey) {
      const file = event.target.files[0];
      if (!file || !file.name.endsWith('.json')) {
        this.validationMessage = 'Please upload a JSON file.';
        return;
      }
      
      if (fileKey === 'millenniumFalcon' && !file.name.includes('millennium')) {
        this.validationMessage = 'Please upload the Millennium Falcon JSON file.';
        return;
      } else if (fileKey === 'empire' && !file.name.includes('empire')) {
        this.validationMessage = 'Please upload the Empire JSON file.';
        return;
      }
      
      this[fileKey] = file;
      this.validationMessage = '';
    },
    calculateOdds() {
      if (!this.millenniumFalcon || !this.empire) {
        this.validationMessage = 'Please upload both Millennium Falcon and Empire JSON files.';
        return;
      }

      const formData = new FormData();
      formData.append('millennium-falcon', this.millenniumFalcon);
      formData.append('empire', this.empire);

      axios.post('http://localhost:5000/calculateOdds', formData)
      .then(response => {
        this.result = response.data;
        this.validationMessage = '';
      })
      .catch(error => {
        if (error.response && error.response.data && error.response.data.error) {
          this.validationMessage = error.response.data.error;
        } else {
          this.validationMessage = 'An unknown error occurred.';
        }
      });
    }
  }
}
</script>

<style scoped>
.star-wars-container {
  background-size: cover;
  background-position: center;
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  padding: 20px;
}

.content {
  text-align: center;
  width: 100%;
  max-width: 600px;
  margin: auto;
  padding: 20px;
  background: rgba(0, 0, 0, 0.8); /* Translucent black background */
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
}

.title {
  font-family: 'Star Jedi', sans-serif; /* Star Wars font */
  color: #ffd700; /* Star Wars yellow text */
  margin-bottom: 20px;
}

.file-upload-section h2 {
  font-family: 'Star Jedi', sans-serif;
  color: #ffe81f;
  margin-bottom: 10px;
}

input[type="file"] {
  font-size: 1rem;
  margin-bottom: 15px;
}

.calculate-button {
  font-size: 1rem;
  padding: 10px 20px;
  margin-top: 20px;
  color: black;
  background-color: #ffd700;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.2s;
}

.calculate-button:hover {
  background-color: #ffc107;
}

.validation-message, .result {
  font-family: 'Star Jedi', sans-serif;
  margin-top: 20px;
}

.validation-message {
  color: #dc3545;
}

.result {
  color: #28a745;
}
</style>



