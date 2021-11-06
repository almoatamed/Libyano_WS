<template>
  <v-container >
      <canvas id="map" width="0" height="0"></canvas>
  </v-container>
</template>

<script>
import ROSLIB from 'roslib';
import env from '../../../../env'


var map = {};
var canvas;
var context ;
var imageData;
var current_pose = null;


function sleep(duration){
    return new Promise(resolve => setTimeout(resolve, duration))
}

async function connect_to_ros(){
    var x = true;
    var ros;
    while(x){
        await sleep(1500).then(()=>{
            ros = new ROSLIB.Ros({
                url : `ws://${env.bridge_address}:9090`
            });
            ros.on('connection', function(){
                x = false;
                console.log('Ros: connected to rosbridge successfully')
            });
            ros.on('error',function(){
                console.error('error connecting to rosbridge')
            })
        })
    }
    return new Promise(resolve => resolve(ros))
}

function makemap(mapdata){
    if(canvas.width ==0){
        canvas.width = mapdata.info.width;
        canvas.height = mapdata.info.height;
    }
    imageData = context.createImageData(mapdata.info.width, mapdata.info.height)
    for ( var row = 0; row < mapdata.info.height; row++) {
        for ( var col = 0; col < mapdata.info.width; col++) {
        // determine the index into the map data
        var mapI = col + ((mapdata.info.height - row - 1) * mapdata.info.width);
        // determine the value
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
        var i = (col + (row * mapdata.info.width)) * 4;
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
function loadpos(self){
    self.$store.dispatch("Ros/getcurrentlocation",null, {root:true}).then(res=>{
        current_pose = res.data.currentlocation
        console.log(current_pose)
        setTimeout(loadpos,300,self)
    })
}

function clear(){
    context.moveTo(0,0)
    context.beginPath()
    context.rect(0,0,canvas.width,canvas.height);  
    context.fillStyle = "black"
    context.fill();
    context.closePath()
}
function showmap(){
    context.putImageData(imageData,0,0);
}

function translatepose(x,y){
    // the +10 is added becausse the map starts from -10m to 10m in x and y dimention
    var xp  = (x+10)/map.info.resolution
    var yp  = canvas.height - (y+10)/map.info.resolution
    console.log(yp)
    return {x:xp,y:yp}
}

function showpose(){
    if(current_pose){
        context.moveTo(0,0)
        var mapping = translatepose(current_pose.position.x,current_pose.position.y);
        context.beginPath();
        console.log(mapping)
        context.arc(mapping.x, mapping.y,6,0, Math.PI*2)    
        context.fillStyle = "blue"
        context.fill();
        context.closePath()
    }
}
function draw(){
    if (Object.keys(map).length != 0) {
        console.log('drawing')
        clear()
        showmap()
        showpose()
    }
    setTimeout(draw,300)

}

export default {
    data(){
        return {
            map: {}
        }
    }, 
    mounted(){
        var self = this;
        canvas = document.getElementById('map');
        context = canvas.getContext('2d');
        console.log(context)
        setTimeout(()=>{
            connect_to_ros().then(ros=>{

                var map_sub = new ROSLIB.Topic({
                    ros: ros,
                    name: '/map',
                    messageType: 'nav_msgs/OccupancyGrid',
                    compression : 'png'
                })
                map_sub.subscribe(function(data){
                    console.log('new map',data);
                    makemap(data);
                    map  = data;
                });

                self.$store.dispatch('Loading/clear', null,{root:true})
                loadpos(self);
                draw();
            })

        },1000)

    }
}
</script>

<style>

</style>