(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["startup_slam_start_scanning"],{"0fd9":function(t,e,n){"use strict";var i=n("ade3"),a=n("5530"),o=(n("caad"),n("2532"),n("99af"),n("b64b"),n("ac1f"),n("5319"),n("4ec9"),n("d3b7"),n("3ca3"),n("ddb0"),n("159b"),n("4b85"),n("2b0e")),c=n("d9f7"),s=n("80d2"),r=["sm","md","lg","xl"],l=["start","end","center"];function u(t,e){return r.reduce((function(n,i){return n[t+Object(s["G"])(i)]=e(),n}),{})}var d=function(t){return[].concat(l,["baseline","stretch"]).includes(t)},f=u("align",(function(){return{type:String,default:null,validator:d}})),h=function(t){return[].concat(l,["space-between","space-around"]).includes(t)},v=u("justify",(function(){return{type:String,default:null,validator:h}})),g=function(t){return[].concat(l,["space-between","space-around","stretch"]).includes(t)},p=u("alignContent",(function(){return{type:String,default:null,validator:g}})),b={align:Object.keys(f),justify:Object.keys(v),alignContent:Object.keys(p)},m={align:"align",justify:"justify",alignContent:"align-content"};function y(t,e,n){var i=m[t];if(null!=n){if(e){var a=e.replace(t,"");i+="-".concat(a)}return i+="-".concat(n),i.toLowerCase()}}var _=new Map;e["a"]=o["default"].extend({name:"v-row",functional:!0,props:Object(a["a"])(Object(a["a"])(Object(a["a"])({tag:{type:String,default:"div"},dense:Boolean,noGutters:Boolean,align:{type:String,default:null,validator:d}},f),{},{justify:{type:String,default:null,validator:h}},v),{},{alignContent:{type:String,default:null,validator:g}},p),render:function(t,e){var n=e.props,a=e.data,o=e.children,s="";for(var r in n)s+=String(n[r]);var l=_.get(s);return l||function(){var t,e;for(e in l=[],b)b[e].forEach((function(t){var i=n[t],a=y(e,t,i);a&&l.push(a)}));l.push((t={"no-gutters":n.noGutters,"row--dense":n.dense},Object(i["a"])(t,"align-".concat(n.align),n.align),Object(i["a"])(t,"justify-".concat(n.justify),n.justify),Object(i["a"])(t,"align-content-".concat(n.alignContent),n.alignContent),t)),_.set(s,l)}(),t(n.tag,Object(c["a"])(a,{staticClass:"row",class:l}),o)}})},"169a":function(t,e,n){"use strict";var i=n("5530"),a=n("2909"),o=n("ade3"),c=(n("a9e3"),n("498a"),n("caad"),n("2532"),n("7db0"),n("368e"),n("480e")),s=n("4ad4"),r=n("b848"),l=n("75eb"),u=n("e707"),d=n("e4d3"),f=n("21be"),h=n("f2e7"),v=n("a293"),g=n("58df"),p=n("d9bd"),b=n("80d2"),m=Object(g["a"])(s["a"],r["a"],l["a"],u["a"],d["a"],f["a"],h["a"]);e["a"]=m.extend({name:"v-dialog",directives:{ClickOutside:v["a"]},props:{dark:Boolean,disabled:Boolean,fullscreen:Boolean,light:Boolean,maxWidth:{type:[String,Number],default:"none"},noClickAnimation:Boolean,origin:{type:String,default:"center center"},persistent:Boolean,retainFocus:{type:Boolean,default:!0},scrollable:Boolean,transition:{type:[String,Boolean],default:"dialog-transition"},width:{type:[String,Number],default:"auto"}},data:function(){return{activatedBy:null,animate:!1,animateTimeout:-1,isActive:!!this.value,stackMinZIndex:200,previousActiveElement:null}},computed:{classes:function(){var t;return t={},Object(o["a"])(t,"v-dialog ".concat(this.contentClass).trim(),!0),Object(o["a"])(t,"v-dialog--active",this.isActive),Object(o["a"])(t,"v-dialog--persistent",this.persistent),Object(o["a"])(t,"v-dialog--fullscreen",this.fullscreen),Object(o["a"])(t,"v-dialog--scrollable",this.scrollable),Object(o["a"])(t,"v-dialog--animated",this.animate),t},contentClasses:function(){return{"v-dialog__content":!0,"v-dialog__content--active":this.isActive}},hasActivator:function(){return Boolean(!!this.$slots.activator||!!this.$scopedSlots.activator)}},watch:{isActive:function(t){var e;t?(this.show(),this.hideScroll()):(this.removeOverlay(),this.unbind(),null==(e=this.previousActiveElement)||e.focus())},fullscreen:function(t){this.isActive&&(t?(this.hideScroll(),this.removeOverlay(!1)):(this.showScroll(),this.genOverlay()))}},created:function(){this.$attrs.hasOwnProperty("full-width")&&Object(p["e"])("full-width",this)},beforeMount:function(){var t=this;this.$nextTick((function(){t.isBooted=t.isActive,t.isActive&&t.show()}))},beforeDestroy:function(){"undefined"!==typeof window&&this.unbind()},methods:{animateClick:function(){var t=this;this.animate=!1,this.$nextTick((function(){t.animate=!0,window.clearTimeout(t.animateTimeout),t.animateTimeout=window.setTimeout((function(){return t.animate=!1}),150)}))},closeConditional:function(t){var e=t.target;return!(this._isDestroyed||!this.isActive||this.$refs.content.contains(e)||this.overlay&&e&&!this.overlay.$el.contains(e))&&this.activeZIndex>=this.getMaxZIndex()},hideScroll:function(){this.fullscreen?document.documentElement.classList.add("overflow-y-hidden"):u["a"].options.methods.hideScroll.call(this)},show:function(){var t=this;!this.fullscreen&&!this.hideOverlay&&this.genOverlay(),this.$nextTick((function(){t.$nextTick((function(){t.previousActiveElement=document.activeElement,t.$refs.content.focus(),t.bind()}))}))},bind:function(){window.addEventListener("focusin",this.onFocusin)},unbind:function(){window.removeEventListener("focusin",this.onFocusin)},onClickOutside:function(t){this.$emit("click:outside",t),this.persistent?this.noClickAnimation||this.animateClick():this.isActive=!1},onKeydown:function(t){if(t.keyCode===b["y"].esc&&!this.getOpenDependents().length)if(this.persistent)this.noClickAnimation||this.animateClick();else{this.isActive=!1;var e=this.getActivator();this.$nextTick((function(){return e&&e.focus()}))}this.$emit("keydown",t)},onFocusin:function(t){if(t&&this.retainFocus){var e=t.target;if(e&&![document,this.$refs.content].includes(e)&&!this.$refs.content.contains(e)&&this.activeZIndex>=this.getMaxZIndex()&&!this.getOpenDependentElements().some((function(t){return t.contains(e)}))){var n=this.$refs.content.querySelectorAll('button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'),i=Object(a["a"])(n).find((function(t){return!t.hasAttribute("disabled")}));i&&i.focus()}}},genContent:function(){var t=this;return this.showLazyContent((function(){return[t.$createElement(c["a"],{props:{root:!0,light:t.light,dark:t.dark}},[t.$createElement("div",{class:t.contentClasses,attrs:Object(i["a"])({role:"document",tabindex:t.isActive?0:void 0},t.getScopeIdAttrs()),on:{keydown:t.onKeydown},style:{zIndex:t.activeZIndex},ref:"content"},[t.genTransition()])])]}))},genTransition:function(){var t=this.genInnerContent();return this.transition?this.$createElement("transition",{props:{name:this.transition,origin:this.origin,appear:!0}},[t]):t},genInnerContent:function(){var t={class:this.classes,ref:"dialog",directives:[{name:"click-outside",value:{handler:this.onClickOutside,closeConditional:this.closeConditional,include:this.getOpenDependentElements}},{name:"show",value:this.isActive}],style:{transformOrigin:this.origin}};return this.fullscreen||(t.style=Object(i["a"])(Object(i["a"])({},t.style),{},{maxWidth:"none"===this.maxWidth?void 0:Object(b["g"])(this.maxWidth),width:"auto"===this.width?void 0:Object(b["g"])(this.width)})),this.$createElement("div",t,this.getContentSlot())}},render:function(t){return t("div",{staticClass:"v-dialog__container",class:{"v-dialog__container--attached":""===this.attach||!0===this.attach||"attach"===this.attach},attrs:{role:"dialog"}},[this.genActivator(),this.genContent()])}})},"368e":function(t,e,n){},"5a28":function(t,e,n){"use strict";n.r(e);var i=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"loading",staticStyle:{display:"grid","place-items":"center"}},[n("v-container",{attrs:{fluid:""}},[n("v-row",[n("v-col",{staticStyle:{display:"flex","justify-content":"space-around"},attrs:{cols:"12"}},[n("div",{staticClass:"text-h5 font-weight-bold",staticStyle:{"text-align":"center"}},[t._v("Build map by scanning the sorrounding area")])]),n("v-col",{staticStyle:{display:"flex","justify-content":"space-around"}},[n("div",{staticClass:"font-weight-bold",staticStyle:{"text-align":"center"}},[t._v(" In order to build a map you need to manually move the robot around the place till the robot having a good visual of its sourrounding where it will autonomously navigate ")])]),n("v-col",{staticStyle:{display:"flex","justify-content":"space-around"},attrs:{cols:"12"}},[n("v-dialog",{attrs:{dark:t.isDark,width:"500"},scopedSlots:t._u([{key:"activator",fn:function(e){var i=e.on,a=e.attrs;return[n("v-btn",t._g(t._b({attrs:{color:"purple white--text",dark:t.isDark,disabled:t.continue_loading}},"v-btn",a,!1),i),[t._v(" Cancel ")])]}}]),model:{value:t.cancel_dialog,callback:function(e){t.cancel_dialog=e},expression:"cancel_dialog"}},[n("v-card",{staticClass:"pa-4"},[n("v-card-title",{},[t._v(" Cancel Salmming ")]),n("v-card-text",[t._v(" If you cancel the slamming procedure all the work has been done will be ignored "),n("br"),t._v(" Cancel? ")]),n("v-divider"),n("v-card-actions",[n("v-btn",{attrs:{color:"purple",text:""},on:{click:function(e){t.cancel(),t.cancel_dialog=!1}}},[t._v(" Yes ")]),n("v-spacer"),n("v-btn",{attrs:{color:"purple",text:""},on:{click:function(e){t.cancel_dialog=!1}}},[t._v(" No ")])],1)],1)],1),n("v-dialog",{attrs:{dark:t.isDark,width:"500"},scopedSlots:t._u([{key:"activator",fn:function(e){var i=e.on,a=e.attrs;return[n("v-btn",t._g(t._b({attrs:{color:"purple white--text",dark:t.isDark,disabled:t.continue_loading}},"v-btn",a,!1),i),[t._v(" Start Scanning ")])]}}]),model:{value:t.start_scanning_dialog,callback:function(e){t.start_scanning_dialog=e},expression:"start_scanning_dialog"}},[n("v-card",{staticClass:"pa-4"},[n("v-card-title",{},[t._v(" Start Scanning Area ")]),n("v-card-text",[t._v(" you can start scanning the sorrounding area by navigating arount the robot manually "),n("br"),t._v(" Start Scanning? ")]),n("v-divider"),n("v-card-actions",[n("v-btn",{attrs:{color:"purple",text:""},on:{click:function(e){t.start_scanning(),t.start_scanning_dialog=!1}}},[t._v(" Yes ")]),n("v-spacer"),n("v-btn",{attrs:{color:"purple",text:""},on:{click:function(e){t.start_scanning_dialog=!1}}},[t._v(" Not Yet ")])],1)],1)],1)],1)],1)],1)],1)},a=[],o={computed:{isDark:function(){return this.$store.getters["Theme/isDark"]}},data:function(){return{continue_loading:!1,cancel_dialog:!1,start_scanning_dialog:!1}},methods:{start_scanning:function(){var t=this;console.log("Where There is Will there is Way"),this.$store.dispatch("Ros/take_action","startup/remote_interface",{root:!0}).then((function(e){"slam_start_scanning"==e&&(t.continue_loading=!0,console.log(e),t.$store.dispatch("Ros/take_action","startup/perform/slam/confirm/yes",{root:!0}).then((function(t){console.log(t)})))}))},cancel:function(){var t=this;console.log("Where There is Will there is Way"),this.$store.dispatch("Ros/take_action","startup/remote_interface",{root:!0}).then((function(e){"slam_start_scanning"==e&&(console.log(e),t.$store.dispatch("Ros/take_action","startup/perform/slam/confirm/end",{root:!0}).then((function(e){console.log(e),t.$router.push({name:"startup_loading"})})))}))}}},c=o,s=(n("af12"),n("2877")),r=n("6544"),l=n.n(r),u=n("8336"),d=n("b0af"),f=n("99d9"),h=n("62ad"),v=n("a523"),g=n("169a"),p=n("ce7e"),b=n("0fd9"),m=n("2fa4"),y=Object(s["a"])(c,i,a,!1,null,"4d6febce",null);e["default"]=y.exports;l()(y,{VBtn:u["a"],VCard:d["a"],VCardActions:f["a"],VCardText:f["b"],VCardTitle:f["c"],VCol:h["a"],VContainer:v["a"],VDialog:g["a"],VDivider:p["a"],VRow:b["a"],VSpacer:m["a"]})},"62ad":function(t,e,n){"use strict";var i=n("ade3"),a=n("5530"),o=(n("a9e3"),n("b64b"),n("ac1f"),n("5319"),n("4ec9"),n("d3b7"),n("3ca3"),n("ddb0"),n("caad"),n("159b"),n("2ca0"),n("4b85"),n("2b0e")),c=n("d9f7"),s=n("80d2"),r=["sm","md","lg","xl"],l=function(){return r.reduce((function(t,e){return t[e]={type:[Boolean,String,Number],default:!1},t}),{})}(),u=function(){return r.reduce((function(t,e){return t["offset"+Object(s["G"])(e)]={type:[String,Number],default:null},t}),{})}(),d=function(){return r.reduce((function(t,e){return t["order"+Object(s["G"])(e)]={type:[String,Number],default:null},t}),{})}(),f={col:Object.keys(l),offset:Object.keys(u),order:Object.keys(d)};function h(t,e,n){var i=t;if(null!=n&&!1!==n){if(e){var a=e.replace(t,"");i+="-".concat(a)}return"col"!==t||""!==n&&!0!==n?(i+="-".concat(n),i.toLowerCase()):i.toLowerCase()}}var v=new Map;e["a"]=o["default"].extend({name:"v-col",functional:!0,props:Object(a["a"])(Object(a["a"])(Object(a["a"])(Object(a["a"])({cols:{type:[Boolean,String,Number],default:!1}},l),{},{offset:{type:[String,Number],default:null}},u),{},{order:{type:[String,Number],default:null}},d),{},{alignSelf:{type:String,default:null,validator:function(t){return["auto","start","end","center","baseline","stretch"].includes(t)}},tag:{type:String,default:"div"}}),render:function(t,e){var n=e.props,a=e.data,o=e.children,s=(e.parent,"");for(var r in n)s+=String(n[r]);var l=v.get(s);return l||function(){var t,e;for(e in l=[],f)f[e].forEach((function(t){var i=n[t],a=h(e,t,i);a&&l.push(a)}));var a=l.some((function(t){return t.startsWith("col-")}));l.push((t={col:!a||!n.cols},Object(i["a"])(t,"col-".concat(n.cols),n.cols),Object(i["a"])(t,"offset-".concat(n.offset),n.offset),Object(i["a"])(t,"order-".concat(n.order),n.order),Object(i["a"])(t,"align-self-".concat(n.alignSelf),n.alignSelf),t)),v.set(s,l)}(),t(n.tag,Object(c["a"])(a,{class:l}),o)}})},"8e54":function(t,e,n){},af12:function(t,e,n){"use strict";n("8e54")}}]);
//# sourceMappingURL=startup_slam_start_scanning.82657c60.js.map