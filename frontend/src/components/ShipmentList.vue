<template>
  <div>
    <h2>Shipment List</h2>
    <ul>
      <li v-for="shipment in shipments" :key="shipment.id">
        {{ shipment.id }} - {{ shipment.origin }} to {{ shipment.destination }}
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const shipments = ref([]);

onMounted(async () => {
  try {
    const response = await axios.get('/api/shipments');
    shipments.value = response.data;
  } catch (error) {
    console.error('Error fetching shipments:', error);
  }
});
</script>

<style scoped>
ul {
  list-style-type: none;
  padding: 0;
}
</style>
