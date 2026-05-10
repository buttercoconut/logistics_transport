<template>
  <div>
    <h2>Shipment Detail</h2>
    <div v-if="shipment">
      <p><strong>ID:</strong> {{ shipment.id }}</p>
      <p><strong>Origin:</strong> {{ shipment.origin }}</p>
      <p><strong>Destination:</strong> {{ shipment.destination }}</p>
      <p><strong>Status:</strong> {{ shipment.status }}</p>
    </div>
    <div v-else>
      <p>Loading...</p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import axios from 'axios';

const route = useRoute();
const shipment = ref(null);

onMounted(async () => {
  try {
    const res = await axios.get(`http://localhost:8000/shipments/${route.params.id}`);
    shipment.value = res.data;
  } catch (e) {
    console.error(e);
  }
});
</script>
