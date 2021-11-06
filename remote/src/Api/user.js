import Api from './Api';

export default {
    login(body){
        return new Promise((resolve, reject)=>{
            Api.post('auth/login',body).then(res=>{
                console.log('Api/login: logging in succeed,',res);
                resolve(res);
            }).catch(err=>{
                console.log('Api/login: loggin in failed, ',err)
                reject(err)
            })
        })
    }
}