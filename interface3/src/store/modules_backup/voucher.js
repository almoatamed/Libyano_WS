import rosApi from '../../Api/Ros'
export default {
    namespaced: true,
    state:{
        message: {},
        show: false,
        counter:0,
    },
    actions:{
        takein({commit},req){
            console.log('taking in', req)
            commit('add_counter')
            return new Promise((resolve,reject)=>{
                rosApi.cash_reader_takein(req).then((res)=>{
                    resolve(res)
                }).catch((err)=>{
                    reject(err)
                })
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
        }
    }
    
}