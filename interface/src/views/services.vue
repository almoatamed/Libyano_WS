<template>
  <v-container>
    <v-row height="10%" class="colbar text-center">
      <v-spacer></v-spacer>
      <v-btn color="btn_color" width="150" @click="$router.push({name:'topup'})" dark  class="pa-4 px-6" rounded large>Top-Up</v-btn>
      <v-spacer></v-spacer>
      <v-spacer></v-spacer>
      <v-btn color="btn_color" width="150" @click="$router.push({name:'offers'})" dark  class="pa-4 px-6" rounded large>Offers</v-btn>
      <v-spacer></v-spacer>
    </v-row>

    <v-row height="10%" class="ma-4 colbar text-center">
      <v-spacer></v-spacer>
      <img src="img/1x/libyano.png" height="220" alt="">
      <v-spacer></v-spacer>
    </v-row>

    <v-row height="10%" class="colbar text-center">
      <v-spacer></v-spacer>
      <v-btn color="btn_color" width="150" @click="$router.push({name:'roaming'})" dark  class="pa-4 px-6" rounded large>Roaming</v-btn>
      <v-spacer></v-spacer>
      <v-spacer></v-spacer>
      <v-btn color="btn_color" width="150" @click="$router.push({name:'internet'})" dark  class="pa-4 px-6" rounded large>Internet</v-btn>
      <v-spacer></v-spacer>
    </v-row>
  </v-container>
</template>
<style scoped>
</style>
