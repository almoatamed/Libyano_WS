<template>
  <v-carousel @click="serve()" v-model="model" class="pa-0 ma-0 hcontrol" :show-arrows="false" hide-delimiters cycle height="100%">
    <v-carousel-item
      class="img pa-0 ma-0 hcontrol"
      v-for="img in imgs"
      :key="img"
    >
      <v-sheet
        @click="serve()" 
        :color="img"
        height="100%"
        tile
        class="pa-0 ma-0"
      >
      <v-img
       :src="`img/${img}`"
       class="img"
      ></v-img>
      </v-sheet>
    </v-carousel-item>
  </v-carousel>
</template>

<script>
export default {
   data(){
      return {
         imgs:[
            'offers/4.jpg','offers/5.jpg','offers/3.jpg'
         ]
      }
   },
   methods:{
    serve(){
      this.$store.dispatch('Ros/change_mode', 'grt', {root:true})
    }
   },
   created(){
      this.$store.dispatch('Ros/change_mode', 'nav', {root:true})
   }
}
</script>

<style>
.img{
  display: block;
  max-width: 100%;
  min-width: 100%;
}
body, html, div{
 overflow: hidden;
}
.hcontrol{
  max-height: 100%;
}
</style>