import Vue from 'vue'
import VueRouter from 'vue-router'
import main from '../views/main/main.vue'
import store from '../store/index'

Vue.use(VueRouter)

const routes = [

  {
    path: '/',
    name: 'main',
    component: main,
    children: [

      {
        path: '',
        name: 'slide-show',
        component: () => import(/* webpackChunkName: "slide_show" */ '../views/main/slide-show.vue'),
        meta: { interactive: false },
      },

      {
        path: 'lang',
        name: 'language',
        component: () => import(/* webpackChunkName: "language" */ '../views/main/language.vue'),
        meta: { interactive: false },
      },

      {
        path: 'srvc',
        name: 'services',
        meta: { interactive: true, interactive_footer: true, },
        component: () => import(/* webpackChunkName: "services" */ '../views/main/services.vue')
      },
      {
        path: 'srvc/topup',
        name: 'topup',
        meta: { interactive: true, interactive_footer: true, },
        component: () => import(/* webpackChunkName: "topup" */ '../views/main/topup.vue')
      },
      {
        path: 'srvc/offers',
        name: 'offers',
        meta: { interactive: true, interactive_footer: true, },
        component: () => import(/* webpackChunkName: "offers" */ '../views/main/offers.vue')
      },
      {
        path: 'srvc/internet',
        name: 'internet',
        meta: { interactive: true, interactive_footer: true, },
        component: () => import(/* webpackChunkName: "internet" */ '../views/main/internet.vue')
      },
      {
        path: 'srvc/roaming',
        name: 'roaming',
        meta: { interactive: true, interactive_footer: false },
        component: () => import(/* webpackChunkName: "roaming" */ '../views/main/roaming.vue')
      },
    ]
  },
  // {
  //   path: '/lowbattery',
  //   name: 'lowbattery',
  //   meta: {interactive:false, interactive_footer:false},
  //   component: () => import(/* webpackChunkName: "services" */ '../views/low_battery.vue')
  // },
  // {
  //   path: '/mapload',
  //   name: 'mapload',
  //   meta: {interactive:false, interactive_footer:false},
  //   component: () => import(/* webpackChunkName: "services" */ '../views/map_loading.vue')
  // },
  // {
  //   path: '/mapselect',
  //   name: 'mapselect',
  //   meta: {interactive:false, interactive_footer:true},
  //   component: () => import(/* webpackChunkName: "services" */ '../views/map_select.vue')
  // },

  {
    path: '/bootup',
    name: 'bootup',
    meta: { interactive: false, interactive_footer: false },
    component: () => import(/* webpackChunkName: "bootup" */ '../views/bootup/bootup.vue')
  },

]

const router = new VueRouter({
  // mode: 'history',
  base: process.env.BASE_URL,
  routes
})


function check_main_set_meta_requirements(to) {
  console.log('Performing interactivetiy check on route', to.name)
  return new Promise((resolve) => {
    if (to.matched.some(route => route.meta.interactive)) {
      store.dispatch('Interactive/set_interactive', null, { root: true })
    } else {
      store.dispatch('Interactive/clear_interactive', null, { root: true })
    }
    if (to.matched.some(route => route.meta.interactive_footer)) {
      store.dispatch('Interactive/set_interactive_footer', null, { root: true })
    } else {
      store.dispatch('Interactive/clear_interactive_footer', null, { root: true })
    }
    resolve()
  })
}

function perform_routing_acts(to, from) {
  // console.log('performing triggering acts on ',to.name, from.name)
  return new Promise((resolve) => {
    var config = store.getters['Interface/get_interface_config']
    if (config) {
      if (config['interface']['routes'][from.name]) {
        config['interface']['routes'][from.name]['destroy_acts'].forEach(act => {
          console.log('performing ', act, 'prior to routing from ', from.name)
          store.dispatch('Ros/take_action', `act/push_to_queue_by_name/${act}`, { root: true }).then(res => { console.log(res) }).catch(err => { console.error(err) })
        })
      }
      if (config['interface']['routes'][to.name]) {
        config['interface']['routes'][to.name]['mounted_acts'].forEach(act => {
          console.log('performing ', act, 'prior to routing to ', to.name)
          store.dispatch('Ros/take_action', `act/push_to_queue_by_name/${act}`, { root: true }).then(res => { console.log(res) }).catch(err => { console.error(err) })
        })
      }
    }
    resolve()
  })
}


router.beforeEach((to, from, next) => {
  perform_routing_acts(to, from).then(() => {
    check_main_set_meta_requirements(to).then(() => {
      next()
    })
  })
})

export default router
