export default {
    namespaced: true,
    state: {
        lang: 'ar',
        langs:['ar', 'en']
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
        }
    }
}