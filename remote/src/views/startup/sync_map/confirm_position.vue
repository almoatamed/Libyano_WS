<template>
  <v-container fluid id='root' fill-height class="pa-0 ma-0" >

    
    <canvas fill-height class="pa-0 ma-0" id="map"></canvas>
    <canvas v-show="false" id='temp'></canvas>
    <v-card 
        class=" px-2"
        flat
        style="background-color:rgba(20,20,30,1);width:150px;right:10px;bottom:27%;position:absolute;"
        rounded='xl'
        dark
    >
        <v-card-text>

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
                <v-btn color="purple accent-4" @mousedown="continue_movement_up = true; up($event)" @mouseup="continue_movement_up = false;" fab small icon>
                    <v-icon>
                        mdi-chevron-up
                    </v-icon>
                </v-btn>
                <v-spacer></v-spacer>
            </v-row>
            <v-row class="pa-2">
                <v-btn color="purple accent-4" @mousedown="continue_movement_left = true; left($event)" @mouseup="continue_movement_left = false;"  fab small icon>
                    <v-icon>
                        mdi-chevron-left
                    </v-icon>
                </v-btn>
                <v-spacer></v-spacer>
                <v-btn color="purple accent-4" @mousedown="continue_movement_right = true; right($event)" @mouseup="continue_movement_right = false;" fab small icon>
                    <v-icon>
                        mdi-chevron-right
                    </v-icon>
                </v-btn>
            </v-row>
            <v-row class="pa-2">
                <v-spacer></v-spacer>
                <v-btn color="purple accent-4" @mousedown="continue_movement_down = true; down($event)" @mouseup="continue_movement_down = false;" fab small icon>
                    <v-icon>
                        mdi-chevron-down
                    </v-icon>
                </v-btn>
                <v-spacer></v-spacer>
            </v-row>
        </v-card-text>
    </v-card>
    <v-card 
        class="floating px-2"
        flat
        style="background-color:rgba(20,20,30,1)"
        rounded='xl'
        dark
    >
        <v-divider></v-divider>

        <v-card-title :dark='isDark' class="">
            Confirm Position
        </v-card-title>

        <v-card-text :dark='true'>
            Is the robot placed properly?
        </v-card-text>

        <v-card-actions>                    
        <v-dialog
        v-model="cancel_dialog"
        :dark='isDark'
        width="500"
        >
        <template v-slot:activator="{ on, attrs }">
            <v-btn
            color="purple white--text"
            :dark='isDark'
            v-bind="attrs"
            v-on="on"
            text
            :loading='continue_loading'
            :disabled="continue_loading"
            >
                Cancel
            </v-btn>
        </template>

        <v-card class="pa-4">
            <v-card-title class="">
                Cancel Salmming
            </v-card-title>

            <v-card-text>
                If you cancel the slamming procedure all the work has been done will be ignored.
                <br> Cancel?
            </v-card-text>

            <v-divider></v-divider>

            <v-card-actions>
            <v-btn
                color="purple"
                text
                @click="cancel();cancel_dialog=false"
            >
                Yes
            </v-btn>
            <v-spacer></v-spacer>
            <v-btn
                color="purple"
                text
                @click="cancel_dialog = false"
            >
                No
            </v-btn>
            </v-card-actions>
        </v-card>
        </v-dialog>
        <v-spacer></v-spacer>
        <v-btn
            color="purple"
            text
            :loading='continue_loading'
            :disabled="continue_loading || !update_flag"
            @click="update_position()"
        >
            Update Position
        </v-btn>
        <v-spacer></v-spacer>
        <v-btn
            color="purple"
            text
            :loading='continue_loading'
            :disabled="continue_loading"
            @click="confirm()"
        >
            Confirm
        </v-btn>
        </v-card-actions>
    </v-card>
  </v-container>
</template>

<script>
import env from '../../../../env'
import ROSLIB from 'roslib'
import q from 'quaternion'
var root

var canvas
var c
var temp_canvas
var temp_c

var bar
var map
var imageData
var current_pose

var zoom = 1.0
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
            // ////console.log(mapdata)
            var i = (mapdata.info.width - col + (row * mapdata.info.width))*4
            // i = (mapdata.info.width*mapdata.info.height)*4 -i
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

function drawpoint(){
    if(point.draw){
        drawarrow(point.robot_x,point.robot_y,point.angle,'green')
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
    drawpoint()
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

            continue_movement_left :false,
            continue_movement_up :false,
            continue_movement_right :false,
            continue_movement_down :false,

            continue_zoomout :false,
            continue_zoomin :false,


            canvas:null,
            temp_canvas:null,
            c:null,
            temp_c:null,
            
            cancel_dialog:false,
            continue_loading:false,
            update_flag:false,
            
        }
    },
    methods:{

        //############################################## Arrow Controls #####################################
        down(){
            if(this.continue_movement_down){
                this.movedown()
                setTimeout(this.down,60)
            }
        },
        up(){
            if(this.continue_movement_up){
                this.moveup()
                setTimeout(this.up,60)
            }
        },
        right(){
            if(this.continue_movement_right){
                this.moveright()
                setTimeout(this.right,60)
            }
        },
        left(){
            if(this.continue_movement_left){
                this.moveleft()
                setTimeout(this.left,60)
            }
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
        angled_goal_mousedown_handler(e){
            var data = c.getImageData(e.layerX,e.layerY,1,1).data
            if(data[0] == 255, data[1] == 255, data[2] == 255){
                this.update_flag = false
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
                point.pose = {}
                point.pose.position = {}
                point.pose.position.x = point.robot_x
                point.pose.position.y = point.robot_y
                point.pose.position.z = 0.0
                point.pose.orientation = {}
                point.pose.orientation.x = qs.x
                point.pose.orientation.y = qs.y
                point.pose.orientation.z = qs.z
                point.pose.orientation.w = qs.w
                if(point.angle){
                    point.draw = true
                    if(point.draw){
                        this.update_flag  = true
                    }
                }
                console.log(point)


            }
        },
        //######################## stage controller #################################3

        cancel(){
            this.continue_loading = true
            console.log('Where There is Will there is Way')
            this.$store.dispatch('Ros/take_action', 'startup/remote_interface', {root:true}).then(res=>{
                if(res=='confirm_position'){
                    console.log(res)
                    this.$store.dispatch('Ros/take_action', 'startup/perform/slam/confirm/end', {root:true}).then(res=>{
                        console.log(res)
                        this.$router.push({name:'startup_loading'})
                    })
                }else{
                    this.continue_loading = false
                }
            })
        },
        update_position(){
            this.continue_loading = true
            if(!point.draw){
                console.log('error man')
                return 
            }
            this.$store.dispatch('Ros/take_action', 'startup/remote_interface', {root:true}).then(res=>{
                if(res=='confirm_position'){
                    console.log(res)
                    this.$store.dispatch('Ros/take_action', `navigation/update_pose/${point.pose.position.x}&${point.pose.position.y}&${point.pose.position.z}&${point.pose.orientation.x}&${point.pose.orientation.y}&${point.pose.orientation.z}&${point.pose.orientation.w}`,{root:true}).then(res=>{
                        console.log(res)
                        this.continue_loading = false
                    })
                }else{
                    this.continue_loading = false
                }
            })
        },
        confirm(){
            this.continue_loading = true
            this.$store.dispatch('Ros/take_action', 'startup/remote_interface', {root:true}).then(res=>{
                if(res=='confirm_position'){
                    console.log(res)
                    this.$store.dispatch('Ros/take_action', `startup/perform/chose_existing_map/confirm/yes`,{root:true}).then(res=>{
                        console.log(res)
                    })
                }else{
                    this.continue_loading = false
                }
            })
        }
    },
    mounted(){
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

        canvas.addEventListener('mousedown',this.angled_goal_mousedown_handler)
        canvas.addEventListener('mouseup',this.angled_goal_mouseup_handler)
    },
    destroyed(){
        canvas.removeEventListener('mousedown',this.angled_goal_mousedown_handler)
        canvas.removeEventListener('mouseup',this.angled_goal_mouseup_handler)
    },
    computed:{
        nopoint(){
            return !point.draw
        },
        isDark(){
        return this.$store.getters['Theme/isDark']
        }
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