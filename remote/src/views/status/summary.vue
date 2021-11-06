<template>
  <div id="rooot" class="">
    <v-container>
      <div class="text-h4">Summary</div>
      <v-divider class="py-2"></v-divider>
        <v-card rounded="xl" elevation="6" :dark="isDark">
          <v-card-text>
            <v-data-table
              class="pa-4"
              :headers="remoteControleHeaders"
              :items="items"
              :loading="loading"
              hide-default-footer
              dense
            >
              <template v-slot:item.actions="{ item }">
                <v-switch
                  v-if="item.action"
                  small
                  :disabled="loading"
                  class="mr-2"
                  v-model="item.model"
                  :label="item.actionName"
                  @change="set(item)"
                >
                </v-switch>
              </template>
            </v-data-table>
          </v-card-text>
        </v-card>
    </v-container>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  data() {
    return {
      loading: false,
      remoteControleHeaders: [
        { text: "Name", value: "name" },
        { text: "Value", value: "value" },
        { text: "Actions", value: "actions", sortable: false },
      ],
      items: [
        {
          name: "Mode",
          value: this.mode,
          action: false,
        },
        {
          name: "Battery percentage",
          value: 'Undefined',
          action: false,
        },
        {
          name: "Charging",
          value: '',
          action: false,
        },
      ],
    };
  },
  computed: {
    ...mapGetters("Theme", ["isDark"]),
    ...mapGetters("Ros", ["mode", "status", "batteryPercentage", "isCharging"]),
  },
  watch: {
    mode() {
      var self = this;
      self.items.find((e) => e.name == "Mode").value = this.$store.getters["Ros/mode"];
    },
    batteryPercentage(){
      var self = this;
      self.items.find(e => e.name == 'Battery percentage').value = this.batteryPercentage
    },
    isCharging(val){
      console.log(val)
      this.items.find(e => e.name == "Charging").value = val
    }
  },
  methods: {
    set(item) {
      console.log(item.model)
      var self = this;
      self.loading = true;
      self.$store
        .dispatch(item.activation, item.model, { root: true })
        .then(() => {
          self.$store.dispatch("Ros/fetchMode").then(() => {
            self.items.find(
              (e) => e.name == "Mode"
            ).value = this.$store.getters["Ros/mode"];
            for (var key in self.items) {
              if (self.items[key].action) {
                self.items[key].model =
                  self.items[key].actionMode == this.$store.getters["Ros/mode"]
                    ? true
                    : false;
              }
            }
            setTimeout(() => {
              self.loading = false;
            }, 1500);
          }).catch(()=>{
            self.$store.dispatch("Ros/fetchConnectionFlag", null, { root: true });
            self.$router.push({ name: "noConnection" });
            self.laoding = false;
          });
        });
    },
  },
  created() {
    var self = this;
    self.$store.dispatch("Loading/set", null, { root: true });
    self.$store
      .dispatch("Ros/fetchMode", null, { root: true })
      .then(() => {
        self.$store
          .dispatch("Ros/fetchStatus", null, { root: true })
          .then(() => {
            self.items.find(
              (e) => e.name == "Mode"
            ).value = this.$store.getters["Ros/mode"];
            for (var key in self.items) {
              if (self.items[key].action) {
                self.items[key].model =
                  self.items[key].actionMode == this.$store.getters["Ros/mode"]
                    ? true
                    : false;
              }
            }
            self.$store.dispatch("Loading/clear", null, { root: true });
          })
          .catch(() => {
            self.$store.dispatch("Ros/fetchConnectionFlag", null, {
              root: true,
            });
            self.$store.dispatch("Loading/clear", null, { root: true });
            self.$router.push({ name: "noConnection" });
          });
      })
      .catch(() => {
        self.$store.dispatch("Ros/fetchConnectionFlag", null, { root: true });
        self.$store.dispatch("Loading/clear", null, { root: true });
        self.$router.push({ name: "noConnection" });
      });
  },
};
</script>

<style>
</style>