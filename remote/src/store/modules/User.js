import UserApi from '../../Api/user'
export default {
    namespaced:true,
    state:{
        token: ''
    },
    getters:{
        auth(state){
            console.log('Store/User: getters, gettigng auth state', state.token);
            return !!state.token;
        },
        token(state){
            console.log('Store/User: getters, gettigng token', state.token);
            return state.token;
        }
    },
    mutations: {
        setToken(state, token){
            state.token = token;
        },
        clearToken(state){
            state.token = '';
        }
    },
    actions:{
        checkToken(context){
            context.commit('setToken',localStorage.getItem('token'));
        },
        setToken(context,token){
            console.log('Store/User: setting token Dispatch, ', token)
            return new Promise(resolve=>{
                if(token){
                    localStorage.setItem('token', token)
                    context.commit('setToken',token)
                }
                resolve()
            })
        },
        clearToken(context){
            console.log('Store/User: clearing token Dispatch, ', localStorage.getItem('token'))
            localStorage.removeItem('token');
            context.commit('clearToken')
        },
        login(context, body){
            return new Promise((resolve, reject)=>{
                UserApi.login(body).then(res => {
                    console.log('Store/User: logging in Dispatch succeed, ', res)
                    context.dispatch('setToken', res.data.token)
                    resolve(res)
                }).catch(err => {
                    console.log('Store/User: logging in Dispatch failed, ', err);
                    context.dispatch('clearToken');
                    reject(err);
                })
            })
        },
        logout(context){
            return new Promise((resolve)=> {
                context.dispatch('clearToken');
                resolve();
            });
        }
    }
}