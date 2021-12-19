<template>
  <v-app>
    <v-container @click="touchy" fluid style="height:100%; background-color:#ecf0f1;">
        <v-row style="margin-top:10%">
            <v-col class="d-flex justify-center" md="12">
                <v-img id="battery" src="./assets/logo.svg" max-width="300"></v-img>
            </v-col>
        </v-row>
    </v-container>
  </v-app>
</template>

<script>
const child_process = require("child_process");

export default {
  name: 'App',
  methods:{
    touchy(){
      console.log('sdfsdfsdf')
      child_process.exec("rosnode list",(err,stdout,stderr)=>{
        console.log(err,stdout,stderr)
      });
    } 
  },

  data: () => ({
    //
  }),
};
</script>

<style>
@keyframes blink {
    0% {
        opacity: 1;
    }
    50% {
        opacity: 0;
    }
    100% {
        opacity: 1;
    }
}
#battery {
    -webkit-animation: blink 2s;
    -webkit-animation-iteration-count: 100;

    animation: blink 2s;
    animation-iteration-count: 100;
}
</style>