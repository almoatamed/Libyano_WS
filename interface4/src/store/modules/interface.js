import ar_content from './ar/content.js'
import en_content from './en/content.js'
import ar_media from './ar/media.js'
import en_media from './en/media.js'

export default {
    namespaced: true,
    state: {

        lang: 'en',
        langs: ['ar', 'en'],

        medias: {
            ar: ar_media,
            en: en_media
        },

        contents: {
            ar: ar_content,
            en: en_content
        },

        content: en_content,
        media: en_media,

        timeout_value: 10e3,

        interface_config: null,
    },
    actions: {
        set_lang(context, lang) {
            if (context.state.langs.includes(lang)) {
                context.commit('set_lang', lang)
            }
        },
        set_interface_config(context, config) {
            context.commit('set_interface_config', config)
        },
        async perform_event_acts(context, event_name) {
                if (context.state.interface_config) {
                    console.log(context.state.interface_config)
                    if (event_name in context.state.interface_config['interface']['special_events']) {
                        await context.state.interface_config['interface']['special_events'][event_name].forEach(act => {
                            console.log('performing act ', act)
                            context.dispatch('Ros/take_action', `act/push_to_queue_by_name/${act}`, { root: true })
                        })
                        return Promise.resolve({messag: 'Done'})
                    } else {
                        return Promise.reject({ message: 'event not found' })
                    }
                } else {
                    return Promise.reject({ message: 'config is not loaded yet' })
                }
        }
    },
    mutations: {
        set_lang(state, lang) {
            state.lang = lang
            state.media = state.medias[lang]
            state.content = state.contents[lang]
            console.log('changing lang', state.media, state.content)

        },
        set_interface_config(state, config) {
            state.interface_config = config
        }
    },
    getters: {
        get_langs(state) {
            return state.langs
        },
        get_lang(state) {
            return state.lang
        },
        get_timeout_val(state) {
            return state.timeout_value
        },
        get_media(state) {
            return state.media
        },
        get_content(state) {
            return state.content
        },
        get_interface_config(state) {
            return state.interface_config
        }
    }
}