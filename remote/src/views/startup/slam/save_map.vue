<template>
    <div class="loading" style="display:grid;place-items:center;">
        <v-container fluid>
            <v-card  class="mx-auto" max-width="400" :dark='isDark' rounded="lg">
                <v-card-title class="">
                    Save Map
                </v-card-title>

                <v-card-text>
                    What do you want to call the map?
                </v-card-text>

                <v-card-text>
                    <v-form ref='name'>
                        <v-text-field
                        v-model="name"
                        color="purple darken-2"
                        label="Map name"
                        :rules="name_rules"
                        required
                        ></v-text-field>
                    </v-form>
                </v-card-text>

                <v-divider></v-divider>

                <v-card-actions>                    
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
                        text
                        :loading='continue_loading'
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
                            If you cancel the slamming procedure all the work has been done will be ignored.
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
                <v-spacer></v-spacer>
                <v-btn
                    color="purple"
                    text
                    :loading='continue_loading'
                    :disabled="continue_loading"
                    @click="save_map()"
                >
                    Save
                </v-btn>
                </v-card-actions>
            </v-card>
        </v-container>
    </div>
</template>

<script>
export default {
    computed:{
        isDark(){
            return this.$store.getters['Theme/isDark']
        },
        name_rules(){
            var Rules = [
                v => ((v || '').length <= 50) || 'Name must be less then 50 characters',
                v => ((v || '').indexOf(' ') < 0) || 'Name cannot conatin spaces',
                v => !!v || 'Name is Required'
            ]
            return Rules
        },
    },
    data:()=>({
        name:'',
        cancel_dialog: false,
        continue_loading: false
    }),
    methods:{
        not_valid(){
            return this.name.length
        },
        save_map(){
            console.log(this.$refs.name.validate())
            if(!this.$refs.name.validate()){
                return 
            }
            this.continue_loading = true
            console.log('Where There is Will there is Way')
            this.$store.dispatch('Ros/take_action', 'startup/remote_interface', {root:true}).then(res=>{
                console.log(res)
                if(res=='slam_save_scanned_map'){
                    this.continue_loading= true
                    console.log(res)
                    this.$store.dispatch('Ros/take_action', `startup/perform/slam/confirm/${this.name}`, {root:true}).then(res=>{
                        console.log(res)
                    })
                }
            })
        },
        cancel(){
            this.continue_loading = true
            console.log('Where There is Will there is Way')
            this.$store.dispatch('Ros/take_action', 'startup/remote_interface', {root:true}).then(res=>{
                if(res=='slam_save_scanned_map'){
                    console.log(res)
                    this.$store.dispatch('Ros/take_action', 'startup/perform/slam/confirm/end', {root:true}).then(res=>{
                        console.log(res)
                        this.$router.push({name:'startup_loading'})
                    })
                }else{
                    this.continue_loading = false
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