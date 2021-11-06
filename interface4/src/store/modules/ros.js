import RosApi from '../../Api//Ros'
export default {
    namespaced: true, 
    state:{
        n:0,
    },
    actions:{
        take_action(context, action){
            context.commit('increase')
            return new Promise((resolve, reject)=>{
                RosApi.action(action).then(res=>{
                    resolve(res)
                }).catch(err=>{
                    reject(err)
                })
            })
        }
    },
    mutations:{
        
        increase(state){
            state.n+=1
        }
    }
}