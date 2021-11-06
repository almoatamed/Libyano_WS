export default {
    namespaced: true,

    state: {
        interactive: false,
        interactive_footer:false   
    },
    actions: {
        set_interactive({ commit }) {
            commit('set_interactive')
        },
        clear_interactive({commit}) {
            commit('clear_interactive')
        },
        set_interactive_footer({ commit }) {
            commit('set_interactive_footer')
        },
        clear_interactive_footer({commit}) {
            commit('clear_interactive_footer')
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
        },
        set_interactive_footer(state) {
            state.interactive_footer = true
            console.log('setting interactive footer')
        },
        clear_interactive_footer(state) {
            state.interactive_footer = false
            console.log('clearign interactive footer')
        }
    },
    getters: {
        get_interactive(state) {
            return state.interactive
        },

        get_interactive_footer(state) {
            return state.interactive_footer
        }
    }
}