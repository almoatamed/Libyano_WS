<template>
    <div class="loading" style="display:grid;place-items:center;">
        <v-container fluid>
            <v-row>
                <v-col
                style="display: flex; justify-content: space-around"
                cols="12"
                >
                    <div
                    class="text-h5 font-weight-bold"
                    style="text-align: center;"
                    >I want to go home!</div>
                </v-col>
                <v-col
                style="display: flex; justify-content: space-around"
                >
                    <div
                    class="font-weight-bold"
                    style="text-align: center;"
                    >
                     In order to continue the slamming process the robot must go to the chargin spot, give permission for it to autonomously go to the chargin Dock
                    </div>
                </v-col>
                <v-col cols="12"  style="display: flex; justify-content: space-around">
                    <v-dialog
                    v-model="cancel_dialog"
                    :dark='isDark'
                    width="500"
                    >
                    <template v-slot:activator="{ on, attrs }">
                        <v-btn
                        color="purple white--text"
                        :dark='isDark'
                        v-bind="attrs"
                        v-on="on"
                        :disabled="continue_loading"
                        >
                         Cancel
                        </v-btn>
                    </template>

                    <v-card class="pa-4">
                        <v-card-title class="">
                            Cancel Salmming
                        </v-card-title>

                        <v-card-text>
                            If you cancel the slamming procedure all the work has been done will be ignored
                            <br> Cancel?
                        </v-card-text>

                        <v-divider></v-divider>

                        <v-card-actions>
                        <v-btn
                            color="purple"
                            text
                            @click="cancel();cancel_dialog=false"
                        >
                            Yes
                        </v-btn>
                        <v-spacer></v-spacer>
                        <v-btn
                            color="purple"
                            text
                            @click="cancel_dialog = false"
                        >
                            No
                        </v-btn>
                        </v-card-actions>
                    </v-card>
                    </v-dialog>
                    <v-dialog
                    v-model="go_home_dialog"
                    :dark='isDark'
                    width="500"
                    >
                    <template v-slot:activator="{ on, attrs }">
                        <v-btn
                        color="purple white--text"
                        :dark='isDark'
                        v-bind="attrs"
                        v-on="on"
                        :disabled="continue_loading"
                        >
                         Go Home
                        </v-btn>
                    </template>

                    <v-card class="pa-4">
                        <v-card-title class="">
                            Go Home
                        </v-card-title>

                        <v-card-text>
                            Let the robot autonomously go to the charging Dock?
                        </v-card-text>

                        <v-divider></v-divider>

                        <v-card-actions>
                        <v-btn
                            color="purple"
                            text
                            @click="go_home();go_home_dialog=false"
                        >
                            Yes
                        </v-btn>
                        <v-spacer></v-spacer>
                        <v-btn
                            color="purple"
                            text
                            @click="go_home_dialog = false"
                        >
                            Not Yet
                        </v-btn>
                        </v-card-actions>
                    </v-card>
                    </v-dialog>
                </v-col>
            </v-row>
        </v-container>
    </div>
</template>

<script>
export default {
    computed:{
        isDark(){
            return this.$store.getters['Theme/isDark']
        }
    },
    data:()=>({
        continue_loading:false,
        cancel_dialog:false,
        go_home_dialog:false,
    }),
    methods:{
        go_home(){
            console.log('Where There is Will there is Way')
            this.$store.dispatch('Ros/take_action', 'startup/remote_interface', {root:true}).then(res=>{
                if(res=='slam_wants_to_go_home'){
                    this.continue_loading= true
                    console.log(res)
                    this.$store.dispatch('Ros/take_action', 'startup/perform/slam/confirm/yes', {root:true}).then(res=>{
                        console.log(res)
                    })
                }
            })
        },
        cancel(){
            console.log('Where There is Will there is Way')
            this.$store.dispatch('Ros/take_action', 'startup/remote_interface', {root:true}).then(res=>{
                if(res=='slam_wants_to_go_home'){
                    console.log(res)
                    this.$store.dispatch('Ros/take_action', 'startup/perform/slam/confirm/end', {root:true}).then(res=>{
                        console.log(res)
                        this.$router.push({name:'startup_loading'})
                    })
                }
            })
        }
    }
}
</script>

<style scoped>
.loading {
  position: absolute;
  top: 0%;
  left: 0%;
  bottom: 0%;
  right: 0%;
  margin: 0px;
  background-color: rgb(255, 255, 255,0.1);
  background-size: cover;
  overflow: auto;
  background-repeat: no-repeat;
}
</style>