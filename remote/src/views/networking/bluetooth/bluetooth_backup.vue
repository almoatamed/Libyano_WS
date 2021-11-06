<template>
  <div id="root">

    <v-container>

      <!-- Title -->
      <div class="text-h4">Bluetooth Controller</div>
      <v-divider class="py-4"></v-divider>

      <v-card rounded="xl" elevation="6" :dark="isDark">

        <!-- Actions -->
        <v-container fluid>
          <v-row>
            <v-col cols="12">
              <div class="text-h6">Actions</div>
            </v-col>
            <v-col
              cols="12"
              class="flex-wrap justify-space-between"
            >
              <v-btn  @click='connect'  text color="purple">
                connect
              </v-btn>
              <v-btn  @click='disconnect'  text color="purple">
                Disconnect
              </v-btn>

            </v-col>
          </v-row>
        </v-container>

      </v-card>
    </v-container>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  data: () => ({
   
  }),

  computed: {
    ...mapGetters("Theme", ["isDark"]),

  },

  methods: {

    disconnect() {
      console.log("disconnecting ");
      this.$store.dispatch('Ros/take_action', 'bluetooth/disconnect', {root:true}).then(res=>{
        console.log('disconnecting finished wiht ', res)
      }).catch(err=>{
        console.log(err)
      })
    },

    connect() {
      console.log("connecting ");
      this.$store.dispatch('Ros/take_action', 'bluetooth/connect/any', {root:true}).then(res=>{
        console.log('disconnecting finished wiht ', res)
      }).catch(err=>{
        console.log(err)
      })
    },

  },
};
</script>

<style scoped>
</style>