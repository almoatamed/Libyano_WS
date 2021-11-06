export default {
    namespaced: true,
    state: {
        lang: 'ar',
        langs:['ar', 'en'],
        timeout_value: 120e3
    },
    actions:{
        set_lang(context, lang){
            if(context.state.langs.includes(lang)){
                context.commit('set_lang',lang)
            }
        }
    },
    mutations:{
        set_lang(state,lang){
            state.lang = lang
        }
    },
    getters: {
        get_langs(state){
            return state.langs
        },
        get_lang(state){
            return state.lang
        },
        get_timeout_val(state){
            return state.timeout_value
        }
    }
}