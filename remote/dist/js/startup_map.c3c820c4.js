(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["startup_map"],{aa6b:function(e,n,o){"use strict";o.r(n);var t,a,i,l,r,s,c,u,_,m,d=function(){var e=this,n=e.$createElement,o=e._self._c||n;return o("v-container",{staticClass:"pa-0 ma-0",attrs:{fluid:"",id:"root","fill-height":""}},[o("canvas",{staticClass:"pa-0 ma-0",attrs:{"fill-height":"",id:"map"}}),o("canvas",{directives:[{name:"show",rawName:"v-show",value:!1,expression:"false"}],attrs:{id:"temp"}}),e.controllers?o("v-card",{staticClass:"floating px-2",staticStyle:{"background-color":"rgba(20,20,30,1)"},attrs:{width:"170px",flat:"",rounded:"xl"}},[o("v-card-text",[e.arrow_goal_flag||e.point_goal_flag?o("v-row",{staticClass:"pa-2"},[e.arrow_goal_flag?o("v-btn",{attrs:{text:"",color:"purple accent-4",disabled:e.goal_flag},on:{click:e.wait_for_angled_goal}},[e._v("Arrow Goal")]):e._e(),e.point_goal_flag?o("v-btn",{attrs:{text:"",color:"purple accent-4",disabled:e.goal_flag},on:{click:e.wait_for_unangled_goal}},[e._v("Point Goal")]):e._e(),o("v-btn",{attrs:{text:"",color:"purple accent-4",disabled:!e.goal_flag},on:{click:e.cancel_goal}},[e._v("Cancel")]),o("v-btn",{attrs:{text:"",color:"purple accent-4",disabled:e.goal_flag},on:{click:e.clear_goal}},[e._v("clear")])],1):e._e(),o("v-row",{staticClass:"pa-2"},[o("v-spacer"),e.cmd_vel_flag?o("v-switch",{attrs:{label:"arrow control",color:"purple accent-4",dark:""},model:{value:e.cmd_vel,callback:function(n){e.cmd_vel=n},expression:"cmd_vel"}}):e._e(),o("v-spacer")],1),o("v-row",{staticClass:"pa-2"},[o("v-btn",{attrs:{color:"purple accent-4",fab:"",small:"",icon:""},on:{mousedown:function(n){e.continue_zoomin=!0,e.zoomin(n)},mouseup:function(n){e.continue_zoomin=!1}}},[o("v-icon",[e._v(" mdi-plus ")])],1),o("v-spacer"),o("v-btn",{attrs:{color:"purple accent-4",fab:"",small:"",icon:""},on:{mousedown:function(n){e.continue_zoomout=!0,e.zoomout(n)},mouseup:function(n){e.continue_zoomout=!1}}},[o("v-icon",[e._v(" mdi-minus ")])],1)],1),o("v-row",{staticClass:"pa-2"},[o("v-spacer"),o("v-btn",{attrs:{color:"purple accent-4",fab:"",small:"",icon:""},on:{mousedown:function(n){e.continue_movement_up=!0,e.up(n)},mouseup:function(n){e.continue_movement_up=!1,e.cmd_vel&&e.stop()}}},[o("v-icon",[e._v(" mdi-chevron-up ")])],1),o("v-spacer")],1),o("v-row",{staticClass:"pa-2"},[o("v-btn",{attrs:{color:"purple accent-4",fab:"",small:"",icon:""},on:{mousedown:function(n){e.continue_movement_left=!0,e.left(n)},mouseup:function(n){e.continue_movement_left=!1,e.cmd_vel&&e.stop()}}},[o("v-icon",[e._v(" mdi-chevron-left ")])],1),o("v-spacer"),o("v-btn",{attrs:{color:"purple accent-4",fab:"",small:"",icon:""},on:{click:function(n){return e.stop()}}},[o("v-icon",[e._v(" mdi-close-circle-outline ")])],1),o("v-spacer"),o("v-btn",{attrs:{color:"purple accent-4",fab:"",small:"",icon:""},on:{mousedown:function(n){e.continue_movement_right=!0,e.right(n)},mouseup:function(n){e.continue_movement_right=!1,e.cmd_vel&&e.stop()}}},[o("v-icon",[e._v(" mdi-chevron-right ")])],1)],1),o("v-row",{staticClass:"pa-2"},[o("v-spacer"),o("v-btn",{attrs:{color:"purple accent-4",fab:"",small:"",icon:""},on:{mousedown:function(n){e.continue_movement_down=!0,e.down(n)},mouseup:function(n){e.continue_movement_down=!1,e.cmd_vel&&e.stop()}}},[o("v-icon",[e._v(" mdi-chevron-down ")])],1),o("v-spacer")],1)],1)],1):e._e()],1)},g=[],h=o("1da1"),f=(o("96cf"),o("d3b7"),o("cb29"),o("159b"),o("ac1f"),o("1276"),o("caad"),o("2532"),o("47e3")),p=o("e86b"),v=o.n(p),w=o("6176"),b=o.n(w),y={},x=2,P=0,z=0;function T(e){return new Promise((function(n){return setTimeout(n,e)}))}function M(){return I.apply(this,arguments)}function I(){return I=Object(h["a"])(regeneratorRuntime.mark((function e(){var n,o;return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:n=!0;case 1:if(!n){e.next=6;break}return e.next=4,T(1500).then((function(){o=new v.a.Ros({url:"ws://".concat(f["a"].bridge_address,":9090")}),o.on("connection",(function(){n=!1})),o.on("error",(function(){console.error("error connecting to rosbridge")}))}));case 4:e.next=1;break;case 6:return e.abrupt("return",new Promise((function(e){return e(o)})));case 7:case"end":return e.stop()}}),e)}))),I.apply(this,arguments)}function k(e){var n={};Object.assign(n,e),l.width=n.info.width,l.height=n.info.height,_=i.createImageData(n.info.width,n.info.height);for(var o=n.info.height-1;o>-1;o--)for(var t=n.info.width-1;t>-1;t--){var a,r=t+o*n.info.width,s=n.data[r];a=100===s?0:0===s?255:127;var c=4*(n.info.width-t+o*n.info.width);_.data[c]=a,_.data[++c]=a,_.data[++c]=a,_.data[++c]=255}}function Y(){i.moveTo(0,0),i.beginPath(),i.rect(0,0,a.width,a.height),i.fillStyle="rgb(127,127,127)",i.fill(),i.closePath()}function C(e){var n=e.w,o=e.x,t=e.y,a=e.z;return-Math.atan2(2*(n*a+o*t),1-2*(t*t+a*a))}function E(e,n,o){var t=u.info.width-(e-u.info.origin.position.x)/u.info.resolution,a=(n-u.info.origin.position.y)/u.info.resolution,i=null;return o&&(i=C(o),i<0&&(i=2*Math.PI+i)),{x:t,y:a,theta:i}}function X(){if(m){var e=7,n=E(m.position.x,m.position.y,m.orientation),o=n.x,t=n.y,a=n.theta+Math.PI,i=a+Math.PI/6,l=a-Math.PI/6;i=i>2*Math.PI?i-2*Math.PI:i<0?i+2*Math.PI:i,l=l>2*Math.PI?l-2*Math.PI:l<0?l+2*Math.PI:l,r.beginPath(),r.moveTo(o,t),r.arc(o,t,e,i,l),r.fillStyle="purple",r.fill(),r.closePath()}}var L={};function R(e,n,o,t){var a=E(e,n);r.beginPath(),r.moveTo(a.x,a.y),r.arc(a.x,a.y,t,0,2*Math.PI),r.fillStyle=o,r.fill(),r.closePath()}function S(e,n,o,t){var a=E(e,n),i=20*Math.cos(o)+a.x,l=-20*Math.sin(o)+a.y;r.beginPath(),r.moveTo(a.x,a.y),r.lineTo(i,l),r.strokeStyle=t,r.lineWidth=2,r.stroke(),r.closePath()}function V(){y.poses&&y.poses.length>0&&y.poses.forEach((function(e){R(e.pose.position.x,e.pose.position.y,"blue",1)}))}function q(){if(L.draw&&c){var e="blue";if(!(L.robot_x-c["pose"]["x"]<.15&&L.robot_y-c["pose"]["y"]<.15))return void console.log("returning");"succeed"==c.state?e="green":"running"==c.state?(V(),e="orange"):"false"==c.state&&(e="red"),c.is_angled?S(L.robot_x,L.robot_y,L.angle,e):R(L.robot_x,L.robot_y,e,2)}}function B(){_&&(r.beginPath(),r.moveTo(0,0),r.putImageData(_,0,0),r.closePath(),X(),q(),i.drawImage(l,P,z,a.width/x>>0,a.height/x>>0,0,0,a.width,a.height),i.closePath())}function D(){return O.apply(this,arguments)}function O(){return O=Object(h["a"])(regeneratorRuntime.mark((function e(){return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return Y(),B(),e.next=4,T(100);case 4:requestAnimationFrame(D);case 5:case"end":return e.stop()}}),e)}))),O.apply(this,arguments)}var j={data:function(){return{cmd_vel:!1,cmd_vel_pub:null,goal_pub:null,unangled_goal_pub:null,continue_movement_left:!1,continue_movement_up:!1,continue_movement_right:!1,continue_movement_down:!1,continue_zoomout:!1,continue_zoomin:!1,goal_flag:!1,canvas:null,temp_canvas:null,c:null,temp_c:null,controllers:!0,manual_control_flags:[],cmd_vel_flag:null,point_goal_flag:null,arrow_goal_flag:null,navigation_mode_interval_holder:null}},methods:{down:function(){this.continue_movement_down&&(this.cmd_vel?this.cmd_vel_down():this.movedown(),setTimeout(this.down,60))},up:function(){this.continue_movement_up&&(this.cmd_vel?this.cmd_vel_up():this.moveup(),setTimeout(this.up,60))},right:function(){this.continue_movement_right&&(this.cmd_vel?this.cmd_vel_right():this.moveright(),setTimeout(this.right,60))},left:function(){this.continue_movement_left&&(this.cmd_vel?this.cmd_vel_left():this.moveleft(),setTimeout(this.left,60))},cmd_vel_right:function(){var e=new v.a.Message({linear:{x:0,y:0,z:0},angular:{x:0,y:0,z:-1}});this.cmd_vel_pub.publish(e)},cmd_vel_left:function(){var e=new v.a.Message({linear:{x:0,y:0,z:0},angular:{x:0,y:0,z:1}});this.cmd_vel_pub.publish(e)},cmd_vel_up:function(){var e=new v.a.Message({linear:{x:.24,y:0,z:0},angular:{x:0,y:0,z:0}});this.cmd_vel_pub.publish(e)},cmd_vel_down:function(){var e=new v.a.Message({linear:{x:-.24,y:0,z:0},angular:{x:0,y:0,z:0}});this.cmd_vel_pub.publish(e)},stop:function(){var e=new v.a.Message({linear:{x:0,y:0,z:0},angular:{x:0,y:0,z:0}});this.cmd_vel_pub.publish(e)},zoomin:function(){this.continue_zoomin&&(x<2.5?x+=.1:this.continue_zoomin=!1,setTimeout(this.zoomin,60))},zoomout:function(){this.continue_zoomout&&(x>.5?x-=.1:this.continue_zoomout=!1,setTimeout(this.zoomout,60))},moveup:function(){z>-.1*a.height?z-=10:this.continue_movement_up=!1},movedown:function(){z+a.height/x<1.1*a.height?z+=10:this.continue_movement_down=!1},moveright:function(){P+a.width/x<1.1*a.width?P+=10:this.continue_movement_right=!1},moveleft:function(){P>-.1*a.width?P-=10:this.continue_movement_left=!1},wait_for_angled_goal:function(){this.goal_flag=!0,a.addEventListener("mousedown",this.angled_goal_mousedown_handler),a.addEventListener("mouseup",this.angled_goal_mouseup_handler)},wait_for_unangled_goal:function(){this.goal_flag=!0,a.addEventListener("mousedown",this.unangled_goal_mousedown_handler),a.addEventListener("mouseup",this.unangled_goal_mouseup_handler)},angled_goal_mousedown_handler:function(e){var n=i.getImageData(e.layerX,e.layerY,1,1).data;n[0],n[1],255==n[2]&&(L={},L.x=e.layerX/x+P,L.layerX=e.layerX,L.y=e.layerY/x+z,L.layerY=e.layerY,L.drop=!0,L.draw=!1)},angled_goal_mouseup_handler:function(e){if(L.drop&&u.info){L.drop=!1,L.abs_angle=Math.atan(Math.abs((e.layerY-L.layerY)/(e.layerX-L.layerX))),L.end_layerX=e.layerX,L.end_layerY=e.layerY,L.end_layerX-L.layerX>0?L.end_layerY-L.layerY>0?L.angle=2*Math.PI-L.abs_angle:L.angle=L.abs_angle:L.end_layerY-L.layerY>0?L.angle=Math.PI+L.abs_angle:L.angle=Math.PI-L.abs_angle,L.robot_angle=Math.PI+L.angle,L.robot_angle>2*Math.PI&&(L.robot_angle=-2*Math.PI+L.robot_angle),L.robot_x=(u.info.width-L.x)*u.info.resolution+u.info.origin.position.x,L.robot_y=L.y*u.info.resolution+u.info.origin.position.y;var n=b.a.fromEuler(0,0,L.robot_angle,"XYZ");L.draw=!0;var o=new v.a.Message({header:{seq:0,stamp:0,frame_id:"slamware_map"},pose:{position:{x:L.robot_x,y:L.robot_y,z:L.robot_z},orientation:{x:n.x,y:n.y,z:n.z,w:n.w}}});this.goal_pub.publish(o)}this.cancel_goal()},unangled_goal_mousedown_handler:function(e){var n=i.getImageData(e.layerX,e.layerY,1,1).data;n[0],n[1],255==n[2]&&(L={},L.x=e.layerX/x+P,L.layerX=e.layerX,L.y=e.layerY/x+z,L.layerY=e.layerY,L.drop=!0,L.draw=!1)},unangled_goal_mouseup_handler:function(){if(L.drop&&u.info){L.drop=!1,L.robot_x=(u.info.width-L.x)*u.info.resolution+u.info.origin.position.x,L.robot_y=L.y*u.info.resolution+u.info.origin.position.y,L.draw=!0;var e=new v.a.Message({location:{x:L.robot_x,y:L.robot_y,z:0}});this.unangled_goal_pub.publish(e)}this.cancel_goal()},clear_goal:function(){L={}},cancel_goal:function(){this.goal_flag=!1,a.removeEventListener("mousedown",this.angled_goal_mousedown_handler),a.removeEventListener("mouseup",this.angled_goal_mouseup_handler),a.removeEventListener("mousedown",this.unangled_goal_mousedown_handler),a.removeEventListener("mouseup",this.unangled_goal_mouseup_handler)}},watch:{},mounted:function(){var e=this,n=this;this.canvas=a=document.getElementById("map"),this.temp_canvas=l=document.getElementById("temp"),this.$store.dispatch("Loading/clear"),t=document.getElementById("root"),s=document.getElementById("mainbar"),a.width=t.offsetWidth,a.height=window.innerHeight-s.offsetHeight,this.c=i=a.getContext("2d"),this.temp_c=r=l.getContext("2d"),setTimeout((function(){M().then((function(e){var o=new v.a.Topic({ros:e,name:"/current_pose",messageType:"geometry_msgs/Pose"});o.subscribe((function(e){m=e}));var t=new v.a.Topic({ros:e,name:"/slamware_ros_sdk_server_node/global_plan_path",messageType:"nav_msgs/Path"});t.subscribe((function(e){y=e}));var a=new v.a.Topic({ros:e,name:"/slamware_ros_sdk_server_node/map",messageType:"nav_msgs/OccupancyGrid",compression:"png"});a.subscribe((function(e){u=e,k(e)}));var i=new v.a.Topic({ros:e,name:"/navigation/goal_monitor",messageType:"status_msgs/goal_monitor_msg"});i.subscribe((function(e){c=e})),n.cmd_vel_pub=new v.a.Topic({ros:e,name:"/navigation/cmd_vel_req",messageType:"geometry_msgs/Twist"}),n.goal_pub=new v.a.Topic({ros:e,name:"/navigation/goal_req",messageType:"geometry_msgs/PoseStamped"}),n.unangled_goal_pub=new v.a.Topic({ros:e,name:"/navigation/unangled_goal_req",messageType:"slamware_ros_sdk/MoveToRequest"})}))}),10),window.onresize=function(){setTimeout((function(){a.width=t.offsetWidth,a.height=window.innerHeight-s.offsetHeight}),10)},D(),this.navigation_mode_interval_holder=setInterval((function(){e.$store.dispatch("Ros/take_action","navigation/get_mode",{root:!0}).then((function(n){"manual"==n?e.$store.dispatch("Ros/take_action","startup/get_manual_controls",{root:!0}).then((function(n){e.controllers=!0,console.log(n.split("|")),e.manual_control_flags=n.split("|"),e.manual_control_flags.includes("cmd_vel")||(e.cmd_vel=!1),e.arrow_goal_flag=!!e.manual_control_flags.includes("arrow_goal"),e.cmd_vel_flag=!!e.manual_control_flags.includes("cmd_vel"),e.point_goal_flag=!!e.manual_control_flags.includes("point_goal")})):(e.controllers=!1,e.manual_control_flags=[])}))}),400)},beforeDestroy:function(){clearInterval(this.navigation_mode_interval_holder)},computed:{}},H=j,$=(o("d7f5"),o("2877")),G=o("6544"),W=o.n(G),A=o("8336"),J=o("b0af"),F=o("99d9"),N=o("a523"),Z=o("132d"),K=o("0fd9"),Q=o("2fa4"),U=o("b73d"),ee=Object($["a"])(H,d,g,!1,null,"59432912",null);n["default"]=ee.exports;W()(ee,{VBtn:A["a"],VCard:J["a"],VCardText:F["b"],VContainer:N["a"],VIcon:Z["a"],VRow:K["a"],VSpacer:Q["a"],VSwitch:U["a"]})},d7f5:function(e,n,o){"use strict";o("f459")},f459:function(e,n,o){}}]);
//# sourceMappingURL=startup_map.c3c820c4.js.map