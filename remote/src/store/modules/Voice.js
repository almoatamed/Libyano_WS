import voiceApi from '../../Api/voice'
export default {
    namespaced: true, 
    state: {
        counter: 0
    },
    actions:{
        fetch_sounds({commit}){
            commit('add_counter')
            return new Promise((resolve, reject)=>{
                voiceApi.fetch_sounds().then(res=>{
                    console.log('resolving sounds list',res.data)
                    resolve(res.data)
                }).catch(err=>{
                    console.error('error whiel fetching sound list',err)
                    reject(err)
                })
            })
        },
        del_file({commit},name){
            commit('add_counter')
            return new Promise((resolve, reject)=>{
                voiceApi.del_sound(name).then(res=>{
                    console.log('resolving deleting sound',res.data)
                    resolve(res.data)
                }).catch(err=>{
                    console.error('error whiel deleting sound file',err)
                    reject(err)
                })
            })
        },
        play_saved_file({commit},args){
            commit('add_counter')
            return new Promise((resolve, reject)=>{
                voiceApi.play_save_file(args).then(res=>{
                    console.log('resolving playing saved sound',res.data)
                    resolve(res.data)
                }).catch(err=>{
                    console.error('error whiel playing saved sound',err)
                    reject(err)
                })
            })
        },
        play_temp({commit},args){
            commit('add_counter')
            return new Promise((resolve, reject)=>{
                voiceApi.play_temp(args).then(res=>{
                    console.log('resolving play temp sound',res.data)
                    resolve(res.data)
                }).catch(err=>{
                    console.error('error whiel playing temp sound',err)
                    reject(err)
                })
            })
        },
        save_file({commit},args){
            commit('add_counter')
            return new Promise((resolve, reject)=>{
                voiceApi.save_sound(args).then(res=>{
                    console.log('resolving save sound',res.data)
                    resolve(res.data)
                }).catch(err=>{
                    console.error('error whiel saving sound',err)
                    reject(err)
                })
            })
        },
    },
    getters: {

    },
    mutations:{
        add_counter(state){
            state.counter+=1
        }
    }
}