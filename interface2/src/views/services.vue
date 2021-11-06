<template>
    <v-container fluid style="margin-top:5%">
        <v-row justify="center">

          <v-col md="4">
            <v-card @click="$router.push({name:'offers'})" tile elevation="10" color="libyana" min-height="140px" style="padding-top:25px;">
                <v-img src='../assets/offers_icon.svg' max-width="260" max-height="140px" style="margin-left:80px;"></v-img>
            </v-card>
          </v-col>
          
          <v-col md="4">
            <v-card @click="$router.push({name:'topup'})" tile elevation="10" color="libyana" min-height="140px" style="padding-top:25px;">
                <v-img src='../assets/topup_icon.svg' max-width="260" max-height="140px" style="margin-left:80px;"></v-img>
            </v-card>
          </v-col>

        </v-row>
        <v-row justify="center">

          <v-col md="4">
            <v-card @click="$router.push({name:'roaming'})" tile elevation="10" color="libyana" min-height="140px" style="padding-top:25px;">
                <v-img src='../assets/roaming_icon.svg' max-width="260" max-height="140px" style="margin-left:80px;"></v-img>
            </v-card>
          </v-col>
          
          <v-col md="4">
            <v-card tile elevation="10" color="libyana" min-height="140px" style="padding-top:25px;">
                <v-img src='../assets/internet_icon.svg' max-width="260" max-height="140px" style="margin-left:80px;"></v-img>
            </v-card>
          </v-col>

        </v-row>
    </v-container>
</template>
<script>
// export default {
//   data(){
//     return {
//       goback_timeout: null,
//     }
//   },
//   methods:{
//     change_mode(){
//       this.$store.dispatch('Ros/change_mode','grtcancel', {root:true}).then(()=>{}).catch(err=>{
//         console.error('Error while trying to change mode from interface', err)
//       })
//     },
//     reset_goback_timeout(){
//       clearTimeout(this.goback_timeout)
//       console.log('resetting time out on services')
//       this.goback_timeout = setTimeout(()=>{
//         this.reset_goback_timeout()
//         this.change_mode();
//       },this.timeout_val)
//     }
//   },
//   created(){
//     this.goback_timeout = setTimeout(()=>{
//       this.reset_goback_timeout()
//       this.change_mode();
//     },this.timeout_val)
//     window.addEventListener('click', this.reset_goback_timeout)
//   },
//   beforeDestroy(){
//     console.log('destroying services')
//     clearTimeout(this.goback_timeout)
//     window.removeEventListener('click', this.reset_goback_timeout)
//   },
//   computed:{
//     timeout_val(){
//       return this.$store.getters['Interface/get_timeout_val']
//     }
//   }
// }
</script>