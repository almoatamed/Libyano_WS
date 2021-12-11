<template>
  <div id="rooot" class="">
    <v-container>
      <div class="text-h4">Summary</div>
      <v-divider class="py-2"></v-divider>
        <v-card  elevation="6" :dark="isDark">
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
          actions: false,
        },
        {
          name: "Battery percentage",
          value: 'Undefined',
          actions: false,
        },
        {
          name: "Charging",
          value: '',
          actions: false,
        },
      ],
    };
  },
  computed: {
    ...mapGetters("Theme", ["isDark"]),
    ...mapGetters("Ros", [ "status"]),
  },
  watch: {
    status(val){
      var items = [] 
      items[0] = {
        name: 'Mode', 
        value: val['mode'], 
        actions: false
      }
      items[1] = {
        name: 'Battery Percentage', 
        value: val['power']['battery'], 
        actions: false
      }
      items[2] = {
        name: 'Is Charging', 
        value: val['power']['charging_status'], 
        actions: false,
      }
      this.items = items
    }

  },
  methods: {
  },
  created() {
  },
};
</script>

<style>
</style>