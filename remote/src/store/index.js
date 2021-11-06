import Vue from 'vue'
import Vuex from 'vuex'
import User from './modules/User'
import Ros from './modules/Ros'
import Theme from './modules/Theme'
import Loading from './modules/Loading'
import Notify from './modules/Notify'
import ApiError from './modules/ApiError'
import Voice from './modules/Voice'
import Router from './modules/Router'
Vue.use(Vuex)

export default new Vuex.Store({
  state: {
  },
  mutations: {
  },
  actions: {
  },
  modules: {
    User, Ros, Theme, Loading, Notify, ApiError, Voice, Router
  }
})
