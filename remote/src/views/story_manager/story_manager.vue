<template>
  <div id="root">
    <!-- New Story Dialog-->
    <v-dialog
      v-model="story_obj.new_story_dialog.show"
      scrollable
      persistent
      :overlay="false"
      max-width="500px"
      transition="dialog-transition"
    >
      <v-card class="pa-2" elevation="6" :dark="isDark">
        <v-container fluid>
          <v-row>
            <v-col cols="12">
              <v-container>
                <v-text-field
                  type="text"
                  label="Story Name"
                  v-model="story_obj.new_story_dialog.name"
                ></v-text-field>
              </v-container>
              <v-divider class="py-2"></v-divider>
              <v-container>
                <v-row>
                  <v-btn
                    @click="story_obj.new_story_dialog.show = false"
                    text
                    icon
                  >
                    <v-icon>mdi-close</v-icon>
                  </v-btn>
                  <v-spacer></v-spacer>
                  <v-btn @click="create_story" text icon>
                    <v-icon>mdi-plus</v-icon>
                  </v-btn>
                </v-row>
              </v-container>
            </v-col>
          </v-row>
        </v-container>
      </v-card>
    </v-dialog>

    <!-- edit story dialog -->
    <v-dialog
      v-model="story_obj.edit_story_dialog.show"
      scrollable
      fullscreen
      persistent
      :overlay="false"
      transition="dialog-transition"
    >
      <v-card class="pa-2" :dark="isDark">
        <v-card-actions>
          <v-container fluid>
            <v-row>
              <span class="text-h6">{{
                story_obj.edit_story_dialog.story["name"]
              }}</span>
              <v-spacer></v-spacer>
              <v-btn text icon @click="story_obj.edit_story_dialog.show = false"
                ><v-icon>mdi-close</v-icon></v-btn
              >
            </v-row>
            <v-row>
              <v-divider></v-divider>
            </v-row>
          </v-container>
        </v-card-actions>
        <v-card-text>
          <v-container fluid>
            <v-row>
              <v-col cols="12">
                <v-container
                  fluid
                  :style="`outline:solid ${
                    isDark ? 'rgba(255,255,255,0.2)' : 'rgba(0,0,0,0.2)'
                  } 1px; padding:20px`"
                >
                  <v-row> Repetition Count </v-row>
                  <v-row>
                    <v-text-field
                      label="Count"
                      type="number"
                      v-model="story_obj.edit_story_dialog.story.count"
                    ></v-text-field>
                  </v-row>
                  <v-row>
                    <span style="font-size: 14px">
                      Chose the number of time this story is supposed to be
                      played (if 0 is chosen then the story will continue
                      playing indefinetly).
                    </span>
                  </v-row>
                </v-container>
              </v-col>
            </v-row>
            <v-row>
              <v-divider></v-divider>
            </v-row>
            <v-row>
              <v-col cols="12">
                <v-container
                  fluid
                  :style="`outline:solid ${
                    isDark ? 'rgba(255,255,255,0.2)' : 'rgba(0,0,0,0.2)'
                  } 1px; padding:20px`"
                >
                  <v-row> End Action </v-row>
                  <v-row>
                    <v-col cols="12">
                      <v-container
                        :style="`outline:solid  \
                      ${isDark ? 'rgba(255,255,255,0.2)' : 'rgba(0,0,0,0.2)'} \
                      1px; \
                      padding:20px`"
                      >
                        <v-row
                          v-for="(end_action, index) in story_obj.stories[
                            'end_actions'
                          ]"
                          :key="index"
                          @click="select_end_action(end_action)"
                          :class="`${
                            story_obj.edit_story_dialog.story.end_action ==
                            end_action
                              ? 'success'
                              : ''
                          } ${isDark ? 'outline_dark' : 'outline'}`"
                        >
                          {{ end_action }}
                        </v-row>
                      </v-container>
                    </v-col>
                  </v-row>
                  <v-row>
                    <span style="font-size: 14px">
                      The action to be performed after finishing the Story.
                    </span>
                  </v-row>
                </v-container>
              </v-col>
            </v-row>
            <v-row>
              <v-divider></v-divider>
            </v-row>

            <v-row>
              <v-col cols="12">
                <v-container
                  fluid
                  :style="`outline:solid ${
                    isDark ? 'rgba(255,255,255,0.2)' : 'rgba(0,0,0,0.2)'
                  } 1px; padding:20px`"
                >
                  <v-row> Acts</v-row>
                  <v-row>
                    <v-spacer></v-spacer>
                    <v-btn
                      color="primary"
                      icon
                      text
                      @click="add_selected_act"
                      v-show="
                        story_obj.edit_story_dialog.selected_act.side ==
                          'left' &&
                        (story_obj.edit_story_dialog.selected_act.act_name !=
                          '' ||
                          story_obj.edit_story_dialog.selected_act.index !=
                            null)
                      "
                    >
                      <v-icon>mdi-plus</v-icon>
                    </v-btn>
                    <v-btn
                      color="primary"
                      icon
                      text
                      @click="delete_selected_act"
                      v-show="
                        story_obj.edit_story_dialog.selected_act.side ==
                          'right' &&
                        (story_obj.edit_story_dialog.selected_act.act_name !=
                          '' ||
                          story_obj.edit_story_dialog.selected_act.index !=
                            null)
                      "
                    >
                      <v-icon>mdi-delete</v-icon>
                    </v-btn>
                    <v-spacer></v-spacer>
                  </v-row>
                  <v-row>
                    <v-col cols="6">
                      <v-container
                        :style="`
                          outline:\
                            solid \
                            ${
                              isDark
                                ? 'rgba(255,255,255,0.2)'
                                : 'rgba(0,0,0,0.2)'
                            } \
                            1px;\
                          overflow-y:auto;\
                          max-height:350px;
                          `"
                      >
                        <v-row
                          v-for="(act, index) in story_obj.available_acts"
                          :key="index"
                          :class="
                            (story_obj.edit_story_dialog.selected_act.side ==
                              'left' &&
                            story_obj.edit_story_dialog.selected_act.act_name ==
                              act
                              ? 'success'
                              : '') + ` ${isDark ? 'outline_dark' : 'outline'}`
                          "
                          @click="
                            select_act_from_edit_story_dialog(act, 'left')
                          "
                        >
                          {{ act }}
                        </v-row>
                      </v-container>
                    </v-col>
                    <v-col cols="6">
                      <v-container
                        :style="`
                          outline:\
                            solid\
                            ${
                              isDark
                                ? 'rgba(255,255,255,0.2)'
                                : 'rgba(0,0,0,0.2)'
                            }\
                            1px;\ 
                          overflow-y:auto;\
                          max-height:350px;
                          `"
                      >
                        <v-row
                          v-for="(act, index) in story_obj.edit_story_dialog
                            .story.acts"
                          :key="index"
                          :class="
                            (story_obj.edit_story_dialog.selected_act.side ==
                              'right' &&
                            story_obj.edit_story_dialog.selected_act.index ==
                              index
                              ? 'success'
                              : '') + ` ${isDark ? 'outline_dark' : 'outline'}`
                          "
                          @click="
                            select_act_from_edit_story_dialog(index, 'right')
                          "
                        >
                          {{ act }}
                        </v-row>
                      </v-container>
                    </v-col>
                  </v-row>
                </v-container>
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-container fluid>
            <v-row>
              <v-divider></v-divider>
            </v-row>
            <v-row>
              <v-spacer></v-spacer>
              <v-btn
                text
                icon
                :disabled="
                  story_obj.edit_story_dialog.buttons.save_button.disabled
                "
                :loading="
                  story_obj.edit_story_dialog.buttons.save_button.loading
                "
                @click="save_edited_story"
                ><v-icon>mdi-content-save</v-icon></v-btn
              >
            </v-row>
          </v-container>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <!-- New Story Dialog-->
    <v-dialog
      v-model="story_obj.set_default_story_dialog.show"
      scrollable
      persistent
      :overlay="false"
      max-width="500px"
      transition="dialog-transition"
    >
      <v-card class="pa-2" elevation="6" :dark="isDark">
        <v-container fluid>
          <v-row>
            <v-col cols="12">
              <v-container>
                <v-row>
                  <div class="text-h6">Stories</div>
                  <v-spacer></v-spacer>
                  <div class="text-h6">
                    {{ story_obj.stories["default_story"] }}
                  </div>
                  <v-spacer></v-spacer>
                  <v-btn
                    @click="story_obj.set_default_story_dialog.show = false"
                    text
                    icon
                  >
                    <v-icon>mdi-close</v-icon>
                  </v-btn>
                </v-row>
                <v-row>
                  <v-divider class="py-2"></v-divider>
                </v-row>
                <v-row v-if="stories_array.length > 0">
                  <v-col cols="12">
                    <v-container
                      :style="`
                          outline:\
                            solid \
                            ${
                              isDark
                                ? 'rgba(255,255,255,0.2)'
                                : 'rgba(0,0,0,0.2)'
                            } \
                            1px;\
                          overflow-y:auto;\
                          max-height:350px;
                          `"
                    >
                      <v-row
                        v-for="(story, index) in stories_array"
                        :key="index"
                        :style="`
                          outline:\
                            solid \
                            ${
                              isDark
                                ? 'rgba(255,255,255,0.2)'
                                : 'rgba(0,0,0,0.2)'
                            } \
                            1px;\
                          overflow-y:auto;\
                          max-height:350px;
                          `"
                        :class="
                          story_obj.set_default_story_dialog.story_name ==
                          story['name']
                            ? 'success'
                            : ''
                        "
                        @click="
                          story_obj.set_default_story_dialog.story_name =
                            story['name']
                        "
                      >
                        <v-spacer></v-spacer>
                        <span>
                          {{ story["name"] }}
                        </span>
                        <v-spacer></v-spacer>
                      </v-row>
                    </v-container>
                  </v-col>
                </v-row>
                <v-row v-else>
                  <span>There is no Stories</span>
                </v-row>
                <v-row>
                  <v-divider class="mt-2"></v-divider>
                </v-row>
                <v-row>
                  <v-spacer></v-spacer>
                  <v-btn
                    :disabled="
                      story_obj.set_default_story_dialog.buttons.set.disabled
                    "
                    :laoding="
                      story_obj.set_default_story_dialog.buttons.set.laoding
                    "
                    @click="set_selected_default_story"
                    text
                    icon
                  >
                    <v-icon>mdi-content-save</v-icon>
                  </v-btn>
                </v-row>
              </v-container>
            </v-col>
          </v-row>
        </v-container>
      </v-card>
    </v-dialog>

    <!-- Stories list -->
    <v-container>
      <div class="text-h4">Story Manager</div>
      <v-divider class="py-4"></v-divider>
      <v-card class="pa-2" elevation="6" :dark="isDark">
        <v-container fluid>
          <v-row>
            <v-col cols="12">
              <v-container>
                <v-row>
                  <div class="text-h6">Stories</div>
                  <v-spacer></v-spacer>
                  <div class="text-h6">
                    {{ story_obj.stories["default_story"] }}
                  </div>
                  <v-spacer></v-spacer>
                  <v-btn @click="set_default_story" text icon>
                    <v-icon>mdi-book-check</v-icon>
                  </v-btn>
                  <v-btn @click="new_story" text icon>
                    <v-icon>mdi-plus</v-icon>
                  </v-btn>
                </v-row>
              </v-container>
              <v-divider></v-divider>
            </v-col>
            <v-col cols="12">
              <v-container v-if="stories_array.length > 0">
                <v-row v-for="(story, index) in stories_array" :key="index">
                  <span>{{ index }}</span>
                  <v-spacer></v-spacer>
                  <v-spacer></v-spacer>
                  <span style="font-size: 18px"> {{ story.name }} </span>
                  <v-spacer></v-spacer>
                  <v-btn @click="edit_story(story)" text icon>
                    <v-icon>mdi-pencil</v-icon>
                  </v-btn>
                  <v-btn @click="del_story(story.name)" text icon>
                    <v-icon>mdi-delete</v-icon>
                  </v-btn>
                </v-row>
              </v-container>
              <v-container
                v-else
                style="display: flex; justify-content: space-around"
              >
                <span> No Stories </span>
              </v-container>
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
    story_obj: {
      default_story: {
        name: "",
        acts: [],
        end_action: "",
        count: 0,
      },
      available_acts: [],
      stories: {
        end_actions: [],
        stories: {},
        default_story: "",
      },
      new_story_dialog: {
        show: false,
        name: "",
      },
      set_default_story_dialog: {
        buttons: {
          set: {
            disabled: false,
            loading: false,
          },
        },
        show: false,
        story_name: "",
      },
      edit_story_dialog: {
        buttons: {
          save_button: {
            loading: false,
            disabled: false,
          },
        },
        show: false,
        selected_act: {
          side: "",
          act_name: "",
          index: "",
        },
        story: {
          name: "",
          acts: [],
          end_action: "",
          count: 0,
        },
      },
    },
  }),
  computed: {
    ...mapGetters("Theme", ["isDark"]),
    stories_array() {
      if (this.story_obj.stories["stories"]) {
        return Object.values(this.story_obj.stories["stories"]);
      } else {
        return [];
      }
    },
  },
  created() {
    this.$store
      .dispatch("Ros/take_action", "operation/get_stories", { root: true })
      .then((res) => {
        console.log(res);
        this.story_obj.stories = JSON.parse(res);
        console.log(this.story_obj.stories);
      });
    this.$store
      .dispatch("Ros/take_action", "act/get_acts_names", { root: true })
      .then((res) => {
        this.story_obj.available_acts = res.split("|").sort();
        console.log(this.story_obj.available_acts);
      });
  },
  methods: {
    create_story() {
      console.log("creating story", this.story_obj.new_story_dialog.name);
      if (this.story_obj.new_story_dialog.name != "") {
        this.story_obj.edit_story_dialog.story = JSON.parse(JSON.stringify(this.story_obj.default_story)) 
        this.story_obj.edit_story_dialog.story.name =
          this.story_obj.new_story_dialog.name;
        this.story_obj.new_story_dialog.show = false;
        this.story_obj.edit_story_dialog.show = true;
      }
    },
    new_story() {
      this.story_obj.new_story_dialog.name = "";
      this.story_obj.new_story_dialog.show = true;
    },
    select_end_action(action) {
      if (
        this.story_obj.stories["end_actions"].some(
          (end_action) => end_action == action
        )
      ) {
        this.story_obj.edit_story_dialog.story.end_action = action;
      }
    },
    select_act_from_edit_story_dialog(act, side) {
      console.log(act, side);
      if (side == "right") {
        this.story_obj.edit_story_dialog.selected_act.side = side;
        this.story_obj.edit_story_dialog.selected_act.index = act;
      } else {
        this.story_obj.edit_story_dialog.selected_act.side = side;
        this.story_obj.edit_story_dialog.selected_act.act_name = act;
      }
    },
    add_selected_act() {
      console.log(
        "adding selected act",
        this.story_obj.available_acts.some(
          (act) => act == this.story_obj.edit_story_dialog.selected_act.act_name
        ),
        this.story_obj.edit_story_dialog.selected_act.side == "left"
      );
      if (
        this.story_obj.available_acts.some(
          (act) => act == this.story_obj.edit_story_dialog.selected_act.act_name
        ) &&
        this.story_obj.edit_story_dialog.selected_act.side == "left"
      ) {
        this.story_obj.edit_story_dialog.story.acts.push(
          this.story_obj.edit_story_dialog.selected_act.act_name
        );
      }
    },
    delete_selected_act() {
      if (
        this.story_obj.edit_story_dialog.selected_act.side == "right" &&
        this.story_obj.edit_story_dialog.selected_act.index <
          this.story_obj.edit_story_dialog.story.acts.length
      ) {
        this.story_obj.edit_story_dialog.story.acts.splice(
          this.story_obj.edit_story_dialog.selected_act.index,
          1
        );
        // this.story_obj.edit_story_dialog.selected_act.side = ''
        // this.story_obj.edit_story_dialog.selected_act.act_name = ''
        // this.story_obj.edit_story_dialog.selected_act.index = null
      }
    },
    save_edited_story() {
      if (this.story_obj.edit_story_dialog.story["name"] == "") {
        this.$store.dispatch(
          "Notify/notify",
          {
            group: "main",
            text: "Story Should have a name.",
            title: "Not a valid Name",
            type: "warning",
          },
          { root: true }
        );
        return;
      } else if (this.story_obj.edit_story_dialog.story["acts"].length < 1) {
        this.$store.dispatch(
          "Notify/notify",
          {
            group: "main",
            text: "Story Should have a valid number of acts.",
            title: "no acts added",
            type: "warning",
          },
          { root: true }
        );
        return;
      } else if (
        !this.story_obj.stories["end_actions"].some(
          (end_action) =>
            end_action == this.story_obj.edit_story_dialog.story["end_action"]
        )
      ) {
        this.$store.dispatch(
          "Notify/notify",
          {
            group: "main",
            text: "Story Should have an End Action",
            title: "no end action",
            type: "warning",
          },
          { root: true }
        );
        return;
      } else if (
        this.story_obj.edit_story_dialog.story["count"] < 0 ||
        this.story_obj.edit_story_dialog.story["count"] > 100
      ) {
        this.$store.dispatch(
          "Notify/notify",
          {
            group: "main",
            text: "Story Should have a valid repetition count.",
            title: "not a valid repetition count (0-100)",
            type: "warning",
          },
          { root: true }
        );
        return;
      } else {
        this.story_obj.edit_story_dialog.buttons.save_button.disabled = true;
        this.story_obj.edit_story_dialog.buttons.save_button.loading = true;
        var story_parse = JSON.stringify(
          this.story_obj.edit_story_dialog.story
        );
        console.log(story_parse);
        this.$store
          .dispatch("Ros/take_action", `operation/add_story/${story_parse}`)
          .then((res) => {
            this.story_obj.edit_story_dialog.buttons.save_button.disabled = false;
            this.story_obj.edit_story_dialog.buttons.save_button.loading = false;
            if (res == "story_controller_is_running") {
              this.$store.dispatch(
                "Notify/notify",
                {
                  group: "main",
                  text: "Automation mode is runing, please stop the automation mode before attempting to add story",
                  title: "Unautharized",
                  type: "warning",
                },
                { root: true }
              );
            } else {
              console.log("story have been saved", res);
              this.$store.dispatch(
                "Notify/notify",
                {
                  group: "main",
                  text: "story is saved successfully",
                  title: "Story has been saved",
                  type: "success",
                },
                { root: true }
              );
              this.$store
                .dispatch("Ros/take_action", "operation/get_stories", {
                  root: true,
                })
                .then((res) => {
                  console.log(res);
                  this.story_obj.stories = JSON.parse(res);
                  console.log(this.story_obj.stories);
                  this.story_obj.edit_story_dialog.show = false;
                });
            }
          })
          .catch((err) => {
            console.log("Error while saving story", err);
            this.$store.dispatch(
              "Notify/notify",
              {
                group: "main",
                text: "Error occured while saving story",
                title: "Error saving story",
                type: "error",
              },
              { root: true }
            );
            // this.story_obj.edit_story_dialog.buttons.save_button.disabled =false
            // this.story_obj.edit_story_dialog.buttons.save_button.loading =false
          });
      }
    },
    edit_story(story) {
      this.story_obj.edit_story_dialog.story = JSON.parse(
        JSON.stringify(story)
      );
      this.story_obj.edit_story_dialog.show = true;
    },
    del_story(story_name) {
      this.$store
        .dispatch(
          "Ros/take_action",
          `operation/del_story/${JSON.stringify({ name: story_name })}`,
          { root: true }
        )
        .then((res) => {
          console.log("finished deleting story ", res);
          if (res == "story_controller_is_running") {
            this.$store.dispatch(
              "Notify/notify",
              {
                group: "main",
                text: "Automation mode is runing, please stop the automation mode before attempting to delete story",
                title: "Unautharized",
                type: "warning",
              },
              { root: true }
            );
          } else {
            this.$store
              .dispatch("Ros/take_action", "operation/get_stories", {
                root: true,
              })
              .then((res) => {
                this.$store.dispatch(
                  "Notify/notify",
                  {
                    group: "main",
                    text: "Story has been deleted",
                    title: "Story Deleted",
                    type: "secondary",
                  },
                  { root: true }
                );
                console.log(res);
                this.story_obj.stories = JSON.parse(res);
                console.log(this.story_obj.stories);
              });
          }
        })
        .catch((err) => {
          console.log("Error while Deleting story", err);
          this.$store.dispatch(
            "Notify/notify",
            {
              group: "main",
              text: "Error occured while deleting story",
              title: "Error deleting story",
              type: "error",
            },
            { root: true }
          );
        });
    },
    set_default_story() {
      this.story_obj.set_default_story_dialog.story_name = "";
      this.story_obj.set_default_story_dialog.show = true;
    },
    set_selected_default_story() {
      if (this.story_obj.set_default_story_dialog.story_name == "") {
        this.$store.dispatch(
          "Notify/notify",
          {
            group: "main",
            text: "Select a story to be set as defaults",
            title: "No story is selected",
            type: "warning",
          },
          { root: true }
        );
      } else {
        this.story_obj.set_default_story_dialog.buttons.set.disabled = true;
        this.story_obj.set_default_story_dialog.buttons.set.loading = true;
        this.$store
          .dispatch(
            "Ros/take_action",
            `operation/set_default_story/${this.story_obj.set_default_story_dialog.story_name}`,
            { root: true }
          )
          .then((res) => {
            this.story_obj.set_default_story_dialog.buttons.set.disabled = false;
            this.story_obj.set_default_story_dialog.buttons.set.loading = false;
            if (res == "story_controller_is_running") {
              this.$store.dispatch(
                "Notify/notify",
                {
                  group: "main",
                  text: "Automation mode is runing, please stop the automation mode before attempting to set default story",
                  title: "Unautharized",
                  type: "warning",
                },
                { root: true }
              );
            } else {
              if (res == "story_not_found") {
                this.$store.dispatch(
                  "Notify/notify",
                  {
                    group: "main",
                    text: "Story name is not found",
                    title: "Story is not found",
                    type: "error",
                  },
                  { root: true }
                );
              } else {
                this.story_obj.set_default_story_dialog.show = false;
                this.$store.dispatch(
                  "Notify/notify",
                  {
                    group: "main",
                    text: `Default story is changed to ${this.story_obj.set_default_story_dialog.story_name}`,
                    title: "Default story is changed ",
                    type: "success",
                  },
                  { root: true }
                );
                this.$store
                  .dispatch("Ros/take_action", "operation/get_stories", {
                    root: true,
                  })
                  .then((res) => {
                    console.log(res);
                    this.story_obj.stories = JSON.parse(res);
                    console.log(this.story_obj.stories);
                  });
              }
            }
          })
          .catch((err) => {
            console.log("error occured while trying to set default story", err);
            this.story_obj.set_default_story_dialog.buttons.set.disabled = false;
            this.story_obj.set_default_story_dialog.buttons.set.loading = false;
            this.$store.dispatch(
              "Notify/notify",
              {
                group: "main",
                text: `error occured while trying to set default story ${err}`,
                title: "Default story error ",
                type: "error",
              },
              { root: true }
            );
          });
      }
    },
  },
};
</script>

<style scoped>
.divider_margin {
  margin-top: 20px;
}
.outline {
  padding-left: 10px;
  outline: solid rgba(0, 0, 0, 0.2) 1px;
}
.outline_dark {
  padding-left: 10px;
  outline: solid rgba(255, 255, 255, 0.2) 1px;
}
.orange {
  background-color: orange;
}
</style>