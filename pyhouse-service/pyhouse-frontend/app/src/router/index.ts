import { createRouter, createWebHashHistory, RouteRecordRaw } from 'vue-router'
import Home from '../views/Home.vue'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/login',
    component: () => import("../views/auth/Login.vue")
  },
  {
    path: '/new-mypassword',
    component: () => import("../views/auth/NewPassword.vue")
  },

]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router