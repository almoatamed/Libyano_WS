import store from '../store/index'
import ar_content from './ar/content.js'
import en_content from './en/content.js'
import ar_media from './ar/media.js'
import en_media from './en/media.js'


const langs = {
    ar:ar_content,
    en:en_content 
}

const media = {
    ar:ar_media,
    en:en_media
}

export default {
    translateMedia(src){
        var media_obj = media[store.getters['Interface/get_lang']]
        if(src in media_obj){
            console.log('translation media found ', media_obj[src])
            return media_obj[src]
        }else {
            console.log('no translation media found ', src)
            return src
        }
    },

    translate(sentance){
        var lang_obj = langs[store.getters['Interface/get_lang']]
        if(sentance in lang_obj ){
            return lang_obj[sentance]
        }else{
            return sentance
        }
    } 
}  