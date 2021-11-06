export default {
    namespaced: true,
    state: {
        loading: true
    },
    actions:{
        set(context){
            context.commit('set')
        },
        clear(context){
            context.commit('clear')
        }
    },
    mutations:{
        set(state){
            state.loading = true
        },
        clear(state){
            state.loading = false
        }
    },
    getters:{
        get(state){
            return state.loading
        }
    }
}