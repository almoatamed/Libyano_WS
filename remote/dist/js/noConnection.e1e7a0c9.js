(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["noConnection"],{"0058":function(t,e,n){"use strict";n.r(e);var a=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{attrs:{id:"root"}},[n("v-container",[n("div",{staticClass:"text-h4"},[t._v("Voice Manager")]),n("v-divider",{staticClass:"py-2"}),n("v-card",{attrs:{elevation:"6",dark:t.isDark}},[n("v-form",{ref:"SoundForm",model:{value:t.valid,callback:function(e){t.valid=e},expression:"valid"}},[n("v-container",{attrs:{fluid:""}},[n("v-row",[n("v-col",{attrs:{cols:"12"}},[n("v-text-field",{attrs:{disabled:t.disabled,loading:t.loading,rules:t.name_rules,color:"purple darken-2",label:"File name",required:""},model:{value:t.form.name,callback:function(e){t.$set(t.form,"name",e)},expression:"form.name"}})],1),n("v-col",{attrs:{cols:"12"}},[n("v-select",{attrs:{dark:t.isDark,disabled:t.disabled,loading:t.loading,rules:t.lang_rules,items:t.form.langs,label:"Language",color:"purple darken-2",required:""},model:{value:t.form.lang,callback:function(e){t.$set(t.form,"lang",e)},expression:"form.lang"}})],1),n("v-col",{attrs:{cols:"12"}},[n("v-textarea",{attrs:{color:"teal",disabled:t.disabled,loading:t.loading,rules:t.text_rules},scopedSlots:t._u([{key:"label",fn:function(){return[n("div",[t._v("Text")])]},proxy:!0}]),model:{value:t.form.content,callback:function(e){t.$set(t.form,"content",e)},expression:"form.content"}})],1),n("v-col",{attrs:{cols:"12"}},[n("v-menu",{attrs:{"offset-y":""},scopedSlots:t._u([{key:"activator",fn:function(e){var a=e.attrs,o=e.on;return[n("v-btn",t._g(t._b({attrs:{icon:""}},"v-btn",a,!1),o),[n("v-icon",[t._v("mdi-file")])],1)]}}])},[n("v-list",{attrs:{dark:t.isDark,dense:"","min-width":"180"}},[n("v-list-item-group",t._l(t.sounds,(function(e){return n("v-list-item",{key:e[0],attrs:{link:""},on:{click:function(n){return t.set_sound(e)}}},[n("v-list-item-content",[n("v-list-item-title",[t._v(" "+t._s(e[0]))])],1)],1)})),1)],1)],1)],1)],1)],1),n("v-card-actions",[n("v-btn",{attrs:{disabled:t.play_loading,loading:t.play_loading,text:""},on:{click:t.play}},[t._v(" Play ")]),n("v-spacer"),n("v-btn",{attrs:{disabled:t.play_loading,loading:t.play_loading,text:""},on:{click:t.queue}},[t._v(" Queue ")]),n("v-spacer"),n("v-btn",{attrs:{disabled:t.disabled||t.save_loading,loading:t.save_loading,text:"",color:"primary"},on:{click:t.save}},[t._v(" Save ")]),n("v-spacer"),n("v-btn",{attrs:{disabled:!("temp"!=t.sound&&""!=t.sound),loading:t.loading,text:""},on:{click:t.del}},[t._v(" del ")])],1)],1)],1)],1)],1)},o=[],i=n("5530"),s=(n("dca8"),n("b0c0"),n("ac1f"),n("1276"),n("159b"),n("2f62")),l={data:function(){var t=Object.freeze({name:"",content:"",langs:["en","ar","fr"],lang:"ar"});return{form:Object.assign({},t),sounds:[["temp",""]],sound:"",valid:!0,loading:!1,save_loading:!1,play_loading:!1,defaultForm:t}},computed:Object(i["a"])(Object(i["a"])({},Object(s["b"])("Theme",["isDark"])),{},{name_rules:function(){var t=[function(t){return(t||"").length<=50||"Name must be less then 50 characters"},function(t){return(t||"").indexOf(" ")<0||"Name cannot conatin spaces"},function(t){return!!t||"Name is Required"}];return t},text_rules:function(){return[function(t){return!!t||"Text is Required"}]},lang_rules:function(){return[function(t){return!!t||"Language is Required"}]},disabled:function(){return!("temp"==this.sound&&!this.loading)}}),methods:{resetForm:function(){this.form=Object.assign({},this.defaultForm),this.$refs.SoundForm.reset()},set_sound:function(t){"temp"==t[0]?(this.sound="temp",this.resetForm()):(this.form.name=t[0],this.form.content=t[1],this.form.lang="en",this.sound=t[0])},fetch_sounds:function(){var t=this;this.loading=!0,this.save_loading=!0,this.play_loading=!0,t.sounds=[["temp",""]],this.$store.dispatch("Voice/fetch_sounds",null,{root:!0}).then((function(e){console.log("dispatched fetch sounds",e),e=e.message,e?(e=e.split("%"),e.forEach((function(e){t.sounds.push(e.split("&"))}))):t.sounds=[["temp",""]],t.loading=!1,t.save_loading=!1,t.play_loading=!1})).catch((function(e){console.error(e),t.loading=!1,t.save_loading=!1,t.play_loading=!1}))},save:function(){var t=this;this.$refs.SoundForm.validate()&&(this.loading=!0,this.save_loading=!0,this.play_loading=!0,this.$store.dispatch("Voice/save_file",{lang:this.form.lang,name:this.form.name,content:this.form.content},{root:!0}).then((function(e){console.log("Dispatched Save Voice ",e),setTimeout((function(){t.fetch_sounds()}),2e3)})).catch((function(e){console.error("Error whiel Saving voice ",e),t.fetch_sounds()})))},play:function(){var t=this;this.$refs.SoundForm.validate()&&(this.loading=!0,this.save_loading=!0,this.play_loading=!0,"temp"==this.sound?this.$store.dispatch("Voice/play_temp",{content:this.form.content,lang:this.form.lang},{root:!0}).then((function(e){console.log("Dispatched play temp",e),t.loading=!1,t.save_loading=!1,t.play_loading=!1})).catch((function(e){console.error("Error while playing temp",e),t.loading=!1,t.save_loading=!1,t.play_loading=!1})):""!=this.sound&&this.$store.dispatch("Voice/play_saved_file",this.form.name,{root:!0}).then((function(e){console.log("Dispatched play temp",e),t.loading=!1,t.save_loading=!1,t.play_loading=!1})).catch((function(e){console.error("Error while playing temp",e),t.loading=!1,t.save_loading=!1,t.play_loading=!1})))},queue:function(){this.$refs.SoundForm.validate()&&"temp"!=this.sound&&this.$store.dispatch("Ros/take_action","interactive/speak_push_to_queue/".concat(this.form.name,".mp3"),{root:!0}).then((function(){console.log("queued")})).catch((function(t){console.log("error while trying to push",t)}))},del:function(){var t=this;this.$refs.SoundForm.validate()&&(this.loading=!0,this.save_loading=!0,this.play_loading=!0,this.$store.dispatch("Voice/del_file",this.form.name,{root:!0}).then((function(e){console.log("Dispatched del Voice ",e),setTimeout((function(){t.fetch_sounds(),t.set_sound(["temp",""])}),2e3)})).catch((function(e){console.error("Error whiel Del voice ",e),t.fetch_sounds()})))}},created:function(){this.fetch_sounds()}},r=l,c=n("2877"),u=n("6544"),d=n.n(u),h=n("8336"),f=n("b0af"),v=n("99d9"),p=n("62ad"),g=n("a523"),b=n("ce7e"),_=n("4bd4"),m=n("132d"),y=n("8860"),x=n("da13"),w=n("5d23"),j=n("1baa"),V=n("e449"),S=n("0fd9"),C=n("b974"),k=n("2fa4"),$=n("8654"),O=n("a844"),D=Object(c["a"])(r,a,o,!1,null,null,null);e["default"]=D.exports;d()(D,{VBtn:h["a"],VCard:f["a"],VCardActions:v["a"],VCol:p["a"],VContainer:g["a"],VDivider:b["a"],VForm:_["a"],VIcon:m["a"],VList:y["a"],VListItem:x["a"],VListItemContent:w["a"],VListItemGroup:j["a"],VListItemTitle:w["b"],VMenu:V["a"],VRow:S["a"],VSelect:C["a"],VSpacer:k["a"],VTextField:$["a"],VTextarea:O["a"]})},"0254":function(t,e,n){"use strict";n.r(e);var a=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("v-container",{staticClass:"center"},[a("v-row",[a("v-col",{attrs:{cols:"12"}},[a("h4",{staticClass:"text-h2 text-center"},[t._v("Ros Not Connected")])]),a("v-col",{attrs:{cols:"12"}},[a("v-img",{staticClass:"mx-auto",attrs:{src:n("16f4"),"min-width":"100px","max-width":"200"}})],1)],1)],1)},o=[],i=(n("b0c0"),{created:function(){var t=this;this.$store.dispatch("Loading/set",null,{root:!0}),this.$store.dispatch("Ros/fetchConnectionFlag",null,{root:!0}).then((function(){console.log("clearing Loading"),t.$store.dispatch("Loading/clear",null,{root:!0}),t.$route.meta.requiresConnectoin||null===t.$route.name||t.$router.push(t.$route.query.redirect).catch((function(t){if(2!=t.type)throw new Error("something went wrong while pushing ".concat(t))}))})).catch((function(){t.$store.dispatch("Loading/clear",null,{root:!0})}))}}),s=i,l=(n("0d66"),n("2877")),r=n("6544"),c=n.n(r),u=n("62ad"),d=n("a523"),h=n("adda"),f=n("0fd9"),v=Object(l["a"])(s,a,o,!1,null,"c9710b00",null);e["default"]=v.exports;c()(v,{VCol:u["a"],VContainer:d["a"],VImg:h["a"],VRow:f["a"]})},"0d66":function(t,e,n){"use strict";n("9b0b")},"0fd9":function(t,e,n){"use strict";var a=n("ade3"),o=n("5530"),i=(n("caad"),n("2532"),n("99af"),n("b64b"),n("ac1f"),n("5319"),n("4ec9"),n("d3b7"),n("3ca3"),n("ddb0"),n("159b"),n("4b85"),n("2b0e")),s=n("d9f7"),l=n("80d2"),r=["sm","md","lg","xl"],c=["start","end","center"];function u(t,e){return r.reduce((function(n,a){return n[t+Object(l["G"])(a)]=e(),n}),{})}var d=function(t){return[].concat(c,["baseline","stretch"]).includes(t)},h=u("align",(function(){return{type:String,default:null,validator:d}})),f=function(t){return[].concat(c,["space-between","space-around"]).includes(t)},v=u("justify",(function(){return{type:String,default:null,validator:f}})),p=function(t){return[].concat(c,["space-between","space-around","stretch"]).includes(t)},g=u("alignContent",(function(){return{type:String,default:null,validator:p}})),b={align:Object.keys(h),justify:Object.keys(v),alignContent:Object.keys(g)},_={align:"align",justify:"justify",alignContent:"align-content"};function m(t,e,n){var a=_[t];if(null!=n){if(e){var o=e.replace(t,"");a+="-".concat(o)}return a+="-".concat(n),a.toLowerCase()}}var y=new Map;e["a"]=i["default"].extend({name:"v-row",functional:!0,props:Object(o["a"])(Object(o["a"])(Object(o["a"])({tag:{type:String,default:"div"},dense:Boolean,noGutters:Boolean,align:{type:String,default:null,validator:d}},h),{},{justify:{type:String,default:null,validator:f}},v),{},{alignContent:{type:String,default:null,validator:p}},g),render:function(t,e){var n=e.props,o=e.data,i=e.children,l="";for(var r in n)l+=String(n[r]);var c=y.get(l);return c||function(){var t,e;for(e in c=[],b)b[e].forEach((function(t){var a=n[t],o=m(e,t,a);o&&c.push(o)}));c.push((t={"no-gutters":n.noGutters,"row--dense":n.dense},Object(a["a"])(t,"align-".concat(n.align),n.align),Object(a["a"])(t,"justify-".concat(n.justify),n.justify),Object(a["a"])(t,"align-content-".concat(n.alignContent),n.alignContent),t)),y.set(l,c)}(),t(n.tag,Object(s["a"])(o,{staticClass:"row",class:c}),i)}})},1681:function(t,e,n){},"16f4":function(t,e,n){t.exports=n.p+"img/404.5bb55ce7.png"},"1f22":function(t,e,n){},2677:function(t,e,n){"use strict";var a=n("8654");e["a"]=a["a"]},"270d":function(t,e,n){"use strict";n.r(e);var a=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{attrs:{id:"root"}},[t.loading.show?n("div",{staticClass:"loading",staticStyle:{display:"grid","place-items":"center"}},[n("v-card",{staticClass:"transition-fast-in-fast-out v-card--reveal pa-4",attrs:{elevation:"6",dark:""}},[n("v-card-title",{staticClass:"text-h6 font-weight-bold",staticStyle:{"text-align":"center","padding-top":"30px"}},[t._v(t._s(t.loading.title))]),-1!=t.loading.timer?n("v-card-text",{staticClass:"text-h6 font-weight-bold",staticStyle:{"text-align":"center","padding-top":"10px"}},[t._v(" "+t._s(t.loading.timer)+" ")]):t._e(),n("v-card-text",{},[n("v-container",{attrs:{fluid:""}},[n("v-row",[n("v-col",{staticStyle:{display:"flex","justify-content":"space-around"}},[n("v-progress-circular",{staticStyle:{"text-align":"center","padding-top":"10px"},attrs:{size:50,color:"primary",indeterminate:""}})],1)],1)],1)],1)],1)],1):t._e(),n("v-container",[n("div",{staticClass:"text-h4"},[t._v("Bluetooth Controller")]),n("v-divider",{staticClass:"py-4"}),n("v-card",{attrs:{elevation:"6",dark:t.isDark}},[n("v-container",{attrs:{fluid:""}},[n("v-row",[n("v-col",{attrs:{cols:"12"}},[n("div",{staticClass:"text-h6"},[t._v("Actions")])]),n("v-col",{staticClass:"flex-wrap justify-space-between",attrs:{cols:"12"}},[n("v-btn",{attrs:{disabled:!1,loading:!1,text:"",color:"purple"},on:{click:t.disconnect}},[t._v(" Disconnect ")]),n("v-btn",{attrs:{disabled:!1,loading:!1,text:"",color:"purple"},on:{click:t.reset_volume_control}},[t._v(" reset volume ")]),n("v-btn",{attrs:{disabled:!1,loading:!1,text:"",color:"purple"},on:{click:t.clear_default}},[t._v(" Clear Default ")]),n("v-btn",{attrs:{loading:!1,disabled:!t.bluetooth.connect_table.show,text:"",color:"purple"},on:{click:t.set_default}},[t._v(" Set Default ")]),n("v-btn",{attrs:{loading:!1,text:"",color:"purple"},on:{click:t.connect_default}},[t._v(" Connect Default ")]),n("v-btn",{attrs:{disabled:!1,loading:!1,text:"",color:"purple"},on:{click:t.scan}},[t._v(" scan ")])],1)],1)],1),n("v-container",{attrs:{fluid:""}},[n("v-row",[n("v-col",{attrs:{cols:"12"}},[n("v-divider")],1)],1)],1),n("v-container",{attrs:{fluid:""}},[n("v-row",[n("v-col",{attrs:{cols:"12"}},[n("div",{staticClass:"text-h6"},[t._v("Connected Devices")])]),t.bluetooth.connect_table.show?n("v-col",{attrs:{cols:"12"}},[n("v-data-table",{staticClass:"elevation-1",attrs:{headers:t.bluetooth.connect_table.headers,items:t.bluetooth.connect_table.data}})],1):n("v-col",{attrs:{cols:"12"}},[n("v-container",{staticStyle:{display:"flex","justify-content":"space-around"}},[n("span",{},[t._v(t._s(t.bluetooth.connect_table.alternative))])])],1)],1)],1),n("v-container",{attrs:{fluid:"",id:""}},[n("v-row",[n("v-col",{attrs:{cols:"12"}},[n("v-divider")],1)],1)],1),n("v-container",{attrs:{fluid:""}},[n("v-row",[n("v-col",{attrs:{cols:"12"}},[n("div",{staticClass:"text-h6"},[t._v("Scanning Results")])]),t.bluetooth.scan_table.show?n("v-col",{attrs:{cols:"12"}},[n("v-data-table",{staticClass:"elevation-1",attrs:{headers:t.bluetooth.scan_table.headers,items:t.bluetooth.scan_table.data},scopedSlots:t._u([{key:"item.actions",fn:function(e){var a=e.item;return[n("v-icon",{staticClass:"mr-2",attrs:{small:"",disabled:t.bluetooth.connect_table.show},on:{click:function(e){return t.connect(a.uuid)}}},[t._v(" mdi-bluetooth-connect ")])]}}],null,!1,3368011951)})],1):n("v-col",{attrs:{cols:"12"}},[n("v-container",{staticStyle:{display:"flex","justify-content":"space-around"}},[n("span",{},[t._v(t._s(t.bluetooth.scan_table.alternative))])])],1)],1)],1)],1)],1)],1)},o=[],i=n("5530"),s=(n("ac1f"),n("1276"),n("159b"),n("7db0"),n("fb6a"),n("2f62")),l={data:function(){return{loading:{show:!0,timer:-1,timer_state:!1,interval_holder:null},bluetooth:{defaults:{scan_table:{headers:[{text:"Name",value:"name",align:"start"},{text:"UUID",value:"uuid"},{text:"Connect",value:"actions",sortable:!1}],show:!1,data:null},connect_table:{headers:[{text:"Name",value:"name",align:"start"},{text:"UUID",value:"uuid"},{text:"Default",value:"default"}],show:!1,data:null,alternative:null}},scan_table:{headers:[{text:"Name",value:"name",sortable:!1,align:"start"},{text:"UUID",value:"uuid"},{text:"Connect",value:"actions",sortable:!1}],show:!1,data:null,alternative:"Please Scan To Show Nearbye Devices"},connect_table:{headers:[{text:"Name",value:"name",sortable:!1,align:"start"},{text:"UUID",value:"uuid"},{text:"Default",value:"default"}],show:!1,data:null,alternative:null},default:null}}},computed:Object(i["a"])({},Object(s["b"])("Theme",["isDark"])),created:function(){this.update()},methods:{scan:function(){var t=this;this.set_loading(!0,"Loading...",15),Object.assign(this.bluetooth.scan_table,this.bluetooth.defaults.scan_table),this.$store.dispatch("Ros/take_action","bluetooth/scan",{root:!0}).then((function(e){if(console.log("Bluetooth Scanning results Camse Back",e),"no_scan"==e)t.bluetooth.scan_table.alternative="No Devices Found";else{var n=[];e=e.split("|"),e.forEach((function(t){t=t.split("/"),n.find((function(e){return e.uuid==t[0]}))||n.push({name:t[1],uuid:t[0]})})),console.log(n),t.bluetooth.scan_table.data=n,t.bluetooth.scan_table.show=!0}t.update(),t.set_loading(!1)})).catch((function(e){console.log(e),t.set_loading(!1)}))},update:function(){var t=this;this.set_loading(!0,"Loading..."),Object.assign(this.bluetooth.connect_table,this.bluetooth.defaults.connect_table),this.$store.dispatch("Ros/take_action","bluetooth/get_default",{root:!0}).then((function(e){console.log("default bluetooth dev",e),t.bluetooth.default="empty"==e?null:e,t.$store.dispatch("Ros/take_action","bluetooth/connected",{root:!0}).then((function(e){console.log("connected devices",e),"not_"==e.slice(0,4)?t.bluetooth.connect_table.alternative="No Connection Found":(e=e.split("|"),e.forEach((function(n,a){n=n.split("/"),console.log(n[0],t.bluetooth.default),e[a]={name:n[1],uuid:n[0],default:t.bluetooth.default==n[0]?"Yes":"No"}})),t.bluetooth.connect_table.data=e,t.bluetooth.connect_table.show=!0),t.set_loading(!1)})).catch((function(e){console.log(e),t.set_loading(!1)}))})).catch((function(e){console.log(e),t.set_loading(!1)}))},disconnect:function(){var t=this;console.log("disconnecting "),Object.assign(this.bluetooth.connect_table,this.bluetooth.defaults.connect_table),this.set_loading(!0,"Disconnecting..."),this.$store.dispatch("Ros/take_action","bluetooth/disconnect",{root:!0}).then((function(e){console.log("disconnecting finished wiht ",e),t.update()})).catch((function(e){console.log(e),t.set_loading(!1)}))},clear_default:function(){var t=this;this.$store.dispatch("Ros/take_action","bluetooth/clear_default",{root:!0}).then((function(e){console.log("Clearing Default Done",e),t.update()})).catch((function(e){console.log("Error while Clearing Default",e),t.update()}))},reset_volume_control:function(){var t=this;this.$store.dispatch("Ros/take_action","bluetooth/reset_volume/100",{root:!0}).then((function(e){console.log("Clearing Default Done",e),t.update()})).catch((function(e){console.log("Error while Clearing Default",e),t.update()}))},set_default:function(){var t=this;if(console.log("setting default "),this.bluetooth.connect_table.show&&this.bluetooth.connect_table.data){var e=this.bluetooth.connect_table.data[0].uuid;this.$store.dispatch("Ros/take_action","bluetooth/set_default/"+e).then((function(e){console.log("Done",e),t.update()})).catch((function(e){console.log("Error while setting default bluetooth device",e),t.update()}))}},connect_default:function(){var t=this;console.log("setting default "),this.$store.dispatch("Ros/take_action","bluetooth/connect_default/0").then((function(e){console.log("Done",e),t.update()})).catch((function(e){console.log("Error while setting default bluetooth device",e),t.update()}))},connect:function(t){var e=this;console.log("setting connection ",t),Object.assign(this.bluetooth.connect_table,this.bluetooth.defaults.connect_table),this.set_loading(!0,"Connecting..."),this.$store.dispatch("Ros/take_action","bluetooth/connect/"+t,{root:!0}).then((function(t){console.log("connecting finished wiht ",t),e.update()})).catch((function(t){console.log(t),e.update(),e.set_loading(!1)}))},set_loading:function(t){var e=this,n=arguments.length>1&&void 0!==arguments[1]?arguments[1]:"",a=arguments.length>2&&void 0!==arguments[2]?arguments[2]:-1;console.log("setting loading",t,a),t?(this.loading.show=t,this.loading.title=n,-1!=a?(this.loading.timer=a,this.loading.interval_holder=setInterval((function(){e.loading.timer-=1,e.loading.timer<=1&&(clearInterval(e.interval_holder),e.loading.timer=-1)}),1e3)):(clearInterval(this.interval_holder),this.loading.timer=-1)):(this.loading.show=!1,clearInterval(this.interval_holder),this.loading.timer=-1)}}},r=l,c=(n("8ee1"),n("2877")),u=n("6544"),d=n.n(u),h=n("8336"),f=n("b0af"),v=n("99d9"),p=n("62ad"),g=n("a523"),b=n("8fea"),_=n("ce7e"),m=n("132d"),y=n("490a"),x=n("0fd9"),w=Object(c["a"])(r,a,o,!1,null,"ccef675c",null);e["default"]=w.exports;d()(w,{VBtn:h["a"],VCard:f["a"],VCardText:v["b"],VCardTitle:v["c"],VCol:p["a"],VContainer:g["a"],VDataTable:b["a"],VDivider:_["a"],VIcon:m["a"],VProgressCircular:y["a"],VRow:x["a"]})},"4bd4":function(t,e,n){"use strict";var a=n("5530"),o=(n("caad"),n("2532"),n("07ac"),n("4de4"),n("159b"),n("7db0"),n("58df")),i=n("7e2b"),s=n("3206");e["a"]=Object(o["a"])(i["a"],Object(s["b"])("form")).extend({name:"v-form",provide:function(){return{form:this}},inheritAttrs:!1,props:{disabled:Boolean,lazyValidation:Boolean,readonly:Boolean,value:Boolean},data:function(){return{inputs:[],watchers:[],errorBag:{}}},watch:{errorBag:{handler:function(t){var e=Object.values(t).includes(!0);this.$emit("input",!e)},deep:!0,immediate:!0}},methods:{watchInput:function(t){var e=this,n=function(t){return t.$watch("hasError",(function(n){e.$set(e.errorBag,t._uid,n)}),{immediate:!0})},a={_uid:t._uid,valid:function(){},shouldValidate:function(){}};return this.lazyValidation?a.shouldValidate=t.$watch("shouldValidate",(function(o){o&&(e.errorBag.hasOwnProperty(t._uid)||(a.valid=n(t)))})):a.valid=n(t),a},validate:function(){return 0===this.inputs.filter((function(t){return!t.validate(!0)})).length},reset:function(){this.inputs.forEach((function(t){return t.reset()})),this.resetErrorBag()},resetErrorBag:function(){var t=this;this.lazyValidation&&setTimeout((function(){t.errorBag={}}),0)},resetValidation:function(){this.inputs.forEach((function(t){return t.resetValidation()})),this.resetErrorBag()},register:function(t){this.inputs.push(t),this.watchers.push(this.watchInput(t))},unregister:function(t){var e=this.inputs.find((function(e){return e._uid===t._uid}));if(e){var n=this.watchers.find((function(t){return t._uid===e._uid}));n&&(n.valid(),n.shouldValidate()),this.watchers=this.watchers.filter((function(t){return t._uid!==e._uid})),this.inputs=this.inputs.filter((function(t){return t._uid!==e._uid})),this.$delete(this.errorBag,e._uid)}}},render:function(t){var e=this;return t("form",{staticClass:"v-form",attrs:Object(a["a"])({novalidate:!0},this.attrs$),on:{submit:function(t){return e.$emit("submit",t)}}},this.$slots.default)}})},5803:function(t,e,n){},"62ad":function(t,e,n){"use strict";var a=n("ade3"),o=n("5530"),i=(n("a9e3"),n("b64b"),n("ac1f"),n("5319"),n("4ec9"),n("d3b7"),n("3ca3"),n("ddb0"),n("caad"),n("159b"),n("2ca0"),n("4b85"),n("2b0e")),s=n("d9f7"),l=n("80d2"),r=["sm","md","lg","xl"],c=function(){return r.reduce((function(t,e){return t[e]={type:[Boolean,String,Number],default:!1},t}),{})}(),u=function(){return r.reduce((function(t,e){return t["offset"+Object(l["G"])(e)]={type:[String,Number],default:null},t}),{})}(),d=function(){return r.reduce((function(t,e){return t["order"+Object(l["G"])(e)]={type:[String,Number],default:null},t}),{})}(),h={col:Object.keys(c),offset:Object.keys(u),order:Object.keys(d)};function f(t,e,n){var a=t;if(null!=n&&!1!==n){if(e){var o=e.replace(t,"");a+="-".concat(o)}return"col"!==t||""!==n&&!0!==n?(a+="-".concat(n),a.toLowerCase()):a.toLowerCase()}}var v=new Map;e["a"]=i["default"].extend({name:"v-col",functional:!0,props:Object(o["a"])(Object(o["a"])(Object(o["a"])(Object(o["a"])({cols:{type:[Boolean,String,Number],default:!1}},c),{},{offset:{type:[String,Number],default:null}},u),{},{order:{type:[String,Number],default:null}},d),{},{alignSelf:{type:String,default:null,validator:function(t){return["auto","start","end","center","baseline","stretch"].includes(t)}},tag:{type:String,default:"div"}}),render:function(t,e){var n=e.props,o=e.data,i=e.children,l=(e.parent,"");for(var r in n)l+=String(n[r]);var c=v.get(l);return c||function(){var t,e;for(e in c=[],h)h[e].forEach((function(t){var a=n[t],o=f(e,t,a);o&&c.push(o)}));var o=c.some((function(t){return t.startsWith("col-")}));c.push((t={col:!o||!n.cols},Object(a["a"])(t,"col-".concat(n.cols),n.cols),Object(a["a"])(t,"offset-".concat(n.offset),n.offset),Object(a["a"])(t,"order-".concat(n.order),n.order),Object(a["a"])(t,"align-self-".concat(n.alignSelf),n.alignSelf),t)),v.set(l,c)}(),t(n.tag,Object(s["a"])(o,{class:c}),i)}})},"8ee1":function(t,e,n){"use strict";n("1f22")},"9b0b":function(t,e,n){},a844:function(t,e,n){"use strict";var a=n("5530"),o=(n("a9e3"),n("1681"),n("8654")),i=n("58df"),s=Object(i["a"])(o["a"]);e["a"]=s.extend({name:"v-textarea",props:{autoGrow:Boolean,noResize:Boolean,rowHeight:{type:[Number,String],default:24,validator:function(t){return!isNaN(parseFloat(t))}},rows:{type:[Number,String],default:5,validator:function(t){return!isNaN(parseInt(t,10))}}},computed:{classes:function(){return Object(a["a"])({"v-textarea":!0,"v-textarea--auto-grow":this.autoGrow,"v-textarea--no-resize":this.noResizeHandle},o["a"].options.computed.classes.call(this))},noResizeHandle:function(){return this.noResize||this.autoGrow}},watch:{lazyValue:function(){this.autoGrow&&this.$nextTick(this.calculateInputHeight)},rowHeight:function(){this.autoGrow&&this.$nextTick(this.calculateInputHeight)}},mounted:function(){var t=this;setTimeout((function(){t.autoGrow&&t.calculateInputHeight()}),0)},methods:{calculateInputHeight:function(){var t=this.$refs.input;if(t){t.style.height="0";var e=t.scrollHeight,n=parseInt(this.rows,10)*parseFloat(this.rowHeight);t.style.height=Math.max(n,e)+"px"}},genInput:function(){var t=o["a"].options.methods.genInput.call(this);return t.tag="textarea",delete t.data.attrs.type,t.data.attrs.rows=this.rows,t},onInput:function(t){o["a"].options.methods.onInput.call(this,t),this.autoGrow&&this.calculateInputHeight()},onKeyDown:function(t){this.isFocused&&13===t.keyCode&&t.stopPropagation(),this.$emit("keydown",t)}}})},c52c:function(t,e,n){"use strict";n.r(e);var a=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{attrs:{id:"root"}},[n("v-container",[n("div",{staticClass:"text-h4"},[t._v("Voucher Loading Manager")]),n("v-divider",{staticClass:"py-2"}),n("v-card",{attrs:{elevation:"6",dark:t.isDark}},[n("v-form",{ref:"voucherForm",model:{value:t.valid,callback:function(e){t.valid=e},expression:"valid"}},[n("v-container",{attrs:{fluid:""}},[n("v-row",[n("v-col",{attrs:{cols:"12"}},[n("v-file-input",{attrs:{counter:"","show-size":"","truncate-length":"15"},on:{change:function(e){return t.check()}},model:{value:t.file.obj,callback:function(e){t.$set(t.file,"obj",e)},expression:"file.obj"}}),t.file.error?n("p",{staticClass:"pl-6 red--text text--lighten-3"},[t._v(" "+t._s(t.file.error_dictionary[t.file.error_type])+" ")]):t._e(),t.file.loaded?n("p",{staticClass:"pl-6 green--text text--lighten-3"},[t._v(" The Vouchers Has Been Stored in Database Successfully ")]):t._e()],1)],1)],1),t.file.is_valid_vouchers?n("v-container",{attrs:{fluid:""}},[n("v-row",[n("v-col",[n("div",{staticClass:"text-h6"},[t._v("Valid Vouchers")])]),n("v-col",{attrs:{cols:"12"}},[n("v-data-table",{attrs:{dense:"",headers:t.file.headers,items:t.file.valid_vouchers,"item-key":"Serial"}})],1)],1)],1):t._e(),t.file.is_rejected_vouchers?n("v-container",{attrs:{fluid:""}},[n("v-row",[n("v-col",[n("div",{staticClass:"text-h6"},[t._v("Rejected Vouchers")])]),n("v-col",{attrs:{cols:"12"}},[n("v-data-table",{attrs:{dense:"",headers:t.file.headers,items:t.file.rejected_vouchers,"item-key":"Serial"}})],1)],1)],1):t._e(),n("v-card-actions",[n("v-spacer"),n("v-btn",{attrs:{disabled:!t.file.is_valid_vouchers,loading:t.file.loading,text:"",color:"primary"},on:{click:function(e){return t.load()}}},[t._v(" Load ")]),n("v-spacer"),n("v-btn",{attrs:{disabled:t.file.loading||t.file.saving,loading:t.file.loading||t.file.saving,text:"",color:"primary"},on:{click:function(e){return t.clear()}}},[t._v(" Clear ")]),n("v-spacer")],1)],1)],1)],1)],1)},o=[],i=n("5530"),s=(n("dca8"),n("b0c0"),n("ac1f"),n("1276"),n("d81d"),n("fb6a"),n("159b"),n("2f62")),l={data:function(){var t=Object.freeze({obj:{},error:!1,error_dictionary:{not_csv:"Please chose and open either CSV file or xlsx file",not_valid:"The CSV file is not valid",no_file:"Please chose Valid file",over_size:"The File size should be less then 30kB"},error_type:null,loaded:!1,loading:!1,headers:[{text:"Serial Number",value:"Serial"},{text:"PIN",value:"PIN"},{text:"Value",value:"Value"}],saving:!1,valid:!1,valid_vouchers:[],rejected_vouchers:[],is_valid_vouchers:!1,is_rejected_vouchers:!1});return{file:Object.assign({},t),defaultForm:t,valid:!0}},computed:Object(i["a"])(Object(i["a"])({},Object(s["b"])("Theme",["isDark"])),{},{disabled:function(){return!1}}),methods:{resetForm:function(){this.file=Object.assign({},this.defaultForm),this.$refs.voucherForm.reset()},check:function(){var t=this;if(t.file.valid_vouchers=[],t.file.rejected_vouchers=[],t.file.loaded=!1,t.file.error=!1,this.file.obj){if(console.log(this.file),!this.file.obj.name)return this.clear(),this.file.error_type="no_file",void(this.file.error=!0);console.log("a file has been chosen");var e=this.file.obj.name.split(".");if(e=e[e.length-1],console.log(e),"csv"!=e)return this.clear(),this.file.error_type="not_csv",void(this.file.error=!0);if(this.file.obj.size>3e4)return this.clear(),this.file.error_type="over_size",void(this.file.error=!0);var n=new FileReader;n.onload=function(){var e=n.result.split("\n");e=e.map((function(t){return t.split(",")}));var a=e[0];e=e.slice(1,e.length-1);var o=[];e.forEach((function(t){var e={};t.forEach((function(t,n){e[a[n]]=t})),o.push(e)})),o.forEach((function(e){13!=e.PIN.length?t.file.rejected_vouchers.push(e):5==parseInt(e.Value)||10==parseInt(e.Value)?t.file.valid_vouchers.push(e):t.file.rejected_vouchers.push(e)})),t.file.is_valid_vouchers=t.file.valid_vouchers.length>0,t.file.is_rejected_vouchers=t.file.rejected_vouchers.length>0,console.log(o)},n.readAsText(this.file.obj)}},clear:function(){this.resetForm()},load:function(){var t=this;this.$store.dispatch("Ros/postVouchers",this.file.valid_vouchers,{root:!0}).then((function(){t.clear(),t.file.loaded=!0}))}},created:function(){}},r=l,c=n("2877"),u=n("6544"),d=n.n(u),h=n("8336"),f=n("b0af"),v=n("99d9"),p=n("62ad"),g=n("a523"),b=n("8fea"),_=n("ce7e"),m=n("2909"),y=n("53ca"),x=(n("a9e3"),n("caad"),n("99af"),n("a434"),n("5803"),n("2677")),w=n("cc20"),j=n("80d2"),V=n("d9bd"),S=n("d9f7"),C=x["a"].extend({name:"v-file-input",model:{prop:"value",event:"change"},props:{chips:Boolean,clearable:{type:Boolean,default:!0},counterSizeString:{type:String,default:"$vuetify.fileInput.counterSize"},counterString:{type:String,default:"$vuetify.fileInput.counter"},hideInput:Boolean,placeholder:String,prependIcon:{type:String,default:"$file"},readonly:{type:Boolean,default:!1},showSize:{type:[Boolean,Number],default:!1,validator:function(t){return"boolean"===typeof t||[1e3,1024].includes(t)}},smallChips:Boolean,truncateLength:{type:[Number,String],default:22},type:{type:String,default:"file"},value:{default:void 0,validator:function(t){return Object(j["H"])(t).every((function(t){return null!=t&&"object"===Object(y["a"])(t)}))}}},computed:{classes:function(){return Object(i["a"])(Object(i["a"])({},x["a"].options.computed.classes.call(this)),{},{"v-file-input":!0})},computedCounterValue:function(){var t=this.isMultiple&&this.lazyValue?this.lazyValue.length:this.lazyValue instanceof File?1:0;if(!this.showSize)return this.$vuetify.lang.t(this.counterString,t);var e=this.internalArrayValue.reduce((function(t,e){var n=e.size,a=void 0===n?0:n;return t+a}),0);return this.$vuetify.lang.t(this.counterSizeString,t,Object(j["w"])(e,1024===this.base))},internalArrayValue:function(){return Object(j["H"])(this.internalValue)},internalValue:{get:function(){return this.lazyValue},set:function(t){this.lazyValue=t,this.$emit("change",this.lazyValue)}},isDirty:function(){return this.internalArrayValue.length>0},isLabelActive:function(){return this.isDirty},isMultiple:function(){return this.$attrs.hasOwnProperty("multiple")},text:function(){var t=this;return this.isDirty||!this.isFocused&&this.hasLabel?this.internalArrayValue.map((function(e){var n=e.name,a=void 0===n?"":n,o=e.size,i=void 0===o?0:o,s=t.truncateText(a);return t.showSize?"".concat(s," (").concat(Object(j["w"])(i,1024===t.base),")"):s})):[this.placeholder]},base:function(){return"boolean"!==typeof this.showSize?this.showSize:void 0},hasChips:function(){return this.chips||this.smallChips}},watch:{readonly:{handler:function(t){!0===t&&Object(V["b"])("readonly is not supported on <v-file-input>",this)},immediate:!0},value:function(t){var e=this.isMultiple?t:t?[t]:[];Object(j["j"])(e,this.$refs.input.files)||(this.$refs.input.value="")}},methods:{clearableCallback:function(){this.internalValue=this.isMultiple?[]:null,this.$refs.input.value=""},genChips:function(){var t=this;return this.isDirty?this.text.map((function(e,n){return t.$createElement(w["a"],{props:{small:t.smallChips},on:{"click:close":function(){var e=t.internalValue;e.splice(n,1),t.internalValue=e}}},[e])})):[]},genControl:function(){var t=x["a"].options.methods.genControl.call(this);return this.hideInput&&(t.data.style=Object(S["c"])(t.data.style,{display:"none"})),t},genInput:function(){var t=x["a"].options.methods.genInput.call(this);return delete t.data.domProps.value,delete t.data.on.input,t.data.on.change=this.onInput,[this.genSelections(),t]},genPrependSlot:function(){var t=this;if(!this.prependIcon)return null;var e=this.genIcon("prepend",(function(){t.$refs.input.click()}));return this.genSlot("prepend","outer",[e])},genSelectionText:function(){var t=this.text.length;return t<2?this.text:this.showSize&&!this.counter?[this.computedCounterValue]:[this.$vuetify.lang.t(this.counterString,t)]},genSelections:function(){var t=this,e=[];return this.isDirty&&this.$scopedSlots.selection?this.internalArrayValue.forEach((function(n,a){t.$scopedSlots.selection&&e.push(t.$scopedSlots.selection({text:t.text[a],file:n,index:a}))})):e.push(this.hasChips&&this.isDirty?this.genChips():this.genSelectionText()),this.$createElement("div",{staticClass:"v-file-input__text",class:{"v-file-input__text--placeholder":this.placeholder&&!this.isDirty,"v-file-input__text--chips":this.hasChips&&!this.$scopedSlots.selection}},e)},genTextFieldSlot:function(){var t=this,e=x["a"].options.methods.genTextFieldSlot.call(this);return e.data.on=Object(i["a"])(Object(i["a"])({},e.data.on||{}),{},{click:function(){return t.$refs.input.click()}}),e},onInput:function(t){var e=Object(m["a"])(t.target.files||[]);this.internalValue=this.isMultiple?e:e[0],this.initialValue=this.internalValue},onKeyDown:function(t){this.$emit("keydown",t)},truncateText:function(t){if(t.length<Number(this.truncateLength))return t;var e=Math.floor((Number(this.truncateLength)-1)/2);return"".concat(t.slice(0,e),"…").concat(t.slice(t.length-e))}}}),k=n("4bd4"),$=n("0fd9"),O=n("2fa4"),D=Object(c["a"])(r,a,o,!1,null,null,null);e["default"]=D.exports;d()(D,{VBtn:h["a"],VCard:f["a"],VCardActions:v["a"],VCol:p["a"],VContainer:g["a"],VDataTable:b["a"],VDivider:_["a"],VFileInput:C,VForm:k["a"],VRow:$["a"],VSpacer:O["a"]})}}]);
//# sourceMappingURL=noConnection.e1e7a0c9.js.map