<template>
  <div class="map-container">
    <div id="map" style="width: 100%; height: 500px;"></div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import L from 'leaflet';

onMounted(() => {
  const map = L.map('map').setView([37.5665, 126.9780], 13);
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors',
  }).addTo(map);
  // Example marker
  L.marker([37.5665, 126.9780]).addTo(map).bindPopup('Seoul').openPopup();
});
</script>

<style scoped>
.map-container {
  padding: 1rem;
}
#map {
  width: 100%;
  height: 500px;
}
</style>
