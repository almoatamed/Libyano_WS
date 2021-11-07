<template>
  <v-app id="app" transition="slide-y-transition"> 

    <!-- warn/error/success/nothign/ -->
    <notifications group="main" position='bottom right' :max='5' :duration='10000' />

    <div class="loading" v-if="loading">
      <v-progress-circular
        style="position:fixed;top:50%;left:50%;"
        :size="50"
        color="primary"
        indeterminate
      ></v-progress-circular>
    </div>

    <v-app-bar
    v-if='auth'
    color='#706f6f'
    id="mainbar"
    app
    dense
    clipped-left
    dark
    > 
      <v-app-bar-nav-icon @click='navDrawer=!navDrawer'></v-app-bar-nav-icon>

      <span class="font-weight-black pl-4"
        ><v-icon>mdi-battery</v-icon>:{{status['power']['battery']}}</span
      >
      <span class="font-weight-black pl-2"
        >| <v-icon>mdi-battery-charging-100</v-icon>: {{status['power']['charging_status'] || status['power']['cord']? 'YES' : 'NO' }}</span
      >
      <span class="font-weight-black pl-2"
        >| <v-icon>mdi-thermometer</v-icon>: {{('' +status['sensors']['temp'][0]).slice(0,2)}}</span
      >
      <v-spacer></v-spacer>
      <v-btn class="ml-2" 
      color='error'      
      @click='toggle_navigation_detach'
      > {{navigation_detached?'RELEASE': 'EMG'}} </v-btn>
      <v-menu
      offset-y
      >
        <template
        v-slot:activator="{attrs,on}"
        >
          <v-btn
          icon
          v-bind ='attrs'
          v-on='on'
          >
            <v-icon style="font-size:40px">mdi-account</v-icon>
          </v-btn>
        </template>
        <v-list :dark="isDark" dense min-width="180">

          <v-list-item-group>

            <v-list-item link @click="logout"> 
              <v-icon left small>mdi-key</v-icon>
              <v-list-item-content >
                <v-list-item-title > Logout</v-list-item-title>
              </v-list-item-content>
            </v-list-item>

            <v-list-item link @click="setIsDark"> 
              <v-icon left small>mdi-white-balance-sunny</v-icon>
              <v-list-item-content >
                <v-list-item-title > Dark Theme</v-list-item-title>
              </v-list-item-content>
            </v-list-item>

          </v-list-item-group>

        </v-list>
      </v-menu>
    </v-app-bar>

    <v-navigation-drawer 
      app 
      v-if="auth"
      color='#060633' 
      v-model='navDrawer'
      clipped
      dark
      :mini-variant='navDrawerMini'
    >
      <v-list
        :rounded='!navDrawerMini' 
      >

        <!-- this list item for the minimize button for the side drawer -->
        <v-list-item
          @click='navDrawerMini = !navDrawerMini'
        >
          <v-list-item-icon >
            <v-icon >{{navDrawerExpansionArrow}}</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title class="ml-4">
              Minimize
            </v-list-item-title>
          </v-list-item-content>
        </v-list-item>

        <v-divider class="my-2"></v-divider>

        <v-list-group color="white" prepend-icon="mdi-robot" v-if="!restrictions['startup']">
          <template v-slot:activator>
            <v-list-item-title>Startup</v-list-item-title>
          </template>
          <v-list-item :to="{name:'startup'}">
            <v-list-item-icon>
              <v-icon small class="mx-auto">mdi-launch</v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title >Startup</v-list-item-title>        
            </v-list-item-content>
          </v-list-item>
          <v-list-item :to="{name:'startup_map'}">
            <v-list-item-icon>
              <v-icon small class="mx-auto">mdi-map</v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title >Startup Map</v-list-item-title>        
            </v-list-item-content>
          </v-list-item>
        </v-list-group>

        <v-list-group color="white" prepend-icon="mdi-robot" >
          <template v-slot:activator>
            <v-list-item-title>Basic</v-list-item-title>
          </template>
          <v-list-item :to="{name:'summary'}">
            <v-list-item-icon>
              <v-icon small class="mx-auto">mdi-information</v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title >Summary</v-list-item-title>        
            </v-list-item-content>
          </v-list-item>
        </v-list-group>

        <v-list-item :to="{name:'live'}" >
          <v-list-item-icon>
            <v-icon small class="mx-auto">mdi-information</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title >Live</v-list-item-title>        
          </v-list-item-content>
        </v-list-item>

        <v-list-item :to="{name:'points_manager'}">
          <v-list-item-icon>
            <v-icon small class="mx-auto">mdi-map-marker</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title >Point Manager</v-list-item-title>        
          </v-list-item-content>
        </v-list-item>


        <v-list-item :to="{name:'act_manager'}">
          <v-list-item-icon>
            <v-icon small class="mx-auto">mdi-play</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title >Act Manager</v-list-item-title>        
          </v-list-item-content>
        </v-list-item>

        <v-list-group color="white" prepend-icon="mdi-access-point-network" >
          <template v-slot:activator>
            <v-list-item-title>Networking</v-list-item-title>
          </template>
          <v-list-item :to="{name:'bluetooth'}">
            <v-list-item-icon>
              <v-icon small class="mx-auto">mdi-bluetooth</v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title >Bluetooth</v-list-item-title>        
            </v-list-item-content>
          </v-list-item>
        </v-list-group>

        <v-list-group color="white" prepend-icon="mdi-cash-multiple" >
          <template v-slot:activator>
            <v-list-item-title>Voucher</v-list-item-title>
          </template>
          <v-list-item :to="{name:'voucher_loader'}">
            <v-list-item-icon>
              <v-icon small class="mx-auto">mdi-ticket-confirmation</v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title >Voucher Loader</v-list-item-title>        
            </v-list-item-content>
          </v-list-item>
        </v-list-group>

        <v-list-group color="white" prepend-icon="mdi-volume-high" >
          <template v-slot:activator>
            <v-list-item-title>Speach Controller</v-list-item-title>
          </template>
          <v-list-item :to="{name:'voice'}">
            <v-list-item-icon>
              <v-icon small class="mx-auto">mdi-pencil</v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title >Speach Generater</v-list-item-title>        
            </v-list-item-content>
          </v-list-item>
        </v-list-group>

        <!-- <v-list-group color="white" prepend-icon="mdi-map-marker"  v-if="!restrictions['map']">
          <template v-slot:activator>
            <v-list-item-title>Navigation</v-list-item-title>
          </template>
          <v-list-item :to="{name:'map'}">
            <v-list-item-icon>
              <v-icon small class="mx-auto">mdi-map</v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title >Map</v-list-item-title>        
            </v-list-item-content>
          </v-list-item>
        </v-list-group> -->
      </v-list>
    </v-navigation-drawer>


      <v-main  
      :class='`${isDark?"blue-grey darken-4 grey--text text--lighten-4":"grey lighten-4 grey--text text--darken-2"} `'
      >
        <v-container 
         fluid class="pa-0 ma-0">
          <router-view></router-view>
        </v-container>
        
        
        <v-footer
          class='blue-grey darken-2 text-center hidden-lg-and-down pa-0 ma-0'
          padless
          fixed
        >
          <v-card 
            flat
            tile
            color="blue-grey darken-2"
            class="pa-0 "
            width='100%'
          >
          <v-card-text  class=" white--text pa-0 caption">
            {{new Date().getFullYear()}} - <strong>Libyano</strong>
          </v-card-text>
          </v-card>
        </v-footer>
      </v-main>
      
    </v-app>
</template>

<script>
  export default {
    computed: {
      status(){
        if( this.$store.getters['Ros/status']['power']){
          return this.$store.getters['Ros/status']
        }else{
          return this.temp_status
        }
      },
      navDrawerExpansionArrow(){
        if(this.navDrawerMini){
          return 'mdi-arrow-right';
        }
        return 'mdi-arrow-left';
      },

      isDark(){
        return this.$store.getters['Theme/isDark'];
      },

      auth(){
        return this.$store.getters['User/auth'] ;
      },

      alert(){
        return this.$store.getters['Notify/alert'];
      },
      
      notifyMessage(){
        return this.$store.getters['Notify/message'];
      },

      loading(){
        return this.$store.getters['Loading/get'];
      },

    restrictions(){
        return this.$store.getters['Router/get_restrictions']
      }

    },
    data () {
      return{
        navDrawer:true,
        navDrawerMini:false,
        navigation_detached:false,
        temp_status:{
          power:{
            battery:'Unknown',
            charging_status:'Unknown', 
            cord: 'Unknown'
          },
          sensors:{
            temp:['Unknown']
          }
        }
      }
    },
    watch: {
      alert(){
        if(this.alert){
          console.log('App: alerting ...  ', this.notifyMessage);
          let n  = this.notifyMessage
          if (n.duration){
            this.$notify({
              title:n.title,
              text:n.text,
              type: n.type,
              duration: n.duration,
              groupt: 'main'
            });
          }else{
            this.$notify({
              title: n.title,
              text: n.text, 
              type: n.type, 
              group: 'main'
            });
          }
          this.$store.dispatch('Notify/clear',null, {root:true});
        }
      }
    },
    methods:{
      toggle_navigation_detach(){
        this.$store.dispatch('Ros/take_action', 'navigation/toggle_detach', {root:true}).then(res=>{
          console.log(res)
        })
      },
      setIsDark(){
        console.log('App: changing theme');
        this.$store.dispatch('Theme/setDark',null,{root:true});
      },
      logout(){
        this.$store.dispatch('Loading/set',null,{root:true});
        console.log('Logging out')
        this.$store.dispatch('User/logout',null,{root:true}).then(()=>{
          this.$router.push('login').then(()=>{}).catch(err=>{console.log(err)});
          this.$store.dispatch('Loading/clear',null,{root:true});
        })
    },
    },
    created(){ 
      setInterval(()=>{
        this.$store.dispatch('Ros/take_action','navigation/is_detached', {root:true}).then(res=>{
          this.navigation_detached = res=='1'?false:true
        })
      },500)
      this.$store.dispatch('User/checkToken', null, {root:true})
      var self = this;
      setInterval(() => {
        if(self.auth && self.$store.getters['Ros/connectionFlag']){
          self.$store.dispatch('Ros/fetchStatus',null, {root:true});
          self.$store.dispatch('Ros/fetchMode',null,{root:true}).then(()=>{
            self.$store.dispatch('Router/update_restrictions',null,{root:true}).then(()=>{
              if(this.$route.matched.some(route=>{      
                  // console.log(route.name,self.restrictions[route.name])    
                  return !!self.restrictions[route.name]
                })){
                this.$router.push({name:this.$store.getters['Router/get_unrestricted_route']})
              }
            })
          });
        }
      }, 1000);
    }
  }
</script>

<style scoped>
  .loading{
    position:absolute;
    top:0%;
    left:0%;
    bottom:0%;
    right:0%;
    z-index:10000;
    margin:0px;
    /* background-image: url('./views/assets/Login.jpg'); */
    background-color:rgb(255,255,255,1);
    background-size: cover;
    overflow: auto;
    background-repeat: no-repeat;
    /* transition:display 0.5s ease-in-out; */
  }
</style>