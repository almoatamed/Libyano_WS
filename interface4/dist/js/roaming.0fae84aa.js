(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["roaming"],{"1f4f":function(t,a,e){"use strict";var o=e("5530"),s=(e("a9e3"),e("8b37"),e("80d2")),r=e("7560"),i=e("58df");a["a"]=Object(i["a"])(r["a"]).extend({name:"v-simple-table",props:{dense:Boolean,fixedHeader:Boolean,height:[Number,String]},computed:{classes:function(){return Object(o["a"])({"v-data-table--dense":this.dense,"v-data-table--fixed-height":!!this.height&&!this.fixedHeader,"v-data-table--fixed-header":this.fixedHeader,"v-data-table--has-top":!!this.$slots.top,"v-data-table--has-bottom":!!this.$slots.bottom},this.themeClasses)}},methods:{genWrapper:function(){return this.$slots.wrapper||this.$createElement("div",{staticClass:"v-data-table__wrapper",style:{height:Object(s["f"])(this.height)}},[this.$createElement("table",this.$slots.default)])}},render:function(t){return t("div",{staticClass:"v-data-table",class:this.classes},[this.$slots.top,this.genWrapper(),this.$slots.bottom])}})},5160:function(t,a,e){t.exports=e.p+"img/map10.6fe1f26f.png"},"55a3":function(t,a,e){"use strict";e.r(a);var o=function(){var t=this,a=t.$createElement,o=t._self._c||a;return o("v-container",{attrs:{fluid:""}},[o("img",{staticStyle:{display:"block","margin-left":"auto","margin-right":"auto"},attrs:{src:e("5160"),usemap:"#image-map"}}),o("map",{attrs:{name:"image-map"}},[o("area",{attrs:{target:"",alt:"asia",title:"asia",coords:"628,121,649,127,709,113,799,81,824,94,908,93,1005,133,1001,143,927,187,923,172,919,161,891,165,876,177,888,182,886,198,858,225,859,238,840,223,838,232,840,249,835,265,806,274,813,290,804,300,771,275,753,281,740,308,715,272,703,264,694,270,659,293,646,273,636,250,632,231,619,226,646,215,626,204,614,181,616,162,630,148,632,128",shape:"poly"},on:{click:function(a){t.dialog3=!0}}}),o("area",{attrs:{target:"",alt:"asiaLabel",title:"asiaLabel",coords:"930,58,996,93",shape:"rect"},on:{click:function(a){t.dialog3=!0}}}),o("area",{attrs:{target:"",alt:"europe",title:"europe",coords:"618,113,595,116,579,134,565,148,565,162,580,167,566,182,552,171,545,127,541,136,535,166,527,183,531,200,543,202,529,213,530,226,548,224,568,212,585,218,605,215,615,206,606,199,599,183,596,169,605,152,618,147",shape:"poly"},on:{click:function(a){t.dialog2=!0}}}),o("area",{attrs:{target:"",alt:"europeLabel",title:"europeLabel",coords:"568,61,694,104",shape:"rect"},on:{click:function(a){t.dialog2=!0}}}),o("area",{attrs:{target:"",alt:"africa",title:"africa",coords:"539,235,577,234,619,245,627,256,637,277,647,297,663,303,665,312,655,319,650,328,646,338,646,354,667,354,670,369,661,387,642,371,632,385,612,409,596,409,575,366,582,341,573,328,568,312,531,315,510,295,508,269,521,250",shape:"poly"},on:{click:function(a){t.dialog=!0}}}),o("area",{attrs:{target:"",alt:"africaLabel",title:"africaLabel",coords:"635,401,711,427",shape:"rect"},on:{click:function(a){t.dialog=!0}}}),o("area",{attrs:{target:"",alt:"australia",title:"australia",coords:"872,323,905,337,911,347,917,386,915,407,904,425,880,410,829,411,823,387,846,369,864,351",shape:"poly"},on:{click:function(a){t.dialog7=!0}}}),o("area",{attrs:{target:"",alt:"australiaLabel",title:"australiaLabel",coords:"821,424,928,457",shape:"rect"},on:{click:function(a){t.dialog7=!0}}}),o("area",{attrs:{target:"",alt:"northamerica",title:"northamerica",coords:"169,109,237,117,277,127,309,129,326,126,341,136,331,149,327,166,347,174,358,187,362,178,364,153,375,152,383,160,392,166,397,160,418,184,424,203,408,199,400,192,399,209,355,247,358,261,343,251,324,254,317,267,326,276,339,269,350,291,360,303,352,305,320,288,298,276,275,257,249,191,217,164,185,163,163,172,154,154,149,134,152,121",shape:"poly"},on:{click:function(a){t.dialog5=!0}}}),o("area",{attrs:{target:"",alt:"northamericaLabel",title:"northamericaLabel",coords:"373,235,465,279",shape:"rect"},on:{click:function(a){t.dialog5=!0}}}),o("area",{attrs:{target:"",alt:"southamerica",title:"southamerica",coords:"367,302,382,296,464,339,454,375,438,399,443,410,424,420,405,424,388,455,390,472,380,472,366,455,373,427,379,368,363,354,355,329",shape:"poly"},on:{click:function(a){t.dialog6=!0}}}),o("area",{attrs:{target:"",alt:"southamericaLabel",title:"southamericaLabel",coords:"183,377,283,426",shape:"rect"},on:{click:function(a){t.dialog6=!0}}}),o("area",{attrs:{target:"",alt:"northpole",title:"northpole",coords:"259,86,358,53,397,55,467,49,517,60,503,74,504,99,495,122,462,137,448,159,421,133,402,90,364,85,360,101,387,116,402,134,392,151,370,142,371,127,344,110,334,97,316,101,311,107,302,115,280,120,248,110",shape:"poly"},on:{click:function(a){t.dialog4=!0}}}),o("area",{attrs:{target:"",alt:"help",title:"help",coords:"1035,392,1091,464",shape:"rect"},on:{click:function(a){t.help=!0}}}),o("area",{attrs:{target:"",alt:"australiaIsland",title:"australiaIsland",coords:"948,407,984,451",shape:"rect"},on:{click:function(a){t.dialog7=!0}}})]),o("v-dialog",{attrs:{"max-width":"750px"},model:{value:t.dialog,callback:function(a){t.dialog=a},expression:"dialog"}},[o("v-card",{staticClass:"mx-auto",attrs:{"max-width":"750",outlined:""}},[o("v-card-title",{staticClass:"text-h7 font-weight-bold grey lighten-2"},[t._v(" "+t._s(t.translate("Africa"))+" ")]),o("v-card-text",{staticStyle:{"padding-top":"10px"}},[o("v-simple-table",{attrs:{"fixed-header":""}},[o("thead",{staticStyle:{"background-color":"#92278f",color:"white"}},[o("tr",[o("td",[t._v(t._s(t.translate("Operator")))]),o("td",[t._v(t._s(t.translate("Network Service Status")))]),o("td",[t._v(t._s(t.translate("Incoming Call")))]),o("td",[t._v(t._s(t.translate("Outgoing Call to Libya")))]),o("td",[t._v(t._s(t.translate("Outgoing Local Call")))]),o("td",[t._v(t._s(t.translate("SMS")))])])]),t._l(t.africa,(function(a){return o("tbody",{key:a.country},[a.country?o("tr",[o("td",{staticClass:"text-h6",staticStyle:{"font-weight":"700","text-align":"center",color:"#92278f"},attrs:{colspan:"6"}},[t._v(" "+t._s(t.translate(a.country))+" ")])]):t._e(),o("tr",[o("td",[t._v(t._s(t.translate(a.operator)))]),o("td",[t._v(t._s(t.translate(a.netstatus)))]),o("td",[t._v(t._s(t.translate(a.mtc)))]),o("td",[t._v(t._s(t.translate(a.moclib)))]),o("td",[t._v(t._s(t.translate(a.mocloc)))]),o("td",[t._v(t._s(t.translate(a.sms)))])])])}))],2)],1),o("v-divider"),o("v-card-actions",[o("v-btn",{attrs:{text:""},on:{click:function(a){t.dialog=!1}}},[t._v(" Close ")])],1)],1)],1),o("v-dialog",{attrs:{"max-width":"750px"},model:{value:t.dialog2,callback:function(a){t.dialog2=a},expression:"dialog2"}},[o("v-card",{staticClass:"mx-auto",attrs:{"max-width":"750",outlined:""}},[o("v-card-title",{staticClass:"text-h7 font-weight-bold grey lighten-2"},[t._v(" "+t._s(t.translate("Europe"))+" ")]),o("v-card-text",{staticStyle:{"padding-top":"10px"}},[o("v-simple-table",{attrs:{"fixed-header":""}},[o("thead",{staticStyle:{"background-color":"#92278f",color:"white"}},[o("tr",[o("td",[t._v(t._s(t.translate("Operator")))]),o("td",[t._v(t._s(t.translate("Network Service Status")))]),o("td",[t._v(t._s(t.translate("Incoming Call")))]),o("td",[t._v(t._s(t.translate("Outgoing Call to Libya")))]),o("td",[t._v(t._s(t.translate("Outgoing Local Call")))]),o("td",[t._v(t._s(t.translate("SMS")))])])]),t._l(t.europe,(function(a){return o("tbody",{key:a.country},[a.country?o("tr",[o("td",{staticClass:"text-h6",staticStyle:{"font-weight":"700","text-align":"center",color:"#92278f"},attrs:{colspan:"6"}},[t._v(" "+t._s(t.translate(a.country))+" ")])]):t._e(),o("tr",[o("td",[t._v(t._s(t.translate(a.operator)))]),o("td",[t._v(t._s(t.translate(a.netstatus)))]),o("td",[t._v(t._s(t.translate(a.mtc)))]),o("td",[t._v(t._s(t.translate(a.moclib)))]),o("td",[t._v(t._s(t.translate(a.mocloc)))]),o("td",[t._v(t._s(t.translate(a.sms)))])])])}))],2)],1),o("v-divider"),o("v-card-actions",[o("v-btn",{attrs:{text:""},on:{click:function(a){t.dialog2=!1}}},[t._v(" Close ")])],1)],1)],1),o("v-dialog",{attrs:{"max-width":"750px"},model:{value:t.dialog3,callback:function(a){t.dialog3=a},expression:"dialog3"}},[o("v-card",{staticClass:"mx-auto",attrs:{"max-width":"750",outlined:""}},[o("v-card-title",{staticClass:"text-h7 font-weight-bold grey lighten-2"},[t._v(" "+t._s(t.translate("Asia"))+" ")]),o("v-card-text",{staticStyle:{"padding-top":"10px"}},[o("v-simple-table",{attrs:{"fixed-header":""}},[o("thead",{staticStyle:{"background-color":"#92278f",color:"white"}},[o("tr",[o("td",[t._v(t._s(t.translate("Operator")))]),o("td",[t._v(t._s(t.translate("Network Service Status")))]),o("td",[t._v(t._s(t.translate("Incoming Call")))]),o("td",[t._v(t._s(t.translate("Outgoing Call to Libya")))]),o("td",[t._v(t._s(t.translate("Outgoing Local Call")))]),o("td",[t._v(t._s(t.translate("SMS")))])])]),t._l(t.asia,(function(a){return o("tbody",{key:a.country},[a.country?o("tr",[o("td",{staticClass:"text-h6",staticStyle:{"font-weight":"700","text-align":"center",color:"#92278f"},attrs:{colspan:"6"}},[t._v(" "+t._s(t.translate(a.country))+" ")])]):t._e(),o("tr",[o("td",[t._v(t._s(t.translate(a.operator)))]),o("td",[t._v(t._s(t.translate(a.netstatus)))]),o("td",[t._v(t._s(t.translate(a.mtc)))]),o("td",[t._v(t._s(t.translate(a.moclib)))]),o("td",[t._v(t._s(t.translate(a.mocloc)))]),o("td",[t._v(t._s(t.translate(a.sms)))])])])}))],2)],1),o("v-divider"),o("v-card-actions",[o("v-btn",{attrs:{text:""},on:{click:function(a){t.dialog3=!1}}},[t._v(" Close ")])],1)],1)],1),o("v-dialog",{attrs:{"max-width":"750px"},model:{value:t.dialog4,callback:function(a){t.dialog4=a},expression:"dialog4"}},[o("v-card",{staticClass:"mx-auto",attrs:{"max-width":"750",outlined:""}},[o("v-card-title",{staticClass:"text-h7 font-weight-bold grey lighten-2"},[t._v(" "+t._s(t.translate("North Pole, Not coming that soon -.- "))+" ")]),o("v-divider"),o("v-card-actions",[o("v-btn",{attrs:{text:""},on:{click:function(a){t.dialog4=!1}}},[t._v(" Close ")])],1)],1)],1),o("v-dialog",{attrs:{"max-width":"750px"},model:{value:t.dialog5,callback:function(a){t.dialog5=a},expression:"dialog5"}},[o("v-card",{staticClass:"mx-auto",attrs:{"max-width":"750",outlined:""}},[o("v-card-title",{staticClass:"text-h7 font-weight-bold grey lighten-2"},[t._v(" "+t._s(t.translate("North America"))+" ")]),o("v-card-text",{staticStyle:{"padding-top":"10px"}},[o("v-simple-table",{attrs:{"fixed-header":""}},[o("thead",{staticStyle:{"background-color":"#92278f",color:"white"}},[o("tr",[o("td",[t._v(t._s(t.translate("Operator")))]),o("td",[t._v(t._s(t.translate("Network Service Status")))]),o("td",[t._v(t._s(t.translate("Incoming Call")))]),o("td",[t._v(t._s(t.translate("Outgoing Call to Libya")))]),o("td",[t._v(t._s(t.translate("Outgoing Local Call")))]),o("td",[t._v(t._s(t.translate("SMS")))])])]),t._l(t.america,(function(a){return o("tbody",{key:a.country},[a.country?o("tr",[o("td",{staticClass:"text-h6",staticStyle:{"font-weight":"700","text-align":"center",color:"#92278f"},attrs:{colspan:"6"}},[t._v(" "+t._s(t.translate(a.country))+" ")])]):t._e(),o("tr",[o("td",[t._v(t._s(t.translate(a.operator)))]),o("td",[t._v(t._s(t.translate(a.netstatus)))]),o("td",[t._v(t._s(t.translate(a.mtc)))]),o("td",[t._v(t._s(t.translate(a.moclib)))]),o("td",[t._v(t._s(t.translate(a.mocloc)))]),o("td",[t._v(t._s(t.translate(a.sms)))])])])}))],2)],1),o("v-divider"),o("v-card-actions",[o("v-btn",{attrs:{text:""},on:{click:function(a){t.dialog5=!1}}},[t._v(" Close ")])],1)],1)],1),o("v-dialog",{attrs:{"max-width":"750px"},model:{value:t.dialog6,callback:function(a){t.dialog6=a},expression:"dialog6"}},[o("v-card",{staticClass:"mx-auto",attrs:{"max-width":"750",outlined:""}},[o("v-card-title",{staticClass:"text-h7 font-weight-bold grey lighten-2"},[t._v(" "+t._s(t.translate("South America"))+" ")]),o("v-card-text",{staticStyle:{"padding-top":"10px"}},[o("v-simple-table",{attrs:{"fixed-header":""}},[o("thead",{staticStyle:{"background-color":"#92278f",color:"white"}},[o("tr",[o("td",[t._v(t._s(t.translate("Operator")))]),o("td",[t._v(t._s(t.translate("Network Service Status")))]),o("td",[t._v(t._s(t.translate("Incoming Call")))]),o("td",[t._v(t._s(t.translate("Outgoing Call to Libya")))]),o("td",[t._v(t._s(t.translate("Outgoing Local Call")))]),o("td",[t._v(t._s(t.translate("SMS")))])])]),t._l(t.south_america,(function(a){return o("tbody",{key:a.country},[a.country?o("tr",[o("td",{staticClass:"text-h6",staticStyle:{"font-weight":"700","text-align":"center",color:"#92278f"},attrs:{colspan:"6"}},[t._v(" "+t._s(t.translate(a.country))+" ")])]):t._e(),o("tr",[o("td",[t._v(t._s(t.translate(a.operator)))]),o("td",[t._v(t._s(t.translate(a.netstatus)))]),o("td",[t._v(t._s(t.translate(a.mtc)))]),o("td",[t._v(t._s(t.translate(a.moclib)))]),o("td",[t._v(t._s(t.translate(a.mocloc)))]),o("td",[t._v(t._s(t.translate(a.sms)))])])])}))],2)],1),o("v-divider"),o("v-card-actions",[o("v-btn",{attrs:{text:""},on:{click:function(a){t.dialog6=!1}}},[t._v(" Close ")])],1)],1)],1),o("v-dialog",{attrs:{"max-width":"750px"},model:{value:t.dialog7,callback:function(a){t.dialog7=a},expression:"dialog7"}},[o("v-card",{staticClass:"mx-auto",attrs:{"max-width":"750",outlined:""}},[o("v-card-title",{staticClass:"text-h7 font-weight-bold grey lighten-2"},[t._v(" "+t._s(t.translate("Australia, Coming Soon!"))+" ")]),o("v-divider"),o("v-card-actions",[o("v-btn",{attrs:{text:""},on:{click:function(a){t.dialog7=!1}}},[t._v(" Close ")])],1)],1)],1),o("v-dialog",{attrs:{"max-width":"750px"},model:{value:t.help,callback:function(a){t.help=a},expression:"help"}},[o("v-card",{staticClass:"mx-auto",attrs:{"max-width":"750",outlined:""}},[o("v-row",{staticStyle:{"background-color":"#0f0f33"}},[o("v-col",{attrs:{md:"10"}},[o("v-card-title",{staticClass:"text-h7 white--text",staticStyle:{"font-weight":"700"}},[t._v(" "+t._s(t.translate("Help"))+" ")])],1),o("v-col",{staticClass:"text-center mt-3",attrs:{md:"2"}},[o("v-icon",{attrs:{large:"",color:"orange lighten-3"},on:{click:function(a){t.help=!1}}},[t._v("mdi-close-circle")])],1)],1),o("v-card-text",{staticClass:"text--primary",staticStyle:{"padding-top":"60px","margin-bottom":"20px",height:"220px","font-size":"18px","text-align":"center"}},[t._v(" "+t._s(t.translate("Roaming Service allows you to use your Libyana SIM abroad, according to the host country’s billing** fees. For information on these fees click on each continent to view its host countries. ** Billing is LYD per 60 seconds."))+" ")]),o("v-divider")],1)],1)],1)},s=[],r=e("9923"),i={methods:{translate:r["a"].translate},data:function(){return{dialog:!1,dialog2:!1,dialog3:!1,dialog4:!1,dialog5:!1,dialog6:!1,dialog7:!1,help:!1,africa:[{flag:"../../assets/flags/Flag_of_Algeria.svg",country:"Algeria",operator:"Wataniya",netstatus:"Postpaid+Prepaid",mtc:"5.81",moclib:"14.22",mocloc:"4.54",sms:"3.03"},{operator:"DJEZZY",netstatus:"Postpaid",mtc:"5.81",moclib:"11.37",mocloc:"4.60",sms:"2.36"},{country:"Egypt",operator:"Etisalat Misr ",netstatus:"Postpaid+Prepaid",mtc:"2.40",moclib:"37.33",mocloc:"6.23",sms:"3.93"},{operator:"Vodafone",netstatus:"Postpaid+Prepaid",mtc:"2.40",moclib:"7.87",mocloc:"4.54",sms:"3.93"},{operator:"Orange",netstatus:"Postpaid+Prepaid",mtc:"2.40",moclib:"8.59",mocloc:"4.66",sms:"0.36"},{country:"South Africa",operator:"Cell C",netstatus:"Postpaid",mtc:"3.00",moclib:"6.18",mocloc:"3.90",sms:"0.48"},{operator:"Telkom South Africa",netstatus:"Postpaid",mtc:"4.80",moclib:"13.31",mocloc:"13.31",sms:"1.09"},{operator:"VODACOM PTY LTD",netstatus:"Postpaid",mtc:"5.70",moclib:"5.75",mocloc:"5.75",sms:"0.42"},{country:"Tunisia",operator:"Tunisie Telecom",netstatus:"Postpaid+Prepaid",mtc:"5.70",moclib:"9.68",mocloc:"5.81",sms:"0.79"},{operator:"Orange",netstatus:"Postpaid+Prepaid",mtc:"5.70",moclib:"9.68",mocloc:"9.44",sms:"1.51"},{operator:"Ooredoo",netstatus:"Postpaid+Prepaid",mtc:"5.70",moclib:"8.47",mocloc:"5.14",sms:"0.79"}],america:[{country:"United States",operator:"AT&T",netstatus:"Postpaid",mtc:"5.10",moclib:"5.01",mocloc:"5.25",sms:"1.17"},{operator:"Union Wireless",netstatus:"Postpaid",mtc:"9.36",moclib:"12.94",mocloc:"7.58",sms:"1.98"},{country:"Canada",operator:"Rogers Fido",netstatus:"Postpaid",mtc:"8.10",moclib:"12.71",mocloc:"7.52",sms:"2.22"}],europe:[{country:"France",operator:"Orange",netstatus:"Postpaid+Prepaid",mtc:"3.08",moclib:"7.38",mocloc:"7.38",sms:"1.03"},{operator:"Bouygues",netstatus:"Postpaid",mtc:"3.85",moclib:"17.85",mocloc:"7.74",sms:"1.69"},{country:"Germany",operator:"Telekom Deutschland",netstatus:"Postpaid+Prepaid",mtc:"3.60",moclib:"13.98",mocloc:"8.71",sms:"1.57"},{operator:"Vodafone",netstatus:"Postpaid",mtc:"3.60",moclib:"5.51",mocloc:"5.51",sms:"0.36"},{country:"Italy",operator:"Telecom Italia TI",netstatus:"Postpaid+Prepaid",mtc:"2.40",moclib:"5.20",mocloc:"3.27",sms:"0.12"},{operator:"Wind",netstatus:"Postpaid+Prepaid",mtc:"2.40",moclib:"19.72",mocloc:"7.44",sms:"1.63"},{operator:"Vodafone",netstatus:"Postpaid+Prepaid",mtc:"2.40",moclib:"5.51",mocloc:"5.51",sms:"0.36"},{country:"Malta",operator:"Vodafone",netstatus:"Postpaid+Prepaid",mtc:"4.33",moclib:"5.57",mocloc:"5.57",sms:"0.61"},{operator:"GoMobile",netstatus:"Postpaid",mtc:"4.33",moclib:"6.59",mocloc:"4.84",sms:"0.18"},{country:"Spain",operator:"Vodafone",netstatus:"Postpaid+Prepaid",mtc:"4.20",moclib:"6.35",mocloc:"6.35",sms:"0.42"},{operator:"Vodafone",netstatus:"Postpaid+Prepaid",mtc:"4.20",moclib:"9.92",mocloc:"5.08",sms:"2.06"},{country:"United Kingdom",operator:"Three",netstatus:"Postpaid+Prepaid",mtc:"3.60",moclib:"10.45",mocloc:"3.96",sms:"1.13"},{operator:"Orange(EE)",netstatus:"Postpaid+Prepaid",mtc:"3.60",moclib:"31.64",mocloc:"5.93",sms:"2.03"},{operator:"O2(Telefonica)",netstatus:"Postpaid",mtc:"3.60",moclib:"17.06",mocloc:"5.93",sms:"1.92"},{operator:"Vodafone",netstatus:"Postpaid",mtc:"3.60",moclib:"5.25",mocloc:"5.25",sms:"0.55"}],asia:[{country:"Cyprus",operator:"Prime Tel",netstatus:"Postpaid+Prepaid",mtc:"4.20",moclib:"13.31",mocloc:"6.66",sms:"0.91"},{country:"Jordan",operator:"Umniah",netstatus:"Postpaid+Prepaid",mtc:"3.12",moclib:"22.04",mocloc:"10.21",sms:"2.90"},{country:"Saudi Arabia",operator:"Mobily",netstatus:"Postpaid+Prepaid",mtc:"3.36",moclib:"3.96",mocloc:"2.94",sms:"0.68"},{operator:"Mobily",netstatus:"Postpaid+Prepaid",mtc:"3.36",moclib:"3.96",mocloc:"2.94",sms:"0.57"},{operator:"Zain",netstatus:"Postpaid+Prepaid",mtc:"8.10",moclib:"33.90",mocloc:"6.89",sms:"2.26"},{country:"Turkey",operator:"Vodafone",netstatus:"Postpaid+Prepaid",mtc:"3.60",moclib:"5.75",mocloc:"5.81",sms:"0.61"},{operator:"Avea (TT)",netstatus:"Postpaid+Prepaid",mtc:"3.60",moclib:"10.71",mocloc:"6.35",sms:"0.73"},{operator:"Turkcell",netstatus:"Postpaid+Prepaid",mtc:"3.60",moclib:"6.35",mocloc:"5.14",sms:"0.36"},{country:"United Arab Emirates",operator:"Etisalat",netstatus:"Postpaid+Prepaid",mtc:"10.68",moclib:"29.50",mocloc:"15.64",sms:"2.95"},{operator:"Thuraya (Satellite)",netstatus:"Postpaid",mtc:"18.00",moclib:"22.15",mocloc:"22.04",sms:"5.60"}]}}},l=i,n=e("2877"),c=e("6544"),d=e.n(c),m=e("8336"),u=e("b0af"),p=e("99d9"),g=e("62ad"),h=e("a523"),v=e("169a"),y=e("ce7e"),b=e("132d"),f=e("0fd9"),_=e("1f4f"),x=Object(n["a"])(l,o,s,!1,null,null,null);a["default"]=x.exports;d()(x,{VBtn:m["a"],VCard:u["a"],VCardActions:p["a"],VCardText:p["c"],VCardTitle:p["d"],VCol:g["a"],VContainer:h["a"],VDialog:v["a"],VDivider:y["a"],VIcon:b["a"],VRow:f["a"],VSimpleTable:_["a"]})},"8b37":function(t,a,e){},9923:function(t,a,e){"use strict";var o=e("4360"),s={"If you're done using Libyano, please tap on the 'Yes' button. If you would still like to explore Libyano, Tap on the 'No' button.":'إذا انتهيت من استخدام ليبيانو ، فالرجاء النقر فوق الزر "نعم". إذا كنت لا تزال ترغب في استكشاف ليبيانو ، فانقر فوق الزر "لا".',"Thank you for using Libyano Robot! Its been my pleasure to serve you!":"شكرا لك على استخدام روبوت ليبيانو! كان من دواعي سروري أن أخدمك!",Close:"اغلاق",Done:"تم","Learn More":"معرفة المزيد","Tap to Learn More":"آضغط لمعرفة المزيد",Yes:"نعم",No:"لا","Libyano Robot":"روبوت ليبيانو","Five LYD":"خمسة دينار","Five Libyan Dinars":"خمسة دينار","Top-Up of 5 LYD for your mobile credit!":"اشحن خمسة دينار الي رصيدك","Ten Libyan Dinars":"عشرة دينار","Top-Up of 10 LYD for your mobile credit!":"اشحن عشرة دينار الي رصيدك",Request:"اطـلـب","It seems the we are out of 5 LYD vouchers":"يبدو ان كروت تعبئة 5 دينار","It seems the we are out of 10 LYD vouchers":"يبدو ان كروت تعبئة 10 دينار","You have not inserted a bill in the given time!":"!لم تقم بإدخال عملة نقدية في الوقت المحدد","It seems that the bill was not inserted properly, or an error occured while inserting it, please try again properly!":"يبدو أنه لم يتم إدخال العملة نقدية بشكل صحيح، أو حدث خطأ أثناء إدخالها، يرجى المحاولة مرة أخرى بشكل صحيح!","It seems that an internal error occurred, please try again!":"يبدو أنه حدث خطأ داخلي ، يرجى المحاولة مرة أخرى","Internet for all":"نت للكل","Choose your package and enjoy Libyana’s internet with different speed, capacity, and price tailored for your needs.":"استمتع بانترنت ليبيانا بسعات وأسعار وسرعات متفاوتة حسب الباقة المناسبة ليك ولاحتياجاتك","Internet for all your needs!":"باقات انترنت لكل احتياجاتك!","Internet all night":"نت للصبح","Get more for less, off peak-period.":"باقات أكثر بأسعار أقل خارج وقت الذروة","Stream, download, and play all night with Libyana’s discounted packages from 3 AM to 10 AM.":"حمل، العب، وتفرج مع باقات نت للصبح من --- الساعة 3 صباحاً حتّى الساعة 10 صباحاً.","Internet extra.":"نت للكل اكسترا","Extra quota for essential packages to spend on socials or streaming.":"حصة إضافية للباقات الأساسية مخصصة لمواقع التواصل ومنصات البث","Extra Social ":"باقة اكسترا سوشيال","Stay connected with the extra social package on all your social networks.":"خليك على تواصل مع باقة اكسترا سوشيال لمنصات التواصل الاجتماعي.","Extra Stream":"باقة اكسترا ستريم","Download, watch, and stream your favorite media with Extra Stream package.":"حمّل، شاهد، واستمع على منصات البث مع باقة اكسترا ستريم.",Daily:"يومي",Weekly:"أسبوعي","Bi-Weekly":"نصف اسبوعي","Bi-Monthly":"نصف شهري",Monthly:"شهري","Package Type":"نوع الباقة","Package Capacity":"سعة الباقة","Package Price":"سعر الباقة","Download Speed":"سرعة التحميل",Technology:"التقنية","Free Minutes":"الدقائق المجانية داخل الشبكة","Package Validity":"صلاحية الباقة","Gift Package":"بقات الهداية","Required Points":"لنقاط المجمعة","Subscription Method":"طريقة الاشتراك",Internet:"انترنت","Text Messages (Libyana-Libyana)":"رسائل - ليبيانا","Minutes (Libyana-Libyana)":"دقائق (ليبيانا - ليبيانا)","One Week":"اسبوع","Two Weeks":"اسبوعين","One Month":"شهر","Two Months":"شهرين",LYD:"د.ل",Minutes:"دقيقة",Messages:"رسالة",Points:"نقطة",Unlimited:"غير محدودة","MyLibyana Application":"تطبيق MyLibyana","All Libyana’s services & offers at the - press of a button #foryourcomfort":" كل خدمات وعروض ليبيانا بضغطة زر #أريحلك","Through 'MyLibyana' app you can benefit from all services, access all offers, and get the latest of Libyana’s updates in one place. The application is available in Arabic and English.":"يوفر تطبيق MyLibyana  كافة الخدمات والعروض والمعلومات المقدمة من شركة ليبيانا في مكان واحد وبواجهة مستخدم سهلة الاستخدام، كما يتوفر باللغتين العربية والانجليزية.","Download MyLibyana from Appstore or Playstore and get 1 Giga + 15 minutes free.":"حمل التطبيق من Appstore أو Playstore وأحصل على 1جيجا + 15 دقيقة مجاناً.",Sallefny:"خدمة سلفني","dial *121# and don’t let the credit limit you.":"#121* وما تخليش الرصيد يوقفك","With the credit loan service, you can borrow credit from Libyana and use it to make calls, subscribe to Internet packages, and benefit from all other Libyana services.":"مع خدمة سلفني تقدر تستعير رصيد بالقيمة المتاحة من ليبيانا وتستخدمه لأداء مكالماتك، الاشتراك في باقات الانترنت، والاستفادة من الخدمات الأخرى.","To get the service dial *121# or use MyLibyana app.":"لاستخدام خدمة سلفني اتصل بالرمز #121* أو عن طريق تطبيق MyLibyana","Don’t let the credit limit you.":"ما تخليش الرصيد يوقفك.","Call Center":"مركز التواصل","150 we’re there because we care.":"150 ديما مهتمين","Our customer service team is always ready to help you 24/7, just call 150 or message us on our facebook page.":"مركز التواصل من شركة ليبيانا مستعد للإجابة عن جميع استفساراتك واستقبال شكاويك طيلة أيام الأسبوع 24 ساعة باليوم عبر الرقم المجاني 150 أو بريد صفحة الفيس بوك.","My Points Program":"برنامج نقاطي","Use more services & get more points":"استخدام أكثر، نقاط أكثر، باقات أكبر","Collect more points as you use services and replace those points for free (minutes, SMS, and Internet) from Libyana.":"جمع نقاط كل ما تتكلم أو تستخدم الانترنت واستبدلها بباقات (دقائق، رسائل، وانترنت) من ليبيانا.","To view your points or see the available packages dial *333# or use MyLibyana app.":"للاستفسار عن رصيد نقاطك أو الاطلاع على الباقات المتاحة اتصل ب #333* أو عن طريق تطبيق   MyLibyana","You are the lead":"أنتوا الصدارة","You are the lead packages":" باقات أنتوا الصدارة","With Libyana you’re always in the lead.":"خليك مع ليبيانا خليك في الصدارة","You are the lead offers special packages to Libyana’s most loyal customers that includes special monthly internet packages as well as free minutes to spend on the network.":"عروض خاصة تشمل باقات انترنت شهرية ودقائق مجانية للمشتركين أكثر استخداماً للشبكة","The Special Offers:":"باقات العروض الشهرية الخاصة:","All Night Special Offers:":"باقة نت للصبح الخاصة:","Additionally, You’re the lead offer includes double quota for the weekly and biweekly internet packages:":"كما توفر لكم عروض إنتو الصدارة ضعف الحصة في الباقات الإسبوعية والنصف شهرية:","Roaming Service allows you to use your Libyana SIM abroad, according to the host country’s billing** fees. For information on these fees click on each continent to view its host countries. ** Billing is LYD per 60 seconds.":"خدمة التجوال تمكنك من استخدام شريحة ليبيانا الخاصة بك عند السفر وذلك وفقاً لتكلفة الاتصال للدولة المستضيفة. لمعرفة المزيد حول تكلفة الاتصال قم بالنقر على أي قارة لعرض الدول المختلفة بها. ** تكلفة الاتصال معرّفة بالدينار الليبي لكل 60 ثانية.",Help:"مساعدة",Operator:"المشغل","Network Service Status":"الحالة","Incoming Call":"تكلفة استقبال مكالمة","Outgoing Call to Libya":"تكلفة مكالمة صادرة إلى ليبيا","Outgoing Local Call":"تكلفة مكالمة صادرة إلى رقم محلي",SMS:"تكلفة إرسال الرسائل القصيرة",Africa:"أفريقيا",Europe:"أوروبا",Asia:"آسيا","North America":"أمريكا الشمالية","South America":"أمريكا الجنوبية","North Pole, Not coming that soon -.- ":"القطب الشمالي، مش قريب هلبا -.-","Australia, Coming Soon!":"أستراليا، قريبا!",Algeria:"الجزائر",Canada:"كندا",Cyprus:"قبرص",Egypt:"مصر",France:"فرنسا",Germany:"ألمانيا",Italy:"إيطاليا",Jordan:"الأردن",Malta:"مالطا","New Zealand":"نيوزيلاندا","Saudi Arabia":"المملكة العربية السعودية","South Africa":"جنوب أفريقيا",Spain:"إسبانيا",Tunisia:"تونس",Turkey:"تركيا","United Arab Emirates":"الإمارات العربية المتحدة","United Kingdom":"المملكة المتحدة","United States":"الولايات المتحدة الأمريكية"},r={},i={"./assets/bar/back.svg":"./assets/bar/back_rtl.svg",five_lyd:e("f6b0"),ten_lyd:e("e7d1"),offers_icon:e("e465"),topup_icon:e("46fe"),roaming_icon:e("012e"),internet_icon:e("68e1")},l={five_lyd:e("6ff8"),ten_lyd:e("6322"),offers_icon:e("38b7"),topup_icon:e("6452"),roaming_icon:e("9444"),internet_icon:e("c3c8")},n={ar:s,en:r},c={ar:i,en:l};a["a"]={translateMedia:function(t){var a=c[o["a"].getters["Interface/get_lang"]];return t in a?(console.log("translation media found ",a[t]),a[t]):(console.log("no translation media found ",t),t)},translate:function(t){var a=n[o["a"].getters["Interface/get_lang"]];return t in a?a[t]:t}}}}]);
//# sourceMappingURL=roaming.0fae84aa.js.map