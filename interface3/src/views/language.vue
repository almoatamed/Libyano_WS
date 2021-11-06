<template>
  <v-container fluid style="padding:0px;">
    <v-row>
      <v-col md="12">
        <v-img
          :src="require('../assets/lang/logo_lg.svg')"
          max-width="280"
          style="display: block;
                margin-left: auto;
                margin-right: auto;
                width: 40%;
                margin-top:5%;"
        ></v-img>
      </v-col>
    </v-row>
    <v-row style="padding-top:5%" no-gutters>
      <v-col md="4">
        <v-img
          @click="serve('en')"
          :src="require('../assets/lang/eng.svg')"
          max-width="420"
          style="display: block;
                margin-left: auto;
                margin-right: auto;
                width: 40%;"
        ></v-img>
      </v-col>
      <v-col md="4">
        <v-img
          @click="serve('ar')"
          :src="require('../assets/lang/arb.svg')"
          max-width="420"
          style="display: block;
                margin-left: auto;
                margin-right: auto;
                width: 40%;"
        ></v-img>
      </v-col>
      <v-col md="4">
        <v-img
          :src="require('../assets/lang/amzg.svg')"
          max-width="420"
          style="display: block;
                margin-left: auto;
                margin-right: auto;
                width: 40%;"
        ></v-img>
      </v-col>
    </v-row>

    <v-row>
      <v-col md="12">
        <div id="cf">
          <img
            :src="require('../assets/lang/explr_en.svg')"
            style="width:600px; margin-left:30%; padding-top:50px;"
            class="bottom"
          />
          <img
            :src="require('../assets/lang/explr_ar.svg')"
            class="top"
            style="width:600px; margin-left:30%; padding-top:50px;"
          />
        </div>
      </v-col>
    </v-row>
    <v-img :src="require('../assets/lang/waves2.svg')" style="margin-top:12.35%; padding:0px;"></v-img>
  </v-container>
</template>

<!-- CSS Animation for pick language -->
<style>
#cf img {
  position: absolute;
  left: 0;
  -webkit-transition: opacity 1s ease-in-out;
  -moz-transition: opacity 1s ease-in-out;
  -o-transition: opacity 1s ease-in-out;
  transition: opacity 1s ease-in-out;
}

@keyframes cf3FadeInOut {
  0% {
    opacity: 1;
  }
  45% {
    opacity: 1;
  }
  55% {
    opacity: 0;
  }
  100% {
    opacity: 0;
  }
};

#cf img.top {
  animation-name: cf3FadeInOut;
  animation-timing-function: ease-in-out;
  animation-iteration-count: infinite;
  animation-duration: 4s;
  animation-direction: alternate;
};

</style>


<script>
export default {
  methods: {
    serve(lang) {
      this.get_lang(lang)
      this.$router.push({name:'services'})

    },
    get_lang(lang) {
      this.$store.dispatch('Interface/set_lang', lang, {route: true})
    }
  }
}
</script>