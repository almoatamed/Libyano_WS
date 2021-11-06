<template>
  <v-app :style="appStyle">
    <v-dialog v-model="voucher.dialog.show" max-width="400px" persistent>
      <v-card class="mx-auto" max-width="400" outlined dark color="#92278f">
        <v-card-title
          >{{ voucher.dialog.messages[voucher.dialog.counter].title }}
        </v-card-title>
        <v-card-text
          v-if="voucher.dialog.counter == 0"
          class="text-h5 font-weight-bold"
        >
          <p>
            {{ voucher.dialog.messages[0].text[0] }}
          </p>
        </v-card-text>

        <v-card-text class="text-h5 font-weight-bold" v-else>
          <p>
            {{ voucher.dialog.messages[0].text[0] }}
          </p>
          <p>
            {{ voucher.dialog.messages[0].text[0] }}
          </p>
          <p>{{ translate("Secret") }}: {{ voucher.card.secret }}</p>
          <p>Serial: {{ voucher.card.serial }}</p>
          <p>Val: {{ voucher.card.val }}</p>
        </v-card-text>
        <v-card-actions>
          <v-btn color="#ffc74a" @click="close_dialog()" light>
            {{ voucher.dialog.messages[voucher.dialog.counter].action }}
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-app-bar
      v-if="interactive"
      app
      flat
      extended
      extension-height="140px;"
      color="background"
      src="./assets/bar/banner2.svg"
    >
      <dir @click="goBack()" :class="rtl ? 'goback_right' : 'goback_left'"></dir>
      <v-container>
        <v-row>
          <v-img
            @click="goBack()"
            :src="translateMedia('./assets/bar/back.svg')"
            style="margin-top: 120px"
            max-width="60px"
            max-height="60px"
          ></v-img>
          <v-spacer></v-spacer>
          <v-spacer></v-spacer>
          <v-img
            src="./assets/bar/dima_m3ana.svg"
            max-width="260"
            max-height="100"
            style="margin-top: 140px;"
            class="ms-16"
          ></v-img>
          <v-spacer></v-spacer>
          <v-spacer></v-spacer>
          <v-img
            @click="set_lang('en')"
            src="./assets/bar/en.svg"
            style="margin-top: 120px"
            max-width="60px"
            max-height="60px"
          ></v-img>
          <v-img
            @click="set_lang('ar')"
            src="./assets/bar/ar.svg"
            style="margin-top: 120px;"
            max-width="60px"
            max-height="60px"
            class="ms-3"
          ></v-img>
        </v-row>
      </v-container>
    </v-app-bar>

    <v-main>
      <router-view></router-view>
    </v-main>

    <v-footer v-if="interactive_footer" app height="140" color="stream">
      <v-container>
        <v-row justify="space-between">
          <v-col md="3">
            <v-img
              src="./assets/bar/libyano.svg"
              max-height="300px"
              max-width="300px"
            ></v-img>
          </v-col>
          <v-col md="3" style="display: flex">
            <v-img
              src="./assets/bar/stream.svg"
              max-width="110px"
              max-height="100px"
              style="margin-left: 100px"
            ></v-img>
            <v-img
              src="./assets/bar/libyana.svg"
              max-width="80px"
              max-height="80px"
              style="margin-left: 40px; margin-top: 3px"
            ></v-img>
          </v-col>
        </v-row>
      </v-container>
    </v-footer>
  </v-app>
</template>

<script>
export default {
  name: "App",

  methods: {
    reset_timeout(){
      console.log('resetting time out')
      clearTimeout(this.timeout_handler)
      this.timeout_handler = setTimeout(()=>{
        if(this.$route.name != 'slide-show'){
          this.change_mode()
        }
      },180e3)
    },
    change_mode(){
      this.$store.dispatch('Ros/change_mode','grtcancel', {root:true}).then(()=>{}).catch(err=>{
        console.error('Error while trying to change mode from interface', err)
      })
    },
    set_lang(lang) {
      this.$store.dispatch('Interface/set_lang', lang, {route: true})
    },
    goBack() {
      var path = this.$route.path.split('/')
      path = path.slice(0,path.length - 1).join('/')
      if(!path){
        this.change_mode()
      }else{
        this.$router.push(path)
      }
    },
    translateMedia(src){
      return this.$store.getters['Interface/get_media'][src]
    },
    translate(phrase){
      var t_phrase = this.$store.getters['Interface/get_content'][phrase]
      if(!t_phrase){
        return phrase
      }else{
        return t_phrase
      }
    },
    close_dialog(){
      this.voucher.dialog.counter +=1
      if(this.voucher.dialog.counter == 2){
        clearTimeout(this.voucher.timeout)
        this.$store.dispatch('Voucher/clear',null, {root:true})
        this.voucher.continue = true
        this.voucher.dialog.show = false
        this.voucher.card = {}
      }
    },
  },

  computed: {
    loading() {
      return this.$store.getters["Loading/getLoading"];
    },
    interactive() {
      return this.$store.getters["Interactive/get_interactive"];
    },

    interactive_footer() {
      return this.$store.getters["Interactive/get_interactive_footer"];
    },

    voucher_show() {
      return this.$store.getters["Voucher/show"];
    },

    voucher_message() {
      return this.$store.getters["Voucher/message"];
    },
    rtl(){
      return this.$vuetify.rtl
    },
    lang(){
      return this.$store.getters["Interface/get_lang"]
    }
  },
  watch:{
    voucher_show(){
      if(this.voucher_show){
        this.voucher.card = this.voucher_message
        this.voucher.dialog.counter = 0
        this.voucher.dialog.show = true
        this.voucher.continue = false
        this.voucher.timeout = setTimeout(()=>{
          this.$store.dispatch('Voucher/clear',null, {root:true})
          this.voucher.continue = true
          this.voucher.dialog.show = false
          this.voucher.card = {}
        },60e3)
      }
    },
    lang(){
      if(this.lang != this.current_lang){
        this.current_lang = this.lang
        if (this.current_lang == 'ar') {
          this.appStyle.fontFamily = 'Tajawal'
          this.$vuetify.rtl = true;
          console.log("Font and RTL Activated")
        }
        else {
          this.appStyle.fontFamily = "Montserrat"
          this.$vuetify.rtl = false;
        }
      }
    }
  },
  created(){
    var self = this
    setInterval(()=>{
      if(self.voucher.continue){
        self.$store.dispatch('Voucher/check',null,{root:true}).then(()=>{}).catch(()=>{}) 
      }
    },500)
    setInterval(()=>{
      self.$store.dispatch('Ros/fetch_mode',null,{root:true}).then((mode)=>{
          if (mode == 'str'){

          }else if(mode == 'grt'){
            if(this.$route.name == 'slide-show' || this.$route.name == 'bootup'){
              this.$router.push({name:'language'})
            }
          }else{
            if(this.$route.name != 'slide-show'){
              this.$router.push({name:'slide-show'})
            }
          }
      }).catch(()=>{}) 
    },250)
    this.reset_timeout()
    window.addEventListener('click', this.reset_timeout)
  },
  data() {
    return {
      voucher:{
        dialog:{
          messages:[
            {
              title:'You Have Succeed',
              text:['Please Press continue to get you voucher!'],
              action:'get'
            },
            {
              title:'Voucher Card',
              text:['Please use the shown Voucher Card!','','',''],
              action:'Received'
            },
            {}
          ],
          counter: 0,
          show: false,
          timeout:{}
        },
        card:{},
        continue:true,
      },
      appStyle: {
        backgroundColor: "#ecf0f1",
        fontFamily: "Montserrat",
      },
      timeout_handler:null,
      current_lang:'',
    };
  },
};
</script>
<style>
@import url('./assets/css/font.css'); 
::-webkit-scrollbar {
    display: none;
}
.goback_left{
  position: absolute;
  top: 20%;
  left: 7%;
  z-index: 1000;
  width: 100px;
  height: 100px;
}
.goback_right{
  position: absolute;
  top: 20%;
  z-index: 1000;
  right: 7%;
  width: 100px;
  height: 100px;
}
</style>
 
