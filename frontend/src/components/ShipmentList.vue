<template>
  <div>
    <h2>Shipment List</h2>
    <ul>
      <li v-for="shipment in shipments" :key="shipment.id">
        <router-link :to="{ name: 'ShipmentDetail', params: { id: shipment.id } }">
          {{ shipment.id }} - {{ shipment.origin }} to {{ shipment.destination }}
        </router-link>
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
    const res = await axios.get('http://localhost:8000/shipments');
    shipments.value = res.data;
  } catch (e) {
    console.error(e);
  }
});
</script>

<style scoped>
ul { list-style: none; padding: 0; }
li { margin: 0.5rem 0; }
</style>
