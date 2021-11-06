<template>
  <v-container fluid id='root' fill-height class="pa-0 ma-0">
    <router-view></router-view>
  </v-container>
</template>

<script>
export default {
    data:()=>({
        interval_holder:null

    }),
    computed:{
        mode(){
            return this.$store.getters['Ros/mode']
        }
    },
    created(){
        var self = this
        console.log('Createed startup ')
        self.$store.dispatch('Ros/take_action', 'startup/get_current_stage', {root:true}).then(res=>{
            if(!res){
                if(this.mode == 'str'){
                    self.$store.dispatch('Ros/take_action', 'startup/begin', {root:true}).then(res=>{
                        console.log('beginning the str' ,res)
                        self.check_periodically()
                    })
                }
            }else{
                self.check_periodically()
            }
        })
    },
    methods:{
        check_periodically(){
            this.interval_holder = setInterval(() => {
                this.$store.dispatch('Ros/take_action', 'startup/remote_interface',{root:true}).then(res=>{
                    // console.log('current startup interface', 'startup_' + res)
                    if(this.$route.name != 'startup_' + res){
                        this.$router.push({name:'startup_' + res})
                    }
                })
            }, 250);
        }
    },
    beforeDestroy(){
        clearInterval(this.interval_holder) 
    }
}
</script>

<style>

</style>