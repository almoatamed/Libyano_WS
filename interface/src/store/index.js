import Vue from 'vue'
import Vuex from 'vuex'
import Loading from './modules/Loading'
import Ros from './modules/ros'
import Interactive from './modules/interactive'
Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    Loading,
    Interactive,
    Ros
  },
  state: {
  },
  mutations: {
  },
  actions: {
  },
})
