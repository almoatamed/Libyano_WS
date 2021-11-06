<template>

    <div class="loading" style="display:grid;place-items:center;">
        <v-container fluid>
          <v-card v-if="items.length" class="mx-auto" max-width="400" :dark='isDark' rounded="lg" >
            <v-list >
              <v-list-item-group v-model="choice" color="indigo">
                <v-list-item v-for="(item, i) in items" :key="i">
                  <v-list-item-content>
                    <v-list-item-title v-text="item"></v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
              </v-list-item-group>
            </v-list>
            <v-card-actions>
              <v-btn color="purple" text @click="cancel()">Cancel</v-btn>
              <v-spacer></v-spacer>
              <v-btn color="purple" :disabled='(choice === undefined) || loading' :loading='loading' text @click="set_map()"> Set map </v-btn>
            </v-card-actions>
          </v-card>
          <v-card v-else class="mx-auto" max-width="400" :dark="isDark">
            <v-card-text>There is no Maps Saved Yet</v-card-text>
            <v-card-actions>
              <v-btn color="purple" text @click="cancel()">Cancel</v-btn>
              <v-spacer></v-spacer>
            </v-card-actions>
          </v-card>
        </v-container>
    </div>
</template>

<script>
export default {
  computed:{
    isDark(){
      return this.$store.getters['Theme/isDark']
    }
  },
  methods:{
    cancel(){
      this.loading =true
      this.$store.dispatch('Ros/take_action', 'startup/perform/chose_existing_map/confirm/end').then(()=>{
        this.$router.push({name:'startup_loading'})
      })
    },
    set_map(){
      this.loading = true
      console.log(this.items, this.choice, this.items[this.choice])
      this.$store.dispatch('Ros/take_action', 'navigation/set_map/'+this.items[this.choice], {root:true}).then((res)=>{
        console.log('map has been synced',res)
        if(res != 'not_found'){
          this.$store.dispatch('Ros/take_action', 'startup/perform/chose_existing_map/confirm/synced').then(()=>{
            this.$router.push({name:'startup_loading'})
          })
        }else{this.loading = false}
      })
    }
  },
  data: () => ({
    items: [],
    choice: null,
    loading: false
  }),
  created() {
    this.$store
      .dispatch("Ros/take_action", "navigation/get_maps_names", { root: true }).then((res) => {
        if(res != 'no_maps'){
          this.items = res.split('|')
        }
      });
  },
  watch:{
    choice(val){
      console.log(val)
    }
  }
};
</script>

<style scoped>
.loading {
  position: absolute;
  top: 0%;
  left: 0%;
  bottom: 0%;
  right: 0%;
  margin: 0px;
  background-color: rgb(255, 255, 255,0.1);
  background-size: cover;
  overflow: auto;
  background-repeat: no-repeat;
}
</style>