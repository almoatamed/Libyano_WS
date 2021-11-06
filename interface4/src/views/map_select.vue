<template>
    <v-container fluid style=" background-color:#0f0f33; height:100%;">
      <v-row style="margin-top:8%;">
        <v-col md="12"> <h1 class="white--text d-flex justify-center align-center">Please Choose any of the following methods to start Libyano!</h1></v-col>
      </v-row>
        <v-row justify="center" style="margin-top:8%;">

          <v-col md="4" class="d-flex justify-center align-center">
            <v-btn @click="loadMap()" color="primary" width="280" height="140" style="font-size:18px;"> Load Map </v-btn>
          </v-col>
          
          <v-col md="4" class="d-flex justify-center align-center">
            <v-btn @click="createMap()" width="280" color="primary" height="140" style="font-size:18px;"> Create New Map </v-btn>
          </v-col>

          <v-col md="4" class="d-flex justify-center align-center">
            <v-btn @click="fileMap()" color="primary" width="280" height="140" style="font-size:18px;"> Load From File </v-btn>
          </v-col>
        </v-row>

        <v-dialog v-model="loadMapD">
          <v-card elevation="1" color="#CB9F49">
          <v-card-title>Saved Maps:</v-card-title>
          <v-simple-table>
            <tbody>
              <tr>
                <td width="60%">map name1</td>
                <td>
                  <v-chip class="ma-2" close color="red" text-color="white">
                    Remove
                  </v-chip>
                  <v-chip class="ma-2">
                    Default
                  </v-chip>
                </td>
              </tr>
              <tr>
                <td width="60%">map name2</td>
                <td>
                  <v-chip class="ma-2" close color="red" text-color="white">
                    Remove
                  </v-chip>
                  <v-chip class="ma-2" color="green" outlined>
                    Make Default
                  </v-chip>
                </td>
              </tr>
              <tr>
                <td width="60%">map name3</td>
                <td>
                  <v-chip class="ma-2" close color="red" text-color="white">
                    Remove
                  </v-chip>
                  <v-chip class="ma-2" color="green" outlined>
                    Make Default
                  </v-chip>
                </td>
              </tr>
            </tbody>
          </v-simple-table>
        </v-card>
        </v-dialog>

        <v-dialog v-model="createMapD" width="360">
          <v-card height="140">
            <v-row class="d-flex justify-center align-center text-center">
              <v-col class="mt-7"><h3>Please Continue From Dashboard</h3></v-col>
            </v-row>
            <v-row class="d-flex justify-center align-center text-center">
              <v-btn @click="createMap()" color="success">Done</v-btn>
            </v-row>
          </v-card>
        </v-dialog>

        <v-dialog v-model="fileMapD" width="360">
          <v-card height="140">
            <v-row class="d-flex justify-center align-center text-center">
              <v-col class="mt-7"><h3>Please Continue From Dashboard</h3></v-col>
            </v-row>
            <v-row class="d-flex justify-center align-center text-center">
              <v-btn @click="fileMap()" color="success">Done</v-btn>
            </v-row>
          </v-card>
        </v-dialog>

    </v-container>
</template>

<script>
export default {
  data() {
    return {
      loadMapD: false,
      createMapD: false,
      fileMapD: false,
    };
  },
  methods: {
    loadMap() {
      this.loadMapD = true

    },

    createMap() {
      if(this.createMapD) {
        this.createMapD = false
      }
      else {
        this.createMapD = true
      }
    },

    fileMap() {
      if(this.fileMapD) {
        this.fileMapD = false
      }
      else {
        this.fileMapD = true
      }
    },

    translateMedia(src) {
      return this.$store.getters["Interface/get_media"][src];
    },
    translate(phrase) {
      var t_phrase = this.$store.getters["Interface/get_content"][phrase];
      if (!t_phrase) {
        return phrase;
      } else {
        return t_phrase;
      }
    },
  },
};
</script>
