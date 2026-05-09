<template>
  <div>
    <h2>Carrier Form</h2>
    <form @submit.prevent="submitForm">
      <div>
        <label for="name">Name:</label>
        <input id="name" v-model="form.name" required />
      </div>
      <div>
        <label for="contact">Contact:</label>
        <input id="contact" v-model="form.contact" required />
      </div>
      <button type="submit">Save</button>
    </form>
  </div>
</template>

<script setup>
import { reactive } from 'vue';
import axios from 'axios';

const form = reactive({
  name: '',
  contact: '',
});

const submitForm = async () => {
  try {
    await axios.post('/api/carriers', form);
    alert('Carrier saved');
    form.name = '';
    form.contact = '';
  } catch (err) {
    console.error(err);
    alert('Error saving carrier');
  }
};
</script>
