<template>
  <v-app id="app">


      <div class="loading" v-if="loading">
        <v-progress-circular
          style="position:fixed;top:50%;left:50%;"
          :size="50"
          color="primary"
          indeterminate
        ></v-progress-circular>
      </div>

      <v-app-bar
      v-if='interactive'
      flat
      color='bar_color'
      app
      clipped-left
      dark
      > 
        <v-btn color="btn_color" class="pa-4 px-6" @click="$router.go(-1)" rounded>Back</v-btn>
        <v-spacer></v-spacer>
        <v-img
          class="mx-2"
          src="img/stream_icon.png"
          max-height = '40'
          max-width = '40'
          contain
        ></v-img>
        <v-img
          class="mx-2"
          src="img/libyano_icon.png"
          max-height = '40'
          max-width = '40'
          contain
        ></v-img>
      </v-app-bar>
      

      <v-main 
      class="grey lighten-4 grey--text text--darken-2"
      >
        <v-container fluid class="ma-0 pa-0 fill-height">
          <router-view></router-view>
        </v-container>
      </v-main>
      <v-footer app height="80"  v-if='interactive'>
        <v-row justify="center">
          <v-img cover src="img/grid.png" class="mt-4" ></v-img>
        </v-row>
      </v-footer>
  </v-app>

</template>


<script>
export default {
  computed: {
    loading(){
      return this.$store.getters['Loading/getLoading']
    },
    interactive(){
      return this.$store.getters['Interactive/get_interactive']
    }
  },
  data () {
    return{
    }
  },
  methods:{
  },
  created(){
    var self = this;
    self.$store.dispatch('Loading/setLoading',null,{root:true})
    self.$store.dispatch('Ros/init',null, {root:true}).then(()=>{
      self.$store.dispatch('Loading/clearLoading',null, {root:true})
    })
  }
}
</script>

<style>

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