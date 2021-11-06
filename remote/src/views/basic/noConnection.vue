<template>
    <v-container class='center'> 
        <v-row>
            <v-col
            cols='12'
            >
                <h4 class="text-h2 text-center">Ros Not Connected</h4>
            </v-col>
            <v-col
            cols='12'
            >
                <v-img src="../../assets/404.png" min-width="100px" max-width="200" class='mx-auto'></v-img>
            </v-col>
        </v-row>
        
    </v-container>
</template>

<script>
export default {
    created(){
      this.$store.dispatch('Loading/set',null,{root:true});
      this.$store.dispatch('Ros/fetchConnectionFlag',null,{root:true}).then(()=>{
        console.log('clearing Loading')
        this.$store.dispatch('Loading/clear',null,{root:true})
        if(!this.$route.meta.requiresConnectoin && this.$route.name !== null){
          this.$router.push(this.$route.query.redirect).catch((err) =>{
              if(err.type != 2){ throw new Error(`something went wrong while pushing ${err}`)}
          })
        }
      }).catch(()=>{
        this.$store.dispatch('Loading/clear',null,{root:true})
      });
    }
}
</script>

<style scoped>
 .center{
  margin: 0;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
 }
</style>