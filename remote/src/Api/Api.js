import axios from 'axios';
import store from '../store/index';
import env from '../../env'
// import store from '../store/index'

let Api = axios.create({
    baseURL: `http://${env.server_addr}:${env.api_port}/api/`
});
// Api.defaults.
console.log(`Api/Api Axios Api handler has been created`)

Api.interceptors.request.use(function(config){
    if(store.getters['User/auth']){
        config.headers.Authorization =  store.getters['User/token'];
    }
    return config;
})

window.api = Api;

export default Api;