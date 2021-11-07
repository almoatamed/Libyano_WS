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
      @click='set_defaults'
      >
        <v-icon large>mdi-robot</v-icon>
      </v-btn>

    </v-app-bar>


    <v-card
      class="pa-0"
      flat
      style="background-color:#FFC74A00; position:fixed; z-index:1; bottom:30px; right:30px;"
    >
      <v-col >
        <v-row>
          <v-spacer></v-spacer>
          <v-btn
            text
            color="#FFC74A"
            @mousedown="move('w')"
            @mouseup="move('stop')"
            @touchstart="move('w')"
            @contextmenu.prevent
            @touchstop="move('stop')"
            @touchcancel="move('stop')"
            @touchend="move('stop')"
          >
            <v-icon large>mdi-chevron-up</v-icon>
          </v-btn>
          <v-spacer></v-spacer>
        </v-row>
        <v-row>
          <v-btn text
            @contextmenu.prevent
            color="#FFC74A"
            @mousedown="move('a')"
            @mouseup="move('stop')"
            @touchstart="move('a')"
            @touchstop="move('stop')"
            @touchcancel="move('stop')"
            @touchend="move('stop')"
          >
            <v-icon large>mdi-chevron-left</v-icon>
          </v-btn>
          <v-spacer></v-spacer>
          <v-btn text
            @contextmenu.prevent
            style='margin-right:-20px;margin-left:-20px'
            color="#FFC74A"
            @mousedown="move('stop')"
            @touchstart="move('stop')"
          >
            <v-icon large>mdi-close-circle-outline</v-icon>
          </v-btn>
          <v-spacer></v-spacer>
          <v-btn text

            @contextmenu.prevent
          
            color="#FFC74A"
            @mousedown="move('d')"
            @mouseup="move('stop')"
            @touchstart="move('d')"
            @touchstop="move('stop')"
            @touchcancel="move('stop')"
            @touchend="move('stop')"
          >
            <v-icon large>mdi-chevron-right</v-icon>
          </v-btn>
        </v-row>
        <v-row >
          <v-spacer></v-spacer>
          <v-btn
            text
            @contextmenu.prevent
            color="#FFC74A"
            @mousedown="move('s')"
            @mouseup="move('stop')"
            @touchstart="move('s')"
            @touchstop="move('stop')"
            @touchcancel="move('stop')"
            @touchend="move('stop')"
          >
            <v-icon large>mdi-chevron-down</v-icon>
          </v-btn>
          <v-spacer></v-spacer>
        </v-row>
      </v-col>
    </v-card>



    <v-card
      class="pa-0"
      flat
      style="background-color:#FFC74A00; position:absolute; z-index:1; bottom:30px; left:30px;"
    >
      <v-col >
        <v-row>
          <v-spacer></v-spacer>
          <v-btn
            text
            color="#FFC74A"
            @mousedown="move_head=true;map_scroll? moveup(): movehead(0,-5)"
            @mouseup="move_head=false"
            @touchstart="move_head=true;map_scroll? moveup(): movehead(0,-5)"
            @contextmenu.prevent
            @touchstop="move_head=false"
            @touchcancel="move_head=false"
            @touchend="move_head=false"
          >
            <v-icon large>mdi-chevron-up</v-icon>
          </v-btn>
          <v-spacer></v-spacer>
        </v-row>
        <v-row>
          <v-btn text
            color="#FFC74A"
            @mousedown="move_head=true;map_scroll? moveleft():movehead(-10,0)"
            @mouseup="move_head=false"
            @touchstart="move_head=true;map_scroll? moveleft():movehead(-10,0)"
            @contextmenu.prevent
            @touchstop="move_head=false"
            @touchcancel="move_head=false"
            @touchend="move_head=false"
          >
            <v-icon large>mdi-chevron-left</v-icon>
          </v-btn>
          <v-spacer></v-spacer>
          <v-btn text
            @contextmenu.prevent
            style='margin-right:-20px;margin-left:-20px'
            color="#FFC74A"
            @mousedown="moveheadhome"
            @touchstart="moveheadhome"
            v-show="!map_scroll"
          >
            <v-icon large>mdi-close-circle-outline</v-icon>
          </v-btn>
          <v-spacer></v-spacer>
          <v-btn text
            color="#FFC74A"
            @mousedown="move_head=true;map_scroll? moveright():movehead(10,0)"
            @mouseup="move_head=false"
            @touchstart="move_head=true;map_scroll? moveright():movehead(10,0)"
            @contextmenu.prevent
            @touchstop="move_head=false"
            @touchcancel="move_head=false"
            @touchend="move_head=false"
          >
            <v-icon large>mdi-chevron-right</v-icon>
          </v-btn>
        </v-row>
        <v-row >
          <v-spacer></v-spacer>
          <v-btn
            text
            color="#FFC74A"
            @mousedown="move_head=true;map_scroll? movedown():movehead(0,5)"
            @mouseup="move_head=false"
            @touchstart="move_head=true;map_scroll? movedown():movehead(0,5)"
            @contextmenu.prevent
            @touchstop="move_head=false"
            @touchcancel="move_head=false"
            @touchend="move_head=false"
          >
            <v-icon large>mdi-chevron-down</v-icon>
          </v-btn>
          <v-spacer></v-spacer>
        </v-row>
      </v-col>
    </v-card>



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
                <!-- <v-btn text @click="speak_stop()">
                  <v-icon>mdi-stop</v-icon>
                </v-btn> -->
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
          <v-btn small @click='angled_point=true' :color="angled_point? 'orange':'primary' " class="mr-2">Angled</v-btn>
          <v-btn small @click='angled_point=false' :color="!angled_point? 'orange':'primary' ">Unangled</v-btn>
          <v-divider class="my-4 secondary" />
          <v-card
            class="mx-auto"
            max-width="300"
            max-height="150"
            tile
            style="overflow-y: auto"
            v-if="!angled_point"

          >
            <v-list-item
            v-for="(point,index) in points.unangled_points"
            :key="index"
            >
              <v-list-item-content 
              :style="selected_point.name==point.name ? 'background:orange' : ''"
              @click="selected_point.name!=point.name?selected_point= point:selected_point= {}" 
              class="pa-0">
                <v-btn text>{{point.name}} </v-btn>
              </v-list-item-content>
            </v-list-item>
          </v-card>
          <v-card
            class="mx-auto"
            max-width="300"
            max-height="150"
            tile
            style="overflow-y: auto"
            v-else

          >
            <v-list-item
            v-for="(point,index) in points.angled_points"
            :key="index"
            >
              <v-list-item-content 
              :style="selected_point.name==point.name ? 'background:orange' : ''"
              @click="selected_point.name!=point.name?selected_point= point:selected_point= {}" 
              class="pa-0">
                <v-btn text>{{point.name}} </v-btn>
              </v-list-item-content>
            </v-list-item>
          </v-card>
          <!-- <v-text-field
            type="number"
            label="Time"
          /> -->
          <v-btn dark color="primary"
          @click="go_to_point"
          > Go </v-btn>
        </v-card-text>
      </v-card>
    </v-menu>

    <!-- interface view -->
    <v-card
      id="interfaces_dialog"
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
      v-model="interfaces_dialog"
      :close-on-content-click="false"
      activator="#interfaces_dialog"
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

    <!-- head motions -->
    <v-card
      id="head_motions_dialog"
      class="py-2 px-4"
      color="rgba(0, 0, 0, .3)"
      dark
      flat
      link
      min-width="100"
      style="
        position: fixed;
        top: 115px;
        right: -35px;
        border-radius: 8px;
        z-index: 1;
      "
    >
      <v-icon large> mdi-robot </v-icon>
    </v-card>
    <v-menu
      v-model="head_motions_dialog"
      :close-on-content-click="false"
      activator="#head_motions_dialog"
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
          <strong class="mb-3 d-inline-block font-weight-black">Head Motions</strong>

          <v-divider class="my-4 secondary" />
          <v-card
            class="mx-auto"
            max-width="300"
            max-height="150"
            tile
            style="overflow-y: auto"
          >
            <v-list-item
              v-for="(motion, index) in head_motions_names"
              :key="index"
              :style="head_motion == motion ? 'background:orange' : ''"
              @click="head_motion = motion"
            >
              <v-list-item-content class="pa-0">
                <v-btn text>
                  {{ motion }}
                </v-btn>
              </v-list-item-content>
            </v-list-item>
          </v-card>
          <v-btn dark @click="set_head_motion" color="primary"> Go </v-btn>
        </v-card-text>
      </v-card>
    </v-menu>

    <!-- Acts -->
    <v-card
      id="acts_dialog"
      class="py-2 px-4"
      color="rgba(0, 0, 0, .3)"
      dark
      flat
      link
      min-width="100"
      style="
        position: fixed;
        top: 505px;
        right: -35px;
        border-radius: 8px;
        z-index: 1;
      "
    >
      <v-icon large> mdi-play </v-icon>
    </v-card>
    <v-menu
      v-model="acts_dialog"
      :close-on-content-click="false"
      activator="#acts_dialog"
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
          <strong class="mb-3 d-inline-block font-weight-black">ACTS</strong>

          <v-divider class="my-4 secondary" />
          <v-card
            class="mx-auto"
            max-width="300"
            max-height="150"
            tile
            style="overflow-y: auto"
          >
            <v-list-item
              v-for="(act, index) in acts_names"
              :key="index"
              :style="act_name == act ? 'background:orange' : ''"
              @click="act_name = act"
            >
              <v-list-item-content class="pa-0">
                <v-btn text>
                  {{ act }}
                </v-btn>
              </v-list-item-content>
            </v-list-item>
          </v-card>
        </v-card-text>
        <v-card-actions>
              <v-btn @click="play_act()" text icon>
                <v-icon>mdi-motion-play-outline</v-icon>
              </v-btn>
              <v-btn @click="push_act()" text icon>
                <v-icon>mdi-shape-circle-plus</v-icon>
              </v-btn>
              <v-btn @click="toggle_pause('0')" text icon>
                <v-icon>mdi-play</v-icon>
              </v-btn>
              <v-btn @click="toggle_pause('1')" text icon>
                <v-icon>mdi-pause</v-icon>
              </v-btn>
              <v-btn @click="stop_and_clear()" text icon>
                <v-icon>mdi-stop</v-icon>
              </v-btn>
        </v-card-actions>
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
        top: 570px;
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
                @mousedown="continue_zoomin=true;zoomin()"
                @mouseup="continue_zoomin=false"
                @touchstart="continue_zoomin=true;zoomin()"
                @contextmenu.prevent
                @touchstop="continue_zoomin=false"
                @touchcancel="continue_zoomin=false"
                @touchend="continue_zoomin=false"
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
                @mousedown="continue_zoomout=true;zoomout()"
                @mouseup="continue_zoomout=false"
                @touchstart="continue_zoomout=true;zoomout()"
                @contextmenu.prevent
                @touchstop="continue_zoomout=false"
                @touchcancel="continue_zoomout=false"
                @touchend="continue_zoomout=false"
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
                :color="!map_scroll?'rgba(0, 0, 0, .3)':'rgba(255, 175, 0, .3)'"
                dark
                flat
                @click="map_scroll=!map_scroll"
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
import env from '../../../env'
import ROSLIB from 'roslib'
import q from 'quaternion'


var root

var canvas
var c
var temp_canvas
var temp_c

var bar
var goal_monitor
var map
var imageData
var current_pose
var global_path = {}

var zoom = 2.5
var movx = 0
var movy = 0

// ####################### connecting to ros #################################3
function sleep(duration){
    return new Promise(resolve => setTimeout(resolve, duration))
}
async function connect_to_ros(){
    var flag = true;
    var ros;
    while(flag){
        await sleep(1500).then(()=>{
            ros = new ROSLIB.Ros({
                url : `ws://${env.bridge_address}:9090`
            });
            ros.on('connection', function(){
                flag = false;
                ////console.log('Ros: connected to rosbridge successfully')
            });
            ros.on('error',function(){
                console.error('error connecting to rosbridge')
            })
        })
    }
    return new Promise(resolve => resolve(ros))
}

// ########################### converting map data to image data valid for canvas ##########3
function makemap(tem_mapdata){
    var mapdata = {}
    Object.assign(mapdata, tem_mapdata)
    temp_canvas.width = mapdata.info.width;
    temp_canvas.height = mapdata.info.height;
    imageData = c.createImageData(mapdata.info.width, mapdata.info.height)
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
                val = 127;
            }

            // determine the index into the image data array
            // also should be equal to width*height - mapI
            var i = (mapdata.info.width - col + (row * mapdata.info.width))*4
            // r
            imageData.data[i] = val;
            // g
            imageData.data[++i] = val;
            // b
            imageData.data[++i] = val;
            // a
            imageData.data[++i] = 255;
        }
    }
}

// ########################## clearing frame ########################################
function clear(){
    c.moveTo(0,0)
    c.beginPath()
    c.rect(0,0,canvas.width,canvas.height);  
    c.fillStyle = "rgb(127,127,127)"
    c.fill();
    c.closePath()
}

// ######################## robot position #################################
function q2y(orientation) {
  var q0 = orientation.w;
  var q1 = orientation.x;
  var q2 = orientation.y;
  var q3 = orientation.z;
  return -Math.atan2(2 * (q0 * q3 + q1 * q2), 1 - 2 * (q2 * q2 + q3 * q3));
}
function translatepose(x,y,q){
    // the 10 should be replaced with the accurate value of the map dimention 
    // this is an echo of the map metadata
    // map_load_time: 
    // secs: 687
    // nsecs: 693000000
    // resolution: 0.0500000007451
    // width: 384
    // height: 384
    // origin: 
    // position: 
    //     x: -10.0
    //     y: -10.0
    //     z: 0.0
    // orientation: 
    //     x: 0.0
    //     y: 0.0
    //     z: 0.0
    //     w: 1.0
    //
    // position is where we take these values from

    var xp  = map.info.width -((x-map.info.origin.position.x)/map.info.resolution)
    var yp  = (y-map.info.origin.position.y)/map.info.resolution
    var theta = null
    if (q){
        theta = q2y(q)
        if(theta<0){
            theta = Math.PI*2 +theta
        }
    }
    return {x:xp,y:yp,theta}
}
function drawpos(){
    if(current_pose){
        var arrow_length = 7
        var mapping = translatepose(current_pose.position.x,current_pose.position.y,current_pose.orientation);
        var x = mapping.x //-arrow_length/2//*Math.cos(mapping.theta)
        var y = mapping.y //-arrow_length/2//*Math.sin(mapping.theta)
        var theta = mapping.theta +Math.PI
        var start_theta = theta + Math.PI/6
        var end_theta = theta - Math.PI/6
        start_theta = start_theta > 2*Math.PI? start_theta - 2*Math.PI: start_theta <0 ? start_theta +2*Math.PI: start_theta
        end_theta = end_theta > 2*Math.PI? end_theta - 2*Math.PI: end_theta <0 ? end_theta +2*Math.PI: end_theta
        temp_c.beginPath();
        temp_c.moveTo(x,y)
        temp_c.arc(x, y,arrow_length,start_theta,end_theta)    
        temp_c.fillStyle = "purple"
        temp_c.fill();
        temp_c.closePath()
    }
}

// ######################### goal animation #############################
var point = {}
function drawpoint(x,y,color,diameter){
        var mapping = translatepose(x,y);        
        temp_c.beginPath();
        temp_c.moveTo(mapping.x,mapping.y)
        temp_c.arc(mapping.x, mapping.y,diameter,0,2*Math.PI)    
        temp_c.fillStyle = color
        temp_c.fill();
        temp_c.closePath()
        
}
function drawarrow(x,y,angle,color){
    var mapping = translatepose(x,y)
    var x_end = (20*Math.cos(angle)+mapping.x)
    var y_end = (-20*Math.sin(angle)+mapping.y)
    temp_c.beginPath();
    temp_c.moveTo(mapping.x, mapping.y);
    temp_c.lineTo(x_end, y_end);
    temp_c.strokeStyle = color;
    temp_c.lineWidth = 2;
    temp_c.stroke();
    temp_c.closePath();
}
function drawTrack(){
    if(global_path.poses){

        if(global_path.poses.length > 0){
            global_path.poses.forEach((pose) => {
                drawpoint(pose.pose.position.x,pose.pose.position.y,'blue', 1)
            });
        }
    }
}
function drawgoal(){
    if(point.draw && goal_monitor)   {
        var color = 'blue'
        if(!((point.robot_x - goal_monitor['pose']['x'] < 0.15) && (point.robot_y - goal_monitor['pose']['y'] < 0.15))){
            console.log('returning')
            return 
        }
        if(goal_monitor.state == 'succeed'){
            color = 'green'
        }else if(goal_monitor.state == 'running'){
            drawTrack()
            color = 'orange'
        }else if(goal_monitor.state == 'false'){
            color = 'red'
        }
        if(goal_monitor.is_angled){
            drawarrow(point.robot_x,point.robot_y,point.angle,color)
        }else{
            drawpoint(point.robot_x,point.robot_y,color,2)
        }
    }
}

// ########################### draw map frame ##################################
function drawmap(){
  if(imageData){
    temp_c.beginPath()
    temp_c.moveTo(0,0)
    temp_c.putImageData(imageData,0,0)
    temp_c.closePath()
    drawpos()
    drawgoal()
    c.drawImage(temp_canvas,movx,movy,(canvas.width/zoom) >> 0,(canvas.height/zoom) >> 0,0,0,canvas.width,canvas.height)
    c.closePath()
  }
}

// ########################### frame drawer #####################################
async function draw(){
  clear()
  drawmap()
  await sleep(100)
  requestAnimationFrame(draw)
} 

export default {
  name: "DashboardView",

  data() {
    return {
      chat: false,
      led: false,
      emoji: false,
      map_point: false,
      interfaces_dialog: false,
      acts_dialog:false,

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

      // ######################### led ring ######################33
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

      // ######################### head motions ######################
      head_motions_names: [],
      head_motion: "",
      head_motions_dialog:false,

      // ######################### navigation ######################
      navigation_manual: false,
      angled_goal: false,
      unangled_goal: false,
      // ######################### map  ######################
      map_scroll: false,
      continue_zoomin:false,
      continue_zoomout:false,

      // ######################### navigation point  ######################
      points:{
        angled_points:[],
        unangled_points:[],
      },
      angled_point:false,
      selected_point:{
        type:'',
        name:'',
        point:{}
      },

      // ######################### acts  ######################
      acts_names:[],
      act_name:'',
    };
  },
  methods: {
    // ######################### Head Movement ######################33
    movehead(x, y) {
      if (this.move_head) {
        this.$store.dispatch(
          "Ros/take_action",
          `interactive/head_relative_move/${x}/${y}/700`
        );
        setTimeout(() => {
          this.movehead(x, y);
        }, 250);
      }
    },
    moveheadhome() {
      this.$store
        .dispatch("Ros/take_action", `interactive/head_move_home`, {
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
            `interactive/speak_push_to_queue/${this.speak_file}.mp3`,
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

    set_defaults(){
      this.interface_view = 'main'
      this.interface_set()
      this.$store.dispatch('Ros/take_action','interactive/head_move_home',{root:true})
      this.$store.dispatch('Ros/take_action', 'interactive/set_eyes/blink/0/1',{root:true})
      this.$store.dispatch('Ros/take_action', 'interactive/set_ring_flow/fadeoutfadein/0/1',{root:true})
      var color = this.emoji_default_color.slice(1, -2);
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
      canvas.addEventListener(
        "mousedown",
        this.angled_goal_mousedown_handler
      );
      canvas.addEventListener("mouseup", this.angled_goal_mouseup_handler);
    },
    wait_for_unangled_goal() {
      this.unangled_goal = true;
      canvas.addEventListener(
        "mousedown",
        this.unangled_goal_mousedown_handler
      );
      canvas.addEventListener(
        "mouseup",
        this.unangled_goal_mouseup_handler
      );
    },

    angled_goal_mousedown_handler(e) {
      var data = c.getImageData(e.layerX, e.layerY, 1, 1).data;
      if ((data[0] == 255, data[1] == 255, data[2] == 255)) {
        point = {};
        point.x = e.layerX / zoom + movx;
        point.layerX = e.layerX;
        point.y = e.layerY / zoom + movy;
        point.layerY = e.layerY;
        point.drop = true;
        point.draw = false;
      }
    },
    angled_goal_mouseup_handler(e) {
      if (point.drop && map.info) {
        point.drop = false;
        point.abs_angle = Math.atan(
          Math.abs(
            (e.layerY - point.layerY) / (e.layerX - point.layerX)
          )
        );
        point.end_layerX = e.layerX;
        point.end_layerY = e.layerY;

        if (point.end_layerX - point.layerX > 0) {
          if (point.end_layerY - point.layerY > 0) {
            point.angle = 2 * Math.PI - point.abs_angle;
          } else {
            point.angle = point.abs_angle;
          }
        } else {
          if (point.end_layerY - point.layerY > 0) {
            point.angle = Math.PI + point.abs_angle;
          } else {
            point.angle = Math.PI - point.abs_angle;
          }
        }

        point.robot_angle = Math.PI + point.angle;
        if (point.robot_angle > 2 * Math.PI) {
          point.robot_angle = -2 * Math.PI + point.robot_angle;
        }

        point.robot_x =
          (map.info.width - point.x) * map.info.resolution +
          map.info.origin.position.x;
        point.robot_y =
          point.y * map.info.resolution + map.info.origin.position.y;
        var qs = q.fromEuler(0, 0, point.robot_angle, "XYZ");
        this.$store
          .dispatch(
            "Ros/take_action",
            `navigation/angled_goal/${point.robot_x}&${
              point.robot_y
            }&${0.0}&${qs.x}&${qs.y}&${qs.z}&${qs.w}`
          )
          .then((res) => {
            console.log(res);
            point.draw = true;
          });
      }
    },

    unangled_goal_mousedown_handler(e) {
      var data = c.getImageData(e.layerX, e.layerY, 1, 1).data;
      if ((data[0] == 255, data[1] == 255, data[2] == 255)) {
        point = {};
        point.x = e.layerX / zoom + movx;
        point.layerX = e.layerX;
        point.y = e.layerY / zoom + movy;
        point.layerY = e.layerY;
        point.drop = true;
        point.draw = false;
      }
    },
    unangled_goal_mouseup_handler() {
      if (point.drop && map.info) {
        point.drop = false;

        point.robot_x =
          (map.info.width - point.x) * map.info.resolution +
          map.info.origin.position.x;
        point.robot_y =
          point.y * map.info.resolution + map.info.origin.position.y;
        this.$store
          .dispatch(
            "Ros/take_action",
            `navigation/unangled_goal/${point.robot_x}&${point.robot_y}`
          )
          .then((res) => {
            console.log(res);
            point.draw = true;
          });
      }
    },

    cancel_goal() {
      console.log("clearing event listener");
      this.angled_goal = false;
      this.unangled_goal = false;
      canvas.removeEventListener(
        "mousedown",
        this.angled_goal_mousedown_handler
      );
      canvas.removeEventListener("mouseup", this.angled_goal_mouseup_handler);
      canvas.removeEventListener(
        "mousedown",
        this.unangled_goal_mousedown_handler
      );
      canvas.removeEventListener("mouseup", this.unangled_goal_mouseup_handler);
    },
    go_home(){
        this.$store.dispatch('Ros/take_action',`navigation/go_home`).then(()=>{
            this.clear_goal()
        }).catch(()=>{
        })
    },
    // ######################### act ######################

    play_act(){
        this.$store.dispatch('Ros/take_action',
        `act/play_new_act_by_name/${this.act_name}`
        , {root:true})
    },
    push_act(){
        this.$store.dispatch('Ros/take_action',
        `act/push_to_queue_by_name/${this.act_name}`
        , {root:true})
    },
    toggle_pause(val){
        this.$store.dispatch('Ros/take_action', `act/toggle_pause/${val}`, {root:true}).then(res=>{
            console.log(res)
        })
    },
    stop_and_clear(){
        this.$store.dispatch('Ros/take_action', 'act/stop_and_clear', {root:true}).then(res=>{
            console.log(res)
        })
    },
    fetch_acts_names() {
      console.log('dispatching fetch acts')
      this.$store
        .dispatch("Ros/take_action", "act/get_acts_names", { root: true })
        .then((res) => {
        console.log(res)
          console.log('valid',res);
          this.acts_names = res.split('|')
        });
    },

    // ######################### Map ######################
    // Map zoomin/zoomout
    zoomin(e) {
      console.log(e);
      if (this.continue_zoomin) {
        if (zoom < 2.5) {
          zoom += 0.1;
        } else {
          this.continue_zoomin = false;
        }
        setTimeout(this.zoomin, 60);
      }
    },
    zoomout() {
      if (this.continue_zoomout) {
        if (zoom > 0.5) {
          zoom -= 0.1;
        } else {
          this.continue_zoomout = false;
        }
        setTimeout(this.zoomout, 60);
      }
    },
    // Map location controls
    moveup() {
      if(this.move_head){
        if (movy > -0.1 * canvas.height) {
          movy -= 10;
        } else {
          this.move_head = false;
        } 
        setTimeout(() => {this.moveup()}, 60);
      }
    },
    movedown() {
      if(this.move_head){
        if (movy + canvas.height / zoom < 1.1 * canvas.height) {
          movy += 10;
        } else {
          this.move_head = false;
        } 
        setTimeout(() => {this.movedown()}, 60);
      }
    },
    moveright() {
      if(this.move_head){
          console.log('attempting moving right')
        if (movx + canvas.width / zoom < 1.1 * canvas.width) {
          console.log('moving right')
          movx += 10;
        } else {

          this.move_head = false;
        } 
        setTimeout(() => {this.moveright()}, 60);
      }
    },
    moveleft() {
      if(this.move_head){
        if (movx > -0.1 * canvas.width) {
          movx -= 10;
        } else {
          this.move_head = false;
        } 
        setTimeout(() => {this.moveleft()}, 60);
      }
    },
    // Map Drawing
    // ######################### navigation ######################
    move(direction){
      if((direction == 'w') && this.navigation_manual){
        this.$store.dispatch('Ros/take_action', 'navigation/move/0.23/0',{root:true})
      }else if((direction == 'a' ) && this.navigation_manual){
        this.$store.dispatch('Ros/take_action', 'navigation/move/0/0.7',{root:true})
      }else if((direction == 's' ) && this.navigation_manual){
        this.$store.dispatch('Ros/take_action', 'navigation/move/-0.23/0',{root:true})
      }else if((direction == 'd' ) && this.navigation_manual){
        this.$store.dispatch('Ros/take_action', 'navigation/move/0/-0.7',{root:true})
      }else if((direction == 'stop' )){
        this.$store.dispatch('Ros/take_action', 'navigation/move/0/0',{root:true})
      }

    },
    handlecontextmenu(e){
      e.preventDefault();
      
      // console.log(e.target.dispatchEvent(new Event('touchstop')))
    },
    go_to_point(){
      if(this.selected_point.name){
        if(this.selected_point.type == 'unangled'){
          this.$store
            .dispatch(
              "Ros/take_action",
              `navigation/unangled_goal/${this.selected_point.point.x}&${this.selected_point.point.y}`,
              {root:true}
            )
            .then((res) => {
              console.log(res);
              point.draw = true;
            });
        }else{
          this.$store
            .dispatch(
              "Ros/take_action",
              `navigation/angled_goal/${this.selected_point.point.position.x}&${this.selected_point.point.position.y}&${this.selected_point.point.position.z}&${this.selected_point.point.orientation.x}&${this.selected_point.point.orientation.y}&${this.selected_point.point.orientation.z}&${this.selected_point.point.orientation.w}`
              ,{root:true}
            )
            .then((res) => {
              console.log(res);
              point.draw = true;
            });

        }
      }
    },

    // ######################### head_motions ######################
    fetch_head_motions_names(){
      this.$store.dispatch('Ros/take_action', 'interactive/head_get_motions_names',{root:true}).then(res=>{
        this.head_motions_names = res.split('|')
      })
    }, 
    set_head_motion(){
      if(this.head_motion != ''){
        this.$store.dispatch('Ros/take_action', `interactive/head_play_motions_by_name/${this.head_motion}`)
      }
    }

  },
  mounted() {
    document.addEventListener('keydown', (event) => {
      var name = event.key;
      if((name == 'w' || name=='ArrowUp') && this.navigation_manual){
        this.$store.dispatch('Ros/take_action', 'navigation/move/0.23/0',{root:true})
      }else if((name == 'a' || name=='ArrowLeft') && this.navigation_manual){
        this.$store.dispatch('Ros/take_action', 'navigation/move/0/0.7',{root:true})
      }else if((name == 's' || name=='ArrowDown') && this.navigation_manual){
        this.$store.dispatch('Ros/take_action', 'navigation/move/-0.23/0',{root:true})
      }else if((name == 'd' || name=='ArrowRight') && this.navigation_manual){
        this.$store.dispatch('Ros/take_action', 'navigation/move/0/-0.7',{root:true})
      }else if((name == 'Enter' || name=='Space')){
        // this.$store.dispatch('Ros/take_action', 'navigation/move/0/0',{root:true})
      }
    }, false);
    document.addEventListener('keyup', (e) => {
      console.log(e.key)
      var name = e.key
      if((name == 'w' || name=='ArrowUp') && this.navigation_manual){
        this.$store.dispatch('Ros/take_action', 'navigation/move/0/0',{root:true})
      }else if((name == 'a' || name=='ArrowLeft') && this.navigation_manual){
        this.$store.dispatch('Ros/take_action', 'navigation/move/0/0',{root:true})
      }else if((name == 's' || name=='ArrowDown') && this.navigation_manual){
        this.$store.dispatch('Ros/take_action', 'navigation/move/0/0',{root:true})
      }else if((name == 'd' || name=='ArrowRight') && this.navigation_manual){
        this.$store.dispatch('Ros/take_action', 'navigation/move/0/0',{root:true})
      }else if((name == 'Enter' || name==' ')){
        this.$store.dispatch('Ros/take_action', 'navigation/move/0/0',{root:true})
      }
    }, false);
    // ######################### head motion ######################
    this.fetch_head_motions_names();
    // ######################### speak ######################
    this.speak_fetch_sounds();

    // ######################### interface ######################
    this.interface_fetch_sets();

    // ######################### acts ######################
    this.fetch_acts_names()

    // ######################### map ######################
    canvas = document.getElementById('map')
    temp_canvas = document.getElementById('temp')

    

    c = canvas.getContext('2d')
    temp_c = temp_canvas.getContext('2d')

    // setInterval(()=>{
    //   this.$store.dispatch('Ros/take_action','navigation/get_current_pose', {root:true}).then(res=>{
    //     current_pose = {}
    //     res = res.split('&')
    //     current_pose.position = {}
    //     current_pose.position.x = parseFloat(res[0])
    //     current_pose.position.y = parseFloat(res[1])
    //     current_pose.position.z = parseFloat(res[2])
    //     current_pose.orientation = {}
    //     current_pose.orientation.x = parseFloat(res[3])
    //     current_pose.orientation.y = parseFloat(res[4])
    //     current_pose.orientation.z = parseFloat(res[5])
    //     current_pose.orientation.w = parseFloat(res[6])
    //   })
    // },300)

    this.$store.dispatch('Ros/take_action', 'navigation/fetch_points',{root:true}).then(res=>{
          if(res == ''){
              console.log('love')
          }else{
              res = res.split('|').slice(1)
              this.points.angled_points = []
              this.points.unangled_points = []
              res.forEach(el=>{
                  el = el.split('&')
                  if(el.length <= 3){
                    this.points.unangled_points.push({
                        name:el[0],
                        type:'unangled',
                        point:{
                          x:el[1],
                          y:el[2]
                        }
                    })
                  }else{
                    this.points.angled_points.push({
                        name:el[0],
                        type:'angled',
                        point:{
                          position:{
                            x:el[1],
                            y:el[2],
                            z:el[3],
                          },
                          orientation:{
                            x:el[4],
                            y:el[5],
                            z:el[6],
                            w:el[7]
                          }
                        },
                    })
                  }
              })
          }
      })


    setTimeout(()=>{
        connect_to_ros().then(ros=>{

            var current_pose = new ROSLIB.Topic({
                throttle_rate: 100,
                // queue_size:1,
                ros: ros,
                name: '/current_pose',
                messageType: 'geometry_msgs/Pose',
            })
            current_pose.subscribe(function(data){
                data['position']
                current_pose = {}
                current_pose.position = {}
                current_pose.position.x = data['position']['x']
                current_pose.position.y = data['position']['y']
                current_pose.position.z = data['position']['z']
                current_pose.orientation = {}
                current_pose.orientation.x = data['orientation']['x']
                current_pose.orientation.y = data['orientation']['y']
                current_pose.orientation.z = data['orientation']['z']
                current_pose.orientation.w = data['orientation']['w']
            }); 
            var global_path_sub = new ROSLIB.Topic({
                throttle_rate: 100,
                // queue_size:1,
                ros: ros,
                name: '/slamware_ros_sdk_server_node/global_plan_path',
                messageType: 'nav_msgs/Path',
            })
            global_path_sub.subscribe(function(data){
                global_path = data
            }); 
            
            var map_sub = new ROSLIB.Topic({
                throttle_rate: 1000,
                queue_size:1,
                ros: ros,
                name: '/slamware_ros_sdk_server_node/map',
                messageType: 'nav_msgs/OccupancyGrid',
                compression : 'png'
            })
            map_sub.subscribe(function(data){
                map  = data;
                makemap(data);
            });
            var goal_monitor_sub = new ROSLIB.Topic({
                throttle_rate: 100,
                // queue_size:1,
                ros: ros,
                name: '/navigation/goal_monitor',
                messageType: 'status_msgs/goal_monitor_msg',
            })
            goal_monitor_sub.subscribe(function(data){
                goal_monitor = data
            });
        })
    },10)

    root = document.getElementById('root')
    bar = document.getElementById('mainbar')

    canvas.width = root.offsetWidth
    canvas.height = window.innerHeight - bar.offsetHeight
    // this event listener used to set the canvas to fit the window changes 
    window.onresize = function(){
      setTimeout(()=>{
        canvas.width = root.offsetWidth
        canvas.height = window.innerHeight - bar.offsetHeight
      },10)
    }
    draw()
  
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
