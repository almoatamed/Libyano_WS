<template>

    <!-- Loading -->
    <div class="loading" style="display:grid;place-items:center;">
        <v-container fluid>
            <v-row>
                <v-col
                style="display: flex; justify-content: space-around"
                cols="12"
                >
                    <div
                    class="text-h6 font-weight-bold"
                    style="text-align: center;"
                    >{{loading.title}}</div>
                </v-col>
                <v-col
                style="display: flex; justify-content: space-around"
                >
                    <v-progress-circular
                        :size="50"
                        color="primary"
                        style="text-align: center;"
                        indeterminate
                    ></v-progress-circular>
                </v-col>
            </v-row>
        </v-container>
      <!-- <v-card
        class="transition-fast-in-fast-out v-card--reveal pa-4"
        elevation="6"
        dark
      >
        <v-card-title
          class="text-h6 font-weight-bold"
          style="text-align: center; padding-top: 30px"
          >{{loading.title}}</v-card-title
        >
        <v-card-text v-if="loading.timer != -1"
          class="text-h6 font-weight-bold"
          style="text-align: center; padding-top: 10px"
        >
          {{ loading.timer }}
        </v-card-text>
        <v-card-text class="">
        </v-card-text>
      </v-card> -->
    </div>  
</template>

<script>
export default {
    data:()=>({
        loading:{
            title:'Processing... '
        }
    })
}
</script>

<style scoped>
.loading {
  position: absolute;
  top: 0%;
  left: 0%;
  bottom: 0%;
  right: 0%;
  margin: 0px;
  /* background-image: url('./views/assets/Login.jpg'); */
  background-color: rgb(255, 255, 255,0.1);
  background-size: cover;
  overflow: auto;
  background-repeat: no-repeat;
  /* transition:display 0.5s ease-in-out; */
}
</style>