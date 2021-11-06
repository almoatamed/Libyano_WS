import Api from './Api'

export default {
    connectionFlag(){
        return new Promise((resolve, reject)=>{
            Api.get('ros/connection').then(res => {
                console.log('Api/ros: connection flag brought successfully', res)
                resolve(res)
            }).catch(err => {
                reject(err)
            })
        })
    },
    status(){
        return new Promise((resolve, reject)=>{
            Api.get('ros/status').then(res => {
                resolve(res)
            }).catch(err => {
                reject(err)
            })
        })
    },
    postVouchers(vouchers){
        return new Promise((resolve, reject)=>{
            console.log(vouchers)
            Api.post('seed/load_vouchers',{vouchers}).then(res => {
                console.log('Api/ros: vouchers uploaded', res)
                resolve(res)
            }).catch(err => {
                reject(err)
            })
        })
    },
    getcurrentlocation(){
        return new Promise((resolve, reject)=>{
            Api.get('ros/currentlocation',{}).then(res =>{
                resolve(res);
            }).catch(err =>{
                reject(err);
            });
        })
    },
    action(action){
        return new Promise((resolve,reject)=>{
            Api.post('ros/action', {action:action}).then(res=>{
                // console.log('Api/ros: action has took place', res)
                resolve(res.data.message)
            }).catch(err=>{
                console.log('taking action failed', err)
                reject(err)
            })
        })
    }
}