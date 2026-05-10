<template>
  <div class="carrier-form">
    <h2>Register New Carrier</h2>
    <form @submit.prevent="submitForm">
      <div>
        <label for="name">Name:</label>
        <input id="name" v-model="form.name" required />
      </div>
      <div>
        <label for="contact">Contact:</label>
        <input id="contact" v-model="form.contact" required />
      </div>
      <div>
        <label for="capacity">Capacity (kg):</label>
        <input id="capacity" type="number" v-model.number="form.capacity" required />
      </div>
      <button type="submit">Register</button>
    </form>
  </div>
</template>

<script setup>
import { reactive } from 'vue';
import axios from 'axios';

const form = reactive({
  name: '',
  contact: '',
  capacity: 0,
});

const submitForm = async () => {
  try {
    await axios.post('/api/carriers', form);
    alert('Carrier registered successfully');
    form.name = '';
    form.contact = '';
    form.capacity = 0;
  } catch (e) {
    console.error('Failed to register carrier', e);
  }
};
</script>

<style scoped>
.carrier-form {
  padding: 1rem;
}
form div {
  margin-bottom: 0.5rem;
}
</style>
