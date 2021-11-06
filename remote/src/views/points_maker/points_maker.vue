<template>
  <v-container fluid id='root' fill-height class="pa-0 ma-0" >

    <!-- Dispaly save_point -->
    <v-dialog v-model="save_point_dialog" max-width="400px" persistent>
      <v-card class="mx-auto pa-4" max-width="400" outlined dark color="">

        <v-card-text class="text-h5 font-weight-bold" >
            <v-text-field
            v-model="point_name"
            type="text"
            label="Point Name"
            ></v-text-field>
        </v-card-text>
        <v-card-actions>
          <v-btn color="#ffc74a" @click="save_point()" light>
            save
          </v-btn>
          <v-spacer></v-spacer>
          <v-btn color="#ffc74a" @click="save_point_dialog=false " light>
            cancel
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    
    <!-- Dispaly manage points -->
    <v-dialog v-model="manage_points_dialog" >
      <v-card class="mx-auto pa-4"  outlined dark color="">

        <v-card-text class="text-h5 font-weight-bold"  v-if="points.show">
              <v-data-table
                :headers="points.headers"
                :items="points.data"
                class="elevation-1"
              >
                <template v-slot:item.actions="{ item }">
                  <v-icon small class="mr-2" @click="del_point(item.name)">
                    mdi-delete
                  </v-icon>
                </template>
              </v-data-table>
        </v-card-text>
        <v-card-text class="text-h5 font-weight-bold"  v-else>
            Sorry No Point Available
        </v-card-text>
      </v-card>
    </v-dialog>
    <canvas fill-height class="pa-0 ma-0" id="map"></canvas>
    <canvas v-show="false" id='temp'></canvas>
    <v-card 
        class="floating pl-2 pr-3"
        width="200px"
        flat
        style="background-color:rgba(255,255,255,1)"
        rounded='xl'
    >
        <v-card-text >
            <v-row class="pa-2">
                <v-btn text color="yellow darken-2" @click='open_save_point_dialog'>save point</v-btn>
                <v-btn text color="yellow darken-2" @click='open_manage_points_dialog'>manage points</v-btn>
            </v-row>
            <v-row class="pa-2">
                <v-btn color="yellow darken-2" @mousedown="continue_zoomin = true; zoomin($event)" @mouseup="continue_zoomin = false;" fab small icon>
                    <v-icon>
                        mdi-plus
                    </v-icon>
                </v-btn>
                <v-spacer></v-spacer>
                <v-btn color="yellow darken-2" fab small @mousedown="continue_zoomout = true; zoomout($event)" @mouseup="continue_zoomout = false;" icon>
                    <v-icon>
                        mdi-minus
                    </v-icon>
                </v-btn>
            </v-row>
            <v-row class="pa-2">
                <v-spacer></v-spacer>
                <v-btn color="yellow darken-2" @mousedown="continue_movement_up = true; up($event)" @mouseup="continue_movement_up = false;" fab small icon>
                    <v-icon>
                        mdi-chevron-up
                    </v-icon>
                </v-btn>
                <v-spacer></v-spacer>
            </v-row>
            <v-row class="pa-2">
                <v-btn color="yellow darken-2" @mousedown="continue_movement_left = true; left($event)" @mouseup="continue_movement_left = false;"  fab small icon>
                    <v-icon>
                        mdi-chevron-left
                    </v-icon>
                </v-btn>
                <v-spacer></v-spacer>
                <v-btn color="yellow darken-2" @ small icon>
                    <v-icon>
                        mdi-close-circle-outline
                    </v-icon>
                </v-btn>
                <v-spacer></v-spacer>
                <v-btn color="yellow darken-2" @mousedown="continue_movement_right = true; right($event)" @mouseup="continue_movement_right = false;" fab small icon>
                    <v-icon>
                        mdi-chevron-right
                    </v-icon>
                </v-btn>
            </v-row>
            <v-row class="pa-2">
                <v-spacer></v-spacer>
                <v-btn color="yellow darken-2" @mousedown="continue_movement_down = true; down($event)" @mouseup="continue_movement_down = false;" fab small icon>
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

var zoom = 2.0
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
        // console.log('drawing pose')
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
        temp_c.fillStyle = "yellow"
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
            color = 'yellow'
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

            unangled_goal_pub:null,

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

            save_point_dialog: false,
            point_name:'',
            manage_points_dialog: false,
            points: {
                headers: [
                { text: "Name", value: "name", sortable: false, align: "start" },
                { text: "X", value: "x" },
                { text: "Y", value: "y" },
                { text: "Delete", value: "actions", sortable: false },
                ],
                show: false,
                data: null,
                alternative:'Please Scan To Show Nearbye Devices',
            },
        }
    },
    methods:{
        open_manage_points_dialog(){
            this.$store.dispatch('Ros/take_action', 'navigation/fetch_points',{root:true}).then(res=>{
                if(res == ''){
                    this.points.show=false
                    console.log('love')
                }else{
                    res = res.split('|').slice(1)
                    this.points.data = []
                    res.forEach(el=>{
                        el = el.split('&')
                        this.points.data.push({
                            name:el[0],
                            x:el[1],
                            y:el[2]
                        })
                    })
                    this.manage_points_dialog = true
                    this.points.show = true
                    console.log(res)
                }
            })
        },
        save_point(){
            if(point.robot_x && point.robot_y && this.point_name){
                this.$store.dispatch('Ros/take_action', `navigation/add_point/${this.point_name}/${point.robot_x}/${point.robot_y}`, {root:true})
                this.save_point_dialog = false
            }
        },
        del_point(p){
            console.log(p)
            this.$store.dispatch('Ros/take_action', `navigation/del_point/${p}`, {root:true}).then(()=>{
                this.$store.dispatch('Ros/take_action', 'navigation/fetch_points',{root:true}).then(res=>{
                    if(res == ''){
                        this.points.show=false
                        console.log('love')
                    }else{
                        res = res.split('|').slice(1)
                        this.points.data = []
                        res.forEach(el=>{
                            el = el.split('&')
                            this.points.data.push({
                                name:el[0],
                                x:el[1],
                                y:el[2]
                            })
                        })
                        this.manage_points_dialog = true
                        this.points.show = true
                        console.log(res)
                    }
                })
            })
        },
       open_save_point_dialog(){
            if(point.draw && goal_monitor)   {
                if(!((point.robot_x - goal_monitor['pose']['x'] < 0.15) && (point.robot_y - goal_monitor['pose']['y'] < 0.15))){
                    console.log('returning')
                    alert('invalid point')
                    return 
                }
                if(goal_monitor.state == 'succeed'){
                    this.point_name = ''
                    this.save_point_dialog = true
                }
            }
        },

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
                this.$store
                .dispatch(
                    "Ros/take_action",
                    `navigation/unangled_goal/${point.robot_x}&${point.robot_y}`
                )
                .then((res) => {
                    console.log(res);
                    point.draw = true;
                });
            }
        },
    },
    watch:{
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

        setInterval(()=>{
        this.$store.dispatch('Ros/take_action','navigation/get_current_pose', {root:true}).then(res=>{
            current_pose = {}
            res = res.split('&')
            current_pose.position = {}
            current_pose.position.x = parseFloat(res[0])
            current_pose.position.y = parseFloat(res[1])
            current_pose.position.z = parseFloat(res[2])
            current_pose.orientation = {}
            current_pose.orientation.x = parseFloat(res[3])
            current_pose.orientation.y = parseFloat(res[4])
            current_pose.orientation.z = parseFloat(res[5])
            current_pose.orientation.w = parseFloat(res[6])
        })
        },50)
    setTimeout(()=>{
        connect_to_ros().then(ros=>{

            var global_path_sub = new ROSLIB.Topic({
                throttle_rate: 10,
                queue_size:1,
                ros: ros,
                name: '/slamware_ros_sdk_server_node/global_plan_path',
                messageType: 'nav_msgs/Path',
            })
            global_path_sub.subscribe(function(data){
                global_path = data
            }); 
            
            var map_sub = new ROSLIB.Topic({
                throttle_rate: 500,
                // queue_size:1,
                ros: ros,
                name: '/slamware_ros_sdk_server_node/map',
                messageType: 'nav_msgs/OccupancyGrid',
                // compression : 'png'
            })
            map_sub.subscribe(function(data){
                map  = data;
                makemap(data);
            });
            var goal_monitor_sub = new ROSLIB.Topic({
                throttle_rate: 10,
                // queue_size:1,
                ros: ros,
                name: '/navigation/goal_monitor',
                messageType: 'status_msgs/goal_monitor_msg',
            })
            goal_monitor_sub.subscribe(function(data){
                goal_monitor = data
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
        canvas.addEventListener('mousedown',this.unangled_goal_mousedown_handler)
        canvas.addEventListener('mouseup',this.unangled_goal_mouseup_handler)
    },
    beforeDestroy() {
      clearInterval(this.navigation_mode_interval_holder)
    },
    computed:{
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