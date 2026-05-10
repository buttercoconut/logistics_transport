import { createRouter, createWebHistory } from 'vue-router';
import ShipmentList from './components/ShipmentList.vue';

const routes = [
  { path: '/', component: ShipmentList },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
