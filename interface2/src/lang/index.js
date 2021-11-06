import store from '../store/index'
import ar_contenct from './ar/content.js'
import en_contenct from './en/content.js'
import ar_media from './ar/media.js'
import en_media from './en/media.js'

const langs = {
    ar:ar_contenct,en:en_contenct
}
const media = {
    ar:ar_media,
    en:en_media
}

export default {
    translateMedia(src){
        var media_obj = media[store.getters['Interface/get_lang']]
        if(src in media_obj){
            return media_obj[src]
        }else{
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