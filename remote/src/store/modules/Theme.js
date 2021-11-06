export default {
    namespaced: true, 
    state: {
        isDark: false
    }, 
    getters: {
        isDark(state){
            return state.isDark
        }
    }, 
    actions:{
        setDark(context){
            context.commit('setDark')
        }
    },
    mutations: {
        setDark(state){
            state.isDark = !state.isDark
        }
    }
}