<template>
  
    <div class="loading" style="display:grid;place-items:center;">
        <v-container fluid>
            <v-row>
                <v-col
                style="display: flex; justify-content: space-around"
                cols="12"
                >
                    <div
                    class="text-h5 font-weight-bold"
                    style="text-align: center;"
                    >Please Remove The DC Cord</div>
                </v-col>
                <v-col
                style="display: flex; justify-content: space-around"
                >
                    <div
                    class="font-weight-bold"
                    style="text-align: center;"
                    >After removing the cord the startup process will continue normally.</div>
                </v-col>
            </v-row>
        </v-container>
    </div>

</template>

<script>
export default {

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