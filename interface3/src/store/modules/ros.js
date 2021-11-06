import RosApi from '../../Api//Ros'
export default {
    namespaced: true, 
    state:{
        n:0,
        mode: ''
    },
    actions:{
        fetch_mode({commit}){
            return new Promise((resolve,reject)=>{
                RosApi.mode().then(resp=>{
                    commit('set_mode',resp.data.mode)
                    resolve(resp.data.mode)
                }).catch((err)=>{
                    console.error('error whiel fetching mode ' ,err)
                    reject(err)
                })
            })
        },
        change_mode(context,mode){
            context.commit('increase')
            console.log('changin mode', mode)
            return new Promise((resolve, reject)=>{
                    RosApi.change_mode(mode).then(resp=>{
                        console.log('changed mode', mode)
                        resolve(resp)
                    }).catch(err=>{
                        console.error('error while changin mode', err)
                        reject(err)
                    })
            })
        }
    },
    mutations:{
        set_mode(state, mode){
            state.mode = mode
        },
        increase(state){
            state.n+=1
        }
    }
}