import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/slide-show.vue'
import store from '../store/index'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'slide-show',
    component: Home,
    meta: {interactive:false},
  },
  {
    path: '/srvc',
    name: 'services',
    meta: {interactive:true},
    // route level code-splitting
    // this generates a separate chunk (services.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "services" */ '../views/services.vue')
  },
  {
    path: '/srvc/topup',
    name: 'topup',
    meta: {interactive:true},
    // route level code-splitting
    // this generates a separate chunk (services.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "services" */ '../views/topup.vue')
  },
  {
    path: '/srvc/offers',
    name: 'offers',
    meta: {interactive:true},
    // route level code-splitting
    // this generates a separate chunk (services.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "services" */ '../views/offers.vue')
  },
  {
    path: '/srvc/roaming',
    name: 'roaming',
    meta: {interactive:true},
    // route level code-splitting
    // this generates a separate chunk (services.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "services" */ '../views/roaming.vue')
  },
  {
    path: '/lang',
    name: 'language',
    meta: {interactive:false},
    // route level code-splitting
    // this generates a separate chunk (services.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "services" */ '../views/language.vue')
  },

]

const router = new VueRouter({
  // mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from , next)=>{
  if(to.matched.some(route => route.meta.interactive)){
    store.dispatch('Interactive/set_interactive', null, {root:true})
  }else{
    store.dispatch('Interactive/clear_interactive', null, {root:true})
  }
  next()
})

export default router
