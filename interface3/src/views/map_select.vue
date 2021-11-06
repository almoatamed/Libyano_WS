<template>
  <v-container fluid style="height:100%; background-color:#262656;">
    <v-container style="height:100%; background-color:#0f0f33;" class="elevation-24 rounded-lg">
    <v-row justify="center" no-gutters style="margin-top:5%;">
      <v-col md="8">
        <v-img
          src="../assets/mapselect.svg"
          max-width="400"
          style="margin-left:auto; margin-right:auto;"
        ></v-img>
      </v-col>
    </v-row>
    <v-row justify="center" style="">
      <v-col md="8">
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
      </v-col>
    </v-row>
    <v-row justify="center">
      <v-col md="4">
        <v-btn block large>
          Load Map
        </v-btn></v-col
      >
      <v-col md="4">
        <v-btn block large>
          Add Map
        </v-btn></v-col
      >
    </v-row>
    </v-container>
  </v-container>
</template>

<script>
export default {
  data() {
    return {};
  },
  methods: {
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
