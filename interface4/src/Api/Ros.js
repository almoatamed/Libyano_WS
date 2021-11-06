import Api from "./Api";

export default {
    connectionFlag() {
        return new Promise((resolve, reject) => {
            Api.get("ros/connection")
                .then((res) => {
                    resolve(res);
                })
                .catch((err) => {
                    reject(err);
                });
        });
    },
    relay(req){
        return new Promise((resolve, reject)=>{
            Api.post('ros/relay', req,{timeout:60e3}).then(res=>{
                resolve(res)
            }).catch(err=>{
                reject(err)
            })
        })
    },
    cash_reader_takein(req) {
        return new Promise((resolve, reject) => {
            Api.post("ros/takein",req,{timeout:60e3})
                .then((res) => {
                    resolve(res);
                })
                .catch((err) => {
                    reject(err);
                });
        });
    },
    voucher_check() {
        return new Promise((resolve, reject) => {
            Api.get("ros/voucher_check")
                .then((res) => {
                    resolve(res);
                })
                .catch((err) => {
                    reject(err);
                });
        });
    },
    cash_reader_cancel(){
        return new Promise((resolve, reject)=>{
            Api.get('ros/cash_reader_cancel').then((x)=>{resolve(x.data)}).catch((x)=>{reject(x.data)})
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
};
