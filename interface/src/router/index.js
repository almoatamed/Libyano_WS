import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/slide_show.vue'
import store from '../store/index'
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'slide_show',
    component: Home,
    props: true,
    meta: {interactive:false}
  },
  // {
  //   path: '/nav',
  //   name: 'nav',
  //   component: () => import(/* webpackChunkName: "nav" */ '../views/nav.vue')
  // },
  {
    path: '/chg',
    name: 'chg',
    component: () => import(/* webpackChunkName: "chg" */ '../views/chg.vue')
  },
  {
    path: '/trk',
    name: 'trk',
    component: () => import(/* webpackChunkName: "trk" */ '../views/trk.vue')
  },
  {
    path: '/services',
    name: 'services',
    meta: {interactive: true},
    component: () => import(/* webpackChunkName: "services" */ '../views/services.vue')
  },
  {
    path: '/offers',
    name: 'offers',
    meta: {interactive: true},
    component: () => import(/* webpackChunkName: "offers" */ '../views/offers.vue')
  },
  {
    path: '/roaming',
    name: 'roaming',
    meta: {interactive: true},
    component: () => import(/* webpackChunkName: "roaming" */ '../views/roaming.vue')
  },
  {
    path: '/topup',
    name: 'topup',
    meta: {interactive: true},
    component: () => import(/* webpackChunkName: "topup" */ '../views/topup.vue')
  },
  {
    path: '/internet',
    name: 'internet',
    meta: {interactive: true},
    component: () => import(/* webpackChunkName: "internet" */ '../views/internet.vue')
  },
  {
    path: '/lbt',
    naminternet: 'lbt',
    component: () => import(/* webpackChunkName: "lbt" */ '../views/lbt.vue')
  }
]



const router = new VueRouter({
  // mode: 'history',
  // base: process.env.BASE_URL,
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
