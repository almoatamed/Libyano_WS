import axios from 'axios'

let Api = axios.create({
    baseURL: 'http://localhost:3421/api'
})

console.log('Api/Api: Axios Api handler has been created')

window.api = Api
export default Api