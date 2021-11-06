export default {
    namespaced: true,

    state: {
        interactive: false    
    },
    actions: {
        set_interactive({ commit }) {
            commit('set_interactive')
        },
        clear_interactive({commit}) {
            commit('clear_interactive')
        }
    },
    mutations: {
        set_interactive(state) {
            state.interactive = true
            console.log('setting interactive')
        },
        clear_interactive(state) {
            state.interactive = false
            console.log('clearign interactive')
        }
    },
    getters: {
        get_interactive(state) {
            return state.interactive
        }
    }
}