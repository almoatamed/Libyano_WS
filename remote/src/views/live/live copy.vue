<template>
  <v-container id="root" fluid tag="section" fill-height class="pa-0 ma-0">
    <!-- Map -->
    <canvas fill-height class="pa-0 ma-0" id="map"></canvas>
    <canvas v-show="false" id="temp"></canvas>

    <!-- upper bar -->
    <v-app-bar
      id="default-app-bar"
      absolute
      class="v-bar--underline"
      color="rgb(0,0,0,0)"
      height="70"
      flat
    >
      <!-- <v-btn class="ml-2" color="error"> EMG </v-btn> -->
      <v-spacer></v-spacer>
      <v-btn
        :style="!angled_goal ?'background:rgb(255,255,255);color:rgb(255,199,74)':'background:rgb(255,199,74);color:white'"
        class="ml-2"
        @click="angled_goal=!angled_goal;wait_for_goal(angled_goal, 'angled')"
      >
        <v-icon large>mdi-map-marker-left </v-icon>
      </v-btn>
      <v-btn
        class="ml-2"
        :style="!unangled_goal ?'background:rgb(255,255,255);color:rgb(255,199,74)':'background:rgb(255,199,74);color:white'"
        @click="unangled_goal=!unangled_goal;wait_for_goal(unangled_goal, 'unangled')"
      >
        <v-icon large>mdi-map-marker-down</v-icon>
      </v-btn>
      <!-- <v-spacer></v-spacer> -->
      <v-btn 
      style='background:rgb(255,255,255);color:rgb(255,199,74)'
      class="ml-2"
      @click='go_home'
      >
        <v-icon style="font-size:40px">mdi-home-map-marker</v-icon>
      </v-btn>
      <v-btn 
      class="ml-2"
      style='background:rgb(255,255,255);color:rgb(255,199,74)'
      color="white"
      >
        <v-icon large>mdi-robot</v-icon>
      </v-btn>

    </v-app-bar>

    <!-- JoyStick Pads -->


    <!-- Side Widgets/Actions -->

    <!-- Chat -->
    <v-card
      id="chat"
      class="py-2 px-4"
      color="rgba(0, 0, 0, .3)"
      dark
      flat
      link
      min-width="100"
      style="
        position: fixed;
        top: 180px;
        right: -35px;
        border-radius: 8px;
        z-index: 1;
      "
    >
      <v-icon large> mdi-chat </v-icon>
    </v-card>
    <v-menu
      v-model="chat"
      :close-on-content-click="false"
      activator="#chat"
      bottom
      content-class="v-settings"
      left
      nudge-top="65"
      nudge-left="8"
      offset-x
      origin="top right"
      transition="scale-transition"
    >
      <v-card class="text-center mb-0" width="300">
        <v-card-text>
          <strong class="mb-3 d-inline-block font-weight-black">CHAT</strong>

          <v-divider class="my-4 secondary" />
          <v-col class="pa-0">
            <v-row>
              <v-col class="ma-auto">
                <v-btn
                  v-for="(lang, index) in speak_langs"
                  :key="index"
                  @click="speak_lang = lang"
                  :color="speak_lang == lang ? 'orange' : 'primary'"
                  dark
                  small
                >
                  {{ lang }}
                </v-btn>
              </v-col>
            </v-row>
            <v-row>
              <v-col md="12" class="mx-auto">
                <v-textarea
                  outlined
                  label="Chat Text"
                  clearable
                  v-model="speak_text"
                  no-resize
                  height="100"
                />
                <v-card
                  class="mx-auto"
                  max-width="300"
                  max-height="100"
                  tile
                  style="overflow-y: auto"
                >
                  <v-list-item
                    v-for="(file, index) in speak_files"
                    :key="index"
                    :style="speak_file == file ? 'background:orange' : ''"
                    @click="
                      file == speak_file
                        ? (speak_file = '')
                        : (speak_file = file)
                    "
                  >
                    <v-list-item-content class="pa-0">
                      <v-btn text>
                        {{ file }}
                      </v-btn>
                    </v-list-item-content>
                  </v-list-item>
                </v-card>
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <!-- <v-btn text>
                  <v-icon>mdi-pause</v-icon>
                </v-btn> -->
                <v-btn text @click="speak_file == '' ? playtemp() : playfile()">
                  <v-icon>mdi-play</v-icon>
                </v-btn>
                <v-btn text @click="speak_stop()">
                  <v-icon>mdi-stop</v-icon>
                </v-btn>
              </v-col>
            </v-row>
          </v-col>
        </v-card-text>
      </v-card>
    </v-menu>

    <!-- Led -->
    <v-card
      id="led"
      class="py-2 px-4"
      color="rgba(0, 0, 0, .3)"
      dark
      flat
      link
      min-width="100"
      style="
        position: fixed;
        top: 245px;
        right: -35px;
        border-radius: 8px;
        z-index: 1;
      "
    >
      <v-icon large> mdi-lightbulb-outline </v-icon>
    </v-card>
    <v-menu
      v-model="led"
      :close-on-content-click="false"
      activator="#led"
      bottom
      content-class="v-settings"
      left
      nudge-left="8"
      nudge-top="130"
      offset-x
      origin="top right"
      transition="scale-transition"
      style="position: absolute; top: 180px"
    >
      <v-card class="text-center mb-0" width="600">
        <v-card-text>
          <strong class="mb-3 d-inline-block font-weight-black">LED</strong>

          <v-divider class="my-4 secondary" />
          <v-row>
            <v-col md="6">
              <v-color-picker
                v-model="led_color"
                dot-size="25"
                hide-mode-switch
                mode="hexa"
                swatches-max-height="200"
              />
              <v-list-item
                :style="led_return_default == true ? 'background:orange' : ''"
              >
                <v-list-item-content class="pa-0">
                  <v-btn text @click="led_return_default = !led_return_default">
                    return to default
                  </v-btn>
                </v-list-item-content>
              </v-list-item>
            </v-col>
            <v-col md="6">
              <v-text-field
                label="Repeat"
                v-model="led_repeat"
                type="number"
                class="pt-0 mt-0"
              />
              <v-subheader> Speed </v-subheader>
              <v-slider v-model="led_speed" thumb-label step="20" max="200" />
              <v-btn
                @click="set_strip_and_ring"
                dark
                color="primary"
                class="mt-12"
              >
                Set
              </v-btn>
              <v-btn
                dark
                color="secondary"
                class="px-1"
                @click="
                  led_color = emoji_default_color;
                  led_repeat = emoji_default_repeat;
                  led_speed = 100;
                "
              >
                default
              </v-btn>
            </v-col>
          </v-row>
        </v-card-text>
      </v-card>
    </v-menu>

    <!-- Eyes Grid -->
    <v-card
      id="emoji"
      class="py-2 px-4"
      color="rgba(0, 0, 0,0.3)"
      dark
      flat
      link
      min-width="100"
      style="
        position: fixed;
        top: 310px;
        right: -35px;
        border-radius: 8px;
        z-index: 1;
      "
    >
      <v-icon large> mdi-baby-face-outline </v-icon>
    </v-card>
    <v-menu
      v-model="emoji"
      :close-on-content-click="false"
      activator="#emoji"
      bottom
      content-class="v-settings"
      left
      nudge-top="195"
      nudge-left="8"
      offset-x
      origin="top right"
      transition="scale-transition"
    >
      <v-card class="text-center mb-0" width="600">
        <v-card-text>
          <strong class="mb-3 d-inline-block font-weight-black">EMOJI</strong>

          <v-divider class="my-4 secondary" />
          <v-row>
            <v-col md="6">
              <v-color-picker
                dot-size="25"
                hide-mode-switch
                mode="hexa"
                v-model="emoji_color"
                swatches-max-height="200"
              />
              <v-list-item
                :style="emoji_return_default == true ? 'background:orange' : ''"
              >
                <v-list-item-content class="pa-0">
                  <v-btn
                    text
                    @click="emoji_return_default = !emoji_return_default"
                  >
                    return to default
                  </v-btn>
                </v-list-item-content>
              </v-list-item>
            </v-col>
            <v-col md="6">
              <!-- emojis list -->
              <v-card
                class="mx-auto"
                max-width="300"
                max-height="150"
                tile
                style="overflow-y: auto"
              >
                <v-list-item
                  :style="emoji == emoji_choise ? 'background:orange' : ''"
                  v-for="(emoji, index) in emojis"
                  :key="index"
                >
                  <v-list-item-content class="pa-0">
                    <v-btn text @click="emoji_choise = emoji">
                      {{ emoji }}
                    </v-btn>
                  </v-list-item-content>
                </v-list-item>
              </v-card>

              <v-subheader> Speed </v-subheader>
              <v-slider thumb-label step="20" v-model="emoji_speed" max="200" />
              <v-text-field
                label="Repeat"
                v-model="emoji_repeat"
                type="number"
                class="pt-0 mt-0"
              />
              <v-btn
                dark
                color="secondary"
                class="px-1"
                @click="
                  emoji_choise = 'blink';
                  emoji_color = emoji_default_color;
                  emoji_repeat = emoji_default_repeat;
                  emoji_speed = 100;
                "
              >
                default
              </v-btn>
              <v-btn dark class="px-1" color="primary" @click="set_emoji">
                Set
              </v-btn>
            </v-col>
          </v-row>
        </v-card-text>
      </v-card>
    </v-menu>

    <!-- map points -->
    <v-card
      id="map_points"
      class="py-2 px-4"
      color="rgba(0, 0, 0, .3)"
      dark
      flat
      link
      min-width="100"
      style="
        position: fixed;
        top: 375px;
        right: -35px;
        border-radius: 8px;
        z-index: 1;
      "
    >
      <v-icon large> mdi-map-marker </v-icon>
    </v-card>
    <v-menu
      v-model="map_point"
      :close-on-content-click="false"
      activator="#map_points"
      bottom
      content-class="v-settings"
      left
      nudge-top="260"
      nudge-left="8"
      offset-x
      origin="top right"
      transition="scale-transition"
    >
      <v-card class="text-center mb-0" width="300">
        <v-card-text>
          <strong class="mb-3 d-inline-block font-weight-black">POINT</strong>

          <v-divider class="my-4 secondary" />
          <v-card
            class="mx-auto"
            max-width="300"
            max-height="150"
            tile
            style="overflow-y: auto"
          >
            <v-list-item>
              <v-list-item-content class="pa-0">
                <v-btn text> Single-line item </v-btn>
              </v-list-item-content>
            </v-list-item>
            <v-list-item>
              <v-list-item-content class="pa-0">
                <v-btn text> Single-line item </v-btn>
              </v-list-item-content>
            </v-list-item>
            <v-list-item>
              <v-list-item-content class="pa-0">
                <v-btn text> Single-line item </v-btn>
              </v-list-item-content>
            </v-list-item>
            <v-list-item>
              <v-list-item-content class="pa-0">
                <v-btn text> Single-line item </v-btn>
              </v-list-item-content>
            </v-list-item>
          </v-card>
          <!-- <v-text-field
            type="number"
            label="Time"
          /> -->
          <v-btn dark color="primary"> Go </v-btn>
        </v-card-text>
      </v-card>
    </v-menu>

    <!-- interface view -->
    <v-card
      id="views"
      class="py-2 px-4"
      color="rgba(0, 0, 0, .3)"
      dark
      flat
      link
      min-width="100"
      style="
        position: fixed;
        top: 440px;
        right: -35px;
        border-radius: 8px;
        z-index: 1;
      "
    >
      <v-icon large> mdi-view-carousel </v-icon>
    </v-card>
    <v-menu
      v-model="views"
      :close-on-content-click="false"
      activator="#views"
      bottom
      content-class="v-settings"
      left
      nudge-top="325"
      nudge-left="8"
      offset-x
      origin="top right"
      transition="scale-transition"
    >
      <v-card class="text-center mb-0" width="300">
        <v-card-text>
          <strong class="mb-3 d-inline-block font-weight-black">VIEWS</strong>

          <v-divider class="my-4 secondary" />
          <v-card
            class="mx-auto"
            max-width="300"
            max-height="150"
            tile
            style="overflow-y: auto"
          >
            <v-list-item
              v-for="(view, index) in interface_view_sets"
              :key="index"
              :style="interface_view == view ? 'background:orange' : ''"
              @click="interface_view = view"
            >
              <v-list-item-content class="pa-0">
                <v-btn text>
                  {{ view }}
                </v-btn>
              </v-list-item-content>
            </v-list-item>
          </v-card>
          <v-btn dark @click="interface_set" color="primary"> View </v-btn>
        </v-card-text>
      </v-card>
    </v-menu>

    <!-- manual contorl -->
    <v-card
      id="views"
      class="py-2 px-4"
      :color="
        !navigation_manual ? 'rgba(0, 0, 0, .3)' : 'rgba(255, 175, 0, .3)'
      "
      dark
      flat
      @click="navigation_manual = !navigation_manual"
      min-width="100"
      style="
        position: fixed;
        top: 505px;
        right: -35px;
        border-radius: 8px;
        z-index: 1;
      "
    >
      <v-icon large>
        {{
          navigation_manual
            ? "mdi-google-controller"
            : "mdi-google-controller-off"
        }}
      </v-icon>
    </v-card>

    <!-- map / zoomin zoomout -->
    <v-row>
      <v-col cols="12" class="pt-0">
        <v-row>
          <v-col cols="12" md="6" lg="12">
            <div
              icon="mdi-map"
              icon-small
              title="Navigation Map"
              color="primary"
              height="560"
              width="100%"
            >
              <v-card
                class="py-2 px-4"
                color="rgba(0, 0, 0, .3)"
                dark
                flat
                link
                style="
                  position: absolute;
                  top: 265px;
                  left: 0px;
                  border-radius: 0px 8px 8px 0px;
                  z-index: 1;
                "
              >
                <v-icon large> mdi-map-plus </v-icon>
              </v-card>
              <v-card
                class="py-2 px-4"
                color="rgba(0, 0, 0, .3)"
                dark
                flat
                link
                style="
                  position: absolute;
                  top: 330px;
                  left: 0px;
                  border-radius: 0px 8px 8px 0px;
                  z-index: 1;
                "
              >
                <v-icon large> mdi-map-minus </v-icon>
              </v-card>
              <v-card
                class="py-2 px-4"
                color="rgba(0, 0, 0, .3)"
                dark
                flat
                link
                style="
                  position: absolute;
                  top: 395px;
                  left: 0px;
                  border-radius: 0px 8px 8px 0px;
                  z-index: 1;
                "
              >
                <v-icon large > mdi-map-search </v-icon>
              </v-card>
            </div>
          </v-col>
        </v-row>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import env from "../../../env";
import ROSLIB from "roslib";
import q from "quaternion";

export default {
  name: "DashboardView",

  data() {
    return {
      chat: false,
      led: false,
      emoji: false,
      map_point: false,
      views: false,
      tab: null,

      // ######################### Head Movement ######################33
      move_head: false,

      // ######################### Eyes ######################33
      emojis: [
        "blink",
        "dollars",
        "happy",
        "mad",
        "off",
        "closing",
        "opening",
        "sneaky",
        "sudden",
        "loadingleft",
        "loadingright",
      ],
      emoji_choise: "blink",
      emoji_speed: 100,
      emoji_color: "#951b81FF",
      emoji_default_color: "#951b81FF",
      emoji_default_repeat: 1,
      emoji_repeat: 1,
      emoji_return_default: false,

      // ######################### Eyes ######################33
      led_color: "#951b81FF",
      led_repeat: 1,
      led_return_default: false,
      led_speed: 100,

      // ######################### Speak ######################33
      speak_lang: "ar",
      speak_langs: ["ar", "en", "fr"],
      speak_files: [],
      speak_file: "",
      speak_text: "",

      // ######################### interface view ######################
      interface_view_sets: [],
      interface_view: "main",

      // ######################### navigation ######################
      navigation_manual: false,
      angled_goal: false,
      unangled_goal: false,

      // ######################### Map ######################
      // elements
      root: null,
      bar: null,

      // canvaces and context
      canvas: null,
      temp_canvas: null,
      c: null,
      temp_c: null,

      // input data from rostopics
      global_path: null,
      map: null,
      goal_monitor: null,
      current_pose: null,

      // goal point
      point: {},

      // map location
      movx: 0,
      movy: 0,
      zoom: 2,

      // map image data
      imageData: null,

      // ######################## Ros #########################
      ros: null,
    };
  },
  methods: {
    // ######################### Head Movement ######################33
    movehead(x, y) {
      if (this.move_head) {
        this.$store.dispatch(
          "Ros/take_action",
          `interactive/move_head_relativ/${x}/${y}/700`
        );
        setTimeout(() => {
          this.movehead(x, y);
        }, 250);
      }
    },
    moveheadhome() {
      this.$store
        .dispatch("Ros/take_action", `interactive/move_head_home`, {
          root: true,
        })
        .then((res) => {
          console.log(res);
        });
    },
    // ######################### Eyes ######################33
    set_emoji() {
      this.$store
        .dispatch(
          "Ros/take_action",
          `interactive/set_eyes/${this.emoji_choise}/${this.emoji_color.slice(
            1,
            -2
          )}/${this.emoji_repeat}/${this.emoji_speed}/${
            this.emoji_return_default ? "1" : "0"
          }`,
          { root: true }
        )
        .then((res) => {
          console.log(res);
        });
    },

    // ######################### ring and strip ######################33

    set_strip_and_ring() {
      this.$store
        .dispatch(
          "Ros/take_action",
          `interactive/set_ring_flow/fadeoutfadein/${this.led_color.slice(
            1,
            -2
          )}/${this.led_repeat}/${this.led_speed}/${
            this.led_return_default ? "1" : "0"
          }`,
          { root: true }
        )
        .then((res) => {
          console.log(res);
        });
      var color = this.led_color.slice(1, -2);
      var r = parseInt(color.slice(0, 2), 16);
      var g = parseInt(color.slice(2, 4), 16);
      var b = parseInt(color.slice(4), 16);
      this.$store
        .dispatch(
          "Ros/take_action",
          `interactive/set_strip_color/${r}/${g}/${b}`,
          { root: true }
        )
        .then((res) => {
          console.log(res);
        });
    },

    // ######################### Speak ######################33
    speak_fetch_sounds() {
      var self = this;
      self.sounds = [["temp", ""]];
      this.$store
        .dispatch("Ros/take_action", "interactive/sounds_list", { root: true })
        .then((res) => {
          res = res.split("%");
          res.forEach((el) => {
            this.speak_files.push(el.split("&")[0]);
          });
        });
    },
    playtemp() {
      if (this.speak_lang != "" && this.speak_text != "") {
        this.$store
          .dispatch(
            "Ros/take_action",
            `interactive/speak_play_temp/${this.speak_lang}/${this.speak_text}`,
            { root: true }
          )
          .then((res) => {
            console.log(res);
          });
      }
    },
    playfile() {
      if (this.speak_file != "") {
        this.$store
          .dispatch(
            "Ros/take_action",
            `interactive/speak/${this.speak_file}.mp3`,
            { root: true }
          )
          .then((res) => {
            console.log(res);
          });
      }
    },
    speak_stop() {
      this.$store
        .dispatch("Ros/take_action", `interactive/speak_set_stop`, {
          root: true,
        })
        .then((res) => {
          console.log(res);
        });
    },

    // ######################### interface view ######################
    interface_fetch_sets() {
      this.$store
        .dispatch("Ros/take_action", "interface/get_sets", { root: true })
        .then((res) => {
          console.log(res);
          this.interface_view_sets = res.split("|");
        });
    },
    interface_set() {
      if (this.interface_view != "") {
        this.$store
          .dispatch(
            "Ros/take_action",
            `interface/change_view_set/${this.interface_view}`,
            { root: true }
          )
          .then((res) => {
            if (res == "current_set_is_serving") {
              this.$store.dispatch(
                "Notify/notify",
                {
                  group: "main",
                  text: "the current interface is in service.",
                  title: "not permitted",
                  type: "warning",
                },
                { root: true }
              );
            }
          });
      }
    },


    // ######################### Navigation ######################
    // enable angled and unangled goal
    wait_for_goal(val, type) {
      if (!val) {
        console.log(val);
        this.cancel_goal();
      } else {
        if (type == "angled") {
          this.cancel_goal();
          this.wait_for_angled_goal();
        } else {
          this.cancel_goal();
          this.wait_for_unangled_goal();
        }
      }
    },
    wait_for_angled_goal() {
      this.angled_goal = true;
      this.canvas.addEventListener(
        "mousedown",
        this.angled_goal_mousedown_handler
      );
      this.canvas.addEventListener("mouseup", this.angled_goal_mouseup_handler);
    },
    wait_for_unangled_goal() {
      this.unangled_goal = true;
      this.canvas.addEventListener(
        "mousedown",
        this.unangled_goal_mousedown_handler
      );
      this.canvas.addEventListener(
        "mouseup",
        this.unangled_goal_mouseup_handler
      );
    },

    angled_goal_mousedown_handler(e) {
      var data = this.c.getImageData(e.layerX, e.layerY, 1, 1).data;
      if ((data[0] == 255, data[1] == 255, data[2] == 255)) {
        this.point = {};
        this.point.x = e.layerX / this.zoom + this.movx;
        this.point.layerX = e.layerX;
        this.point.y = e.layerY / this.zoom + this.movy;
        this.point.layerY = e.layerY;
        this.point.drop = true;
        this.point.draw = false;
      }
    },
    angled_goal_mouseup_handler(e) {
      if (this.point.drop && this.map.info) {
        this.point.drop = false;
        this.point.abs_angle = Math.atan(
          Math.abs(
            (e.layerY - this.point.layerY) / (e.layerX - this.point.layerX)
          )
        );
        this.point.end_layerX = e.layerX;
        this.point.end_layerY = e.layerY;

        if (this.point.end_layerX - this.point.layerX > 0) {
          if (this.point.end_layerY - this.point.layerY > 0) {
            this.point.angle = 2 * Math.PI - this.point.abs_angle;
          } else {
            this.point.angle = this.point.abs_angle;
          }
        } else {
          if (this.point.end_layerY - this.point.layerY > 0) {
            this.point.angle = Math.PI + this.point.abs_angle;
          } else {
            this.point.angle = Math.PI - this.point.abs_angle;
          }
        }

        this.point.robot_angle = Math.PI + this.point.angle;
        if (this.point.robot_angle > 2 * Math.PI) {
          this.point.robot_angle = -2 * Math.PI + this.point.robot_angle;
        }

        this.point.robot_x =
          (this.map.info.width - this.point.x) * this.map.info.resolution +
          this.map.info.origin.position.x;
        this.point.robot_y =
          this.point.y * this.map.info.resolution + this.map.info.origin.position.y;
        var qs = q.fromEuler(0, 0, this.point.robot_angle, "XYZ");
        this.$store
          .dispatch(
            "Ros/take_action",
            `navigation/angled_goal/${this.point.robot_x}&${
              this.point.robot_y
            }&${0.0}&${qs.x}&${qs.y}&${qs.z}&${qs.w}`
          )
          .then((res) => {
            console.log(res);
            this.point.draw = true;
          });
      }
    },

    unangled_goal_mousedown_handler(e) {
      var data = this.c.getImageData(e.layerX, e.layerY, 1, 1).data;
      if ((data[0] == 255, data[1] == 255, data[2] == 255)) {
        this.point = {};
        this.point.x = e.layerX / this.zoom + this.movx;
        this.point.layerX = e.layerX;
        this.point.y = e.layerY / this.zoom + this.movy;
        this.point.layerY = e.layerY;
        this.point.drop = true;
        this.point.draw = false;
      }
    },
    unangled_goal_mouseup_handler() {
      if (this.point.drop && this.map.info) {
        this.point.drop = false;

        this.point.robot_x =
          (this.map.info.width - this.point.x) * this.map.info.resolution +
          this.map.info.origin.position.x;
        this.point.robot_y =
          this.point.y * this.map.info.resolution + this.map.info.origin.position.y;
        this.$store
          .dispatch(
            "Ros/take_action",
            `navigation/unangled_goal/${this.point.robot_x}&${this.point.robot_y}`
          )
          .then((res) => {
            console.log(res);
            this.point.draw = true;
          });
      }
    },

    cancel_goal() {
      console.log("clearing event listener");
      this.angled_goal = false;
      this.unangled_goal = false;
      this.canvas.removeEventListener(
        "mousedown",
        this.angled_goal_mousedown_handler
      );
      this.canvas.removeEventListener("mouseup", this.angled_goal_mouseup_handler);
      this.canvas.removeEventListener(
        "mousedown",
        this.unangled_goal_mousedown_handler
      );
      this.canvas.removeEventListener("mouseup", this.unangled_goal_mouseup_handler);
    },
    go_home(){
        this.$store.dispatch('Ros/take_action',`navigation/go_home`).then(()=>{
            this.clear_goal()
        }).catch(()=>{
        })
    },
    // ######################### Map ######################
    // Map zoomin/zoomout
    zoomin(e) {
      console.log(e);
      if (this.continue_zoomin) {
        if (this.zoom < 2.5) {
          this.zoom += 0.1;
        } else {
          this.continue_zoomin = false;
        }
        setTimeout(this.zoomin, 60);
      }
    },
    zoomout() {
      if (this.continue_zoomout) {
        if (this.zoom > 0.5) {
          this.zoom -= 0.1;
        } else {
          this.continue_zoomout = false;
        }
        setTimeout(this.zoomout, 60);
      }
    },
    // Map location controls
    moveup() {
      if (this.movy > -0.1 * this.canvas.height) {
        this.movy -= 10;
      } else {
        this.continue_movement_up = false;
      }
    },
    movedown() {
      if (this.movy + this.canvas.height / this.zoom < 1.1 * this.lcanvas.height) {
        this.movy += 10;
      } else {
        this.continue_movement_down = false;
      }
    },
    moveright() {
      if (this.movx + this.canvas.width / this.zoom < 1.1 * this.canvas.width) {
        this.movx += 10;
      } else {
        this.continue_movement_right = false;
      }
    },
    moveleft() {
      if (this.movx > -0.1 * this.canvas.width) {
        this.movx -= 10;
      } else {
        this.continue_movement_left = false;
      }
    },

    // Map Drawing
    clear() {
      this.c.moveTo(0, 0);
      this.c.beginPath();
      this.c.rect(0, 0, this.canvas.width, this.canvas.height);
      this.c.fillStyle = "rgb(190,190,190)";
      this.c.fill();
      this.c.closePath();
    },
    q2y(orientation) {
      var q0 = orientation.w;
      var q1 = orientation.x;
      var q2 = orientation.y;
      var q3 = orientation.z;
      return -Math.atan2(2 * (q0 * q3 + q1 * q2), 1 - 2 * (q2 * q2 + q3 * q3));
    },
    makemap(tem_mapdata){
      var mapdata = {}
      Object.assign(mapdata, tem_mapdata)
      this.temp_canvas.width = mapdata.info.width;
      this.temp_canvas.height = mapdata.info.height;
      this.imageData = this.c.createImageData(mapdata.info.width, mapdata.info.height)
      for ( var row = mapdata.info.height-1; row > -1; row--) {
        for ( var col = mapdata.info.width-1; col > -1; col--) {
            var mapI = (col + (row * mapdata.info.width))
            var data = mapdata.data[mapI];
            var val;
            if (data === 100) {
                val = 0;
            } else if (data === 0) {
                val = 255;
            } else {
                val = 190;
            }

            // determine the index into the image data array
            // also should be equal to width*height - mapI
            var i = (mapdata.info.width - col + (row * mapdata.info.width))*4
            // r
            this.imageData.data[i] = val;
            // g
            this.imageData.data[++i] = val;
            // b
            this.imageData.data[++i] = val;
            // a
            this.imageData.data[++i] = 255;
        }
      }
    },
    translatepose(x, y, q) {
      var xp =
        this.map.info.width -
        (x - this.map.info.origin.position.x) / this.map.info.resolution;
      var yp = (y - this.map.info.origin.position.y) / this.map.info.resolution;
      var theta = null;
      if (q) {
        theta = this.q2y(q);
        if (theta < 0) {
          theta = Math.PI * 2 + theta;
        }
      }
      return { x: xp, y: yp, theta };
    },
    drawpoint(x, y, color, diameter) {
      var mapping = this.translatepose(x, y);
      this.temp_c.beginPath();
      this.temp_c.moveTo(mapping.x, mapping.y);
      this.temp_c.arc(mapping.x, mapping.y, diameter, 0, 2 * Math.PI);
      this.temp_c.fillStyle = color;
      this.temp_c.fill();
      this.temp_c.closePath();
    },
    drawarrow(x,y,angle,color){
        var mapping = this.translatepose(x,y)
        var x_end = (20*Math.cos(angle)+mapping.x)
        var y_end = (-20*Math.sin(angle)+mapping.y)
        this.temp_c.beginPath();
        this.temp_c.moveTo(mapping.x, mapping.y);
        this.temp_c.lineTo(x_end, y_end);
        this.temp_c.strokeStyle = color;
        this.temp_c.lineWidth = 2;
        this.temp_c.stroke();
        this.temp_c.closePath();
    },
    drawTrack() {
      if (this.global_path.poses) {
        if (this.global_path.poses.length > 0) {
          this.global_path.poses.forEach((pose) => {
            this.drawpoint(
              pose.pose.position.x,
              pose.pose.position.y,
              "blue",
              1
            );
          });
        }
      }
    },
    drawgoal() {
      if (this.point.draw && this.goal_monitor) {
        var color = "blue";
        if (
          !(
            this.point.robot_x - this.goal_monitor["pose"]["x"] < 0.2 &&
            this.point.robot_y - this.goal_monitor["pose"]["y"] < 0.2
          )
        ) {
          console.log(
            "Not Drawoing Goal because goals point and goal monitor are not matching"
          );
          return;
        }
        if (this.goal_monitor.state == "succeed") {
          color = "green";
        } else if (this.goal_monitor.state == "running") {
          this.drawTrack();
          color = "orange";
        } else if (this.goal_monitor.state == "false") {
          color = "red";
        }
        if (this.goal_monitor.is_angled) {
          this.drawarrow(
            this.point.robot_x,
            this.point.robot_y,
            this.point.angle,
            color
          );
        } else {
          this.drawpoint(this.point.robot_x, this.point.robot_y, color, 2);
        }
      }
    },
    drawpos() {
      if (this.current_pose) {
        var arrow_length = 7;
        var mapping = this.translatepose(
          this.current_pose.position.x,
          this.current_pose.position.y,
          this.current_pose.orientation
        );
        var x = mapping.x;
        var y = mapping.y;
        var theta = mapping.theta + Math.PI;
        var start_theta = theta + Math.PI / 6;
        var end_theta = theta - Math.PI / 6;
        start_theta =
          start_theta > 2 * Math.PI
            ? start_theta - 2 * Math.PI
            : start_theta < 0
            ? start_theta + 2 * Math.PI
            : start_theta;
        end_theta =
          end_theta > 2 * Math.PI
            ? end_theta - 2 * Math.PI
            : end_theta < 0
            ? end_theta + 2 * Math.PI
            : end_theta;
        this.temp_c.beginPath();
        this.temp_c.moveTo(x, y);
        this.temp_c.arc(x, y, arrow_length, start_theta, end_theta);
        this.temp_c.fillStyle = "orange";
        this.temp_c.fill();
        this.temp_c.closePath();
      }
    },
    drawmap() {
      if (this.imageData) {
        this.temp_c.beginPath();
        this.temp_c.moveTo(0, 0);
        this.temp_c.putImageData(this.imageData, 0, 0);
        this.temp_c.closePath();
        this.drawpos();
        this.drawgoal();
        this.c.drawImage(
          this.temp_canvas,
          this.movx,
          this.movy,
          (this.canvas.width / this.zoom) >> 0,
          (this.canvas.height / this.zoom) >> 0,
          0,
          0,
          this.canvas.width,
          this.canvas.height
        );
        this.c.closePath();
      }
    },
    async draw() {
      this.clear();
      this.drawmap();
      await this.sleep(100);
      requestAnimationFrame(this.draw);
    },
    // ######################### Ros ######################
    sleep(duration) {
      return new Promise((resolve) => setTimeout(resolve, duration));
    },
    async connect_to_ros() {
      var flag = true;
      var ros;
      while (flag) {
        await this.sleep(1500).then(() => {
          ros = new ROSLIB.Ros({
            url: `ws://${env.bridge_address}:9090`,
          });
          ros.on("connection", function () {
            flag = false;
            ////console.log('Ros: connected to rosbridge successfully')
          });
          ros.on("error", function () {
            console.error("error connecting to rosbridge");
          });
        });
      }
      return new Promise((resolve) => resolve(ros));
    },
    init_ros() {
      var self = this;
      this.connect_to_ros().then((ros) => {
        self.ros = ros;
        var pose_sub = new ROSLIB.Topic({
          ros: ros,
          name: "/current_pose",
          messageType: "geometry_msgs/Pose",
        });
        pose_sub.subscribe(function (data) {
          self.current_pose = data;
        });

        var global_path_sub = new ROSLIB.Topic({
          ros: ros,
          name: "/slamware_ros_sdk_server_node/global_plan_path",
          messageType: "nav_msgs/Path",
        });
        global_path_sub.subscribe(function (data) {
          self.global_path = data;
        });

        var map_sub = new ROSLIB.Topic({
          ros: ros,
          name: "/slamware_ros_sdk_server_node/map",
          messageType: "nav_msgs/OccupancyGrid",
          compression: "png",
        });
        map_sub.subscribe(function (data) {
          self.map = data;
          self.makemap(data);
        });
        var goal_monitor_sub = new ROSLIB.Topic({
          ros: ros,
          name: "/navigation/goal_monitor",
          messageType: "status_msgs/goal_monitor_msg",
        });
        goal_monitor_sub.subscribe(function (data) {
          self.goal_monitor = data;
        });
      });
    },
  },
  mounted() {
    var self = this
    // ######################### speak ######################
    this.speak_fetch_sounds();

    // ######################### interface ######################
    this.interface_fetch_sets();

    // ######################### map ######################
    this.canvas = document.getElementById("map");
    this.temp_canvas = document.getElementById("temp");
    this.c = this.canvas.getContext("2d");
    this.temp_c = this.temp_canvas.getContext("2d");

    this.init_ros();

    this.root = document.getElementById("root");
    this.bar = document.getElementById("mainbar");

    this.canvas.width = this.root.offsetWidth;
    this.canvas.height = window.innerHeight - this.bar.offsetHeight;
    window.onresize = function () {
      setTimeout(() => {
        self.canvas.width = self.root.offsetWidth;
        self.canvas.height = window.innerHeight - self.bar.offsetHeight;
      }, 10);
    };

    this.draw();
  },
};
</script>
<style>
  
      canvas
      {
          image-rendering: optimizeSpeed;
          image-rendering: -moz-crisp-edges;
          image-rendering: -webkit-optimize-contrast;
          image-rendering: -o-crisp-edges;
          image-rendering: crisp-edges;
          -ms-interpolation-mode: nearest-neighbor;
          touch-action: none;
          -ms-touch-action: none;
      }
</style>
