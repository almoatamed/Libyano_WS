<template>
    <v-container fluid style="margin-top:5%;">
        <v-row justify="center">

          <v-col md="4">
            <v-card @click="$router.push({name:'offers'})" rounded elevation="10" :img="require('../assets/services/stacked.svg')" min-height="140px" style="padding-top:25px;">
                <v-img :src="translateMedia('offers_icon')" width="260" style="margin-left:auto; margin-right:auto;"></v-img>
            </v-card>
          </v-col>
          
          <v-col md="4">
            <v-card @click="$router.push({name:'topup'})" rounded elevation="10" :img="require('../assets/services/stacked.svg')" min-height="140px" style="padding-top:25px;">
                <v-img :src="translateMedia('topup_icon')" width="260" style="margin-left:auto; margin-right:auto;"></v-img>
            </v-card>
          </v-col>

        </v-row>
        <v-row justify="center">

          <v-col md="4">
            <v-card @click="$router.push({name:'roaming'})" rounded elevation="10" :img="require('../assets/services/stacked.svg')" min-height="140px" style="padding-top:25px;">
                <v-img :src="translateMedia('roaming_icon')" width="260" style="margin-left:auto; margin-right:auto;"></v-img>
            </v-card>
          </v-col>
          
          <v-col md="4">
            <v-card @click="$router.push({name:'internet'})" rounded elevation="10" :img="require('../assets/services/stacked.svg')" min-height="140px" style="padding-top:25px;">
                <v-img :src="translateMedia('internet_icon')" width="260" style="margin-left:auto; margin-right:auto;"></v-img>
            </v-card>
          </v-col>

        </v-row>
    </v-container>
</template>

<script>
export default {
  methods: {
    translateMedia(src){
      return this.$store.getters['Interface/get_media'][src]
    },
    translate(phrase){
      var t_phrase = this.$store.getters['Interface/get_content'][phrase]
      if(!t_phrase){
        return phrase
      }else{
        return t_phrase
      }
    },
  }
}
</script>
