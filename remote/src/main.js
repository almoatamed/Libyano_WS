import Vue from 'vue'
import App from './App.vue'
import router from './router'
import Notifications from 'vue-notification'
import store from './store'
import vuetify from './plugins/vuetify'

Vue.config.productionTip = false
Vue.use(Notifications)

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
