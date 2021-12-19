(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["confirm_position"],{"09ba":function(t,n,e){},"169a":function(t,n,e){"use strict";var o=e("5530"),i=e("2909"),a=e("ade3"),s=(e("a9e3"),e("498a"),e("caad"),e("2532"),e("7db0"),e("368e"),e("480e")),r=e("4ad4"),c=e("b848"),l=e("75eb"),u=e("e707"),d=e("e4d3"),h=e("21be"),m=e("f2e7"),f=e("a293"),v=e("58df"),p=e("d9bd"),g=e("80d2"),_=Object(v["a"])(r["a"],c["a"],l["a"],u["a"],d["a"],h["a"],m["a"]);n["a"]=_.extend({name:"v-dialog",directives:{ClickOutside:f["a"]},props:{dark:Boolean,disabled:Boolean,fullscreen:Boolean,light:Boolean,maxWidth:{type:[String,Number],default:"none"},noClickAnimation:Boolean,origin:{type:String,default:"center center"},persistent:Boolean,retainFocus:{type:Boolean,default:!0},scrollable:Boolean,transition:{type:[String,Boolean],default:"dialog-transition"},width:{type:[String,Number],default:"auto"}},data:function(){return{activatedBy:null,animate:!1,animateTimeout:-1,isActive:!!this.value,stackMinZIndex:200,previousActiveElement:null}},computed:{classes:function(){var t;return t={},Object(a["a"])(t,"v-dialog ".concat(this.contentClass).trim(),!0),Object(a["a"])(t,"v-dialog--active",this.isActive),Object(a["a"])(t,"v-dialog--persistent",this.persistent),Object(a["a"])(t,"v-dialog--fullscreen",this.fullscreen),Object(a["a"])(t,"v-dialog--scrollable",this.scrollable),Object(a["a"])(t,"v-dialog--animated",this.animate),t},contentClasses:function(){return{"v-dialog__content":!0,"v-dialog__content--active":this.isActive}},hasActivator:function(){return Boolean(!!this.$slots.activator||!!this.$scopedSlots.activator)}},watch:{isActive:function(t){var n;t?(this.show(),this.hideScroll()):(this.removeOverlay(),this.unbind(),null==(n=this.previousActiveElement)||n.focus())},fullscreen:function(t){this.isActive&&(t?(this.hideScroll(),this.removeOverlay(!1)):(this.showScroll(),this.genOverlay()))}},created:function(){this.$attrs.hasOwnProperty("full-width")&&Object(p["e"])("full-width",this)},beforeMount:function(){var t=this;this.$nextTick((function(){t.isBooted=t.isActive,t.isActive&&t.show()}))},beforeDestroy:function(){"undefined"!==typeof window&&this.unbind()},methods:{animateClick:function(){var t=this;this.animate=!1,this.$nextTick((function(){t.animate=!0,window.clearTimeout(t.animateTimeout),t.animateTimeout=window.setTimeout((function(){return t.animate=!1}),150)}))},closeConditional:function(t){var n=t.target;return!(this._isDestroyed||!this.isActive||this.$refs.content.contains(n)||this.overlay&&n&&!this.overlay.$el.contains(n))&&this.activeZIndex>=this.getMaxZIndex()},hideScroll:function(){this.fullscreen?document.documentElement.classList.add("overflow-y-hidden"):u["a"].options.methods.hideScroll.call(this)},show:function(){var t=this;!this.fullscreen&&!this.hideOverlay&&this.genOverlay(),this.$nextTick((function(){t.$nextTick((function(){t.previousActiveElement=document.activeElement,t.$refs.content.focus(),t.bind()}))}))},bind:function(){window.addEventListener("focusin",this.onFocusin)},unbind:function(){window.removeEventListener("focusin",this.onFocusin)},onClickOutside:function(t){this.$emit("click:outside",t),this.persistent?this.noClickAnimation||this.animateClick():this.isActive=!1},onKeydown:function(t){if(t.keyCode===g["y"].esc&&!this.getOpenDependents().length)if(this.persistent)this.noClickAnimation||this.animateClick();else{this.isActive=!1;var n=this.getActivator();this.$nextTick((function(){return n&&n.focus()}))}this.$emit("keydown",t)},onFocusin:function(t){if(t&&this.retainFocus){var n=t.target;if(n&&![document,this.$refs.content].includes(n)&&!this.$refs.content.contains(n)&&this.activeZIndex>=this.getMaxZIndex()&&!this.getOpenDependentElements().some((function(t){return t.contains(n)}))){var e=this.$refs.content.querySelectorAll('button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'),o=Object(i["a"])(e).find((function(t){return!t.hasAttribute("disabled")}));o&&o.focus()}}},genContent:function(){var t=this;return this.showLazyContent((function(){return[t.$createElement(s["a"],{props:{root:!0,light:t.light,dark:t.dark}},[t.$createElement("div",{class:t.contentClasses,attrs:Object(o["a"])({role:"document",tabindex:t.isActive?0:void 0},t.getScopeIdAttrs()),on:{keydown:t.onKeydown},style:{zIndex:t.activeZIndex},ref:"content"},[t.genTransition()])])]}))},genTransition:function(){var t=this.genInnerContent();return this.transition?this.$createElement("transition",{props:{name:this.transition,origin:this.origin,appear:!0}},[t]):t},genInnerContent:function(){var t={class:this.classes,ref:"dialog",directives:[{name:"click-outside",value:{handler:this.onClickOutside,closeConditional:this.closeConditional,include:this.getOpenDependentElements}},{name:"show",value:this.isActive}],style:{transformOrigin:this.origin}};return this.fullscreen||(t.style=Object(o["a"])(Object(o["a"])({},t.style),{},{maxWidth:"none"===this.maxWidth?void 0:Object(g["g"])(this.maxWidth),width:"auto"===this.width?void 0:Object(g["g"])(this.width)})),this.$createElement("div",t,this.getContentSlot())}},render:function(t){return t("div",{staticClass:"v-dialog__container",class:{"v-dialog__container--attached":""===this.attach||!0===this.attach||"attach"===this.attach},attrs:{role:"dialog"}},[this.genActivator(),this.genContent()])}})},"368e":function(t,n,e){},b8fd:function(t,n,e){"use strict";e.r(n);var o,i,a,s,r,c,l,u,d,h=function(){var t=this,n=t.$createElement,e=t._self._c||n;return e("v-container",{staticClass:"pa-0 ma-0",attrs:{fluid:"",id:"root","fill-height":""}},[e("canvas",{staticClass:"pa-0 ma-0",attrs:{"fill-height":"",id:"map"}}),e("canvas",{directives:[{name:"show",rawName:"v-show",value:!1,expression:"false"}],attrs:{id:"temp"}}),e("v-card",{staticClass:" px-2",staticStyle:{"background-color":"rgba(20,20,30,1)",width:"150px",right:"10px",bottom:"27%",position:"absolute"},attrs:{flat:"",rounded:"xl",dark:""}},[e("v-card-text",[e("v-row",{staticClass:"pa-2"},[e("v-btn",{attrs:{color:"purple accent-4",fab:"",small:"",icon:""},on:{mousedown:function(n){t.continue_zoomin=!0,t.zoomin(n)},mouseup:function(n){t.continue_zoomin=!1}}},[e("v-icon",[t._v(" mdi-plus ")])],1),e("v-spacer"),e("v-btn",{attrs:{color:"purple accent-4",fab:"",small:"",icon:""},on:{mousedown:function(n){t.continue_zoomout=!0,t.zoomout(n)},mouseup:function(n){t.continue_zoomout=!1}}},[e("v-icon",[t._v(" mdi-minus ")])],1)],1),e("v-row",{staticClass:"pa-2"},[e("v-spacer"),e("v-btn",{attrs:{color:"purple accent-4",fab:"",small:"",icon:""},on:{mousedown:function(n){t.continue_movement_up=!0,t.up(n)},mouseup:function(n){t.continue_movement_up=!1}}},[e("v-icon",[t._v(" mdi-chevron-up ")])],1),e("v-spacer")],1),e("v-row",{staticClass:"pa-2"},[e("v-btn",{attrs:{color:"purple accent-4",fab:"",small:"",icon:""},on:{mousedown:function(n){t.continue_movement_left=!0,t.left(n)},mouseup:function(n){t.continue_movement_left=!1}}},[e("v-icon",[t._v(" mdi-chevron-left ")])],1),e("v-spacer"),e("v-btn",{attrs:{color:"purple accent-4",fab:"",small:"",icon:""},on:{mousedown:function(n){t.continue_movement_right=!0,t.right(n)},mouseup:function(n){t.continue_movement_right=!1}}},[e("v-icon",[t._v(" mdi-chevron-right ")])],1)],1),e("v-row",{staticClass:"pa-2"},[e("v-spacer"),e("v-btn",{attrs:{color:"purple accent-4",fab:"",small:"",icon:""},on:{mousedown:function(n){t.continue_movement_down=!0,t.down(n)},mouseup:function(n){t.continue_movement_down=!1}}},[e("v-icon",[t._v(" mdi-chevron-down ")])],1),e("v-spacer")],1)],1)],1),e("v-card",{staticClass:"floating px-2",staticStyle:{"background-color":"rgba(20,20,30,1)"},attrs:{flat:"",rounded:"xl",dark:""}},[e("v-divider"),e("v-card-title",{attrs:{dark:t.isDark}},[t._v(" Confirm Position ")]),e("v-card-text",{attrs:{dark:!0}},[t._v(" Is the robot placed properly? ")]),e("v-card-actions",[e("v-dialog",{attrs:{dark:t.isDark,width:"500"},scopedSlots:t._u([{key:"activator",fn:function(n){var o=n.on,i=n.attrs;return[e("v-btn",t._g(t._b({attrs:{color:"purple white--text",dark:t.isDark,text:"",loading:t.continue_loading,disabled:t.continue_loading}},"v-btn",i,!1),o),[t._v(" Cancel ")])]}}]),model:{value:t.cancel_dialog,callback:function(n){t.cancel_dialog=n},expression:"cancel_dialog"}},[e("v-card",{staticClass:"pa-4"},[e("v-card-title",{},[t._v(" Cancel Salmming ")]),e("v-card-text",[t._v(" If you cancel the slamming procedure all the work has been done will be ignored. "),e("br"),t._v(" Cancel? ")]),e("v-divider"),e("v-card-actions",[e("v-btn",{attrs:{color:"purple",text:""},on:{click:function(n){t.cancel(),t.cancel_dialog=!1}}},[t._v(" Yes ")]),e("v-spacer"),e("v-btn",{attrs:{color:"purple",text:""},on:{click:function(n){t.cancel_dialog=!1}}},[t._v(" No ")])],1)],1)],1),e("v-spacer"),e("v-btn",{attrs:{color:"purple",text:"",loading:t.continue_loading,disabled:t.continue_loading||!t.update_flag},on:{click:function(n){return t.update_position()}}},[t._v(" Update Position ")]),e("v-spacer"),e("v-btn",{attrs:{color:"purple",text:"",loading:t.continue_loading,disabled:t.continue_loading},on:{click:function(n){return t.confirm()}}},[t._v(" Confirm ")])],1)],1)],1)},m=[],f=e("1da1"),v=(e("96cf"),e("d3b7"),e("cb29"),e("99af"),e("47e3")),p=e("e86b"),g=e.n(p),_=e("6176"),b=e.n(_),w=1,y=0,x=0;function k(t){return new Promise((function(n){return setTimeout(n,t)}))}function C(){return I.apply(this,arguments)}function I(){return I=Object(f["a"])(regeneratorRuntime.mark((function t(){var n,e;return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:n=!0;case 1:if(!n){t.next=6;break}return t.next=4,k(1500).then((function(){e=new g.a.Ros({url:"ws://".concat(v["a"].bridge_address,":9090")}),e.on("connection",(function(){n=!1})),e.on("error",(function(){console.error("error connecting to rosbridge")}))}));case 4:t.next=1;break;case 6:return t.abrupt("return",new Promise((function(t){return t(e)})));case 7:case"end":return t.stop()}}),t)}))),I.apply(this,arguments)}function T(t){var n={};Object.assign(n,t),s.width=n.info.width,s.height=n.info.height,u=a.createImageData(n.info.width,n.info.height);for(var e=n.info.height-1;e>-1;e--)for(var o=n.info.width-1;o>-1;o--){var i,r=o+e*n.info.width,c=n.data[r];i=100===c?0:0===c?255:127;var l=4*(n.info.width-o+e*n.info.width);u.data[l]=i,u.data[++l]=i,u.data[++l]=i,u.data[++l]=255}}function O(){a.moveTo(0,0),a.beginPath(),a.rect(0,0,i.width,i.height),a.fillStyle="rgb(127,127,127)",a.fill(),a.closePath()}function P(t){var n=t.w,e=t.x,o=t.y,i=t.z;return-Math.atan2(2*(n*i+e*o),1-2*(o*o+i*i))}function $(t,n,e){var o=l.info.width-(t-l.info.origin.position.x)/l.info.resolution,i=(n-l.info.origin.position.y)/l.info.resolution,a=null;return e&&(a=P(e),a<0&&(a=2*Math.PI+a)),{x:o,y:i,theta:a}}function A(){if(d){var t=7,n=$(d.position.x,d.position.y,d.orientation),e=n.x,o=n.y,i=n.theta+Math.PI,a=i+Math.PI/6,s=i-Math.PI/6;a=a>2*Math.PI?a-2*Math.PI:a<0?a+2*Math.PI:a,s=s>2*Math.PI?s-2*Math.PI:s<0?s+2*Math.PI:s,r.beginPath(),r.moveTo(e,o),r.arc(e,o,t,a,s),r.fillStyle="purple",r.fill(),r.closePath()}}var z={};function M(t,n,e,o){var i=$(t,n),a=20*Math.cos(e)+i.x,s=-20*Math.sin(e)+i.y;r.beginPath(),r.moveTo(i.x,i.y),r.lineTo(a,s),r.strokeStyle=o,r.lineWidth=2,r.stroke(),r.closePath()}function E(){z.draw&&M(z.robot_x,z.robot_y,z.angle,"green")}function S(){u&&(r.beginPath(),r.moveTo(0,0),r.putImageData(u,0,0),r.closePath(),A(),E(),a.drawImage(s,y,x,i.width/w>>0,i.height/w>>0,0,0,i.width,i.height),a.closePath())}function j(){return B.apply(this,arguments)}function B(){return B=Object(f["a"])(regeneratorRuntime.mark((function t(){return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return O(),S(),t.next=4,k(100);case 4:requestAnimationFrame(j);case 5:case"end":return t.stop()}}),t)}))),B.apply(this,arguments)}var D={data:function(){return{cmd_vel:!1,cmd_vel_pub:null,continue_movement_left:!1,continue_movement_up:!1,continue_movement_right:!1,continue_movement_down:!1,continue_zoomout:!1,continue_zoomin:!1,canvas:null,temp_canvas:null,c:null,temp_c:null,cancel_dialog:!1,continue_loading:!1,update_flag:!1}},methods:{down:function(){this.continue_movement_down&&(this.movedown(),setTimeout(this.down,60))},up:function(){this.continue_movement_up&&(this.moveup(),setTimeout(this.up,60))},right:function(){this.continue_movement_right&&(this.moveright(),setTimeout(this.right,60))},left:function(){this.continue_movement_left&&(this.moveleft(),setTimeout(this.left,60))},zoomin:function(){this.continue_zoomin&&(w<2.5?w+=.1:this.continue_zoomin=!1,setTimeout(this.zoomin,60))},zoomout:function(){this.continue_zoomout&&(w>.5?w-=.1:this.continue_zoomout=!1,setTimeout(this.zoomout,60))},moveup:function(){x>-.1*i.height?x-=10:this.continue_movement_up=!1},movedown:function(){x+i.height/w<1.1*i.height?x+=10:this.continue_movement_down=!1},moveright:function(){y+i.width/w<1.1*i.width?y+=10:this.continue_movement_right=!1},moveleft:function(){y>-.1*i.width?y-=10:this.continue_movement_left=!1},angled_goal_mousedown_handler:function(t){var n=a.getImageData(t.layerX,t.layerY,1,1).data;n[0],n[1],255==n[2]&&(this.update_flag=!1,z={},z.x=t.layerX/w+y,z.layerX=t.layerX,z.y=t.layerY/w+x,z.layerY=t.layerY,z.drop=!0,z.draw=!1)},angled_goal_mouseup_handler:function(t){if(z.drop&&l.info){z.drop=!1,z.abs_angle=Math.atan(Math.abs((t.layerY-z.layerY)/(t.layerX-z.layerX))),z.end_layerX=t.layerX,z.end_layerY=t.layerY,z.end_layerX-z.layerX>0?z.end_layerY-z.layerY>0?z.angle=2*Math.PI-z.abs_angle:z.angle=z.abs_angle:z.end_layerY-z.layerY>0?z.angle=Math.PI+z.abs_angle:z.angle=Math.PI-z.abs_angle,z.robot_angle=Math.PI+z.angle,z.robot_angle>2*Math.PI&&(z.robot_angle=-2*Math.PI+z.robot_angle),z.robot_x=(l.info.width-z.x)*l.info.resolution+l.info.origin.position.x,z.robot_y=z.y*l.info.resolution+l.info.origin.position.y;var n=b.a.fromEuler(0,0,z.robot_angle,"XYZ");z.pose={},z.pose.position={},z.pose.position.x=z.robot_x,z.pose.position.y=z.robot_y,z.pose.position.z=0,z.pose.orientation={},z.pose.orientation.x=n.x,z.pose.orientation.y=n.y,z.pose.orientation.z=n.z,z.pose.orientation.w=n.w,z.angle&&(z.draw=!0,z.draw&&(this.update_flag=!0)),console.log(z)}},cancel:function(){var t=this;this.continue_loading=!0,console.log("Where There is Will there is Way"),this.$store.dispatch("Ros/take_action","startup/remote_interface",{root:!0}).then((function(n){"confirm_position"==n?(console.log(n),t.$store.dispatch("Ros/take_action","startup/perform/slam/confirm/end",{root:!0}).then((function(n){console.log(n),t.$router.push({name:"startup_loading"})}))):t.continue_loading=!1}))},update_position:function(){var t=this;this.continue_loading=!0,z.draw?this.$store.dispatch("Ros/take_action","startup/remote_interface",{root:!0}).then((function(n){"confirm_position"==n?(console.log(n),t.$store.dispatch("Ros/take_action","navigation/update_pose/".concat(z.pose.position.x,"&").concat(z.pose.position.y,"&").concat(z.pose.position.z,"&").concat(z.pose.orientation.x,"&").concat(z.pose.orientation.y,"&").concat(z.pose.orientation.z,"&").concat(z.pose.orientation.w),{root:!0}).then((function(n){console.log(n),t.continue_loading=!1}))):t.continue_loading=!1})):console.log("error man")},confirm:function(){var t=this;this.continue_loading=!0,this.$store.dispatch("Ros/take_action","startup/remote_interface",{root:!0}).then((function(n){"confirm_position"==n?(console.log(n),t.$store.dispatch("Ros/take_action","startup/perform/chose_existing_map/confirm/yes",{root:!0}).then((function(t){console.log(t)}))):t.continue_loading=!1}))}},mounted:function(){this.canvas=i=document.getElementById("map"),this.temp_canvas=s=document.getElementById("temp"),o=document.getElementById("root"),c=document.getElementById("mainbar"),i.width=o.offsetWidth,i.height=window.innerHeight-c.offsetHeight,this.c=a=i.getContext("2d"),this.temp_c=r=s.getContext("2d"),setTimeout((function(){C().then((function(t){var n=new g.a.Topic({ros:t,name:"/current_pose",messageType:"geometry_msgs/Pose"});n.subscribe((function(t){d=t}));var e=new g.a.Topic({ros:t,name:"/slamware_ros_sdk_server_node/map",messageType:"nav_msgs/OccupancyGrid",compression:"png"});e.subscribe((function(t){l=t,T(t)}))}))}),10),window.onresize=function(){setTimeout((function(){i.width=o.offsetWidth,i.height=window.innerHeight-c.offsetHeight}),10)},j(),i.addEventListener("mousedown",this.angled_goal_mousedown_handler),i.addEventListener("mouseup",this.angled_goal_mouseup_handler)},destroyed:function(){i.removeEventListener("mousedown",this.angled_goal_mousedown_handler),i.removeEventListener("mouseup",this.angled_goal_mouseup_handler)},computed:{nopoint:function(){return!z.draw},isDark:function(){return this.$store.getters["Theme/isDark"]}}},Y=D,R=(e("bd7d"),e("2877")),V=e("6544"),X=e.n(V),W=e("8336"),L=e("b0af"),Z=e("99d9"),F=e("a523"),H=e("169a"),N=e("ce7e"),q=e("132d"),J=e("0fd9"),K=e("2fa4"),G=Object(R["a"])(Y,h,m,!1,null,"5804fcda",null);n["default"]=G.exports;X()(G,{VBtn:W["a"],VCard:L["a"],VCardActions:Z["a"],VCardText:Z["b"],VCardTitle:Z["c"],VContainer:F["a"],VDialog:H["a"],VDivider:N["a"],VIcon:q["a"],VRow:J["a"],VSpacer:K["a"]})},bd7d:function(t,n,e){"use strict";e("09ba")}}]);
//# sourceMappingURL=confirm_position.5094ec4f.js.map