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
                    >Is the robot charging.</div>
                </v-col>
                <v-col
                style="display: flex; justify-content: space-around"
                >
                    <div
                    class="font-weight-bold"
                    style="text-align: center;"
                    >If the robot is in the charging dock, please confirm.
                     
                    </div>
                </v-col>
                <v-col cols="12"  style="display: flex; justify-content: space-around">
                    <v-dialog
                    v-model="dialog"
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
                         Is chargin
                        </v-btn>
                    </template>

                    <v-card class="pa-4">
                        <v-card-title class="">
                            is the robot charging
                        </v-card-title>

                        <v-divider></v-divider>

                        <v-card-actions>
                        <v-btn
                            color="purple"
                            text
                            @click="yes_charging();dialog=false"
                        >
                            Yes
                        </v-btn>
                        <v-spacer></v-spacer>
                        <v-btn
                            color="purple"
                            text
                            @click="not_charging();dialog=false"
                        >
                            No
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
        dialog:false
    }),
    methods:{
        yes_charging(){
            this.dialog = false
            console.log('Where There is Will there is Way')
            this.$store.dispatch('Ros/take_action', 'startup/remote_interface', {root:true}).then(res=>{
                if(res=='is_the_robot_charging'){
                    this.continue_loading= true
                    console.log(res)
                    this.$store.dispatch('Ros/take_action', 'startup/perform/power_stage/confirm/yes', {root:true}).then(res=>{
                        console.log(res)
                    })
                }
            })
        },
        not_charging(){
            this.dialog = false
            console.log('Where There is Will there is Way')
            this.$store.dispatch('Ros/take_action', 'startup/remote_interface', {root:true}).then(res=>{
                if(res=='is_the_robot_charging'){
                    this.continue_loading= true
                    console.log(res)
                    this.$store.dispatch('Ros/take_action', 'startup/perform/power_stage/confirm/no', {root:true}).then(res=>{
                        console.log(res)
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