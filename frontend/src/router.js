import { createRouter, createWebHistory } from 'vue-router';
import ShipmentList from './components/ShipmentList.vue';
import ShipmentDetail from './components/ShipmentDetail.vue';
import CarrierForm from './components/CarrierForm.vue';
import Map from './components/Map.vue';

const routes = [
  { path: '/', name: 'Home', component: ShipmentList },
  { path: '/shipments/:id', name: 'ShipmentDetail', component: ShipmentDetail, props: true },
  { path: '/carriers/new', name: 'CarrierForm', component: CarrierForm },
  { path: '/map', name: 'Map', component: Map },
];

export default createRouter({
  history: createWebHistory(),
  routes,
});
