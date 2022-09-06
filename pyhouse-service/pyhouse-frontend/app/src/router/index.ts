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
    path: '/register',
    component: () => import("../views/auth/Register.vue")
  },
  {
    path: '/forget-mypassword',
    component: () => import("../views/auth/ForgetPassword.vue")
  },
  {
    path: '/reset-password',
    component: () => import("../views/auth/ResetPassword.vue")
  },

]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router