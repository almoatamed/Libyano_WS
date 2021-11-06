export default {
    namespaced: true,

    state: {
        loading: false    
    },
    actions: {
        setLoading({ commit }) {
            commit('setLoading')
        },
        clearLoading({commit}) {
            commit('clearLoading')
        }
    },
    mutations: {
        setLoading(state) {
            state.loading = true
        },
        clearLoading(state) {
            state.loading = false
        }
    },
    getters: {
        getLoading(state) {
            return state.loading
        }
    }
}