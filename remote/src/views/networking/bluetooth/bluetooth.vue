<template>
  <div id="root">
    <!-- Loading -->
    <div class="loading" v-if="loading.show" style="display:grid;place-items:center;">
      <v-card
        class="transition-fast-in-fast-out v-card--reveal pa-4"
        elevation="6"
        dark
      >
        <v-card-title
          class="text-h6 font-weight-bold"
          style="text-align: center; padding-top: 30px"
          >{{loading.title}}</v-card-title
        >
        <v-card-text v-if="loading.timer != -1"
          class="text-h6 font-weight-bold"
          style="text-align: center; padding-top: 10px"
        >
          {{ loading.timer }}
        </v-card-text>
        <v-card-text class="">
            <v-container fluid>
                <v-row>
                    <v-col
                    style="display: flex; justify-content: space-around"
                    >
                        <v-progress-circular
                            :size="50"
                            color="primary"
                            style="text-align: center; padding-top: 10px"
                            indeterminate
                        ></v-progress-circular>
                    </v-col>
                </v-row>
            </v-container>
        </v-card-text>
      </v-card>
    </div>

    <v-container>

      <!-- Title -->
      <div class="text-h4">Bluetooth Controller</div>
      <v-divider class="py-4"></v-divider>

      <v-card  elevation="6" :dark="isDark">

        <!-- Actions -->
        <v-container fluid>
          <v-row>
            <v-col cols="12">
              <div class="text-h6">Actions</div>
            </v-col>
            <v-col
              cols="12"
              class="flex-wrap justify-space-between"
            >
              <v-btn :disabled="false" @click='disconnect' :loading="false" text color="purple">
                Disconnect
              </v-btn>

              <v-btn :disabled="false" @click='reset_volume_control' :loading="false" text color="purple">
                reset volume
              </v-btn>

              <v-btn :disabled="false" @click="clear_default" :loading="false" text color="purple">
                Clear Default
              </v-btn>

              <v-btn :loading="false" @click="set_default" :disabled="!bluetooth.connect_table.show" text color="purple">
                Set Default
              </v-btn>

              <v-btn :loading="false" @click="connect_default" text color="purple">
                Connect Default
              </v-btn>


              <v-btn :disabled="false" @click="scan" :loading="false" text color="purple">
                scan
              </v-btn>
            </v-col>
          </v-row>
        </v-container>

        <!-- Divider -->
        <v-container fluid>
          <v-row>
            <v-col cols="12">
              <v-divider></v-divider>
            </v-col>
          </v-row>
        </v-container>

        <!-- Connected Devices Table -->
        <v-container fluid >
          <v-row>
            <v-col cols="12">
              <div class="text-h6">Connected Devices</div>
            </v-col>
            <v-col v-if="bluetooth.connect_table.show" cols="12">
              <v-data-table
                :headers="bluetooth.connect_table.headers"
                :items="bluetooth.connect_table.data"
                class="elevation-1"
              ></v-data-table>
            </v-col>
            <v-col cols="12" v-else class="">
              <v-container 
              style="display: flex; justify-content: space-around"
              >
                <span class="">{{bluetooth.connect_table.alternative}}</span>
              </v-container>
            </v-col>
          </v-row>
        </v-container>

        <!-- Divider -->
        <v-container fluid id>
          <v-row>
            <v-col cols="12">
              <v-divider></v-divider>
            </v-col>
          </v-row>
        </v-container>


        <!-- Scanned Devices Table -->
        <v-container fluid >
          <v-row>
            <v-col cols="12">
              <div class="text-h6">Scanning Results</div>
            </v-col>
            <v-col v-if="bluetooth.scan_table.show" cols="12">
              <v-data-table
                :headers="bluetooth.scan_table.headers"
                :items="bluetooth.scan_table.data"
                class="elevation-1"
              >
                <template v-slot:item.actions="{ item }">
                  <v-icon small class="mr-2" :disabled='bluetooth.connect_table.show' @click="connect(item.uuid)">
                    mdi-bluetooth-connect
                  </v-icon>
                </template>
              </v-data-table>
            </v-col>
            <v-col cols="12" v-else class="">
              <v-container 
              style="display: flex; justify-content: space-around"
              >
                <span class="">{{bluetooth.scan_table.alternative}}</span>
              </v-container>
            </v-col>
          </v-row>
        </v-container>

      </v-card>
    </v-container>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  data: () => ({
    loading: {
      show: true,
      timer: -1,
      timer_state: false,
      interval_holder: null,
    },
    bluetooth: {
      defaults:{
        scan_table: {
          headers: [
            { text: "Name", value: "name", align: "start" },
            { text: "UUID", value: "uuid" },
            { text: "Connect", value: "actions", sortable: false },
          ],
          show: false,
          data: null,
        },
        connect_table: {
          headers: [
            { text: "Name", value: "name", align: "start" },
            { text: "UUID", value: "uuid" },
            { text: "Default", value: "default" },
          ],
          show: false,
          data: null,
          alternative:null
        },
      },
      scan_table: {
        headers: [
          { text: "Name", value: "name", sortable: false, align: "start" },
          { text: "UUID", value: "uuid" },
          { text: "Connect", value: "actions", sortable: false },
        ],
        show: false,
        data: null,
        alternative:'Please Scan To Show Nearbye Devices',
      },
      connect_table: {
        headers: [
          { text: "Name", value: "name", sortable: false, align: "start" },
          { text: "UUID", value: "uuid" },
          { text: "Default", value: "default" },
        ],
        show: false,
        data: null,
        alternative:null
      },
      default:null
    },
  }),

  computed: {
    ...mapGetters("Theme", ["isDark"]),

  },

  created() {
    this.update();
  },

  methods: {
    scan() {
      this.set_loading(true,'Loading...', 15)
      Object.assign(this.bluetooth.scan_table, this.bluetooth.defaults.scan_table)
      this.$store.dispatch('Ros/take_action', 'bluetooth/scan', {root:true}).then(res=>{
        console.log('Bluetooth Scanning results Camse Back', res)
        if(res == 'no_scan'){ 
          this.bluetooth.scan_table.alternative = 'No Devices Found'
        }else{
          var dev_list = []
          res = res.split('|')
          res.forEach((el) => {
            el = el.split('/')
            if(!dev_list.find(dev=>dev.uuid == el[0])){
              dev_list.push({
                  name:el[1],
                  uuid:el[0]
              })         
            }
          });
          console.log(dev_list)
          this.bluetooth.scan_table.data = dev_list
          this.bluetooth.scan_table.show = true
        }
        this.update()
        this.set_loading(false)
      }).catch(err=>{
        console.log(err)
        this.set_loading(false)
      })
    },

    update() {
      this.set_loading(true,'Loading...');
      Object.assign(this.bluetooth.connect_table, this.bluetooth.defaults.connect_table)
      this.$store.dispatch("Ros/take_action", "bluetooth/get_default", { root: true }).then(res=>{
            console.log('default bluetooth dev', res)
            if(res == 'empty'){
              this.bluetooth.default = null
            }else{
              this.bluetooth.default = res
            }
            this.$store.dispatch('Ros/take_action', 'bluetooth/connected',{ root:true }).then(res=>{
                console.log('connected devices', res)
                if(res.slice(0,4) == 'not_'){
                  this.bluetooth.connect_table.alternative = 'No Connection Found'
                }else{
                  res = res.split('|')
                  res.forEach((el,index) => {
                    el = el.split('/')
                    console.log(el[0], this.bluetooth.default)
                    res[index] = {
                        name:el[1],
                        uuid:el[0],
                        default:this.bluetooth.default == el[0]? 'Yes': 'No'
                      }                    
                  });
                  this.bluetooth.connect_table.data = res
                  this.bluetooth.connect_table.show = true
                }
                this.set_loading(false)
            }).catch(err=>{
                console.log(err)
                this.set_loading(false)
            }); 
      }).catch(err=>{
          console.log(err)
          this.set_loading(false)
      }); 
    },

    disconnect() {
      console.log("disconnecting ");
      Object.assign(this.bluetooth.connect_table, this.bluetooth.defaults.connect_table)
      this.set_loading(true, 'Disconnecting...')
      this.$store.dispatch('Ros/take_action', 'bluetooth/disconnect', {root:true}).then(res=>{
        console.log('disconnecting finished wiht ', res)
        this.update()
      }).catch(err=>{
        console.log(err)
        this.set_loading(false)
      })
    },

    clear_default() {
      this.$store.dispatch('Ros/take_action', 'bluetooth/clear_default', {root:true}).then(res=>{
        console.log('Clearing Default Done', res)
        this.update()
      }).catch(err=>{
        console.log('Error while Clearing Default', err)
        this.update()
      })
    },

    reset_volume_control() {
      this.$store.dispatch('Ros/take_action', 'bluetooth/reset_volume/100', {root:true}).then(res=>{
        console.log('Clearing Default Done', res)
        this.update()
      }).catch(err=>{
        console.log('Error while Clearing Default', err)
        this.update()
      })
    },

    set_default() {
      console.log("setting default ");
      if(this.bluetooth.connect_table.show && this.bluetooth.connect_table.data){
        var uuid = this.bluetooth.connect_table.data[0].uuid
        this.$store.dispatch('Ros/take_action', 'bluetooth/set_default/'+uuid).then(res=>{
          console.log('Done', res)
          this.update()
        }).catch(err=>{
          console.log('Error while setting default bluetooth device', err)
          this.update()
        })
      }

    },

    connect_default() {
      console.log("setting default ");
      this.$store.dispatch('Ros/take_action', 'bluetooth/connect_default/0').then(res=>{
        console.log('Done', res)
        this.update()
      }).catch(err=>{
        console.log('Error while setting default bluetooth device', err)
        this.update()
      })

    },

    connect(uuid) {
      console.log("setting connection ", uuid);
      Object.assign(this.bluetooth.connect_table, this.bluetooth.defaults.connect_table)
      this.set_loading(true, 'Connecting...')
      this.$store.dispatch('Ros/take_action', 'bluetooth/connect/'+uuid, {root:true}).then(res=>{
        console.log('connecting finished wiht ', res)
        this.update()
      }).catch(err=>{
        console.log(err)
        this.update()
        this.set_loading(false)
      })
    },

    set_loading(loading_state, title = "", timeout = -1) {
      console.log("setting loading", loading_state, timeout);
      if (loading_state) {
        this.loading.show = loading_state;
        this.loading.title = title;
        if (timeout != -1) {
          this.loading.timer = timeout;
          this.loading.interval_holder = setInterval(() => {
            this.loading.timer -= 1;
            if (this.loading.timer <= 1) {
              clearInterval(this.interval_holder);
              this.loading.timer = -1
            }
          }, 1e3);
        }else{
            clearInterval(this.interval_holder);
            this.loading.timer = -1
        }
      }else{
        this.loading.show = false;
        clearInterval(this.interval_holder);
        this.loading.timer = -1
      }
    },
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
  background-color: rgb(255, 255, 255,0.1);
  background-size: cover;
  overflow: auto;
  background-repeat: no-repeat;
  /* transition:display 0.5s ease-in-out; */
}
</style>