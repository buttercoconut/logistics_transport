<template>
  <div>
    <h2>Shipment Detail</h2>
    <div v-if="shipment">
      <p><strong>ID:</strong> {{ shipment.id }}</p>
      <p><strong>Origin:</strong> {{ shipment.origin }}</p>
      <p><strong>Destination:</strong> {{ shipment.destination }}</p>
      <p><strong>Status:</strong> {{ shipment.status }}</p>
      <p><strong>Estimated Arrival:</strong> {{ shipment.estimated_arrival }}</p>
    </div>
    <div v-else>
      Loading...
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import axios from 'axios';

const route = useRoute();
const shipment = ref(null);

const fetchShipment = async () => {
  try {
    const response = await axios.get(`/api/shipments/${route.params.id}`);
    shipment.value = response.data;
  } catch (err) {
    console.error('Error fetching shipment', err);
  }
};

onMounted(() => {
  fetchShipment();
});
</script>
