<template>
  <v-container fluid id='root' fill-height class="pa-0 ma-0" >

    
    <canvas fill-height class="pa-0 ma-0" id="map"></canvas>
    <canvas v-show="false" id='temp'></canvas>
    <v-card 
        class="floating px-2"
        width="170px"
        flat
        style="background-color:rgba(20,20,30,1)"
        rounded='xl'
    >
        <v-card-text>
            <v-row class="pa-2">
                <v-switch label="Go Home" color="purple accent-4" :disabled='control_loading' :loading="control_loading" @change="go_home()"  v-model="go_home_model" dark ></v-switch>
                <v-spacer></v-spacer>
                <v-switch label="Manual" color="purple accent-4" :disabled='control_loading' :loading="control_loading" @change="manual"  v-model="controllers" dark ></v-switch>
            </v-row>
        </v-card-text>
        <v-card-text v-if='controllers'>
            <v-row class="pa-2">
                <v-btn text color="purple accent-4"  :disabled='goal_flag' @click='wait_for_angled_goal'>Arrow Goal</v-btn>
                <v-btn text color="purple accent-4"  :disabled='goal_flag' @click='wait_for_unangled_goal'>Point Goal</v-btn>
                <v-btn text color="purple accent-4"  :disabled='!goal_flag' @click='cancel_goal'>Cancel</v-btn>
                <v-btn text color="purple accent-4"  :disabled='goal_flag' @click='clear_goal'>clear</v-btn>
            </v-row>
            <v-row class="pa-2">
                <v-spacer></v-spacer>
                <v-switch label="arrow control" color="purple accent-4"  v-model="cmd_vel" dark ></v-switch>
                <v-spacer></v-spacer>
            </v-row>
            <v-row class="pa-2">
                <v-btn color="purple accent-4" @mousedown="continue_zoomin = true; zoomin($event)" @mouseup="continue_zoomin = false;" fab small icon>
                    <v-icon>
                        mdi-plus
                    </v-icon>
                </v-btn>
                <v-spacer></v-spacer>
                <v-btn color="purple accent-4" fab small @mousedown="continue_zoomout = true; zoomout($event)" @mouseup="continue_zoomout = false;" icon>
                    <v-icon>
                        mdi-minus
                    </v-icon>
                </v-btn>
            </v-row>
            <v-row class="pa-2">
                <v-spacer></v-spacer>
                <v-btn color="purple accent-4" @mousedown="continue_movement_up = true; up($event)" @mouseup="continue_movement_up = false;stop()" fab small icon>
                    <v-icon>
                        mdi-chevron-up
                    </v-icon>
                </v-btn>
                <v-spacer></v-spacer>
            </v-row>
            <v-row class="pa-2">
                <v-btn color="purple accent-4" @mousedown="continue_movement_left = true; left($event)" @mouseup="continue_movement_left = false;stop()"  fab small icon>
                    <v-icon>
                        mdi-chevron-left
                    </v-icon>
                </v-btn>
                <v-spacer></v-spacer>
                <v-btn color="purple accent-4" @click="stop()" fab small icon>
                    <v-icon>
                        mdi-close-circle-outline
                    </v-icon>
                </v-btn>
                <v-spacer></v-spacer>
                <v-btn color="purple accent-4" @mousedown="continue_movement_right = true; right($event)" @mouseup="continue_movement_right = false;stop()" fab small icon>
                    <v-icon>
                        mdi-chevron-right
                    </v-icon>
                </v-btn>
            </v-row>
            <v-row class="pa-2">
                <v-spacer></v-spacer>
                <v-btn color="purple accent-4" @mousedown="continue_movement_down = true; down($event)" @mouseup="continue_movement_down = false;stop()" fab small icon>
                    <v-icon>
                        mdi-chevron-down
                    </v-icon>
                </v-btn>
                <v-spacer></v-spacer>
            </v-row>
        </v-card-text>
    </v-card>
  </v-container>
</template>

<script>
import env from '../../../env'
import ROSLIB from 'roslib'
import q from 'quaternion'
var root

var canvas
var c
var temp_canvas
var temp_c

var bar
var goal_monitor
var map
var imageData
var current_pose
var global_path = {}

var zoom = 2.5
var movx = 0
var movy = 0

// ####################### connecting to ros #################################3
function sleep(duration){
    return new Promise(resolve => setTimeout(resolve, duration))
}
async function connect_to_ros(){
    var flag = true;
    var ros;
    while(flag){
        await sleep(1500).then(()=>{
            ros = new ROSLIB.Ros({
                url : `ws://${env.bridge_address}:9090`
            });
            ros.on('connection', function(){
                flag = false;
                ////console.log('Ros: connected to rosbridge successfully')
            });
            ros.on('error',function(){
                console.error('error connecting to rosbridge')
            })
        })
    }
    return new Promise(resolve => resolve(ros))
}

// ########################### converting map data to image data valid for canvas ##########3
function makemap(tem_mapdata){
    var mapdata = {}
    Object.assign(mapdata, tem_mapdata)
    temp_canvas.width = mapdata.info.width;
    temp_canvas.height = mapdata.info.height;
    imageData = c.createImageData(mapdata.info.width, mapdata.info.height)
    for ( var row = mapdata.info.height-1; row > -1; row--) {
        for ( var col = mapdata.info.width-1; col > -1; col--) {
            var mapI = (col + (row * mapdata.info.width))
            var data = mapdata.data[mapI];
            var val;
            if (data === 100) {
                val = 0;
            } else if (data === 0) {
                val = 255;
            } else {
                val = 127;
            }

            // determine the index into the image data array
            // also should be equal to width*height - mapI
            var i = (mapdata.info.width - col + (row * mapdata.info.width))*4
            // r
            imageData.data[i] = val;
            // g
            imageData.data[++i] = val;
            // b
            imageData.data[++i] = val;
            // a
            imageData.data[++i] = 255;
        }
    }
}

// ########################## clearing frame ########################################
function clear(){
    c.moveTo(0,0)
    c.beginPath()
    c.rect(0,0,canvas.width,canvas.height);  
    c.fillStyle = "rgb(127,127,127)"
    c.fill();
    c.closePath()
}

// ######################## robot position #################################
function q2y(orientation) {
  var q0 = orientation.w;
  var q1 = orientation.x;
  var q2 = orientation.y;
  var q3 = orientation.z;
  return -Math.atan2(2 * (q0 * q3 + q1 * q2), 1 - 2 * (q2 * q2 + q3 * q3));
}
function translatepose(x,y,q){
    // the 10 should be replaced with the accurate value of the map dimention 
    // this is an echo of the map metadata
    // map_load_time: 
    // secs: 687
    // nsecs: 693000000
    // resolution: 0.0500000007451
    // width: 384
    // height: 384
    // origin: 
    // position: 
    //     x: -10.0
    //     y: -10.0
    //     z: 0.0
    // orientation: 
    //     x: 0.0
    //     y: 0.0
    //     z: 0.0
    //     w: 1.0
    //
    // position is where we take these values from

    var xp  = map.info.width -((x-map.info.origin.position.x)/map.info.resolution)
    var yp  = (y-map.info.origin.position.y)/map.info.resolution
    var theta = null
    if (q){
        theta = q2y(q)
        if(theta<0){
            theta = Math.PI*2 +theta
        }
    }
    return {x:xp,y:yp,theta}
}
function drawpos(){
    if(current_pose){
        var arrow_length = 7
        var mapping = translatepose(current_pose.position.x,current_pose.position.y,current_pose.orientation);
        var x = mapping.x //-arrow_length/2//*Math.cos(mapping.theta)
        var y = mapping.y //-arrow_length/2//*Math.sin(mapping.theta)
        var theta = mapping.theta +Math.PI
        var start_theta = theta + Math.PI/6
        var end_theta = theta - Math.PI/6
        start_theta = start_theta > 2*Math.PI? start_theta - 2*Math.PI: start_theta <0 ? start_theta +2*Math.PI: start_theta
        end_theta = end_theta > 2*Math.PI? end_theta - 2*Math.PI: end_theta <0 ? end_theta +2*Math.PI: end_theta
        temp_c.beginPath();
        temp_c.moveTo(x,y)
        temp_c.arc(x, y,arrow_length,start_theta,end_theta)    
        temp_c.fillStyle = "purple"
        temp_c.fill();
        temp_c.closePath()
    }
}

// ######################### goal animation #############################
var point = {}
function drawpoint(x,y,color,diameter){
        var mapping = translatepose(x,y);        
        temp_c.beginPath();
        temp_c.moveTo(mapping.x,mapping.y)
        temp_c.arc(mapping.x, mapping.y,diameter,0,2*Math.PI)    
        temp_c.fillStyle = color
        temp_c.fill();
        temp_c.closePath()
        
}
function drawarrow(x,y,angle,color){
    var mapping = translatepose(x,y)
    var x_end = (20*Math.cos(angle)+mapping.x)
    var y_end = (-20*Math.sin(angle)+mapping.y)
    temp_c.beginPath();
    temp_c.moveTo(mapping.x, mapping.y);
    temp_c.lineTo(x_end, y_end);
    temp_c.strokeStyle = color;
    temp_c.lineWidth = 2;
    temp_c.stroke();
    temp_c.closePath();
}
function drawTrack(){
    if(global_path.poses){

        if(global_path.poses.length > 0){
            global_path.poses.forEach((pose) => {
                drawpoint(pose.pose.position.x,pose.pose.position.y,'blue', 1)
            });
        }
    }
}
function drawgoal(){
    if(point.draw && goal_monitor)   {
        var color = 'blue'
        if(!((point.robot_x - goal_monitor['pose']['x'] < 0.15) && (point.robot_y - goal_monitor['pose']['y'] < 0.15))){
            console.log('returning')
            return 
        }
        if(goal_monitor.state == 'succeed'){
            color = 'green'
        }else if(goal_monitor.state == 'running'){
            drawTrack()
            color = 'orange'
        }else if(goal_monitor.state == 'false'){
            color = 'red'
        }
        if(goal_monitor.is_angled){
            drawarrow(point.robot_x,point.robot_y,point.angle,color)
        }else{
            drawpoint(point.robot_x,point.robot_y,color,2)
        }
    }
}

// ########################### draw map frame ##################################
function drawmap(){
  if(imageData){
    temp_c.beginPath()
    temp_c.moveTo(0,0)
    temp_c.putImageData(imageData,0,0)
    temp_c.closePath()
    drawpos()
    drawgoal()
    c.drawImage(temp_canvas,movx,movy,(canvas.width/zoom) >> 0,(canvas.height/zoom) >> 0,0,0,canvas.width,canvas.height)
    c.closePath()
  }
}

// ########################### frame drawer #####################################
async function draw(){
  clear()
  drawmap()
  await sleep(100)
  requestAnimationFrame(draw)
} 

// ############################# vue #########################################3
export default {
    data(){
        return{
            cmd_vel:false,
            cmd_vel_pub:null,

            goal_pub:null,
            unangled_goal_pub:null,
            continue_movement_left :false,
            continue_movement_up :false,
            continue_movement_right :false,
            continue_movement_down :false,

            continue_zoomout :false,
            continue_zoomin :false,

            goal_flag: false,

            canvas:null,
            temp_canvas:null,
            c:null,
            temp_c:null,
            
            control_loading:false,
            go_home_model: false,
            controllers: false,
        }
    },
    methods:{

        //############################################## Arrow Controls #####################################
        down(){
            if(this.continue_movement_down){
                if(this.cmd_vel){
                    this.cmd_vel_down()
                }else{
                    this.movedown()
                }
                setTimeout(this.down,60)
            }
        },
        up(){
            if(this.continue_movement_up){
                if(this.cmd_vel){
                    this.cmd_vel_up()
                }else{
                    this.moveup()
                }
                setTimeout(this.up,60)
            }
        },
        right(){
            if(this.continue_movement_right){
                if(this.cmd_vel){
                    this.cmd_vel_right()
                }else{
                    this.moveright()
                }
                setTimeout(this.right,60)
            }
        },
        left(){
            if(this.continue_movement_left){
                if(this.cmd_vel){
                    this.cmd_vel_left()
                }else{
                    this.moveleft()
                }
                setTimeout(this.left,60)
            }
        },

        //############################################## Cmd vel Controls #####################################
        cmd_vel_right(){
            var twist = new ROSLIB.Message({
             linear : {
             x : 0.0,
             y : 0.0,
             z : 0.0
             },
             angular : {
             x : 0.0,
             y : 0.0,
             z : -1.0
             }
            });
            this.cmd_vel_pub.publish(twist);
        },
        cmd_vel_left(){
            var twist = new ROSLIB.Message({
             linear : {
             x : 0.0,
             y : 0.0,
             z : 0.0
             },
             angular : {
             x : 0.0,
             y : 0.0,
             z : 1.0
             }
            });
            this.cmd_vel_pub.publish(twist);
        },
        cmd_vel_up(){
            var twist = new ROSLIB.Message({
             linear : {
             x : 0.24,
             y : 0.0,
             z : 0.0
             },
             angular : {
             x : 0.0,
             y : 0.0,
             z : 0.0
             }
            });
            this.cmd_vel_pub.publish(twist);
        },
        cmd_vel_down(){
            var twist = new ROSLIB.Message({
             linear : {
             x : -0.24,
             y : 0.0,
             z : 0.0
             },
             angular : {
             x : 0.0,
             y : 0.0,
             z : 0.0
             }
            });
            this.cmd_vel_pub.publish(twist);
        },
        stop(){
            var twist = new ROSLIB.Message({
            linear : {
            x : 0.0,
            y : 0.0,
            z : 0.0
            },
            angular : {
            x : 0.0,
            y : 0.0,
            z : 0.0
            }
            });
            this.cmd_vel_pub.publish(twist);
        },

        //#################################### Zoom Control ####################################################
        zoomin(){
            if(this.continue_zoomin){
                if(zoom < 2.5){
                    zoom+=0.1
                }else{
                    this.continue_zoomin = false;
                }
                setTimeout(this.zoomin,60)
            }
        },
        zoomout(){
            if(this.continue_zoomout){
                if(zoom > 0.5){
                    zoom-=0.1
                }else{
                    this.continue_zoomout = false;
                }
                setTimeout(this.zoomout,60)
            }
        },

        //######################################### map location Controls #####################################
        moveup(){
            if(movy> -0.1*canvas.height){
                movy-=10
            }else{
                this.continue_movement_up = false;
            }
        },
        movedown(){
            if((movy+canvas.height/zoom) < 1.1*canvas.height){
                movy+=10
            }else{
                this.continue_movement_down = false;
            }
        },
        moveright(){
            if((movx+canvas.width/zoom) < 1.1*canvas.width){
                movx+=10
            }else{
                this.continue_movement_right = false;
            }
        },
        moveleft(){            
            if(movx> -0.1*canvas.width){
                movx-=10
            }else{
                this.continue_movement_left = false;
            }
        },

        //######################### goal related methods ##########################
        wait_for_angled_goal(){
            this.goal_flag = true
            canvas.addEventListener('mousedown',this.angled_goal_mousedown_handler)
            canvas.addEventListener('mouseup',this.angled_goal_mouseup_handler)
        },
        wait_for_unangled_goal(){
            this.goal_flag = true
            canvas.addEventListener('mousedown',this.unangled_goal_mousedown_handler)
            canvas.addEventListener('mouseup',this.unangled_goal_mouseup_handler)
        },
        angled_goal_mousedown_handler(e){
            var data = c.getImageData(e.layerX,e.layerY,1,1).data
            if(data[0] == 255, data[1] == 255, data[2] == 255){
                point = {}
                point.x = (e.layerX/zoom + movx) 
                point.layerX = e.layerX
                point.y = (e.layerY/zoom + movy) 
                point.layerY = e.layerY
                point.drop = true
                point.draw = false
            }
        },
        angled_goal_mouseup_handler(e){
            if(point.drop && map.info){
                point.drop = false
                point.abs_angle = Math.atan(Math.abs((e.layerY - point.layerY)/(e.layerX - point.layerX)))
                point.end_layerX = e.layerX 
                point.end_layerY = e.layerY 

                // if(point.end_layerX - point.layerX > 0){
                //     point.x_end = (20*Math.cos(point.abs_angle)+point.x)
                // }else{
                //     point.x_end = (-20*Math.cos(point.abs_angle)+point.x)
                // }
                // if(point.end_layerY - point.layerY > 0){
                //     point.y_end = (20*Math.sin(point.abs_angle)+point.y)
                // }else{
                //     point.y_end = (-20*Math.sin(point.abs_angle)+point.y)
                // }

                if(point.end_layerX - point.layerX > 0){
                    if(point.end_layerY - point.layerY > 0){
                        point.angle = 2*Math.PI - point.abs_angle
                    }else{
                        point.angle = point.abs_angle
                    }
                }else{
                    if(point.end_layerY - point.layerY > 0){
                        point.angle = Math.PI + point.abs_angle 
                    }else{
                        point.angle = Math.PI - point.abs_angle
                    }
                }

                point.robot_angle = Math.PI + point.angle
                if(point.robot_angle> 2*Math.PI){
                    point.robot_angle = -2*Math.PI + point.robot_angle
                }
                
                point.robot_x = (map.info.width - point.x)*map.info.resolution + map.info.origin.position.x
                point.robot_y = (point.y)*map.info.resolution + map.info.origin.position.y
                // console.log(map.info)
                // console.log('point')
                // console.log(point.robot_angle*180/Math.PI)
                var qs = q.fromEuler(0,0,point.robot_angle,"XYZ")
                point.draw = true
                var goal_msg = new ROSLIB.Message({
                    header: {
                        seq: 0,
                        stamp: 0,
                        frame_id: 'slamware_map'
                    },
                    pose:{
                        position:{
                            x:point.robot_x,
                            y:point.robot_y,
                            z:point.robot_z,
                        },
                        orientation:{
                            x:qs.x,
                            y:qs.y,
                            z:qs.z,
                            w:qs.w,
                        }
                    }
                })
                // console.log(goal_msg)
                this.goal_pub.publish(goal_msg)
            }
            this.cancel_goal()
        },
        unangled_goal_mousedown_handler(e){
            var data = c.getImageData(e.layerX,e.layerY,1,1).data
            if(data[0] == 255, data[1] == 255, data[2] == 255){
                point = {}
                point.x = (e.layerX/zoom + movx) 
                point.layerX = e.layerX
                point.y = (e.layerY/zoom + movy) 
                point.layerY = e.layerY
                point.drop = true
                point.draw = false
            }
        },
        unangled_goal_mouseup_handler(){
            if(point.drop && map.info){
                point.drop = false
    
                point.robot_x = (map.info.width - point.x)*map.info.resolution + map.info.origin.position.x
                point.robot_y = (point.y)*map.info.resolution + map.info.origin.position.y
                point.draw = true
                var goal_msg = new ROSLIB.Message({
                    location:{
                        x:point.robot_x,
                        y:point.robot_y,
                        z:0
                    }
                })
                // console.log(goal_msg)
                this.unangled_goal_pub .publish(goal_msg)
            }
            this.cancel_goal()
        },
        clear_goal(){
            point = {}
        },
        cancel_goal(){
            this.goal_flag = false
            canvas.removeEventListener('mousedown',this.angled_goal_mousedown_handler)
            canvas.removeEventListener('mouseup',this.angled_goal_mouseup_handler)
            canvas.removeEventListener('mousedown',this.unangled_goal_mousedown_handler)
            canvas.removeEventListener('mouseup',this.unangled_goal_mouseup_handler)
        },
        //################################################ controls ##############################################
        go_home(){
            this.control_loading = true
            if(this.go_home_model){
                this.$store.dispatch('Ros/take_action',`global_actions/switch_mode/sth`).then(()=>{
                    this.clear_goal()
                    setTimeout(()=>{
                        this.control_loading = false
                    },200)
                }).catch(()=>{
                    setTimeout(()=>{
                        this.go_home_model = false
                        this.control_loading = false
                    },200)
                })
            }else{
                this.$store.dispatch('Ros/take_action',`global_actions/switch_mode/sthcancel`).then(()=>{
                    this.clear_goal()
                    setTimeout(()=>{
                        this.control_loading = false
                        this.go_home_model = false
                    },100)
                }).catch(()=>{
                    setTimeout(()=>{
                        this.control_loading = false
                    },100)
                })
            }
        },
        manual(){
            this.control_loading = true
            if(this.controllers){
                this.controllers = false
                this.$store.dispatch('Ros/take_action',`global_actions/switch_mode/mnl`).then(()=>{
                    this.clear_goal()
                    setTimeout(()=>{
                        this.control_loading = false
                    },100)
                }).catch(()=>{
                    setTimeout(()=>{
                        this.control_loading = false
                    },100)
                })
            }else{
                this.controllers = true
                this.$store.dispatch('Ros/take_action',`global_actions/switch_mode/mnlcancel`).then(()=>{
                    this.clear_goal()
                    setTimeout(()=>{
                        this.control_loading = false
                    },100)
                }).catch(()=>{
                    setTimeout(()=>{
                        this.control_loading = false
                    },100)
                })
            }
        }
    },
    watch:{
        mode(val){
            this.controllers = false
            if(val == 'mnl'){
                this.controllers = true
            }
        }
    },
    mounted(){
        var self = this;
        
        if(this.mode == 'sth'){
            this.go_home_model = true
        }else if(this.mode == 'mnl'){
            this.controllers = true
        }

        this.canvas = canvas = document.getElementById('map')
        this.temp_canvas = temp_canvas = document.getElementById('temp')

        root = document.getElementById('root')
        bar = document.getElementById('mainbar')

        canvas.width = root.offsetWidth
        canvas.height = window.innerHeight - bar.offsetHeight
        

        this.c = c = canvas.getContext('2d')
        this.temp_c = temp_c = temp_canvas.getContext('2d')

        setTimeout(()=>{
            connect_to_ros().then(ros=>{
                var pose_sub = new ROSLIB.Topic({
                    ros: ros,
                    name: '/current_pose',
                    messageType: 'geometry_msgs/Pose',
                })
                pose_sub.subscribe(function(data){
                    // console.log(data)
                    current_pose = data
                }); 

                var global_path_sub = new ROSLIB.Topic({
                    ros: ros,
                    name: '/slamware_ros_sdk_server_node/global_plan_path',
                    messageType: 'nav_msgs/Path',
                })
                global_path_sub.subscribe(function(data){
                    // console.log(data)
                    global_path = data
                }); 
                
                var map_sub = new ROSLIB.Topic({
                    ros: ros,
                    name: '/slamware_ros_sdk_server_node/map',
                    messageType: 'nav_msgs/OccupancyGrid',
                    compression : 'png'
                })
                map_sub.subscribe(function(data){
                    map  = data;
                    makemap(data);
                });
                
                var goal_monitor_sub = new ROSLIB.Topic({
                    ros: ros,
                    name: '/navigation/goal_monitor',
                    messageType: 'status_msgs/goal_monitor_msg',
                })
                goal_monitor_sub.subscribe(function(data){
                    goal_monitor = data
                });
                
                self.cmd_vel_pub = new ROSLIB.Topic({
                    ros : ros,
                    name : '/navigation/cmd_vel_req',
                    messageType : 'geometry_msgs/Twist'
                });

                self.goal_pub = new ROSLIB.Topic({
                    ros : ros,
                    name : '/navigation/goal_req',
                    messageType : 'geometry_msgs/PoseStamped'
                });

                self.unangled_goal_pub = new ROSLIB.Topic({
                    ros : ros,
                    name : '/navigation/unangled_goal_req',
                    messageType : 'slamware_ros_sdk/MoveToRequest'
                });

            })

        },10)

        // this event listener used to set the canvas to fit the window changes 
        window.onresize = function(){
          setTimeout(()=>{
            canvas.width = root.offsetWidth
            canvas.height = window.innerHeight - bar.offsetHeight
          },10)
        }
        draw()

    },
    computed:{
        mode(){
            return this.$store.getters['Ros/mode']
        },
    }
}
</script>

<style scoped>
.floating{
    position: absolute;
    bottom: 10px;
    right: 10px;
}
</style>