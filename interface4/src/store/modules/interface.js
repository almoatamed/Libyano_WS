import ar_content from './ar/content.js'
import en_content from './en/content.js'
import ar_media from './ar/media.js'
import en_media from './en/media.js'

export default {
    namespaced: true,
    state: {

        lang: 'en',
        langs:['ar', 'en'],

        medias:{
            ar:ar_media,
            en:en_media
        },

        contents:{
            ar:ar_content,
            en:en_content
        },
        
        content:en_content,
        media:en_media,
        
        timeout_value: 10e3
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
            state.media = state.medias[lang]
            state.content = state.contents[lang]
            console.log('changing lang', state.media,state.content)

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
        },
        get_media(state){
            return state.media
        },
        get_content(state){
            return state.content
        }
    }
}