<template>
  <div>
    <h2>Shipment List</h2>
    <table class="table">
      <thead>
        <tr>
          <th>ID</th>
          <th>Origin</th>
          <th>Destination</th>
          <th>Status</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="shipment in shipments" :key="shipment.id">
          <td>{{ shipment.id }}</td>
          <td>{{ shipment.origin }}</td>
          <td>{{ shipment.destination }}</td>
          <td>{{ shipment.status }}</td>
          <td>
            <router-link :to="{ name: 'ShipmentDetail', params: { id: shipment.id } }">View</router-link>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const shipments = ref([]);

const fetchShipments = async () => {
  try {
    const response = await axios.get('/api/shipments');
    shipments.value = response.data;
  } catch (err) {
    console.error('Failed to fetch shipments', err);
  }
};

onMounted(() => {
  fetchShipments();
});
</script>

<style scoped>
.table {
  width: 100%;
  border-collapse: collapse;
}
.table th,
.table td {
  border: 1px solid #ddd;
  padding: 8px;
}
.table th {
  background-color: #f2f2f2;
}
</style>
