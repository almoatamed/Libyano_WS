<template>
  <div id="rooot" class="">
    
    <!-- Edit Special Event Dialog -->
    <v-dialog
      v-model="interface_events.edit.edit_special_event_dialog.show"
      scrollable
      max-width="900px"
      persistent
      :overlay="false"
      transition="dialog-transition"
      v-if="interface_events.edit.config_clone"
    >
      <v-card elevation="6" :dark="isDark" class="pa-2">
        <v-card-text>
          <v-row>
            <v-col cols="12">
              <v-container>
                <v-row>
                  <span class="text-h6"
                    >{{
                      interface_events.edit.edit_special_event_dialog
                        .special_events_name
                    }}
                    Special Event</span
                  >
                  <v-spacer></v-spacer>
                  <v-btn
                    text
                    icon
                    @click="
                      interface_events.edit.edit_special_event_dialog.show = false
                    "
                    ><v-icon>mdi-close</v-icon></v-btn
                  >
                </v-row>
                <v-row>
                  <v-divider></v-divider>
                </v-row>
                <v-row>
                  <v-spacer></v-spacer>
                  <v-btn
                    text
                    icon
                    v-if="
                      interface_events.edit.edit_special_event_dialog.selected
                        .side == 'left' &&
                      interface_events.edit.edit_special_event_dialog.selected
                        .index >= 0
                    "
                    @click="add_selected_act_special"
                    ><v-icon>mdi-plus</v-icon></v-btn
                  >
                  <v-btn
                    text
                    icon
                    v-if="
                      interface_events.edit.edit_special_event_dialog.selected
                        .side == 'right' &&
                      interface_events.edit.edit_special_event_dialog.selected
                        .index >= 0
                    "
                    @click="delete_selected_act_from_special"
                    ><v-icon>mdi-delete</v-icon></v-btn
                  >
                  <v-spacer></v-spacer>
                </v-row>
                <v-row>
                  <v-col cols="6">
                    <v-container
                      class=""
                      :style="`
                          overflow-y:auto;\
                          max-height:350px;
                          `"
                    >
                      <v-row>
                        <v-spacer></v-spacer>
                        <span class="text-h6">Acts</span>
                        <v-spacer></v-spacer>
                      </v-row>
                      <v-row
                        v-for="(act, index) in act_names"
                        :key="index"
                        @click="
                          select_for_edit_special_event_dialog(index, 'left')
                        "
                        :style="`background-color: ${
                          interface_events.edit.edit_special_event_dialog
                            .selected.index == index &&
                          interface_events.edit.edit_special_event_dialog
                            .selected.side == 'left'
                            ? 'orange'
                            : ''
                        }`"
                        class="pa-2 btm_border"
                      >
                        <span>{{ act }}</span>
                      </v-row>
                    </v-container>
                  </v-col>
                  <v-col
                    cols="6"
                    :style="`
                          overflow-y:auto;\
                          max-height:350px;
                          `"
                  >
                    <v-container class="">
                      <v-row>
                        <v-spacer></v-spacer>
                        <span class="text-h6"
                          >{{
                            interface_events.edit.edit_special_event_dialog
                              .special_events_name
                          }}
                          Special Event Acts</span
                        >
                        <v-spacer></v-spacer>
                      </v-row>
                      <v-row
                        v-for="(act, index) in interface_events.edit
                          .config_clone['special_events'][
                          interface_events.edit.edit_special_event_dialog
                            .special_events_name
                        ]"
                        :key="index"
                        @click="
                          select_for_edit_special_event_dialog(index, 'right')
                        "
                        :style="`background-color: ${
                          interface_events.edit.edit_special_event_dialog
                            .selected.index == index &&
                          interface_events.edit.edit_special_event_dialog
                            .selected.side == 'right'
                            ? 'orange'
                            : ''
                        }`"
                        class="pa-2 btm_border"
                      >
                        <span>{{ act }}</span>
                      </v-row>
                    </v-container>
                  </v-col>
                </v-row>
                <v-row class="pt-4">
                  <v-spacer></v-spacer>
                  <v-btn text icon @click="save"
                    ><v-icon>mdi-content-save</v-icon></v-btn
                  >
                </v-row>
              </v-container>
            </v-col>
          </v-row>
        </v-card-text>
      </v-card>
    </v-dialog>

    <!-- Edit Route Dialog-->
    <v-dialog
      v-model="interface_events.edit.edit_route_dialog.show"
      scrollable
      max-width="900px"
      persistent
      :overlay="false"
      transition="dialog-transition"
      v-if="interface_events.edit.config_clone"
    >
      <v-card elevation="6" :dark="isDark" class="pa-2">
        <v-card-text>
          <v-row>
            <v-col cols="12">
              <v-container>
                <v-row>
                  <span class="text-h6"
                    >{{
                      interface_events.edit.edit_route_dialog.route_name
                    }}
                    Route</span
                  >
                  <v-spacer></v-spacer>
                  <v-btn
                    text
                    icon
                    @click="
                      interface_events.edit.edit_route_dialog.show = false
                    "
                    ><v-icon>mdi-close</v-icon></v-btn
                  >
                </v-row>
                <v-row>
                  <v-divider></v-divider>
                </v-row>
                <v-row class="pa-2">
                  <v-btn
                    color="orange"
                    text
                    :disabled="
                      interface_events.edit.edit_route_dialog.edit_type ==
                      'mounted'
                    "
                    @click="
                      interface_events.edit.edit_route_dialog.edit_type =
                        'mounted'
                    "
                    >On Mounted</v-btn
                  >
                  <v-btn
                    color="orange"
                    text
                    :disabled="
                      interface_events.edit.edit_route_dialog.edit_type ==
                      'destroy'
                    "
                    @click="
                      interface_events.edit.edit_route_dialog.edit_type =
                        'destroy'
                    "
                    >On destroy</v-btn
                  >
                </v-row>
                <v-row>
                  <v-spacer></v-spacer>
                  <v-btn
                    text
                    icon
                    v-if="
                      interface_events.edit.edit_route_dialog.selected.side ==
                        'left' &&
                      interface_events.edit.edit_route_dialog.selected.index >=
                        0
                    "
                    @click="add_selected_act_route"
                    ><v-icon>mdi-plus</v-icon></v-btn
                  >
                  <v-btn
                    text
                    icon
                    v-if="
                      interface_events.edit.edit_route_dialog.selected.side ==
                        'right' &&
                      interface_events.edit.edit_route_dialog.selected.index >=
                        0
                    "
                    @click="delete_selected_act_from_route"
                    ><v-icon>mdi-delete</v-icon></v-btn
                  >
                  <v-spacer></v-spacer>
                </v-row>
                <v-row>
                  <v-col cols="6">
                    <v-container
                      class=""
                      :style="`
                          overflow-y:auto;\
                          max-height:350px;
                          `"
                    >
                      <v-row>
                        <v-spacer></v-spacer>
                        <span class="text-h6">Acts</span>
                        <v-spacer></v-spacer>
                      </v-row>
                      <v-row
                        v-for="(act, index) in act_names"
                        :key="index"
                        @click="select_for_edit_route_dialog(index, 'left')"
                        :style="`background-color: ${
                          interface_events.edit.edit_route_dialog.selected
                            .index == index &&
                          interface_events.edit.edit_route_dialog.selected
                            .side == 'left'
                            ? 'orange'
                            : ''
                        }`"
                        class="pa-2 btm_border"
                      >
                        <span>{{ act }}</span>
                      </v-row>
                    </v-container>
                  </v-col>
                  <v-col
                    cols="6"
                    :style="`
                          overflow-y:auto;\
                          max-height:350px;
                          `"
                  >
                    <v-container class=""
                    v-if="interface_events.edit
                          .config_clone['routes'][
                          interface_events.edit.edit_route_dialog.route_name
                        ]"
                    >
                      <v-row>
                        <v-spacer></v-spacer>
                        <span class="text-h6"
                          >{{
                            interface_events.edit.edit_route_dialog.route_name
                          }}
                          Route
                          {{
                            interface_events.edit.edit_route_dialog.edit_type
                          }}
                          Acts</span
                        >
                        <v-spacer></v-spacer>
                      </v-row>
                      <v-row
                        v-for="(act, index) in interface_events.edit
                          .config_clone['routes'][
                          interface_events.edit.edit_route_dialog.route_name
                        ][
                          interface_events.edit.edit_route_dialog.edit_type ==
                          'mounted'
                            ? 'mounted_acts'
                            : 'destroy_acts'
                        ]"
                        :key="index"
                        @click="select_for_edit_route_dialog(index, 'right')"
                        :style="`background-color: ${
                          interface_events.edit.edit_route_dialog.selected
                            .index == index &&
                          interface_events.edit.edit_route_dialog.selected
                            .side == 'right'
                            ? 'orange'
                            : ''
                        }`"
                        class="pa-2 btm_border"
                      >
                        <span>{{ act }}</span>
                      </v-row>
                    </v-container>
                  </v-col>
                </v-row>
                <v-row class="pt-4">
                  <v-spacer></v-spacer>
                  <v-btn text icon @click="save"
                    ><v-icon>mdi-content-save</v-icon></v-btn
                  >
                </v-row>
              </v-container>
            </v-col>
          </v-row>
        </v-card-text>
      </v-card>
    </v-dialog>

    <!-- Main Table -->
    <v-container>
      <div class="text-h4">Interface Events</div>
      <v-divider class="py-2"></v-divider>
      <v-card elevation="6" :dark="isDark">
        <v-card-actions>
          <v-btn
            text
            color="orange"
            :disabled="interface_events.main_table.show == 'routes'"
            @click="interface_events.main_table.show = 'routes'"
            >Routes</v-btn
          >
          <v-btn
            text
            color="orange"
            :disabled="interface_events.main_table.show == 'special'"
            @click="interface_events.main_table.show = 'special'"
            >Special Events</v-btn
          >
        </v-card-actions>
        <v-container fluid style="">
          <v-row
            v-if="interface_events.main_table.show == 'special'"
            class="pa-2"
          >
            <v-col cols="12">
              <v-container fluid>
                <v-row>
                  <span class="pa-2 text-h6">Special Events</span>
                </v-row>
                <v-row>
                  <v-divider></v-divider>
                </v-row>
                <v-row v-if="special_events_list.length > 0">
                  <v-col cols="12">
                    <v-container fluid>
                      <v-row
                        v-for="(special_event, index) in special_events_list"
                        class="btm_border"
                        :key="index"
                      >
                        <span class="pt-2">{{ special_event }}</span>
                        <v-spacer></v-spacer>
                        <v-btn
                          text
                          icon
                          @click="edit_special_event(special_event)"
                          ><v-icon>mdi-pencil</v-icon></v-btn
                        >
                      </v-row>
                    </v-container>
                  </v-col>
                </v-row>
                <v-row v-else>
                  <v-spacer></v-spacer>
                  <v-progress-circular
                    indeterminate
                    color="primary"
                  ></v-progress-circular>
                  <v-spacer></v-spacer>
                </v-row>
              </v-container>
            </v-col>
          </v-row>
          <v-row
            v-if="interface_events.main_table.show == 'routes'"
            class="pa-2"
          >
            <v-col cols="12">
              <v-container>
                <v-row>
                  <span class="pa-2 text-h6">Routes</span>
                </v-row>
                <v-row>
                  <v-divider></v-divider>
                </v-row>
                <v-row v-if="routes_list.length > 0">
                  <v-col cols="12">
                    <v-container fluid>
                      <v-row
                        v-for="(route, index) in routes_list"
                        class="btm_border"
                        :key="index"
                      >
                        <span class="pt-2">{{ route }}</span>
                        <v-spacer></v-spacer>
                        <v-btn text icon @click="edit_route(route)"
                          ><v-icon>mdi-pencil</v-icon></v-btn
                        >
                      </v-row>
                    </v-container>
                  </v-col>
                </v-row>
                <v-row v-else>
                  <v-spacer></v-spacer>
                  <v-progress-circular
                    indeterminate
                    color="primary"
                  ></v-progress-circular>
                  <v-spacer></v-spacer>
                </v-row>
              </v-container>
            </v-col>
          </v-row>
        </v-container>
      </v-card>
    </v-container>
  </div>
</template>

<script>
export default {
  data() {
    return {
      act_names: [],
      interface_events: {
        config: {
          routes: {},
          special_events: {},
        },
        edit: {
          config_clone: null,
          edit_route_dialog: {
            route_name: "",
            edit_type: "mounted",
            show: false,
            selected: {
              index: -1,
              side: "",
            },
          },
          edit_special_event_dialog: {
            special_events_name: "",
            show: false,
            selected: {
              index: -1,
              side: "",
            },
          },
        },
        main_table: {
          show: "routes",
        },
      },
    };
  },
  methods: {
    fetch_interface_config() {
      this.$store
        .dispatch("Ros/take_action", "interface/get_interface_config_json", {
          root: true,
        })
        .then((res) => {
          this.interface_events.config = JSON.parse(res);
          console.log('fetched the config and stored in interface_events', this.interface_events.config)
          this.clone_config()
        })
        .catch((err) => {
          this.$store.dispatch(
            "Notify/notify",
            {
              group: "main",
              text: `Failed to fetch inteface configurations ${err}`,
              title: "Error",
              type: "error",
            },
            { root: true }
          );
        });
    },
    fetch_acts_names() {
      this.$store
        .dispatch("Ros/take_action", "act/get_acts_names", { root: true })
        .then((res) => {
          this.act_names = res.split("|");
          console.log(this.act_names);
        })
        .catch((err) => {
          this.$store.dispatch(
            "Notify/notify",
            {
              group: "main",
              text: `Failed to fetch acts names ${err}`,
              title: "Error",
              type: "error",
            },
            { root: true }
          );
        });
    },
    clone_config() {
      console.log('cloning config')
      this.interface_events.edit.config_clone = JSON.parse(
        JSON.stringify(this.interface_events.config)
      );
      console.log('config cloned ', this.interface_events.edit.config_clone, this.interface_events.config)
    },
    edit_route(route_name) {
      this.clone_config();
      this.interface_events.edit.edit_route_dialog.route_name = route_name;
      this.interface_events.edit.edit_route_dialog.show = true;
    },
    select_for_edit_route_dialog(index, side) {
      this.interface_events.edit.edit_route_dialog.selected.index = index;
      this.interface_events.edit.edit_route_dialog.selected.side = side;
    },
    add_selected_act_route() {
      this.interface_events.edit.config_clone["routes"][
        this.interface_events.edit.edit_route_dialog.route_name
      ][
        this.interface_events.edit.edit_route_dialog.edit_type == "mounted"
          ? "mounted_acts"
          : "destroy_acts"
      ].push(
        this.act_names[
          this.interface_events.edit.edit_route_dialog.selected.index
        ]
      );
    },
    delete_selected_act_from_route() {
      this.interface_events.edit.config_clone["routes"][
        this.interface_events.edit.edit_route_dialog.route_name
      ][
        this.interface_events.edit.edit_route_dialog.edit_type == "mounted"
          ? "mounted_acts"
          : "destroy_acts"
      ].splice(this.interface_events.edit.edit_route_dialog.selected.index, 1);
    },
    save() {
      console.log(
        "Ros/take_action",
        `interface/change_interface_config_json/${JSON.stringify(
          this.interface_events.edit.config_clone
        )}`
      );
      this.$store
        .dispatch(
          "Ros/take_action",
          `interface/change_interface_config_json/${JSON.stringify(
            this.interface_events.edit.config_clone
          )}`,
          { root: true }
        )
        .then((res) => {
          console.log(res);
          this.fetch_interface_config();
          this.interface_events.edit.edit_route_dialog.show = false;
          this.interface_events.edit.edit_special_event_dialog.show = false;
          this.$store.dispatch(
            "Notify/notify",
            {
              group: "main",
              text: `inteface configurations updated`,
              title: "Saved",
              type: "success",
            },
            { root: true }
          );
        })
        .catch((err) => {
          this.$store.dispatch(
            "Notify/notify",
            {
              group: "main",
              text: `Failed to Save inteface configurations ${err}`,
              title: "Error",
              type: "error",
            },
            { root: true }
          );
        });
    },
    edit_special_event(event) {
      console.log('opening dialog ')
      this.clone_config();
      console.log('cloned')

      this.interface_events.edit.edit_special_event_dialog.special_events_name =
        event;
        
      console.log('configured')
      this.interface_events.edit.edit_special_event_dialog.show = true;
      console.log('opened')
    },
    select_for_edit_special_event_dialog(index,side){
      this.interface_events.edit.edit_special_event_dialog.selected.index = index;
      this.interface_events.edit.edit_special_event_dialog.selected.side = side;
    },
    add_selected_act_special() {
      this.interface_events.edit.config_clone["special_events"][
        this.interface_events.edit.edit_special_event_dialog.special_events_name
      ].push(
        this.act_names[
          this.interface_events.edit.edit_special_event_dialog.selected.index
        ]
      );
    },
    delete_selected_act_from_special() {
      this.interface_events.edit.config_clone["special_events"][
        this.interface_events.edit.edit_special_event_dialog.special_events_name
      ].splice(this.interface_events.edit.edit_special_event_dialog.selected.index, 1);
    },
  },
  created() {
    this.fetch_interface_config();
    this.fetch_acts_names();
  },
  computed: {
    routes_list() {
      return Object.keys(this.interface_events.config.routes);
    },
    isDark() {
      return this.$store.getters["Theme/isDark"];
    },
    special_events_list() {
      return Object.keys(this.interface_events.config.special_events);
    },
  },
};
</script>

<style scoped>
.btm_border {
  border-bottom: 1px solid lightgrey;
}
.bordered {
  border: 1px solid rgba(211, 211, 211, 0.2);
}
</style>