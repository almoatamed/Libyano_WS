import Vue from "vue";
import Router from "vue-router";
import store from '../store/index'
import summary from '../views/status/summary.vue'

Vue.use(Router);

const router = new Router({
  // mode: "history",
  // linkExactActiveClass: "Active-link",
  routes: [


    //############################# Status ################################333
    {
      path: "/",
      name: "summary",
      component: summary,
      props: true,
      meta: { requiresAuth: true, requiresConnectoin: true }
    },



    //########################### Auth ##############################33
    {
      path: "/login",
      name: "login",
      component: () => import(/* webpackChunkName: "Login" */
        "../views/auth/login.vue"),
      meta: { requiresVisitor: true, requiresConnectoin: true }
    },



    //########################### Live Controller Page ##############################

    {
      path: '/live',
      name: 'live',
      component: () => import(/* webpackChunkNam: "live" */
        '../views/live/live.vue'),
      meta: { requiresAuth: true, requiresConnectoin: true }
    },

    //########################### Act Controller Page ##############################

    {
      path: '/act_manager',
      name: 'act_manager',
      component: () => import(/* webpackChunkNam: "act_manager" */
        '../views/act_manager/act_manager.vue'),
      meta: { requiresAuth: true, requiresConnectoin: true }
    },

    //########################### interface  ##############################
    {
      path: '/interface_events',
      name: 'interface_events',
      component: () => import(/* webpackChunkNam: "interface_events" */
        '../views/interface_events/interface_events.vue'),
      meta: { requiresAuth: true, requiresConnectoin: true }
    },

    //########################### story Controller Page ##############################

    {
      path: '/story_manager',
      name: 'story_manager',
      component: () => import(/* webpackChunkNam: "story_manager" */
        '../views/story_manager/story_manager.vue'),
      meta: { requiresAuth: true, requiresConnectoin: true }
    },

    //########################### startup ###########################
    {
      path: "/startup",
      name:'startup',
      component: () =>
        import(/* webpackChunkName: "startup" */
          "../views/startup/startup.vue"),
      meta: { requiresAuth: true, requiresConnectoin: true },
      children:[
        // ################# Choices ################################
        {
          path:'', 
          component:()=>import(/* webpackChunkName: "Startup_choices" */ "../views/startup/choices.vue"),
          name:'startup_choices'
        },
        // ###################### Loading ###############################
        {
          path:'loading', 
          component:()=>import(/* webpackChunkName: "startup_loading" */ "../views/startup/loading/loading.vue"),
          name:'startup_loading'
        },
        // ###################### Power Stage ###################################3
        {
          path:'remove_dc_cord', 
          component:()=>import(/* webpackChunkName: "Startup_remove_dc_cord" */ "../views/startup/power_stage/remove_cord.vue"),
          name:'startup_remove_dc_cord'
        },
        {
          path:'confirm_initial_position', 
          component:()=>import(/* webpackChunkName: "Startup_confirm_initial_position" */ "../views/startup/power_stage/confirm_initial_position.vue"),
          name:'startup_confirm_initial_position'
        },
        {
          path:'is_the_robot_charging', 
          component:()=>import(/* webpackChunkName: "is_the_robot_charging" */ "../views/startup/power_stage/is_the_robot_charging.vue"),
          name:'startup_is_the_robot_charging'
        },
        // // ####################### Loading Existing map ###########################3
        {
          path:'loading_existing_map', 
          component:()=>import(/* webpackChunkName: "Startup_loading_existing_map" */ "../views/startup/sync_map/list_maps.vue"),
          name:'startup_loading_existing_map'
        },
        {
          path:'confirm_position', 
          component:()=>import(/* webpackChunkName: "confirm_position" */ "../views/startup/sync_map/confirm_position.vue"),
          name:'startup_confirm_position'
        },
        // // ######################## Loading Map File ###########################
        // {
        //   path:'load_map_file',
        //   component:()=>import(/* webpackChunkName: "startup_load_map_file" */ "../views/startup/load_map_file/load_map_file.vue"),
        //   name: 'startup_load_map_file'
        // },
        // ####################### Slam ###########################################
        {
          path: 'slam/scan',
          component: ()=>import(/* webpackChunkName: "startup_slam_scan" */ '../views/startup/slam/finish_scanning.vue'),
          name:'startup_slam_finish_scanning'
        },
        {
          path: 'slam/start_scanning',
          component: ()=>import(/* webpackChunkName: "startup_slam_start_scanning" */ '../views/startup/slam/start_scanning.vue'),
          name:"startup_slam_start_scanning"
        },
        {
          path: 'slam/save_map',
          component: ()=>import(/* webpackChunkName: "startup_slam_save" */ '../views/startup/slam/save_map.vue'),
          name:'startup_slam_save_scanned_map'
        },
        {
          path: 'slam/wants_to_go_home',
          component: ()=>import(/* webpackChunkName: "startup_wants_to_go_home" */ '../views/startup/slam/wants_to_go_home.vue'),
          name:'startup_slam_wants_to_go_home'
        },
      ]
    },

    
    // ####################### startup Map ###########################################
    {
      path: '/startup_map',
      component: ()=>import(/* webpackChunkName: "startup_map" */ '../views/startup/map.vue'),
      name:'startup_map',
      meta: { requiresAuth: true, requiresConnectoin: true }
    },

    // ####################### point manager ###########################################
    {
      path: '/points_manager',
      component: ()=>import(/* webpackChunkName: "points_manager" */ '../views/points_maker/points_maker.vue'),
      name:'points_manager',
      meta: { requiresAuth: true, requiresConnectoin: true }
    },

    //#################################### Sound #######################
    {
      path: "/voice",
      name: "voice",
      component: () =>
        import(/* webpackChunkName: "noConnection" */
          "../views/sound/speak_generator.vue"),
      meta: { requiresAuth: true, requiresConnectoin: true }
    },



    //###################### Voucher #######################
    {
      path: "/voucher_loader",
      name: "voucher_loader",
      component: () =>
        import(/* webpackChunkName: "noConnection" */
          "../views/voucher/voucher_loader.vue"),
      meta: { requiresAuth: true, requiresConnectoin: true }
    },



    //########################## Networking #############################
    {
      path: "/bluetooth",
      name: "bluetooth",
      component: () =>
        import(/* webpackChunkName: "noConnection" */
          "../views/networking/bluetooth/bluetooth.vue"),
      meta: { requiresAuth: true, requiresConnectoin: true }
    },



    //########################### Basic #########################
    {
      path: "/noConnection",
      name: "noConnection",
      component: () =>
        import(/* webpackChunkName: "noConnection" */
          "../views/basic/noConnection.vue"),
      meta: { requiresVisitor: false, requiresNoConnectoin: false }
    },
    {
      alias: "/*",
      path: '/404',
      name: "notFound",
      component: () =>
        import(/* webpackChunkName: "notFound" */
          "../views/basic/notFound.vue"),
      meta: { requiresVisitor: false, requiresConnectoin: true }
    }
  ]
});

router.beforeEach((to, from, next) => {
  console.log(`routing from ${from.name} to ${to.name}`)
  if (to.matched.some(record => {
    console.log(record)
    return record.meta.requiresConnectoin
  })) {
    if (!store.getters['Ros/connectionFlag']) {
      next({
        name: "noConnection",
        query: { redirect: to.fullPath }
      });
    } else {
      if (to.matched.some(record => record.meta.requiresAuth)) {
        if (!store.getters['User/auth']) {
          console.log('redirecting to login due to lack of authinticity')
          next({
            name: "login",
            query: { redirect: to.fullPath }
          });
        } else {
          next()
        }
      } else if (to.matched.some(record => record.meta.requiresVisitor)) {
        if (store.getters['User/auth']) {
          next({
            name: "remote"
          });
        } else {
          next();
        }
      } else {
        next();
      }
    }
  } else {
    console.log('redirecting to', to.name, 'whcih doesnt require connection')
    if (store.getters['Ros/connectionFlag']) {
      next({ name: 'remote' });
    } else {
      next();
    }
  }

});

export default router;