export default {
    namespaced: true, 
    state: {
        alert: false, 
        message: {
            test: '',
            title: '',
            duration: '',
            type: ''
        }
    },
    mutations: {
        notify(state, message) {
            state.message = message
            state.alert  = true
        },
        clear(state){
            state.alert  = false
        }
    },
    actions: {
        notify(context, message){
            context.commit('notify', message)
        },
        clear(context){
            context.commit('clear')
        }
    },
    getters: {
        message(state) {
            return state.message
        },
        alert(state){
            return state.alert
        }
    }
}