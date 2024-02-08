<template>
  <div class="star-wars-container" :style="backgroundImageStyle">
    <div class="content">
      <h1 class="title">What are the odds?</h1>
      <div class="file-upload-section">
        <h2>Millennium Falcon Navigation Data</h2>
        <label for="millennium-falcon" class="file-label">
          {{ millenniumFalconName || 'Choose File to Upload' }}
        </label>
        <input type="file" id="millennium-falcon" @change="handleFileUpload($event, 'millenniumFalcon')" style="display: none;">
      </div>
      <div class="file-upload-section">
        <h2>Empire and Bounty Hunters Data</h2>
        <label for="empire" class="file-label">
          {{ empireName || 'Choose File to Upload' }}
        </label>
        <input type="file" id="empire" @change="handleFileUpload($event, 'empire')" style="display: none;">
      </div>
      <button @click="calculateOdds" class="calculate-button">Calculate Odds</button>
      <div
        class="drag-drop-box"
        @dragover.prevent="dragOverHandler"
        @dragleave.prevent="dragLeaveHandler"
        @drop.prevent="dropHandler"
      >
        Drag and drop JSON files here
      </div>
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
      dragOver: false,
      millenniumFalconName: '', 
      empireName: '', 
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
      this.processFile(file, fileKey);
    },
    processFile(file, fileKey) {
      if (!file || !file.name.endsWith('.json')) {
        this.validationMessage = 'Please upload a JSON file.';
        return;
      }

      if (fileKey === 'millenniumFalcon' && file.name.includes('millennium')) {
        this.millenniumFalcon = file;
        this.millenniumFalconName = file.name; 
        this.validationMessage = '';
      } else if (fileKey === 'empire' && file.name.includes('empire')) {
        this.empire = file;
        this.empireName = file.name; 
        this.validationMessage = '';
      } else {
        this.validationMessage = `Please upload the correct JSON file for ${fileKey}.`;
      }
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
    },
    dragOverHandler() {
      this.dragOver = true; 
    },
    dragLeaveHandler() {
      this.dragOver = false; 
    },
    dropHandler(event) {
      this.dragOver = false; 
      const files = event.dataTransfer.files;
      Array.from(files).forEach(file => {
        if (file.name.includes('millennium')) {
          this.millenniumFalconName = file.name; 
          this.processFile(file, 'millenniumFalcon');
        } else if (file.name.includes('empire')) {
          this.empireName = file.name; 
          this.processFile(file, 'empire');
        } else {
          this.validationMessage = 'Unknown file type. Please drop the Millennium Falcon or Empire JSON files.';
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
  background: rgba(0, 0, 0, 0.8); 
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
}

.title {
  font-size: 3rem;
  font-family: 'Star Jedi', sans-serif;
  color: #ffd700; 
  margin-bottom: 20px;
}

.file-upload-section h2 {
  font-size: 1.25rem;
  font-family: 'Star Jedi', sans-serif;
  color: #ffe81f;
  margin-bottom: 10px;

}

input[type="file"] {
  font-size: 1rem;
  margin-bottom: 15px;
  width: 100%; 
  max-width: 100px; 
  margin: 0 auto; 
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

.drag-drop-box {
  border: 2px dashed #ffd700;
  padding: 20px;
  margin-top: 20px;
  color: #ffd700;
  font-family: 'Star Jedi', sans-serif;
  background: rgba(255, 255, 255, 0.1); 
  border-radius: 5px;
  transition: opacity 0.3s ease;
}

.drag-over {
  opacity: 0.5;
}

.drag-drop-box.drag-over {
  border-style: dashed;
  opacity: 0.5;
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
  font-size: 1.25rem;
  color: #28a745;
}

span {
  display: block; 
  margin-top: 10px;
  color: #ffd700;
  font-family: 'Star Jedi', sans-serif;
}

.file-label {
  width: 100%; 
  max-width: 250px; 
  margin: 0 auto; 
  display: block;
  padding: 10px;
  background: rgba(255, 255, 255, 0.1); 
  color: #fffefe; 
  margin-bottom: 15px;
  text-align: center;
  cursor: pointer;
  border-radius: 5px;
}

.file-label:hover {
  background-color: #817925; 
}
</style>



