<template>
  <div class="shipment-detail">
    <h2>Shipment Detail</h2>
    <div v-if="shipment">
      <p><strong>ID:</strong> {{ shipment.id }}</p>
      <p><strong>Origin:</strong> {{ shipment.origin }}</p>
      <p><strong>Destination:</strong> {{ shipment.destination }}</p>
      <p><strong>Status:</strong> {{ shipment.status }}</p>
      <p><strong>Estimated Cost:</strong> ${{ shipment.estimated_cost }}</p>
    </div>
    <div v-else>Loading...</div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { useRoute } from 'vue-router';

const route = useRoute();
const shipment = ref(null);

const fetchShipment = async () => {
  try {
    const res = await axios.get(`/api/shipments/${route.params.id}`);
    shipment.value = res.data;
  } catch (e) {
    console.error('Failed to fetch shipment', e);
  }
};

onMounted(fetchShipment);
</script>

<style scoped>
.shipment-detail {
  padding: 1rem;
}
</style>
