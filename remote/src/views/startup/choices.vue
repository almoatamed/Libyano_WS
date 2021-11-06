<template>

    <div class="loading" style="display:grid;place-items:center;">
        <v-container fluid>
          <v-card class="mx-auto" max-width="400" :dark='isDark' rounded="lg" >
            <v-list >
              <v-list-item-group v-model="choice" color="indigo">
                <v-list-item v-for="(item, i) in items" :key="i">
                  <v-list-item-content>
                    <v-list-item-title v-text="item.text"></v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
              </v-list-item-group>
            </v-list>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="purple" :loading='loading' :disabled='(choice === undefined) || loading' text @click="set_choice()">Set Choice</v-btn>
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
    set_choice(){
        this.dialog = false
        console.log('Where There is Will there is Way')
        this.$store.dispatch('Ros/take_action', 'startup/remote_interface', {root:true}).then(res=>{
            if(res=='choices'){
                this.continue_loading= true
                console.log(res)
                this.$store.dispatch('Ros/take_action', 'startup/perform/choices_stage/set_choice/'+this.items[this.choice].value, {root:true}).then((res)=>{
                  console.log(res)
                  if(res == 'no_map_set'){
                    this.continue_loading = false
                    this.$store.dispatch('Notify/notify', { group: 'main', text: 'No map is Synced yet', title: 'No Map', type:'error'}, {root:true});
                  }
                })
            }
        })
    },
  },
  data: () => ({
    items: [
      {
        text:'Pick Existing Map', value: 'chose_existing_map'
      },
      {
        text:'Create New Map', value: 'slam'
      },
      {
        text:'Exit', value: 'end'
      }
    ],
    loading: false,
    choice: null,
  }),
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