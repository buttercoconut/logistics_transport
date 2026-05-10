
import { createRouter, createWebHistory } from 'vue-router';
import Dashboard from './components/Dashboard.vue';
import ShipmentList from './components/ShipmentList.vue';
import ShipmentDetail from './components/ShipmentDetail.vue';
import CarrierForm from './components/CarrierForm.vue';

const routes = [
  { path: '/', name: 'Dashboard', component: Dashboard },
  { path: '/shipments', name: 'ShipmentList', component: ShipmentList },
  { path: '/shipments/:id', name: 'ShipmentDetail', component: ShipmentDetail, props: true },
  { path: '/carrier', name: 'CarrierForm', component: CarrierForm },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
