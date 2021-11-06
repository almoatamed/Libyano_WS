
import roslib from 'roslib'
import router from '../../router/index'
function sleep(time){
  return new Promise(resolve => setTimeout(resolve, time))
}


function route(name){    
    router.push({name:name})
}

async function initiate(retryTime){
    var x = true
    while (x) {
      var ros = new roslib.Ros({
        url : 'ws://127.0.0.1:9090'
      })
      ros.on('connection',function(){
        x = false;
        console.log('connecting')
      })
      ros.on('error',function(err){
        console.log('connection error',err)
      })
      await sleep(retryTime)
    }
    console.log('connected')
    return new Promise(resolve=>{
      resolve(ros)
    })
}

export default {
    namespaced: true,

    state: {
        ros: false,
        mode_change_topic:'/mode/change_mode', 
        mode_change_pub:false
    },
    actions: {

        init({ commit }) {
            return new Promise((resolve)=>{
                initiate(1500).then((ros_obj)=>{
                    var ros = ros_obj;
                
                    var rout_sub = new roslib.Topic({
                      ros: ros ,
                      name: '/interactive/set_web_page',
                      messageType: 'std_msgs/String'
                    })
                
                    rout_sub.subscribe(function(data){
                      console.log(data.data)
                      if (data.data == 'slide_show'){
                        route('slide_show');
                      }else if (data.data == 'services'){
                        route('services');
                      }
                    });

                    var mode_sub = new roslib.Topic({
                      ros: ros ,
                      name: '/mode/change_mode',
                      messageType: 'std_msgs/String'
                    })

                    commit('setRos', {ros, mode_sub})
                    resolve()
                  })
            })
        },
    },
    mutations: {
        setRos(state,obj) {
            state.ros = obj.ros
            state.mode_change_pub = obj.mode_sub
        },
    },
}