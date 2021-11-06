import Api from './Api'

export default {
    fetch_sounds(){
        return new Promise((resolve, reject)=>{
            Api.post('ros/action',{action:'interactive/sounds_list'}).then((resp)=>{
                console.log('response for fetching sounds',resp.data)
                resolve(resp)
            }).catch(err=>{
                console.error('Error whiel trying to fetch available file sounds',err)
                reject(err)
            })
        })
    },
    play_temp(args){
        console.log('playing content',args)
        return new Promise((resolve, reject)=>{
            Api.post('ros/action', {action: `interactive/play_temp/${args.lang}/${args.content}`}).then(resp=>{
                resolve(resp)
            }).catch(err=>{
                reject(err)
            })
        })
    },
    play_save_file(name){
        console.log('playing saved file',name)
        return new Promise((resolve, reject)=>{
            Api.post('ros/action', {action: `interactive/play_saved_file/${name}`}).then(resp=>{
                resolve(resp)
            }).catch(err=>{
                reject(err)
            })
        })
    },
    save_sound(args){
        console.log('saving sentacne',args.name, args.content, args.content)
        return new Promise((resolve, reject)=>{
            Api.post('ros/action', {action: `interactive/save_sound/${args.lang}/${args.content}/${args.name}`}).then(resp=>{
                console.log('finished request and responce is ', resp.data)
                resolve(resp)
            }).catch(err=>{
                console.error('error occured while trying to save soudn file', err)
                reject(err)
            })
        })
    },
    del_sound(name){
        console.log('attempting to delete sound file at ', name)
        return new Promise((resolve, reject)=>{
            Api.post('ros/action', {action: `interactive/del_sound/${name}`}).then(resp=>{
                console.log('deleting sound file resulted', resp.data)
                resolve(resp)
            }).catch(err=>{
                console.error('Error deleting sound file', err)
                reject(err)
            })
        })
    }
}