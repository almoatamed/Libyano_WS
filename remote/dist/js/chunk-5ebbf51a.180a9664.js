(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-5ebbf51a"],{"0fd9":function(t,o,e){"use strict";var s=e("ade3"),i=e("5530"),n=(e("caad"),e("2532"),e("99af"),e("b64b"),e("ac1f"),e("5319"),e("4ec9"),e("d3b7"),e("3ca3"),e("ddb0"),e("159b"),e("4b85"),e("2b0e")),a=e("d9f7"),r=e("80d2"),c=["sm","md","lg","xl"],l=["start","end","center"];function d(t,o){return c.reduce((function(e,s){return e[t+Object(r["G"])(s)]=o(),e}),{})}var _=function(t){return[].concat(l,["baseline","stretch"]).includes(t)},u=d("align",(function(){return{type:String,default:null,validator:_}})),y=function(t){return[].concat(l,["space-between","space-around"]).includes(t)},v=d("justify",(function(){return{type:String,default:null,validator:y}})),f=function(t){return[].concat(l,["space-between","space-around","stretch"]).includes(t)},h=d("alignContent",(function(){return{type:String,default:null,validator:f}})),g={align:Object.keys(u),justify:Object.keys(v),alignContent:Object.keys(h)},b={align:"align",justify:"justify",alignContent:"align-content"};function p(t,o,e){var s=b[t];if(null!=e){if(o){var i=o.replace(t,"");s+="-".concat(i)}return s+="-".concat(e),s.toLowerCase()}}var m=new Map;o["a"]=n["default"].extend({name:"v-row",functional:!0,props:Object(i["a"])(Object(i["a"])(Object(i["a"])({tag:{type:String,default:"div"},dense:Boolean,noGutters:Boolean,align:{type:String,default:null,validator:_}},u),{},{justify:{type:String,default:null,validator:y}},v),{},{alignContent:{type:String,default:null,validator:f}},h),render:function(t,o){var e=o.props,i=o.data,n=o.children,r="";for(var c in e)r+=String(e[c]);var l=m.get(r);return l||function(){var t,o;for(o in l=[],g)g[o].forEach((function(t){var s=e[t],i=p(o,t,s);i&&l.push(i)}));l.push((t={"no-gutters":e.noGutters,"row--dense":e.dense},Object(s["a"])(t,"align-".concat(e.align),e.align),Object(s["a"])(t,"justify-".concat(e.justify),e.justify),Object(s["a"])(t,"align-content-".concat(e.alignContent),e.alignContent),t)),m.set(r,l)}(),t(e.tag,Object(a["a"])(i,{staticClass:"row",class:l}),n)}})},"169a":function(t,o,e){"use strict";var s=e("5530"),i=e("2909"),n=e("ade3"),a=(e("a9e3"),e("498a"),e("caad"),e("2532"),e("7db0"),e("368e"),e("480e")),r=e("4ad4"),c=e("b848"),l=e("75eb"),d=e("e707"),_=e("e4d3"),u=e("21be"),y=e("f2e7"),v=e("a293"),f=e("58df"),h=e("d9bd"),g=e("80d2"),b=Object(f["a"])(r["a"],c["a"],l["a"],d["a"],_["a"],u["a"],y["a"]);o["a"]=b.extend({name:"v-dialog",directives:{ClickOutside:v["a"]},props:{dark:Boolean,disabled:Boolean,fullscreen:Boolean,light:Boolean,maxWidth:{type:[String,Number],default:"none"},noClickAnimation:Boolean,origin:{type:String,default:"center center"},persistent:Boolean,retainFocus:{type:Boolean,default:!0},scrollable:Boolean,transition:{type:[String,Boolean],default:"dialog-transition"},width:{type:[String,Number],default:"auto"}},data:function(){return{activatedBy:null,animate:!1,animateTimeout:-1,isActive:!!this.value,stackMinZIndex:200,previousActiveElement:null}},computed:{classes:function(){var t;return t={},Object(n["a"])(t,"v-dialog ".concat(this.contentClass).trim(),!0),Object(n["a"])(t,"v-dialog--active",this.isActive),Object(n["a"])(t,"v-dialog--persistent",this.persistent),Object(n["a"])(t,"v-dialog--fullscreen",this.fullscreen),Object(n["a"])(t,"v-dialog--scrollable",this.scrollable),Object(n["a"])(t,"v-dialog--animated",this.animate),t},contentClasses:function(){return{"v-dialog__content":!0,"v-dialog__content--active":this.isActive}},hasActivator:function(){return Boolean(!!this.$slots.activator||!!this.$scopedSlots.activator)}},watch:{isActive:function(t){var o;t?(this.show(),this.hideScroll()):(this.removeOverlay(),this.unbind(),null==(o=this.previousActiveElement)||o.focus())},fullscreen:function(t){this.isActive&&(t?(this.hideScroll(),this.removeOverlay(!1)):(this.showScroll(),this.genOverlay()))}},created:function(){this.$attrs.hasOwnProperty("full-width")&&Object(h["e"])("full-width",this)},beforeMount:function(){var t=this;this.$nextTick((function(){t.isBooted=t.isActive,t.isActive&&t.show()}))},beforeDestroy:function(){"undefined"!==typeof window&&this.unbind()},methods:{animateClick:function(){var t=this;this.animate=!1,this.$nextTick((function(){t.animate=!0,window.clearTimeout(t.animateTimeout),t.animateTimeout=window.setTimeout((function(){return t.animate=!1}),150)}))},closeConditional:function(t){var o=t.target;return!(this._isDestroyed||!this.isActive||this.$refs.content.contains(o)||this.overlay&&o&&!this.overlay.$el.contains(o))&&this.activeZIndex>=this.getMaxZIndex()},hideScroll:function(){this.fullscreen?document.documentElement.classList.add("overflow-y-hidden"):d["a"].options.methods.hideScroll.call(this)},show:function(){var t=this;!this.fullscreen&&!this.hideOverlay&&this.genOverlay(),this.$nextTick((function(){t.$nextTick((function(){t.previousActiveElement=document.activeElement,t.$refs.content.focus(),t.bind()}))}))},bind:function(){window.addEventListener("focusin",this.onFocusin)},unbind:function(){window.removeEventListener("focusin",this.onFocusin)},onClickOutside:function(t){this.$emit("click:outside",t),this.persistent?this.noClickAnimation||this.animateClick():this.isActive=!1},onKeydown:function(t){if(t.keyCode===g["y"].esc&&!this.getOpenDependents().length)if(this.persistent)this.noClickAnimation||this.animateClick();else{this.isActive=!1;var o=this.getActivator();this.$nextTick((function(){return o&&o.focus()}))}this.$emit("keydown",t)},onFocusin:function(t){if(t&&this.retainFocus){var o=t.target;if(o&&![document,this.$refs.content].includes(o)&&!this.$refs.content.contains(o)&&this.activeZIndex>=this.getMaxZIndex()&&!this.getOpenDependentElements().some((function(t){return t.contains(o)}))){var e=this.$refs.content.querySelectorAll('button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'),s=Object(i["a"])(e).find((function(t){return!t.hasAttribute("disabled")}));s&&s.focus()}}},genContent:function(){var t=this;return this.showLazyContent((function(){return[t.$createElement(a["a"],{props:{root:!0,light:t.light,dark:t.dark}},[t.$createElement("div",{class:t.contentClasses,attrs:Object(s["a"])({role:"document",tabindex:t.isActive?0:void 0},t.getScopeIdAttrs()),on:{keydown:t.onKeydown},style:{zIndex:t.activeZIndex},ref:"content"},[t.genTransition()])])]}))},genTransition:function(){var t=this.genInnerContent();return this.transition?this.$createElement("transition",{props:{name:this.transition,origin:this.origin,appear:!0}},[t]):t},genInnerContent:function(){var t={class:this.classes,ref:"dialog",directives:[{name:"click-outside",value:{handler:this.onClickOutside,closeConditional:this.closeConditional,include:this.getOpenDependentElements}},{name:"show",value:this.isActive}],style:{transformOrigin:this.origin}};return this.fullscreen||(t.style=Object(s["a"])(Object(s["a"])({},t.style),{},{maxWidth:"none"===this.maxWidth?void 0:Object(g["g"])(this.maxWidth),width:"auto"===this.width?void 0:Object(g["g"])(this.width)})),this.$createElement("div",t,this.getContentSlot())}},render:function(t){return t("div",{staticClass:"v-dialog__container",class:{"v-dialog__container--attached":""===this.attach||!0===this.attach||"attach"===this.attach},attrs:{role:"dialog"}},[this.genActivator(),this.genContent()])}})},"368e":function(t,o,e){},"62ad":function(t,o,e){"use strict";var s=e("ade3"),i=e("5530"),n=(e("a9e3"),e("b64b"),e("ac1f"),e("5319"),e("4ec9"),e("d3b7"),e("3ca3"),e("ddb0"),e("caad"),e("159b"),e("2ca0"),e("4b85"),e("2b0e")),a=e("d9f7"),r=e("80d2"),c=["sm","md","lg","xl"],l=function(){return c.reduce((function(t,o){return t[o]={type:[Boolean,String,Number],default:!1},t}),{})}(),d=function(){return c.reduce((function(t,o){return t["offset"+Object(r["G"])(o)]={type:[String,Number],default:null},t}),{})}(),_=function(){return c.reduce((function(t,o){return t["order"+Object(r["G"])(o)]={type:[String,Number],default:null},t}),{})}(),u={col:Object.keys(l),offset:Object.keys(d),order:Object.keys(_)};function y(t,o,e){var s=t;if(null!=e&&!1!==e){if(o){var i=o.replace(t,"");s+="-".concat(i)}return"col"!==t||""!==e&&!0!==e?(s+="-".concat(e),s.toLowerCase()):s.toLowerCase()}}var v=new Map;o["a"]=n["default"].extend({name:"v-col",functional:!0,props:Object(i["a"])(Object(i["a"])(Object(i["a"])(Object(i["a"])({cols:{type:[Boolean,String,Number],default:!1}},l),{},{offset:{type:[String,Number],default:null}},d),{},{order:{type:[String,Number],default:null}},_),{},{alignSelf:{type:String,default:null,validator:function(t){return["auto","start","end","center","baseline","stretch"].includes(t)}},tag:{type:String,default:"div"}}),render:function(t,o){var e=o.props,i=o.data,n=o.children,r=(o.parent,"");for(var c in e)r+=String(e[c]);var l=v.get(r);return l||function(){var t,o;for(o in l=[],u)u[o].forEach((function(t){var s=e[t],i=y(o,t,s);i&&l.push(i)}));var i=l.some((function(t){return t.startsWith("col-")}));l.push((t={col:!i||!e.cols},Object(s["a"])(t,"col-".concat(e.cols),e.cols),Object(s["a"])(t,"offset-".concat(e.offset),e.offset),Object(s["a"])(t,"order-".concat(e.order),e.order),Object(s["a"])(t,"align-self-".concat(e.alignSelf),e.alignSelf),t)),v.set(r,l)}(),t(e.tag,Object(a["a"])(i,{class:l}),n)}})},7679:function(t,o,e){"use strict";e("9b44")},"9b44":function(t,o,e){},deb7:function(t,o,e){"use strict";e.r(o);var s=function(){var t=this,o=t.$createElement,e=t._self._c||o;return e("div",{attrs:{id:"root"}},[e("v-dialog",{attrs:{scrollable:"",persistent:"",overlay:!1,"max-width":"500px",transition:"dialog-transition"},model:{value:t.story_obj.new_story_dialog.show,callback:function(o){t.$set(t.story_obj.new_story_dialog,"show",o)},expression:"story_obj.new_story_dialog.show"}},[e("v-card",{staticClass:"pa-2",attrs:{elevation:"6",dark:t.isDark}},[e("v-container",{attrs:{fluid:""}},[e("v-row",[e("v-col",{attrs:{cols:"12"}},[e("v-container",[e("v-text-field",{attrs:{type:"text",label:"Story Name"},model:{value:t.story_obj.new_story_dialog.name,callback:function(o){t.$set(t.story_obj.new_story_dialog,"name",o)},expression:"story_obj.new_story_dialog.name"}})],1),e("v-divider",{staticClass:"py-2"}),e("v-container",[e("v-row",[e("v-btn",{attrs:{text:"",icon:""},on:{click:function(o){t.story_obj.new_story_dialog.show=!1}}},[e("v-icon",[t._v("mdi-close")])],1),e("v-spacer"),e("v-btn",{attrs:{text:"",icon:""},on:{click:t.create_story}},[e("v-icon",[t._v("mdi-plus")])],1)],1)],1)],1)],1)],1)],1)],1),e("v-dialog",{attrs:{scrollable:"",fullscreen:"",persistent:"",overlay:!1,transition:"dialog-transition"},model:{value:t.story_obj.edit_story_dialog.show,callback:function(o){t.$set(t.story_obj.edit_story_dialog,"show",o)},expression:"story_obj.edit_story_dialog.show"}},[e("v-card",{staticClass:"pa-2",attrs:{dark:t.isDark}},[e("v-card-actions",[e("v-container",{attrs:{fluid:""}},[e("v-row",[e("span",{staticClass:"text-h6"},[t._v(t._s(t.story_obj.edit_story_dialog.story["name"]))]),e("v-spacer"),e("v-btn",{attrs:{text:"",icon:""},on:{click:function(o){t.story_obj.edit_story_dialog.show=!1}}},[e("v-icon",[t._v("mdi-close")])],1)],1),e("v-row",[e("v-divider")],1)],1)],1),e("v-card-text",[e("v-container",{attrs:{fluid:""}},[e("v-row",[e("v-col",{attrs:{cols:"12"}},[e("v-container",{style:"outline:solid "+(t.isDark?"rgba(255,255,255,0.2)":"rgba(0,0,0,0.2)")+" 1px; padding:20px",attrs:{fluid:""}},[e("v-row",[t._v(" Repetition Count ")]),e("v-row",[e("v-text-field",{attrs:{label:"Count",type:"number"},model:{value:t.story_obj.edit_story_dialog.story.count,callback:function(o){t.$set(t.story_obj.edit_story_dialog.story,"count",o)},expression:"story_obj.edit_story_dialog.story.count"}})],1),e("v-row",[e("span",{staticStyle:{"font-size":"14px"}},[t._v(" Chose the number of time this story is supposed to be played (if 0 is chosen then the story will continue playing indefinetly). ")])])],1)],1)],1),e("v-row",[e("v-divider")],1),e("v-row",[e("v-col",{attrs:{cols:"12"}},[e("v-container",{style:"outline:solid "+(t.isDark?"rgba(255,255,255,0.2)":"rgba(0,0,0,0.2)")+" 1px; padding:20px",attrs:{fluid:""}},[e("v-row",[t._v(" End Action ")]),e("v-row",[e("v-col",{attrs:{cols:"12"}},[e("v-container",{style:"outline:solid                      "+(t.isDark?"rgba(255,255,255,0.2)":"rgba(0,0,0,0.2)")+"                     1px;                     padding:20px"},t._l(t.story_obj.stories["end_actions"],(function(o,s){return e("v-row",{key:s,class:(t.story_obj.edit_story_dialog.story.end_action==o?"success":"")+" "+(t.isDark?"outline_dark":"outline"),on:{click:function(e){return t.select_end_action(o)}}},[t._v(" "+t._s(o)+" ")])})),1)],1)],1),e("v-row",[e("span",{staticStyle:{"font-size":"14px"}},[t._v(" The action to be performed after finishing the Story. ")])])],1)],1)],1),e("v-row",[e("v-divider")],1),e("v-row",[e("v-col",{attrs:{cols:"12"}},[e("v-container",{style:"outline:solid "+(t.isDark?"rgba(255,255,255,0.2)":"rgba(0,0,0,0.2)")+" 1px; padding:20px",attrs:{fluid:""}},[e("v-row",[t._v(" Acts")]),e("v-row",[e("v-spacer"),e("v-btn",{directives:[{name:"show",rawName:"v-show",value:"left"==t.story_obj.edit_story_dialog.selected_act.side&&(""!=t.story_obj.edit_story_dialog.selected_act.act_name||null!=t.story_obj.edit_story_dialog.selected_act.index),expression:"\n                      story_obj.edit_story_dialog.selected_act.side ==\n                        'left' &&\n                      (story_obj.edit_story_dialog.selected_act.act_name !=\n                        '' ||\n                        story_obj.edit_story_dialog.selected_act.index !=\n                          null)\n                    "}],attrs:{color:"primary",icon:"",text:""},on:{click:t.add_selected_act}},[e("v-icon",[t._v("mdi-plus")])],1),e("v-btn",{directives:[{name:"show",rawName:"v-show",value:"right"==t.story_obj.edit_story_dialog.selected_act.side&&(""!=t.story_obj.edit_story_dialog.selected_act.act_name||null!=t.story_obj.edit_story_dialog.selected_act.index),expression:"\n                      story_obj.edit_story_dialog.selected_act.side ==\n                        'right' &&\n                      (story_obj.edit_story_dialog.selected_act.act_name !=\n                        '' ||\n                        story_obj.edit_story_dialog.selected_act.index !=\n                          null)\n                    "}],attrs:{color:"primary",icon:"",text:""},on:{click:t.delete_selected_act}},[e("v-icon",[t._v("mdi-delete")])],1),e("v-spacer")],1),e("v-row",[e("v-col",{attrs:{cols:"6"}},[e("v-container",{style:"\n                        outline:                          solid                           "+(t.isDark?"rgba(255,255,255,0.2)":"rgba(0,0,0,0.2)")+"                           1px;                        overflow-y:auto;                        max-height:350px;\n                        "},t._l(t.story_obj.available_acts,(function(o,s){return e("v-row",{key:s,class:("left"==t.story_obj.edit_story_dialog.selected_act.side&&t.story_obj.edit_story_dialog.selected_act.act_name==o?"success":"")+" "+(t.isDark?"outline_dark":"outline"),on:{click:function(e){return t.select_act_from_edit_story_dialog(o,"left")}}},[t._v(" "+t._s(o)+" ")])})),1)],1),e("v-col",{attrs:{cols:"6"}},[e("v-container",{style:"\n                        outline:                          solid                          "+(t.isDark?"rgba(255,255,255,0.2)":"rgba(0,0,0,0.2)")+"                          1px; \n                        overflow-y:auto;                        max-height:350px;\n                        "},t._l(t.story_obj.edit_story_dialog.story.acts,(function(o,s){return e("v-row",{key:s,class:("right"==t.story_obj.edit_story_dialog.selected_act.side&&t.story_obj.edit_story_dialog.selected_act.index==s?"success":"")+" "+(t.isDark?"outline_dark":"outline"),on:{click:function(o){return t.select_act_from_edit_story_dialog(s,"right")}}},[t._v(" "+t._s(o)+" ")])})),1)],1)],1)],1)],1)],1)],1)],1),e("v-card-actions",[e("v-container",{attrs:{fluid:""}},[e("v-row",[e("v-divider")],1),e("v-row",[e("v-spacer"),e("v-btn",{attrs:{text:"",icon:"",disabled:t.story_obj.edit_story_dialog.buttons.save_button.disabled,loading:t.story_obj.edit_story_dialog.buttons.save_button.loading},on:{click:t.save_edited_story}},[e("v-icon",[t._v("mdi-content-save")])],1)],1)],1)],1)],1)],1),e("v-dialog",{attrs:{scrollable:"",persistent:"",overlay:!1,"max-width":"500px",transition:"dialog-transition"},model:{value:t.story_obj.set_default_story_dialog.show,callback:function(o){t.$set(t.story_obj.set_default_story_dialog,"show",o)},expression:"story_obj.set_default_story_dialog.show"}},[e("v-card",{staticClass:"pa-2",attrs:{elevation:"6",dark:t.isDark}},[e("v-container",{attrs:{fluid:""}},[e("v-row",[e("v-col",{attrs:{cols:"12"}},[e("v-container",[e("v-row",[e("div",{staticClass:"text-h6"},[t._v("Stories")]),e("v-spacer"),e("div",{staticClass:"text-h6"},[t._v(" "+t._s(t.story_obj.stories["default_story"])+" ")]),e("v-spacer"),e("v-btn",{attrs:{text:"",icon:""},on:{click:function(o){t.story_obj.set_default_story_dialog.show=!1}}},[e("v-icon",[t._v("mdi-close")])],1)],1),e("v-row",[e("v-divider",{staticClass:"py-2"})],1),t.stories_array.length>0?e("v-row",[e("v-col",{attrs:{cols:"12"}},[e("v-container",{style:"\n                        outline:                          solid                           "+(t.isDark?"rgba(255,255,255,0.2)":"rgba(0,0,0,0.2)")+"                           1px;                        overflow-y:auto;                        max-height:350px;\n                        "},t._l(t.stories_array,(function(o,s){return e("v-row",{key:s,class:t.story_obj.set_default_story_dialog.story_name==o["name"]?"success":"",style:"\n                        outline:                          solid                           "+(t.isDark?"rgba(255,255,255,0.2)":"rgba(0,0,0,0.2)")+"                           1px;                        overflow-y:auto;                        max-height:350px;\n                        ",on:{click:function(e){t.story_obj.set_default_story_dialog.story_name=o["name"]}}},[e("v-spacer"),e("span",[t._v(" "+t._s(o["name"])+" ")]),e("v-spacer")],1)})),1)],1)],1):e("v-row",[e("span",[t._v("There is no Stories")])]),e("v-row",[e("v-divider",{staticClass:"mt-2"})],1),e("v-row",[e("v-spacer"),e("v-btn",{attrs:{disabled:t.story_obj.set_default_story_dialog.buttons.set.disabled,laoding:t.story_obj.set_default_story_dialog.buttons.set.laoding,text:"",icon:""},on:{click:t.set_selected_default_story}},[e("v-icon",[t._v("mdi-content-save")])],1)],1)],1)],1)],1)],1)],1)],1),e("v-container",[e("div",{staticClass:"text-h4"},[t._v("Story Manager")]),e("v-divider",{staticClass:"py-4"}),e("v-card",{staticClass:"pa-2",attrs:{elevation:"6",dark:t.isDark}},[e("v-container",{attrs:{fluid:""}},[e("v-row",[e("v-col",{attrs:{cols:"12"}},[e("v-container",[e("v-row",[e("div",{staticClass:"text-h6"},[t._v("Stories")]),e("v-spacer"),e("div",{staticClass:"text-h6"},[t._v(" "+t._s(t.story_obj.stories["default_story"])+" ")]),e("v-spacer"),e("v-btn",{attrs:{text:"",icon:""},on:{click:t.set_default_story}},[e("v-icon",[t._v("mdi-book-check")])],1),e("v-btn",{attrs:{text:"",icon:""},on:{click:t.new_story}},[e("v-icon",[t._v("mdi-plus")])],1)],1)],1),e("v-divider")],1),e("v-col",{attrs:{cols:"12"}},[t.stories_array.length>0?e("v-container",t._l(t.stories_array,(function(o,s){return e("v-row",{key:s},[e("span",[t._v(t._s(s))]),e("v-spacer"),e("v-spacer"),e("span",{staticStyle:{"font-size":"18px"}},[t._v(" "+t._s(o.name)+" ")]),e("v-spacer"),e("v-btn",{attrs:{text:"",icon:""},on:{click:function(e){return t.edit_story(o)}}},[e("v-icon",[t._v("mdi-pencil")])],1),e("v-btn",{attrs:{text:"",icon:""},on:{click:function(e){return t.del_story(o.name)}}},[e("v-icon",[t._v("mdi-delete")])],1)],1)})),1):e("v-container",{staticStyle:{display:"flex","justify-content":"space-around"}},[e("span",[t._v(" No Stories ")])])],1)],1)],1)],1)],1)],1)},i=[],n=e("5530"),a=(e("07ac"),e("ac1f"),e("1276"),e("b0c0"),e("a434"),e("2f62")),r={data:function(){return{story_obj:{default_story:{name:"",acts:[],end_action:"",count:0},available_acts:[],stories:{end_actions:[],stories:{},default_story:""},new_story_dialog:{show:!1,name:""},set_default_story_dialog:{buttons:{set:{disabled:!1,loading:!1}},show:!1,story_name:""},edit_story_dialog:{buttons:{save_button:{loading:!1,disabled:!1}},show:!1,selected_act:{side:"",act_name:"",index:""},story:{name:"",acts:[],end_action:"",count:0}}}}},computed:Object(n["a"])(Object(n["a"])({},Object(a["b"])("Theme",["isDark"])),{},{stories_array:function(){return this.story_obj.stories["stories"]?Object.values(this.story_obj.stories["stories"]):[]}}),created:function(){var t=this;this.$store.dispatch("Ros/take_action","operation/get_stories",{root:!0}).then((function(o){console.log(o),t.story_obj.stories=JSON.parse(o),console.log(t.story_obj.stories)})),this.$store.dispatch("Ros/take_action","act/get_acts_names",{root:!0}).then((function(o){t.story_obj.available_acts=o.split("|").sort(),console.log(t.story_obj.available_acts)}))},methods:{create_story:function(){console.log("creating story",this.story_obj.new_story_dialog.name),""!=this.story_obj.new_story_dialog.name&&(this.story_obj.edit_story_dialog.story=JSON.parse(JSON.stringify(this.story_obj.default_story)),this.story_obj.edit_story_dialog.story.name=this.story_obj.new_story_dialog.name,this.story_obj.new_story_dialog.show=!1,this.story_obj.edit_story_dialog.show=!0)},new_story:function(){this.story_obj.new_story_dialog.name="",this.story_obj.new_story_dialog.show=!0},select_end_action:function(t){this.story_obj.stories["end_actions"].some((function(o){return o==t}))&&(this.story_obj.edit_story_dialog.story.end_action=t)},select_act_from_edit_story_dialog:function(t,o){console.log(t,o),"right"==o?(this.story_obj.edit_story_dialog.selected_act.side=o,this.story_obj.edit_story_dialog.selected_act.index=t):(this.story_obj.edit_story_dialog.selected_act.side=o,this.story_obj.edit_story_dialog.selected_act.act_name=t)},add_selected_act:function(){var t=this;console.log("adding selected act",this.story_obj.available_acts.some((function(o){return o==t.story_obj.edit_story_dialog.selected_act.act_name})),"left"==this.story_obj.edit_story_dialog.selected_act.side),this.story_obj.available_acts.some((function(o){return o==t.story_obj.edit_story_dialog.selected_act.act_name}))&&"left"==this.story_obj.edit_story_dialog.selected_act.side&&this.story_obj.edit_story_dialog.story.acts.push(this.story_obj.edit_story_dialog.selected_act.act_name)},delete_selected_act:function(){"right"==this.story_obj.edit_story_dialog.selected_act.side&&this.story_obj.edit_story_dialog.selected_act.index<this.story_obj.edit_story_dialog.story.acts.length&&this.story_obj.edit_story_dialog.story.acts.splice(this.story_obj.edit_story_dialog.selected_act.index,1)},save_edited_story:function(){var t=this;if(""!=this.story_obj.edit_story_dialog.story["name"])if(this.story_obj.edit_story_dialog.story["acts"].length<1)this.$store.dispatch("Notify/notify",{group:"main",text:"Story Should have a valid number of acts.",title:"no acts added",type:"warning"},{root:!0});else if(this.story_obj.stories["end_actions"].some((function(o){return o==t.story_obj.edit_story_dialog.story["end_action"]})))if(this.story_obj.edit_story_dialog.story["count"]<0||this.story_obj.edit_story_dialog.story["count"]>100)this.$store.dispatch("Notify/notify",{group:"main",text:"Story Should have a valid repetition count.",title:"not a valid repetition count (0-100)",type:"warning"},{root:!0});else{this.story_obj.edit_story_dialog.buttons.save_button.disabled=!0,this.story_obj.edit_story_dialog.buttons.save_button.loading=!0;var o=JSON.stringify(this.story_obj.edit_story_dialog.story);console.log(o),this.$store.dispatch("Ros/take_action","operation/add_story/".concat(o)).then((function(o){t.story_obj.edit_story_dialog.buttons.save_button.disabled=!1,t.story_obj.edit_story_dialog.buttons.save_button.loading=!1,"story_controller_is_running"==o?t.$store.dispatch("Notify/notify",{group:"main",text:"Automation mode is runing, please stop the automation mode before attempting to add story",title:"Unautharized",type:"warning"},{root:!0}):(console.log("story have been saved",o),t.$store.dispatch("Notify/notify",{group:"main",text:"story is saved successfully",title:"Story has been saved",type:"success"},{root:!0}),t.$store.dispatch("Ros/take_action","operation/get_stories",{root:!0}).then((function(o){console.log(o),t.story_obj.stories=JSON.parse(o),console.log(t.story_obj.stories),t.story_obj.edit_story_dialog.show=!1})))})).catch((function(o){console.log("Error while saving story",o),t.$store.dispatch("Notify/notify",{group:"main",text:"Error occured while saving story",title:"Error saving story",type:"error"},{root:!0})}))}else this.$store.dispatch("Notify/notify",{group:"main",text:"Story Should have an End Action",title:"no end action",type:"warning"},{root:!0});else this.$store.dispatch("Notify/notify",{group:"main",text:"Story Should have a name.",title:"Not a valid Name",type:"warning"},{root:!0})},edit_story:function(t){this.story_obj.edit_story_dialog.story=JSON.parse(JSON.stringify(t)),this.story_obj.edit_story_dialog.show=!0},del_story:function(t){var o=this;this.$store.dispatch("Ros/take_action","operation/del_story/".concat(JSON.stringify({name:t})),{root:!0}).then((function(t){console.log("finished deleting story ",t),"story_controller_is_running"==t?o.$store.dispatch("Notify/notify",{group:"main",text:"Automation mode is runing, please stop the automation mode before attempting to delete story",title:"Unautharized",type:"warning"},{root:!0}):o.$store.dispatch("Ros/take_action","operation/get_stories",{root:!0}).then((function(t){o.$store.dispatch("Notify/notify",{group:"main",text:"Story has been deleted",title:"Story Deleted",type:"secondary"},{root:!0}),console.log(t),o.story_obj.stories=JSON.parse(t),console.log(o.story_obj.stories)}))})).catch((function(t){console.log("Error while Deleting story",t),o.$store.dispatch("Notify/notify",{group:"main",text:"Error occured while deleting story",title:"Error deleting story",type:"error"},{root:!0})}))},set_default_story:function(){this.story_obj.set_default_story_dialog.story_name="",this.story_obj.set_default_story_dialog.show=!0},set_selected_default_story:function(){var t=this;""==this.story_obj.set_default_story_dialog.story_name?this.$store.dispatch("Notify/notify",{group:"main",text:"Select a story to be set as defaults",title:"No story is selected",type:"warning"},{root:!0}):(this.story_obj.set_default_story_dialog.buttons.set.disabled=!0,this.story_obj.set_default_story_dialog.buttons.set.loading=!0,this.$store.dispatch("Ros/take_action","operation/set_default_story/".concat(this.story_obj.set_default_story_dialog.story_name),{root:!0}).then((function(o){t.story_obj.set_default_story_dialog.buttons.set.disabled=!1,t.story_obj.set_default_story_dialog.buttons.set.loading=!1,"story_controller_is_running"==o?t.$store.dispatch("Notify/notify",{group:"main",text:"Automation mode is runing, please stop the automation mode before attempting to set default story",title:"Unautharized",type:"warning"},{root:!0}):"story_not_found"==o?t.$store.dispatch("Notify/notify",{group:"main",text:"Story name is not found",title:"Story is not found",type:"error"},{root:!0}):(t.story_obj.set_default_story_dialog.show=!1,t.$store.dispatch("Notify/notify",{group:"main",text:"Default story is changed to ".concat(t.story_obj.set_default_story_dialog.story_name),title:"Default story is changed ",type:"success"},{root:!0}),t.$store.dispatch("Ros/take_action","operation/get_stories",{root:!0}).then((function(o){console.log(o),t.story_obj.stories=JSON.parse(o),console.log(t.story_obj.stories)})))})).catch((function(o){console.log("error occured while trying to set default story",o),t.story_obj.set_default_story_dialog.buttons.set.disabled=!1,t.story_obj.set_default_story_dialog.buttons.set.loading=!1,t.$store.dispatch("Notify/notify",{group:"main",text:"error occured while trying to set default story ".concat(o),title:"Default story error ",type:"error"},{root:!0})})))}}},c=r,l=(e("7679"),e("2877")),d=e("6544"),_=e.n(d),u=e("8336"),y=e("b0af"),v=e("99d9"),f=e("62ad"),h=e("a523"),g=e("169a"),b=e("ce7e"),p=e("132d"),m=e("0fd9"),j=e("2fa4"),w=e("8654"),x=Object(l["a"])(c,s,i,!1,null,"8888077e",null);o["default"]=x.exports;_()(x,{VBtn:u["a"],VCard:y["a"],VCardActions:v["a"],VCardText:v["b"],VCol:f["a"],VContainer:h["a"],VDialog:g["a"],VDivider:b["a"],VIcon:p["a"],VRow:m["a"],VSpacer:j["a"],VTextField:w["a"]})}}]);
//# sourceMappingURL=chunk-5ebbf51a.180a9664.js.map