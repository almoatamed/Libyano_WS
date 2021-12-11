import RosApi from '../../Api/ros';
export default {
    namespaced: true,
    state:{
        connection_flag:false,
        status: {

        },
        mode: '',
        pass: ''
    },
    actions:{
        fetchConnectionFlag({dispatch, commit}){
            return new Promise((resolve, reject) =>{
                RosApi.connectionFlag().then(res => {
                    commit('setConnectionFlag',res.data.connection)
                    if(res.data.connection){
                        resolve(res)
                    }else{
                        reject(res)
                    } 
                }).catch(err => {
                    dispatch('ApiError/check',err, {root:true});
                    reject(err);
                })
            })
        },
        setMode(context, mode){
            return new Promise(resolve=>{
                context.commit('setMode', mode)
                resolve()
            })
        },
        fetchMode(context){
            return new Promise((resolve, reject)=>{
                context.dispatch('Ros/take_action','global_actions/get_current_mode',{root:true}).then(res=>{
                    context.commit('setMode', res)
                    resolve(res)
                }).catch(err => {
                    context.dispatch('ApiError/check', err, {root: true});
                    reject(err);
                })
            })
        },
        // fetchStatus({dispatch, commit}){
        //     return new Promise((resolve, reject)=>{
        //         RosApi.status().then((res)=>{
        //             commit('setStatus', res.data.status);
        //             resolve(res);
        //         }).catch(err=>{
        //             dispatch('ApiError/check', err, {root: true});
        //             reject(err);
        //         })
        //     })
        // },
        
        getcurrentlocation(context){
            context.commit('pass')
            return new Promise((resolve, reject)=>{
                RosApi.getcurrentlocation().then(res =>{
                    resolve(res)
                }).catch(err => {
                    reject(err)
                })
            })
        },

        postVouchers(context,vouchers){
            context.commit('pass')
            return new Promise((resolve, reject)=>{
                RosApi.postVouchers(vouchers).then(res=>{
                    resolve(res)
                }).catch(err=>{
                    console.log('error while posting  vouchers ',err)
                    reject(err)
                })
            })
        },
        take_action(context, action){
            context.commit('pass')
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
        setConnectionFlag(state, data){
            state.connection_flag = data;
        },
        setStatus(state, data){
            state.status = data;
        },
        setMode(state, data){
            state.mode = data;
        },
        pass(){
        }
    },
    getters:{
        connectionFlag(state){
            return state.connection_flag;
        },
        status(state){
            return state.status;
        },
        batteryPercentage(state){
            if(state.status.power){
                return state.status.power.battery +  '%';
            }else{
                return 'Undefined'
            }
        },
        isCharging(state){
            if(!state.status.power){
                return 'Undefined'
            }else{
                console.log('Charging_status', state.status.power['charging_status'])
                return state.status.power['charging_status'] ? 'yes' : 'no';
            }
        },
        mode(state){
            return state.mode;
        },
    }
}