import rosApi from '../../Api/Ros'
export default {
    namespaced: true,
    state:{
        message: {},
        relay_timeout: null,
        relay_status: false,
        show: false,
        counter:0,
    },
    actions:{
        takein({commit},req){
            commit('add_counter')
            console.log(`taking in ${req.channel} and ${req.val}`)
            return new Promise((resolve,reject)=>{
                rosApi.cash_reader_takein(req).then((res)=>{
                    resolve(res)
                }).catch((err)=>{
                    reject(err)
                })
            })
        },
        launch(context){
            context.commit('add_counter')
            context.commit('clear_relay_timeout')
            return new Promise((resolve, reject)=>{
                if(context.state.relay_status){
                    resolve({message: 'done'})
                }
                rosApi.relay({number:14,value:1.0}).then(resp=>{
                    context.commit('set_relay_status',true)
                    resolve(resp.data)
                }).catch(resp=>{
                    reject(resp.message)
                })
            })
        },
        stop(context){
            context.commit('add_counter')
            return new Promise((resolve)=>{
                context.commit('set_relay_timeout',setTimeout(()=>{
                    rosApi.relay({number:14,value:0.0}).then(resp=>{
                        console.log(resp.data)
                        context.commit('set_relay_status',false)
                    }).catch(resp=>{
                        console.log(resp.message)
                    })
                },15e3))
                resolve()
            })

        },
        check({commit}){
            return new Promise((resolve,reject)=>{
                rosApi.voucher_check().then(res=>{   
                    if(res.status == 200){
                        console.log('a voucher is found',res)
                        commit('set_message',res.data.voucher)
                        resolve()
                    }else{
                        reject()
                    }
                }).catch((err)=>{reject(err)})
            })
        },
        set_message({commit},msg){
            commit('set_message',msg)
        },
        clear({commit}){
            commit('clear')
        },
        cash_reader_cancel({commit}){
            commit('add_counter')
            return new Promise((resolve, reject)=>{
                rosApi.cash_reader_cancel().then((x)=>{resolve(x)}).catch((x)=>{reject(x)})
            })
        }
    },
    getters:{
        message(state){
            return state.message
        },
        show(state){
            return state.show
        }
    },
    mutations:{
        clear(state){
            state.message = {}
            state.show = false
        },
        add_counter(state){
            state.counter += 1
        },
        set_message(state,message){
            state.message = message
            state.show = true
        },
        set_relay_status(state,val){
            state.relay_status = val
        },
        set_relay_timeout(state,timeout){
            state.relay_timeout = timeout
        },
        clear_relay_timeout(state){
            clearTimeout(state.relay_timeout)
        }
    }
    
}