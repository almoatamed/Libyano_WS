(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["Startup_loading_existing_map"],{3015:function(t,a,i){"use strict";i.r(a);var e=function(){var t=this,a=t.$createElement,i=t._self._c||a;return i("div",{staticClass:"loading",staticStyle:{display:"grid","place-items":"center"}},[i("v-container",{attrs:{fluid:""}},[t.items.length?i("v-card",{staticClass:"mx-auto",attrs:{"max-width":"400",dark:t.isDark,rounded:"lg"}},[i("v-list",[i("v-list-item-group",{attrs:{color:"indigo"},model:{value:t.choice,callback:function(a){t.choice=a},expression:"choice"}},t._l(t.items,(function(a,e){return i("v-list-item",{key:e},[i("v-list-item-content",[i("v-list-item-title",{domProps:{textContent:t._s(a)}})],1)],1)})),1)],1),i("v-card-actions",[i("v-btn",{attrs:{color:"purple",text:""},on:{click:function(a){return t.cancel()}}},[t._v("Cancel")]),i("v-spacer"),i("v-btn",{attrs:{color:"purple",disabled:void 0===t.choice||t.loading,loading:t.loading,text:""},on:{click:function(a){return t.set_map()}}},[t._v(" Set map ")])],1)],1):i("v-card",{staticClass:"mx-auto",attrs:{"max-width":"400",dark:t.isDark}},[i("v-card-text",[t._v("There is no Maps Saved Yet")]),i("v-card-actions",[i("v-btn",{attrs:{color:"purple",text:""},on:{click:function(a){return t.cancel()}}},[t._v("Cancel")]),i("v-spacer")],1)],1)],1)],1)},n=[],o=(i("ac1f"),i("1276"),{computed:{isDark:function(){return this.$store.getters["Theme/isDark"]}},methods:{cancel:function(){var t=this;this.loading=!0,this.$store.dispatch("Ros/take_action","startup/perform/chose_existing_map/confirm/end").then((function(){t.$router.push({name:"startup_loading"})}))},set_map:function(){var t=this;this.loading=!0,console.log(this.items,this.choice,this.items[this.choice]),this.$store.dispatch("Ros/take_action","navigation/set_map/"+this.items[this.choice],{root:!0}).then((function(a){console.log("map has been synced",a),"not_found"!=a?t.$store.dispatch("Ros/take_action","startup/perform/chose_existing_map/confirm/synced").then((function(){t.$router.push({name:"startup_loading"})})):t.loading=!1}))}},data:function(){return{items:[],choice:null,loading:!1}},created:function(){var t=this;this.$store.dispatch("Ros/take_action","navigation/get_maps_names",{root:!0}).then((function(a){"no_maps"!=a&&(t.items=a.split("|"))}))},watch:{choice:function(t){console.log(t)}}}),s=o,c=(i("f2af"),i("2877")),r=i("6544"),l=i.n(r),d=i("8336"),u=i("b0af"),p=i("99d9"),h=i("a523"),m=i("8860"),f=i("da13"),v=i("5d23"),_=i("1baa"),g=i("2fa4"),k=Object(c["a"])(s,e,n,!1,null,"5bcb234e",null);a["default"]=k.exports;l()(k,{VBtn:d["a"],VCard:u["a"],VCardActions:p["a"],VCardText:p["b"],VContainer:h["a"],VList:m["a"],VListItem:f["a"],VListItemContent:v["a"],VListItemGroup:_["a"],VListItemTitle:v["b"],VSpacer:g["a"]})},"5a93":function(t,a,i){},f2af:function(t,a,i){"use strict";i("5a93")}}]);
//# sourceMappingURL=Startup_loading_existing_map.4f35e1a4.js.map