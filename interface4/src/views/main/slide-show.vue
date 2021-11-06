<template>
  <v-carousel cycle height="100%">
    <v-carousel-item
      v-for="(item,i) in items"
      :key="i"
      :src="item.src"
      reverse-transition="fade-transition"
      transition="fade-transition"      
      @click="$router.push({name:'language'})"
    ></v-carousel-item>
  </v-carousel>
</template>

<script>
export default {
    data () {
      return {
        items: [
          {
            src: "assets/slideshow/1.png",
          },
          {
            src: "assets/slideshow/2.png",
          },
          {
            src: "assets/slideshow/3.png",
          },
          {
            src: "assets/slideshow/4.png",
          },
          {
            src: "assets/slideshow/5.png",
          },
        ],

        data: () => ({
            interactive: true,
        }),
      }
    },
    methods:{
    },
    created(){
      this.$store.dispatch('Interface/set_lang', 'en', {route: true})
    }
}
</script>

<style>

</style>