export default {
    namespaced:true,
    state:{
        restrictions:{
            startup:true
        },
        restriction_dictionary:{
            default: {
                startup:true,
                unrestricted_route: 'summary'
            },
            str: {
                unrestricted_route: 'summary',
                map: true
            }, 
            ato: {
                unrestricted_route: 'summary',
                act_manager: true,
                startup:true,
                story_manager: true, 
                points_manager: true, 
            }
        }
    },
    actions:{
        update_restrictions(context){
            var mode = context.rootState.Ros.mode
            // console.log(context.state.restriction_dictionary[mode], mode)
            if(context.state.restriction_dictionary[mode]){
                context.commit('set_restrictions',context.state.restriction_dictionary[mode])
            }else{
                context.commit('set_restrictions',context.state.restriction_dictionary.default)
            }
        }
    },
    mutations:{

        set_restrictions(state, selected_restrictions){
            state.restrictions = selected_restrictions
        }
    },
    getters:{
        get_restrictions(state){
            return state.restrictions
        },
        get_unrestricted_route(state){
            return state.restrictions.unrestricted_route
        }
    }
}