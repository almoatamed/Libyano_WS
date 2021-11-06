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
    cash_reader_relay(req){
        return new Promise((resolve, reject)=>{
            Api.post('ros/relay', req,{timeout:60e3}).then(res=>{
                resolve(res)
            }).catch(err=>{
                reject(err)
            })
        })
    },
    cash_reader_takein(req) {
        return new Promise((resolve) => {
            Api.post("ros/takein",req,{timeout:60e3})
                .then((res) => {
                    resolve(res);
                })
                .catch((err) => {
                    resolve(err);
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
    }
};
