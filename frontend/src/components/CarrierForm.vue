<template>
  <div>
    <h2>Carrier Form</h2>
    <form @submit.prevent="submit">
      <div>
        <label for="name">Name:</label>
        <input id="name" v-model="carrier.name" required />
      </div>
      <div>
        <label for="contact">Contact:</label>
        <input id="contact" v-model="carrier.contact" required />
      </div>
      <button type="submit">Save</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';

const carrier = ref({ name: '', contact: '' });

const submit = async () => {
  try {
    await axios.post('http://localhost:8000/carriers', carrier.value);
    alert('Carrier saved');
  } catch (e) {
    console.error(e);
  }
};
</script>
