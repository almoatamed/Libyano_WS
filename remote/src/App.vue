<template>
  <v-app id="app" transition="slide-y-transition">
    <!-- warn/error/success/nothign/ -->
    <notifications
      group="main"
      position="bottom right"
      :max="5"
      :duration="10000"
    />

    <div class="loading" v-if="loading">
      <v-progress-circular
        style="position: fixed; top: 50%; left: 50%"
        :size="50"
        color="primary"
        indeterminate
      ></v-progress-circular>
    </div>

    <v-app-bar
      v-if="auth"
      color="#706f6f"
      id="mainbar"
      app
      dense
      clipped-left
      dark
    >
      <v-app-bar-nav-icon @click="navDrawer = !navDrawer"></v-app-bar-nav-icon>

      <div class="">
        <span class="font-weight-black pl-4" v-if="breakpoint == true"
          ><v-icon>mdi-battery</v-icon>:{{ status["power"]["battery"] }}</span
        >
        <span class="font-weight-black pl-2" v-if="breakpoint == true"
          >| <v-icon>mdi-battery-charging-100</v-icon>:
          {{
            status["power"]["charging_status"] || status["power"]["cord"]
              ? "YES"
              : "NO"
          }}</span
        >
        <span class="font-weight-black pl-2" v-if="breakpoint == true"
          >| <v-icon>mdi-thermometer</v-icon>:
          {{ ("" + status["sensors"]["temp"][0]).slice(0, 2) }}</span
        >
      </div>

      <v-spacer v-if="breakpoint == true && mode == 'ato'"></v-spacer>
      <div class="" v-if="breakpoint == true && mode == 'ato'">
        <span class="font-weight-black pl-2"
          ><v-icon>mdi-book</v-icon>:
          {{
            story_status["default_story"] +
            "-" +
            story_status["story_current_count"]
          }}
        </span>
        <span class="font-weight-black pl-2"
          ><v-icon>mdi-play</v-icon>:
          {{
            story_status["running_action"] == ""
              ? "No Action"
              : story_status["running_action"]
          }}
        </span>
        <span class="font-weight-black pl-2">{{ paused }} </span>
      </div>

      <v-spacer></v-spacer>

      <v-btn
        color=""
        icon
        v-if="mode == 'ato'"
        @click="restart_ato"
        ><v-icon >mdi-replay</v-icon>
      </v-btn>

      <v-btn
        color=""
        icon
        v-if="paused != 'story_ended' && mode == 'ato'"
        @click="toggle_pause_ato"
        ><v-icon v-if="paused == 'user paused'">mdi-play </v-icon>
        <v-icon v-else> mdi-pause </v-icon>
      </v-btn>

      <v-btn
        class="ml-2"
        color="secondary"
        v-if="mode != ''"
        @click="toggle_mode"
      >
        {{ mode == "mnl" ? "Manual" : "Auto" }}
      </v-btn>

      <v-btn class="ml-2" color="error" @click="toggle_navigation_detach">
        {{ navigation_detached ? "RELEASE" : "EMG" }}
      </v-btn>

      <v-menu offset-y>
        <template v-slot:activator="{ attrs, on }">
          <v-btn icon v-bind="attrs" v-on="on">
            <v-icon style="font-size: 40px">mdi-account</v-icon>
          </v-btn>
        </template>
        <v-list :dark="isDark" dense min-width="180">
          <v-list-item-group>
            <v-list-item link @click="logout">
              <v-icon left small>mdi-key</v-icon>
              <v-list-item-content>
                <v-list-item-title> Logout</v-list-item-title>
              </v-list-item-content>
            </v-list-item>

            <v-list-item link @click="setIsDark">
              <v-icon left small>mdi-white-balance-sunny</v-icon>
              <v-list-item-content>
                <v-list-item-title> Dark Theme</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </v-list-item-group>
        </v-list>
      </v-menu>
    </v-app-bar>

    <v-navigation-drawer
      app
      v-if="auth"
      color="#060633"
      v-model="navDrawer"
      clipped
      dark
      :mini-variant="navDrawerMini"
    >
      <v-list :rounded="!navDrawerMini">
        <!-- this list item for the minimize button for the side drawer -->
        <v-list-item @click="navDrawerMini = !navDrawerMini">
          <v-list-item-icon>
            <v-icon>{{ navDrawerExpansionArrow }}</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title class="ml-4"> Minimize </v-list-item-title>
          </v-list-item-content>
        </v-list-item>

        <v-divider class="my-2"></v-divider>

        <v-list-group
          color="white"
          prepend-icon="mdi-robot"
          v-if="!restrictions['startup']"
        >
          <template v-slot:activator>
            <v-list-item-title>Startup</v-list-item-title>
          </template>
          <v-list-item :to="{ name: 'startup' }">
            <v-list-item-icon>
              <v-icon small class="mx-auto">mdi-launch</v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title>Startup</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
          <v-list-item :to="{ name: 'startup_map' }">
            <v-list-item-icon>
              <v-icon small class="mx-auto">mdi-map</v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title>Startup Map</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list-group>

        <v-list-item :to="{ name: 'summary' }" exact>
          <v-list-item-icon>
            <v-icon small class="mx-auto">mdi-robot</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title>Summary</v-list-item-title>
          </v-list-item-content>
        </v-list-item>

        <v-list-item :to="{ name: 'live' }">
          <v-list-item-icon>
            <v-icon small class="mx-auto">mdi-information</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title>Live</v-list-item-title>
          </v-list-item-content>
        </v-list-item>

        <v-list-item
          :to="{ name: 'points_manager' }"
          v-if="!restrictions['points_manager']"
        >
          <v-list-item-icon>
            <v-icon small class="mx-auto">mdi-map-marker</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title>Point Manager</v-list-item-title>
          </v-list-item-content>
        </v-list-item>

        <v-list-item
          :to="{ name: 'act_manager' }"
          v-if="!restrictions['act_manager']"
        >
          <v-list-item-icon>
            <v-icon small class="mx-auto">mdi-play</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title>Act Manager</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        
        <v-list-item
          :to="{ name: 'interface_events' }"
          v-if="!restrictions['interface_events']"
        >
          <v-list-item-icon>
            <v-icon small class="mx-auto">mdi-view-carousel </v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title>Interface Events Manager</v-list-item-title>
          </v-list-item-content>
        </v-list-item>

        <v-list-item
          :to="{ name: 'story_manager' }"
          v-if="!restrictions['story_manager']"
        >
          <v-list-item-icon>
            <v-icon small class="mx-auto">mdi-book</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title>Story Manager</v-list-item-title>
          </v-list-item-content>
        </v-list-item>

        <v-list-item :to="{ name: 'bluetooth' }"
        v-if="!restrictions['bluetooth']">
          <v-list-item-icon>
            <v-icon small class="mx-auto">mdi-bluetooth</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title>Bluetooth</v-list-item-title>
          </v-list-item-content>
        </v-list-item>

        <v-list-item :to="{ name: 'voice' }"
        v-if="!restrictions['voice']"
        >
          <v-list-item-icon>
            <v-icon small class="mx-auto">mdi-pencil</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title>Speach Generater</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        

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
      :class="`${
        isDark
          ? 'blue-grey darken-4 grey--text text--lighten-4'
          : 'grey lighten-4 grey--text text--darken-2'
      } `"
    >
      <v-container fluid class="pa-0 ma-0">
        <router-view></router-view>
      </v-container>

      <v-footer
        class="blue-grey darken-2 text-center hidden-lg-and-down pa-0 ma-0"
        padless
        fixed
      >
        <v-card flat tile color="blue-grey darken-2" class="pa-0" width="100%">
          <v-card-text class="white--text pa-0 caption">
            {{ new Date().getFullYear() }} - <strong>Libyano</strong>
          </v-card-text>
        </v-card>
      </v-footer>
    </v-main>
  </v-app>
</template>

<script>
import env from "../env";
import ROSLIB from "roslib";
// ####################### connecting to ros #################################3
function sleep(duration) {
  return new Promise((resolve) => setTimeout(resolve, duration));
}
async function connect_to_ros() {
  var flag = true;
  var ros;
  while (flag) {
    await sleep(1500).then(() => {
      ros = new ROSLIB.Ros({
        url: `ws://${env.bridge_address}:9090`,
      });
      ros.on("connection", function () {
        flag = false;
        ////console.log('Ros: connected to rosbridge successfully')
      });
      ros.on("error", function () {
        console.error("error connecting to rosbridge");
      });
    });
  }
  return new Promise((resolve) => resolve(ros));
}
export default {
  computed: {
    status() {
      if (this.$store.getters["Ros/status"]["power"]) {
        return this.$store.getters["Ros/status"];
      } else {
        return this.temp_status;
      }
    },
    navDrawerExpansionArrow() {
      if (this.navDrawerMini) {
        return "mdi-arrow-right";
      }
      return "mdi-arrow-left";
    },
    isDark() {
      return this.$store.getters["Theme/isDark"];
    },
    auth() {
      return this.$store.getters["User/auth"];
    },
    alert() {
      return this.$store.getters["Notify/alert"];
    },
    notifyMessage() {
      return this.$store.getters["Notify/message"];
    },
    loading() {
      return this.$store.getters["Loading/get"];
    },
    mode() {
      return this.$store.getters["Ros/mode"];
    },
    restrictions() {
      return this.$store.getters["Router/get_restrictions"];
    },
    breakpoint() {
      var self = this;
      var size = "md";
      console.log(this.$vuetify.breakpoint.name);
      switch (size) {
        case "xs": {
          switch (self.$vuetify.breakpoint.name) {
            case "xs":
              return true;
            case "sm":
              return true;
            case "md":
              return true;
            case "lg":
              return true;
            case "xl":
              return true;
            default:
              return false;
          }
        }
        case "sm": {
          switch (self.$vuetify.breakpoint.name) {
            case "xs":
              return false;
            case "sm":
              return true;
            case "md":
              return true;
            case "lg":
              return true;
            case "xl":
              return true;
            default:
              return false;
          }
        }
        case "md": {
          switch (self.$vuetify.breakpoint.name) {
            case "xs":
              return false;
            case "sm":
              return false;
            case "md":
              return true;
            case "lg":
              return true;
            case "xl":
              return true;
            default:
              return false;
          }
        }
        case "lg": {
          switch (self.$vuetify.breakpoint.name) {
            case "xs":
              return false;
            case "sm":
              return false;
            case "md":
              return false;
            case "lg":
              return true;
            case "xl":
              return true;
            default:
              return false;
          }
        }
        case "xl": {
          switch (self.$vuetify.breakpoint.name) {
            case "xs":
              return false;
            case "sm":
              return false;
            case "md":
              return false;
            case "lg":
              return false;
            case "xl":
              return true;
            default:
              return false;
          }
        }
        default: {
          return false;
        }
      }
    },
    paused() {
      if (!this.story_status.pause_list) return "";
      if (!this.story_status.pause_list[0]) return "";
      if (
        this.story_status.pause_list.some((reason) => reason == "story_ended")
      )
        return "story ended";
      if (this.story_status.pause_list.some((reason) => reason == "user"))
        return "user paused";
      else return this.story_status.pause_list[0];
    },
  },
  data() {
    return {
      navDrawer: true,
      navDrawerMini: false,
      navigation_detached: false,
      story_status: {},
      temp_status: {
        power: {
          battery: "Unknown",
          charging_status: "Unknown",
          cord: "Unknown",
        },
        sensors: {
          temp: ["Unknown"],
        },
      },
    };
  },
  watch: {
    alert() {
      if (this.alert) {
        // console.log('App: alerting ...  ', this.notifyMessage);
        let n = this.notifyMessage;
        if (n.duration) {
          this.$notify({
            title: n.title,
            text: n.text,
            type: n.type,
            duration: n.duration,
            groupt: "main",
          });
        } else {
          this.$notify({
            title: n.title,
            text: n.text,
            type: n.type,
            group: "main",
          });
        }
        this.$store.dispatch("Notify/clear", null, { root: true });
      }
    },
  },
  methods: {
    toggle_mode() {
      if (this.mode == "") {
        return;
      } else {
        if (this.mode == "mnl") {
          this.$store
            .dispatch("Ros/take_action", "operation/main_switch/mnlcancel", {
              root: true,
            })
            .then((res) => {
              console.log(res);
              if (res == "no_default_story") {
                this.$store.dispatch(
                  "Notify/notify",
                  {
                    group: "main",
                    text: "There is no default story selected",
                    title: "No default story",
                    type: "warning",
                  },
                  { root: true }
                );
              }
            })
            .catch((err) => {
              console.log("error while cancelling mnl mode", err);
            });
        } else if (this.mode == "ato") {
          this.$store
            .dispatch("Ros/take_action", "operation/main_switch/mnl", {
              root: true,
            })
            .then((res) => {
              console.log(res);
            })
            .catch((err) => {
              console.log("error while switching to mnl mode", err);
            });
        }
      }
    },
    toggle_navigation_detach() {
      this.$store
        .dispatch("Ros/take_action", "navigation/toggle_detach", { root: true })
        .then((res) => {
          console.log(res);
        });
    },
    setIsDark() {
      console.log("App: changing theme");
      this.$store.dispatch("Theme/setDark", null, { root: true });
    },
    logout() {
      this.$store.dispatch("Loading/set", null, { root: true });
      console.log("Logging out");
      this.$store.dispatch("User/logout", null, { root: true }).then(() => {
        this.$router
          .push("login")
          .then(() => {})
          .catch((err) => {
            console.log(err);
          });
        this.$store.dispatch("Loading/clear", null, { root: true });
      });
    },
    toggle_pause_ato(){
      if(this.story_status.pause_list){
       if(this.story_status.pause_list.some(reason => reason =='user')){
         this.$store.dispatch('Ros/take_action', `operation/continue/user`, {root:true}).then(res=>{
           if(res == 'done'){
              this.$store.dispatch(
                "Notify/notify",
                {
                  group: "main",
                  text: "Story Continued Successfully.",
                  title: "Story Continued",
                  type: "success",
                },
                { root: true }
              );
           }else if(res == 'reason_not_found'){
              this.$store.dispatch(
                "Notify/notify",
                {
                  group: "main",
                  text: "Story is already running.",
                  title: "Story is running",
                  type: "warning",
                },
                { root: true }
              );
           }
         }).catch(err=>{
          console.log('error occured while trying to continue the story', err)
          this.$store.dispatch(
            "Notify/notify",
            {
              group: "main",
              text: `Error occured while trying to continue story ${err}.`,
              title: "Error",
              type: "error",
            },
            { root: true }
          );
         })
       }else{
         this.$store.dispatch('Ros/take_action', `operation/pause/user`, {root:true}).then(res=>{
           console.log(res)
           if(res == 'paused'){
              this.$store.dispatch(
                "Notify/notify",
                {
                  group: "main",
                  text: "Story Paused Successfully.",
                  title: "Story Paused",
                  type: "success",
                },
                { root: true }
              );
           }else if(res == 'reason_exists'){
              this.$store.dispatch(
                "Notify/notify",
                {
                  group: "main",
                  text: "Story is already Paused.",
                  title: "Story is paused",
                  type: "warning",
                },
                { root: true }
              );
           }
         }).catch(err=>{
          console.log('error occured while trying to pause the story', err)
          this.$store.dispatch(
            "Notify/notify",
            {
              group: "main",
              text: `Error occured while trying to pause story ${err}.`,
              title: "Error",
              type: "error",
            },
            { root: true }
          );
         })
       }
      }
    },
    restart_ato(){
      if(this.mode == 'ato'){
        this.$store.dispatch('Ros/take_action', 'operation/restart',{root:true}).then(()=>{
          this.$store.dispatch(
            "Notify/notify",
            {
              group: "main",
              text: `story is restarting`,
              title: "story restarted",
              type: "success",
            },
            { root: true }
          );
        }).catch(err=>{

          this.$store.dispatch(
            "Notify/notify",
            {
              group: "main",
              text: `Error occured while trying to restart story ${err}.`,
              title: "Error",
              type: "error",
            },
            { root: true }
          );

        })
      }
    }
  },
  created() {
    var self = this;

    connect_to_ros().then((ros) => {
      var story_status_sub = new ROSLIB.Topic({
        ros: ros,
        name: "/story_controller/get_status_json",
        messageType: "std_msgs/String",
      });
      story_status_sub.subscribe(function (data) {
        self.story_status = JSON.parse(data.data);
      });

      var status_sub = new ROSLIB.Topic({
        ros: ros,
        throttle_rate: 100,
        name: "/status",
        messageType: "status_msgs/status",
      });
      status_sub.subscribe(function (data) {
        self.$store.commit("Ros/setStatus", data);
      });
      var mode_sub = new ROSLIB.Topic({
        ros: ros,
        name: "/mode",
        throttle_rate: 100,
        messageType: "std_msgs/String",
      });
      mode_sub.subscribe(function (data) {
        self.$store.dispatch("Ros/setMode", data.data).then(() => {
          self.$store
            .dispatch("Router/update_restrictions", null, { root: true })
            .then(() => {
              if (
                self.$route.matched.some((route) => {
                  return !!self.restrictions[route.name];
                })
              ) {
                self.$router.push({
                  name: self.$store.getters["Router/get_unrestricted_route"],
                });
              }
            });
        });
      });
    });

    setInterval(() => {
      this.$store
        .dispatch("Ros/take_action", "navigation/is_detached", { root: true })
        .then((res) => {
          this.navigation_detached = res == "1" ? false : true;
        });
    }, 500);
    this.$store.dispatch("User/checkToken", null, { root: true });

    // setInterval(() => {
    //   if(self.auth && self.$store.getters['Ros/connectionFlag']){
    //     // self.$store.dispatch('Ros/fetchStatus',null, {root:true});
    //     // self.$store.dispatch('Ros/fetchMode',null,{root:true}).then(()=>{
    //       // self.$store.dispatch('Router/update_restrictions',null,{root:true}).then(()=>{
    //       //   if(self.$route.matched.some(route=>{
    //       //       // console.log(route.name,self.restrictions[route.name])
    //       //       return !!self.restrictions[route.name]
    //       //     })){
    //       //     self.$router.push({name:self.$store.getters['Router/get_unrestricted_route']})
    //       //   }
    //       // })
    //     // });
    //   }
    // }, 1000);
  },
};
</script>

<style scoped>
.loading {
  position: absolute;
  top: 0%;
  left: 0%;
  bottom: 0%;
  right: 0%;
  z-index: 10000;
  margin: 0px;
  /* background-image: url('./views/assets/Login.jpg'); */
  background-color: rgb(255, 255, 255, 1);
  background-size: cover;
  overflow: auto;
  background-repeat: no-repeat;
  /* transition:display 0.5s ease-in-out; */
}
</style>