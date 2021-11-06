import RosApi from '../../Api//Ros'
export default {
    namespaced: true, 
    state:{
        n:0
    },
    actions:{
        fetch_mode(){
            return new Promise((resolve,reject)=>{
                RosApi.mode().then(resp=>{
                    resolve(resp.data.mode)
                }).catch((err)=>{
                    console.error('error whiel fetching mode ' ,err)
                    reject(err)
                })
            })
        },
        change_mode(context,mode){
            context.commit('increase')
            return new Promise((resolve, reject)=>{
                    RosApi.change_mode(mode).then(resp=>{
                        resolve(resp)
                    }).catch(err=>{
                        console.error('error while changin mode', err)
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