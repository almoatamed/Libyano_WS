import Vue from 'vue'
import Vuex from 'vuex'

import Interactive from './modules/interactive'
import Voucher from './modules/voucher'
import Ros from './modules/ros'
import Interface from './modules/interface'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    Interactive,
    Voucher,
    Interface,
    Ros
  },
  state: {
  },
  mutations: {
  },
  actions: {
  },
})
