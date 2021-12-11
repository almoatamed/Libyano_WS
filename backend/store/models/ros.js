const roslib = require('roslib')
const Voucher = require('../../database/models/voucher')
const fs = require('fs')
const homedir = require('os').homedir();


function sleep(duration){
    return new Promise(resolve => setTimeout(resolve, duration))
}

async function connect_to_ros(){
    var x = true;
    var ros;
    while(x){
        await sleep(1500).then(()=>{
            ros = new roslib.Ros({
                url : 'ws://localhost:9090'
                // url : 'ws://Libyano_J:9090' 
            });
            ros.on('connection', function(){
                x = false;
                console.log('Ros: connected to rosbridge successfully')
            });
            ros.on('error',function(err){
                console.error('error connecting to rosbridge')
            })
        })
    }
    return new Promise(resolve => resolve(ros))
}

module.exports = {
    state:{
        ros: false,
        status: {},
        mode:'',
        action_client: {},
        timeout: new Date().getTime(),
        current_location: {},
        map:{}, // width, height, resolution, frame_id, data,
        vouchers: [],
        cash_reader_controller: {},
        mode_topic:{},
        voucher_request_checker: null,
        channel_dictionary: {
            0: 10,
            1: 5,
            2: 10
        }
    }, 
    actions:{
        set_voucher_checker(context){
            console.log('starting voucher checker')
            context.commit('set_voucher_checker',setInterval(()=>{
                fs.readFile(homedir+'/catkin_ws/src/public/voucher_system/voucher_request.txt','utf8',(err, data)=>{
                    if(data){
                        console.log('voucher requests', data)
                        var val = context.models['Ros'].state.channel_dictionary[data]
                        Voucher.find().where('used').equals(false).where('val').equals(val).limit(1).exec((err,res)=>{
                            try {
                                console.log(res.length)
                                if(err){
                                    console.log(err)
                                }else{
                                    var voucher = {}
                                    voucher.secret = res[0].secret
                                    voucher.serial = res[0].serial
                                    voucher.val = val
                                    context.commit('Ros/add_voucher',voucher)
                                    res[0].used = true
                                    res[0].save()
                                }
                            } catch (error) {
                            }
                        })
                        fs.writeFile(homedir+'/catkin_ws/src/public/voucher_system/voucher_request.txt','',()=>{})                        
                    }
                })
            },1000))
        },
        async set_ros(context,ros){
            console.log('setting ros');
            await context.commit('Ros/set_ros',ros)
            return new Promise((resolve)=>resolve())
        },
        reconnect(context){
            console.log('reconnecting')
            context.commit('Ros/set_ros',{});
            context.commit('Ros/set_action_client',{});
            context.commit('Ros/set_cash_reader_controller', {})
            context.commit('Ros/set_mode_topic',{})
            return new Promise((resolve,reject)=>{
                context.dispatch('Ros/connect').then(()=>resolve()).catch(()=>reject());
            });
        },
        connect(context){
            return new Promise((resolve, reject)=>{
                console.log('attempting to connect')
                connect_to_ros().then(ros=>{
                    context.dispatch('Ros/set_ros',ros).then(()=>{
                        context.dispatch('Ros/init',{}).then(()=>{
                            console.log('attempting to initiate ros')
                            resolve()
                        }).catch(()=>{
                            reject()
                        });
                    })
                })
            })
        },
        init(context){
            var ros = context.models['Ros'].state.ros
            return new Promise((resolve, reject)=>{
                if(Object.keys(ros).length !=0){
                   //*******************************************************//     
                    var mode_sub = new roslib.Topic({
                        ros: ros,
                        name: '/mode',
                        messageType: 'std_msgs/String'
                    })
                    mode_sub.subscribe(function(data){
                        context.commit('Ros/set_mode',data.data)
                        context.commit('Ros/set_timeout', new Date().getTime());
                    });
                   //*******************************************************//     
                    // var status_sub = new roslib.Topic({
                    //     ros: ros,
                    //     name: '/status',
                    //     messageType: 'status_msgs/status'
                    // })
                    // status_sub.subscribe(function(data){
                    //     context.commit('Ros/set_status',data)
                    // });
                   //*******************************************************//     
                    // var current_location_sub = new roslib.Topic({
                    //     ros: ros,
                    //     name: '/current_pose',
                    //     messageType: 'geometry_msgs/Pose'
                    // })
                    // current_location_sub.subscribe(function(data){
                    //     context.commit('Ros/set_current_location',data)
                    // });
                   //*************************** Map ****************************//     
                    // var map_sub = new roslib.Topic({
                    //     ros: ros,
                    //     name: '/map',
                    //     messageType: 'nav_msgs/OccupancyGrid',
                    //     compression : 'png'
                    // })
                    // map_sub.subscribe(function(data){
                    //     console.log('new map');
                    //     context.commit('Ros/set_map',data)
                    // });
                    //*******************************************************//    
                     var cash_reader_controller = new roslib.Topic({
                         ros: ros,
                         name: '/cash_reader/control',
                         messageType: 'std_msgs/String',
                     })
                     context.commit('Ros/set_cash_reader_controller', cash_reader_controller)
                   //*******************************************************//    
                    var action_client = new roslib.Service({
                        ros: ros, 
                        name: '/action',
                        serviceType: 'action_handler_msgs/action_srv'
                    })                    
                    context.commit('Ros/set_action_client',action_client);
                   //*******************************************************//     

                    setTimeout( async function(){
                        console.log('starting checking loop')
                        context.commit('Ros/set_timeout', new Date().getTime());
                        while (true) {
                            await sleep(3000);
                            if(new Date().getTime() - context.models['Ros'].state.timeout > 3000){
                                context.dispatch('Ros/reconnect');
                                break;
                            }
                        }
                    }, 3000);

                    resolve();
                }else{
                    reject({message:'ros is not connected'})
                }
            })
        },
        check_vouchers(context){
            return new Promise((resolve,reject)=>{
                if(context.models['Ros'].state.vouchers.length >0){
                    voucher = context.models['Ros'].state.vouchers.pop()
                    resolve(voucher)
                }else{
                    reject({message: 'no voucher to be displayed'})
                }
            })
        },
        take_action(context, action_name){
            return new Promise((resolve,reject)=>{
                if(Object.keys(context.models['Ros'].state.action_client).length == 0){
                    reject();
                }
                var request = new roslib.ServiceRequest({
                    action: action_name
                })
                context.models['Ros'].state.action_client.callService(request,result=>{
                    if(result.result == 'failed'){
                        reject(result.result)
                    }else{
                        resolve(result.result);
                    }
                })
            })
        },
        cash_reader_cancel(context){
            return new Promise((resolve,reject)=>{
                console.log('cancelling cash reader')
                if(Object.keys(context.models['Ros'].state.cash_reader_controller).length == 0){
                    console.log('failed to cancel cash reader, the object does not exist',context.models['Ros'].state.cash_reader_controller )
                    reject();
                }
                var msg = new roslib.Message({
                    data: '1'
                })
                context.models['Ros'].state.cash_reader_controller.publish(msg)
                resolve()
            })
        }
    },
    mutations:{
        set_ros(state, ros ){
            state.ros = ros;
        }, 
        set_mode(state, mode){
            state.mode = mode;
        }, 
        set_mode_topic(state, mode_topic){
            console.log('setting change mode topic publisher',mode_topic)
            state.mode_topic = mode_topic
        },
        set_status(state, status){
            state.status = status;
        },
        set_timeout(state,time){
            state.timeout = time;
        },
        add_voucher(state,voucher){
            console.log('adding voucher, current voucher is ',state.vouchers, 'the new voucher is ', voucher)
            state.vouchers.push(voucher)
        },
        set_action_client(state,client){
            state.action_client = client;
        },
        set_current_location(state,pose){
            state.current_location = pose;
        },
        set_map(state,map){
            state.map = map;
        },
        set_cash_reader_controller(state, publisher){
            state.cash_reader_controller = publisher;
        },
    },
    getters:{
        get_ros(state){
            if(Object.keys(state.ros).length != 0){
                return state.ros;
            }else{
                return null
            }
        },
        get_mode(state){
            return state.mode;
        },
        get_status(state){
            if(Object.keys(state.status).length !=0){
                return state.status;
            }else{
                return null;
            }
        },
        get_current_location(state){
            if(Object.keys(state.current_location).length !=0){
                return state.current_location;
            }else{
                return null;
            }
        },
        get_map(state){
            if(Object.keys(state.map).length !=0){
                return state.map;
            }else{
                return null;
            }
        },
    }
}
