import Vue from 'vue'
import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify'
import store from './store'
import carousel3d from './plugins/vue-carousel-3d'

new Vue({
  router,
  vuetify,
  store,
  carousel3d,
  render: h => h(App)
}).$mount('#app')
