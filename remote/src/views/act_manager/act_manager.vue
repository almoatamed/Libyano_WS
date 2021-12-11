<template>
  <div id="root">
    <v-container>
      <!-- New Action-->
      <v-dialog v-model="acts.act_edit.new_action_dialog.show" max-width="500px" persistent>
        <v-card class="mx-auto pa-4" max-width="500px" outlined>
          <v-card-text class="text-h5 font-weight-bold">
            <v-row>
            <v-col cols="12">
                <v-combobox
                v-model="acts.act_edit.new_action_dialog.category"
                :items="acts.actions_categories"
                label="Category"
                ></v-combobox>
            </v-col>
            </v-row>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="primary" @click="create_action" light> Create </v-btn>
            <v-spacer></v-spacer>
            <v-btn color="primary" @click="acts.act_edit.new_action_dialog.show = false" light>
              cancel
            </v-btn>
            <v-spacer></v-spacer>
          </v-card-actions>
        </v-card>
      </v-dialog>


      <!-- New Act-->
      <v-dialog v-model="acts.new_act_dialog.show" max-width="500px" persistent>
        <v-card class="mx-auto pa-4" max-width="500px" outlined>
          <v-card-text class="text-h5 font-weight-bold">
            <v-text-field
              v-model="acts.new_act_dialog.name"
              type="text"
              label="Point Name"
            ></v-text-field>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="primary" @click="create_act" light> Create </v-btn>
            <v-spacer></v-spacer>
            <v-btn color="primary" @click="acts.new_act_dialog.show = false" light>
              cancel
            </v-btn>
            <v-spacer></v-spacer>
          </v-card-actions>
        </v-card>
      </v-dialog>

      <!-- Edit navigation action -->
      <v-dialog v-model="acts.act_edit.action_edit.navigation_dialog.show" max-width="500px" persistent>
        <v-card
        :close-on-content-click="false"
        bottom
        content-class="v-settings"
        left
        nudge-top="260"
        nudge-left="8"
        class="pa-4"
        transition="scale-transition"
        >
        <v-card-text>
            <strong class="mb-3 d-inline-block font-weight-black">POINT ACTION</strong>

            <v-divider class="my-4 secondary" />
            <v-btn small @click='acts.act_edit.action_edit.navigation_dialog.angled_point=true' :color="acts.act_edit.action_edit.navigation_dialog.angled_point? 'orange':'primary' " class="mr-2">Angled</v-btn>
            <v-btn small @click='acts.act_edit.action_edit.navigation_dialog.angled_point=false' :color="!acts.act_edit.action_edit.navigation_dialog.angled_point? 'orange':'primary' ">Unangled</v-btn>
            <v-divider class="my-4 secondary" />
            <v-card
                class="mx-auto"
                max-width="300"
                max-height="150"
                tile
                style="overflow-y: auto"
                v-if="!acts.act_edit.action_edit.navigation_dialog.angled_point"

            >
                <v-list-item
                v-for="(point,index) in acts.act_edit.action_edit.navigation_dialog.points.unangled_points"
                :key="index"
                >
                <v-list-item-content 
                :style="acts.act_edit.action_edit.navigation_dialog.selected_point.name==point.name ? 'background:orange' : ''"
                @click="acts.act_edit.action_edit.navigation_dialog.selected_point =Object.assign({},point)" 
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
                v-for="(point,index) in acts.act_edit.action_edit.navigation_dialog.points.angled_points"
                :key="index"
                >
                <v-list-item-content 
                :style="acts.act_edit.action_edit.navigation_dialog.selected_point.name==point.name ? 'background:orange' : ''"
                @click="acts.act_edit.action_edit.navigation_dialog.selected_point= point" 
                class="pa-0">
                    <v-btn text>{{point.name}} </v-btn>
                </v-list-item-content>
                </v-list-item>

            </v-card>
            <v-divider class="my-4 secondary" />

              <v-list-item
                :style="acts.act_edit.action_edit.navigation_dialog.wait == 'wait' ? 'background:orange' : ''"
              >
              
                <v-list-item-content class="pa-0">
                  <v-btn
                    text
                    @click="acts.act_edit.action_edit.navigation_dialog.wait == 'wait'?  acts.act_edit.action_edit.navigation_dialog.wait = 'dont_wait':acts.act_edit.action_edit.navigation_dialog.wait='wait'"
                  >
                    wait
                  </v-btn>
                </v-list-item-content>
              </v-list-item>
        </v-card-text>
            <v-card-actions>
            <v-btn dark color="primary"
            @click="go_to_point"
            icon
            > <v-icon>mdi-play-outline</v-icon> </v-btn>
            <v-btn dark color="primary"
            @click="stop_and_clear"
            icon
            > <v-icon>mdi-stop</v-icon> </v-btn>
            <v-spacer></v-spacer>
            <v-btn dark color="primary"
            @click="save_navigation_action" 
            icon
            > <v-icon>mdi-content-save</v-icon> </v-btn>
            </v-card-actions>
        </v-card>
      </v-dialog>

      <!-- Edit Head motion action -->
      <v-dialog v-model="acts.act_edit.action_edit.head_motion_dialog.show" max-width="500px" persistent>
        <v-card
        :close-on-content-click="false"
        bottom
        content-class="v-settings"
        left
        nudge-top="260"
        nudge-left="8"
        class="pa-4"
        transition="scale-transition"
        >
        <v-card-text>
            <strong class="mb-3 d-inline-block font-weight-black">POINT ACTION</strong>

            <!-- <v-divider class="my-4 secondary" />
            <v-btn small @click='acts.act_edit.action_edit.head_motion_dialog.angled=true' :color="acts.act_edit.action_edit.head_motion_dialog.angled? 'orange':'primary' " class="mr-2">Angle</v-btn>
            <v-btn small @click='acts.act_edit.action_edit.head_motion_dialog.angled=false' :color="!acts.act_edit.action_edit.head_motion_dialog.angled? 'orange':'primary' ">Motion</v-btn>
            <v-divider class="my-4 secondary" /> -->
            <v-card
                class="mx-auto"
                max-width="300"
                max-height="150"
                tile
                style="overflow-y: auto"
            >
                <v-list-item
                v-for="(motion_name,index) in acts.act_edit.action_edit.head_motion_dialog.head_motion_names"
                :key="index"
                >
                <v-list-item-content 
                :style="acts.act_edit.action_edit.head_motion_dialog.head_motion_name==motion_name ? 'background:orange' : ''"
                @click="acts.act_edit.action_edit.head_motion_dialog.head_motion_name = motion_name" 
                class="pa-0">
                    <v-btn text>{{motion_name}} </v-btn>
                </v-list-item-content>
                </v-list-item>
            </v-card>
            <v-divider class="my-4 secondary" />
        </v-card-text>
            <v-card-actions>
            <v-btn dark color="primary"
            @click="play_head_motion"
            icon
            > <v-icon>mdi-play-outline</v-icon> </v-btn>
            <v-btn dark color="primary"
            @click="stop_and_clear"
            icon
            > <v-icon>mdi-stop</v-icon> </v-btn>
            <v-spacer></v-spacer>
            <v-btn dark color="primary"
            @click="save_head_motion_action" 
            icon
            > <v-icon>mdi-content-save</v-icon> </v-btn>
            </v-card-actions>
        </v-card>
      </v-dialog>

      <!-- Edit eyes action -->
      <v-dialog v-model="acts.act_edit.action_edit.emoji_dialog.show" max-width="500px" persistent>
        <v-card
        :close-on-content-click="false"
        bottom
        content-class="v-settings"
        left
        nudge-top="260"
        nudge-left="8"
        class="pa-4"
        transition="scale-transition"
        >
        <v-card-text>
          <strong class="mb-3 d-inline-block font-weight-black">EMOJI</strong>

          <v-divider class="my-4 secondary" />
          <v-row>
            <v-col md="6">
              <v-color-picker
                dot-size="25"
                hide-mode-switch
                mode="hexa"
                v-model="acts.act_edit.action_edit.emoji_dialog.emoji_color"
                swatches-max-height="200"
              />
              <v-list-item
                :style="acts.act_edit.action_edit.emoji_dialog.emoji_return_default == true ? 'background:orange' : ''"
              >
                <v-list-item-content class="pa-0">
                  <v-btn
                    text
                    @click="acts.act_edit.action_edit.emoji_dialog.emoji_return_default = !acts.act_edit.action_edit.emoji_dialog.emoji_return_default"
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
                  :style="emoji == acts.act_edit.action_edit.emoji_dialog.emoji_choise ? 'background:orange' : ''"
                  v-for="(emoji, index) in acts.act_edit.action_edit.emoji_dialog.emojis"
                  :key="index"
                >
                  <v-list-item-content class="pa-0">
                    <v-btn text @click="acts.act_edit.action_edit.emoji_dialog.emoji_choise = emoji">
                      {{ emoji }}
                    </v-btn>
                  </v-list-item-content>
                </v-list-item>
              </v-card>

              <v-subheader> Speed </v-subheader>
              <v-slider thumb-label step="20" v-model="acts.act_edit.action_edit.emoji_dialog.emoji_speed" min='10' max="200" />
              <v-text-field
                label="Repeat"
                v-model="acts.act_edit.action_edit.emoji_dialog.emoji_repeat"
                type="number"
                class="pt-0 mt-0"
              />
              
            </v-col>
          </v-row>
        </v-card-text>
            <v-card-actions>
            <v-btn dark color="primary"
            @click="set_emoji"
            icon
            > <v-icon>mdi-play-outline</v-icon> </v-btn>
            <v-btn dark color="primary"
            @click="stop_and_clear"
            icon
            > <v-icon>mdi-stop</v-icon> </v-btn>
            <v-spacer></v-spacer>
            <v-btn dark color="primary"
            @click="reset_emoji_color"
            icon
            > <v-icon>mdi-replay</v-icon> </v-btn>
            <v-spacer></v-spacer>
            <v-btn dark color="primary"
            @click="save_emoji_action" 
            icon
            > <v-icon>mdi-content-save</v-icon> </v-btn>
            </v-card-actions>
        </v-card>
      </v-dialog>

      <!-- Edit Led ring action -->
      <v-dialog v-model="acts.act_edit.action_edit.led_ring_dialog.show" max-width="500px" persistent>
        <v-card
        :close-on-content-click="false"
        bottom
        content-class="v-settings"
        left
        nudge-top="260"
        nudge-left="8"
        class="pa-4"
        transition="scale-transition"
        >
        <v-card-text>
          <strong class="mb-3 d-inline-block font-weight-black">Led Ring</strong>

          <v-divider class="my-4 secondary" />
          <v-row>
            <v-col md="6">
              <v-color-picker
                dot-size="25"
                hide-mode-switch
                mode="hexa"
                v-model="acts.act_edit.action_edit.led_ring_dialog.led_color"
                swatches-max-height="200"
              />
              <v-list-item
                :style="acts.act_edit.action_edit.led_ring_dialog.led_return_default == true ? 'background:orange' : ''"
              >
                <v-list-item-content class="pa-0">
                  <v-btn
                    text
                    @click="acts.act_edit.action_edit.led_ring_dialog.led_return_default = !acts.act_edit.action_edit.led_ring_dialog.led_return_default"
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
                  :style="flow == acts.act_edit.action_edit.led_ring_dialog.led_flow ? 'background:orange' : ''"
                  v-for="(flow, index) in acts.act_edit.action_edit.led_ring_dialog.led_flows"
                  :key="index"
                >
                  <v-list-item-content class="pa-0">
                    <v-btn text @click="acts.act_edit.action_edit.led_ring_dialog.led_flow = flow">
                      {{ flow }}
                    </v-btn>
                  </v-list-item-content>
                </v-list-item>
              </v-card>

              <v-subheader> Speed </v-subheader>
              <v-slider thumb-label step="20" v-model="acts.act_edit.action_edit.led_ring_dialog.led_speed" min='10' max="200" />
              <v-text-field
                label="Repeat"
                v-model="acts.act_edit.action_edit.led_ring_dialog.led_repeat"
                type="number"
                class="pt-0 mt-0"
              />
            </v-col>
          </v-row>
        </v-card-text>
            <v-card-actions>
            <v-btn dark color="primary"
            @click="set_led_ring_flow"
            icon
            > <v-icon>mdi-play-outline</v-icon> </v-btn>
            <v-btn dark color="primary"
            @click="stop_and_clear"
            icon
            > <v-icon>mdi-stop</v-icon> </v-btn>
            <v-spacer></v-spacer>
            <v-btn dark color="primary"
            @click="reset_led_ring_color"
            icon
            > <v-icon>mdi-replay</v-icon> </v-btn>
            <v-spacer></v-spacer>
            <v-btn dark color="primary"
            @click="save_led_ring_action" 
            icon
            > <v-icon>mdi-content-save</v-icon> </v-btn>
            </v-card-actions>
        </v-card>
      </v-dialog>

      <!-- Edit Led strip action -->
      <v-dialog v-model="acts.act_edit.action_edit.led_strip_dialog.show" max-width="500px" persistent>
        <v-card
        :close-on-content-click="false"
        bottom
        content-class="v-settings"
        left
        nudge-top="260"
        nudge-left="8"
        class="pa-4"
        transition="scale-transition"
        >
        <v-card-text>
          <strong class="mb-3 d-inline-block font-weight-black">Led Strip</strong>

          <v-divider class="my-4 secondary" />
          <v-row>
            <v-col md="12">
              <v-color-picker
                dot-size="25"
                hide-mode-switch
                mode="hexa"
                v-model="acts.act_edit.action_edit.led_strip_dialog.led_color"
                swatches-max-height="200"
              />
            </v-col>
          </v-row>
        </v-card-text>
            <v-card-actions>
            <v-btn dark color="primary"
            @click="set_led_strip"
            icon
            > <v-icon>mdi-play-outline</v-icon> </v-btn>
            <v-btn dark color="primary"
            @click="stop_and_clear"
            icon
            > <v-icon>mdi-stop</v-icon> </v-btn>
            <v-spacer></v-spacer>
            <v-btn dark color="primary"
            @click="reset_led_strip_color"
            icon
            > <v-icon>mdi-replay</v-icon> </v-btn>
            <v-spacer></v-spacer>
            <v-btn dark color="primary"
            @click="save_led_strip_action" 
            icon
            > <v-icon>mdi-content-save</v-icon> </v-btn>
            </v-card-actions>
        </v-card>
      </v-dialog>

      <!-- Edit Speak action -->
      <v-dialog v-model="acts.act_edit.action_edit.speak_dialog.show" max-width="500px" persistent>
        <v-card
        :close-on-content-click="false"
        bottom
        content-class="v-settings"
        left
        nudge-top="260"
        nudge-left="8"
        class="pa-4"
        transition="scale-transition"
        >
        <v-card-text>

          <strong class="mb-3 d-inline-block font-weight-black">CHAT</strong>

          <v-divider class="my-4 secondary" />
          <v-col class="pa-0">
            <v-row>
              <v-col md="12" class="mx-auto">
                <v-card
                  class="mx-auto"
                  max-width="300"
                  max-height="100"
                  tile
                  style="overflow-y: auto"
                >
                  <v-list-item
                    v-for="(file, index) in acts.act_edit.action_edit.speak_dialog.speak_files"
                    :key="index"
                    :style="acts.act_edit.action_edit.speak_dialog.speak_file == file ? 'background:orange' : ''"
                    @click="
                      file == acts.act_edit.action_edit.speak_dialog.speak_file
                        ? (acts.act_edit.action_edit.speak_dialog.speak_file = '')
                        : (acts.act_edit.action_edit.speak_dialog.speak_file = file)
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
          </v-col>
        </v-card-text>
            <v-card-actions>
            <v-btn dark color="primary"
            @click="playfile"
            icon
            > <v-icon>mdi-play-outline</v-icon> </v-btn>
            <v-btn dark color="primary"
            @click="stop_and_clear"
            icon
            > <v-icon>mdi-stop</v-icon> </v-btn>
            <v-spacer></v-spacer>
            <v-btn dark color="primary"
            @click="save_speak_action" 
            icon
            > <v-icon>mdi-content-save</v-icon> </v-btn>
            </v-card-actions>
        </v-card>
      </v-dialog>

      <!-- Edit Interface action -->
      <v-dialog v-model="acts.act_edit.action_edit.interface_dialog.show" max-width="500px" persistent>
        <v-card
        :close-on-content-click="false"
        bottom
        content-class="v-settings"
        left
        nudge-top="260"
        nudge-left="8"
        class="pa-4"
        transition="scale-transition"
        >
        <v-card-text>

          <strong class="mb-3 d-inline-block font-weight-black">CHAT</strong>

          <v-divider class="my-4 secondary" />
          <v-col class="pa-0">
            <v-row>
              <v-col md="12" class="mx-auto">
                <v-card
                  class="mx-auto"
                  max-width="300"
                  max-height="100"
                  tile
                  style="overflow-y: auto"
                >
                  <v-list-item
                    v-for="(view, index) in acts.act_edit.action_edit.interface_dialog.interface_view_sets"
                    :key="index"
                    :style="acts.act_edit.action_edit.interface_dialog.interface_view == view ? 'background:orange' : ''"
                    @click="acts.act_edit.action_edit.interface_dialog.interface_view = view"
                  >
                    <v-list-item-content class="pa-0">
                      <v-btn text>
                        {{ view }}
                      </v-btn>
                    </v-list-item-content>
                  </v-list-item>
                </v-card>
              </v-col>
            </v-row>
          </v-col>
        </v-card-text>
            <v-card-actions>
            <v-btn dark color="primary"
            @click="set_interface"
            icon
            > <v-icon>mdi-play-outline</v-icon> </v-btn>
            <v-spacer></v-spacer>
            <v-btn dark color="primary"
            @click="save_interface_action" 
            icon
            > <v-icon>mdi-content-save</v-icon> </v-btn>
            </v-card-actions>
        </v-card>
      </v-dialog>

      <!-- Edit wait action -->
      <v-dialog v-model="acts.act_edit.action_edit.wait_dialog.show" max-width="500px" persistent>
        <v-card
        :close-on-content-click="false"
        bottom
        content-class="v-settings"
        left
        nudge-top="260"
        nudge-left="8"
        class="pa-4"
        transition="scale-transition"
        >
        <v-card-text>
          <strong class="mb-3 d-inline-block font-weight-black">Wait</strong>

          <v-divider class="my-4 secondary" />
          <v-row>
            <v-col md="12">
              <v-subheader> Time </v-subheader>
              <v-text-field
                label="Repeat"
                v-model="acts.act_edit.action_edit.wait_dialog.time" 
                type="number"
                class="pt-0 mt-0"
              />
            </v-col>
          </v-row>
        </v-card-text>
            <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn dark color="primary"
            @click="save_wait_action" 
            icon
            > <v-icon>mdi-content-save</v-icon> </v-btn>
            </v-card-actions>
        </v-card>
      </v-dialog>

      <!-- Edit Act Dialog -->
      <v-dialog v-model="acts.act_edit.show" persistent>
        <v-card class="mx-auto pa-4" outlined>
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
            <v-spacer></v-spacer>
            <v-btn color="primary" @click="new_action" icon>
              <v-icon>mdi-plus</v-icon>
            </v-btn>
          </v-card-actions>
          <v-card-text class="text-h5 font-weight-bold">
            <v-row>
                
              <v-col cols="12">
                <div >{{ acts.act_edit.act.name }}</div>
              </v-col>

                <!-- Divider -->
                <v-container fluid class="pa-0">
                <v-row>
                    <v-col cols="12">
                    <v-divider></v-divider>
                    </v-col>
                </v-row>
                </v-container>

              <v-col v-if="acts.act_edit.act.actions.length >0" cols="12">
                <v-container>
                  <v-row
                    v-for="(action, index) in acts.act_edit.act.actions"
                    :key="index"
                  >
                    <span>{{ index }}</span>
                    <v-spacer></v-spacer>
                    <v-spacer></v-spacer>
                    <span style='font-size:18px'> {{ action.action_args.slice(0,3).join(' | ') }} </span>
                    <v-spacer></v-spacer>
                    <v-btn @click="edit_action(index)" text icon>
                      <v-icon>mdi-pencil</v-icon>
                    </v-btn>
                    <v-btn @click="del_action(index)" text icon>
                      <v-icon>mdi-delete</v-icon>
                    </v-btn>
                    <v-btn @click="move_action(index, -1)" text icon>
                      <v-icon>mdi-arrow-up</v-icon>
                    </v-btn>
                    <v-btn @click="move_action(index, 1)" text icon>
                      <v-icon>mdi-arrow-down</v-icon>
                    </v-btn>
                  </v-row>
                </v-container>
              </v-col>
              <v-col cols="12" v-else class="">
                <v-container
                  style="display: flex; justify-content: space-around"
                >
                  <span class="">Create Actions</span>
                </v-container>
              </v-col>
            </v-row>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="primary" @click="save_edited_act"> Save </v-btn>
            <v-spacer></v-spacer>
            <v-btn color="primary" @click="acts.act_edit.show = false">
              exit
            </v-btn>
            <v-spacer></v-spacer>
          </v-card-actions>
        </v-card>
      </v-dialog>

      <!-- Act table -->
      <div class="text-h4">Act Manager</div>
      <v-divider class="py-4"></v-divider>
      <v-card  elevation="6" :dark="isDark">
        <!-- Actions -->
        <v-container fluid>
          <v-row>
            <v-col>
              <v-btn @click="toggle_pause('0')" text icon>
                <v-icon>mdi-play</v-icon>
              </v-btn>
              <v-btn @click="toggle_pause('1')" text icon>
                <v-icon>mdi-pause</v-icon>
              </v-btn>
              <v-btn @click="stop_and_clear()" text icon>
                <v-icon>mdi-stop</v-icon>
              </v-btn>
              <v-btn @click="new_act" text icon>
                <v-icon>mdi-plus</v-icon>
              </v-btn>
            </v-col>
          </v-row>
        </v-container>

        <!-- Divider -->
        <v-container fluid class="pa-0">
          <v-row>
            <v-col cols="12">
              <v-divider></v-divider>
            </v-col>
          </v-row>
        </v-container>
        <v-container fluid>
          <v-row>
            <v-col cols="12">
              <div class="text-h6">avaialbe acts</div>
            </v-col>
            <v-col v-if="acts.acts_table.show" cols="12">
                <v-container>
                  <v-row
                    v-for="(act, index) in acts.acts_table.data"
                    :key="index"
                  >
                    <span>{{ index }}</span>
                    <v-spacer></v-spacer>
                    <v-spacer></v-spacer>
                    <span style='font-size:18px'> {{ act.name}} </span>
                    <v-spacer></v-spacer>
                    <v-btn @click="edit_act(act)" text icon>
                      <v-icon>mdi-pencil</v-icon>
                    </v-btn>
                    <v-btn @click="del_act(act.name)" text icon>
                      <v-icon>mdi-delete</v-icon>
                    </v-btn>
                  </v-row>
                </v-container>
            </v-col>
            <v-col cols="12" v-else class="">
              <v-container style="display: flex; justify-content: space-around">
                <span class="">{{ acts.acts_table.alternative }}</span>
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
    acts: {
      actions_categories: [
        "navigation",
        "eyes emoji",
        "led strip",
        "led ring",
        "speak",
        "head motion",
        'interface',
        'wait',
      ],
      acts_table: {
        headers: [
          { text: "Name", value: "name", sortable: false, align: "start" },
          { text: "Edit", value: "edit_act", sortable: false },
          { text: "Delete", value: "delete_act", sortable: false },
        ],
        show: false,
        data: [],
        alternative: "There is no acts yet",
      },
      new_act_dialog: {
        name: '',
        show: false,
      },
      act_edit: {
        act: {
            actions:[],
            name:'',
        },
        new_action_dialog:{
            show: false,
            category: '', 
        },
        action_edit:{
            index: null,
            navigation_dialog:{
                show:false,
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
                wait:false,
            },
            emoji_dialog:{
                show:false,
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

            },
            led_strip_dialog:{
                show:false,
                led_color:"#951b81FF"
            },
            led_ring_dialog:{
                show:false,
                led_flows: [
                    'off', 
                    'fadeoutfadein'
                ],
                led_flow:'',
                led_color: "#951b81FF",
                led_repeat: 1,
                led_return_default: false,
                led_speed: 100,
            }, 
            speak_dialog:{
                show:false,
                speak_files: [],
                speak_file: "",
            },
            head_motion_dialog:{
                show:false,
                angled:false, 
                head_motion_name:'',
                head_motion_names:[],
                angle:{
                  x:0,
                  y:0,
                  speed:500,
                  delay:0,
                },
            },
            interface_dialog:{
                show:false,
                interface_view_sets: [],
                interface_view: "main",
            }, 
            wait_dialog:{
                show:false,
                time:0.0
            }
        },
        show: false,
      },
    },
  }),

  computed: {
    ...mapGetters("Theme", ["isDark"]),
  },

  created() {
    this.fetch_acts();
    this.fetch_points();
    this.speak_fetch_sounds()
    this.interface_fetch_sets()
    this.fetch_head_motions()
  },

  methods: {

    parse_actions(){
        if(this.acts.act_edit.act.actions.length>0){
            var action_strings = []
            this.acts.act_edit.act.actions.forEach(action=>{
                action_strings.push(action.action_args.join('&'))
            })
            return action_strings.join('|')
        }else{
            return ''
        }
    },

    update_action_table(){
        this.acts.act_edit.act.actions.push(1)
        this.acts.act_edit.act.actions.pop()

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


    fetch_acts() {
      this.acts.acts_table.data = [];
      console.log('dispatching fetch acts')
      this.$store
        .dispatch("Ros/take_action", "act/get_acts", { root: true })
        .then((res) => {
        console.log(res)
          if (res == "") {
            this.acts.acts_table.show = false;
          } else {
            console.log('valid',res);
            res = res.split("$");
            res.forEach((act) => {
              var act_obj = {};
              act = act.split(":");
              act_obj.name = act[0];
              act_obj.actions = [];
              act[1].split("|").forEach((el) => {
                el = el.split("/");
                act_obj.actions.push({
                  category: el[0],
                  action_args: el,
                });
              });
              this.acts.acts_table.data.push(act_obj);
              console.log(this.acts.acts_table.data)
              this.acts.acts_table.show = true;

            });
          }
        });
    },
    fetch_points(){
        this.$store.dispatch('Ros/take_action', 'navigation/fetch_points',{root:true}).then(res=>{
          if(res == ''){
              console.log('love')
          }else{
              res = res.split('|').slice(1)
              this.acts.act_edit.action_edit.navigation_dialog.points.angled_points = []
              this.acts.act_edit.action_edit.navigation_dialog.points.unangled_points = []
              res.forEach(el=>{
                  el = el.split('&')
                  if(el.length <= 3){
                    this.acts.act_edit.action_edit.navigation_dialog.points.unangled_points.push({
                        name:el[0],
                        type:'unangled',
                        point:{
                          x:el[1],
                          y:el[2]
                        }
                    })
                  }else{
                    this.acts.act_edit.action_edit.navigation_dialog.points.angled_points.push({
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

    },
    speak_fetch_sounds() {
      var self = this;
      self.sounds = [["temp", ""]];
      this.$store
        .dispatch("Ros/take_action", "interactive/sounds_list", { root: true })
        .then((res) => {
          res = res.split("%");
          res.forEach((el) => {
            this.acts.act_edit.action_edit.speak_dialog.speak_files.push(el.split("&")[0]);
          });
        });
    },
    interface_fetch_sets() {
      this.$store
        .dispatch("Ros/take_action", "interface/get_sets", { root: true })
        .then((res) => {
          console.log(res);
          this.acts.act_edit.action_edit.interface_dialog.interface_view_sets = res.split("|");
        });
    },
    fetch_head_motions(){
      this.$store.dispatch('Ros/take_action', 'interactive/head_get_motions_names', {root:true}).then(res=>{
        if(res != ''){
          this.acts.act_edit.action_edit.head_motion_dialog.head_motion_names = res.split('|')
        }
      })
    },

    new_act(){
        this.acts.new_act_dialog.name=''
        this.acts.new_act_dialog.show=true
    },
    create_act(){
        if(this.acts.new_act_dialog.name != ''){
            this.acts.act_edit.act.name = this.acts.new_act_dialog.name
            this.acts.act_edit.act.actions = []
            this.acts.act_edit.show = true
            this.acts.new_act_dialog.show = false
        }
    },
    edit_act(item) {
      this.acts.act_edit.act = item;
      this.acts.act_edit.show = true;
    },
    del_act(act_name){
        this.$store.dispatch('Ros/take_action', `act/del_act/${act_name}`,{root:true}).then(res=>{
            console.log(res)
            this.fetch_acts()
        })
    },
    play_act(){
        this.$store.dispatch('Ros/take_action',
        `act/play_new_act_by_act/${this.parse_actions()}`
        , {root:true})
    },
    push_act(){
        this.$store.dispatch('Ros/take_action',
        `act/push_to_queue_by_act/${this.parse_actions()}`
        , {root:true})
    },
    save_edited_act(){
        if(this.acts.act_edit.act.actions.length >0 && this.acts.act_edit.act.name != ''){
            this.$store.dispatch('Ros/take_action',
            `act/add_act/${this.acts.act_edit.act.name}:${this.parse_actions()}`
            , {root:true}).then(()=>{
              this.fetch_acts()
                this.acts.act_edit.show = false
            })
        }
    },


    new_action(){
        this.acts.act_edit.new_action_dialog.category = '',
        this.acts.act_edit.new_action_dialog.show = true
    },
    create_action(){
        if(this.acts.act_edit.new_action_dialog.category != ''){
            this.acts.act_edit.act.actions.push({
                category:this.acts.act_edit.new_action_dialog.category,
                action_args:[]
            })
            this.acts.act_edit.new_action_dialog.show = false
            this.edit_action(this.acts.act_edit.act.actions.length-1)
        }
    },
    edit_action(index){
        switch (this.acts.act_edit.act.actions[index].category) {
            case 'navigation':
                this.edit_navigation_action(index)
                break;
        
            case 'eyes emoji':
                this.edit_emoji_action(index)
                break;
        
            case 'led strip':
                this.edit_led_strip_action(index)
                break;
        
            case 'led ring':
                this.edit_led_ring_action(index)
                break;
        
            case 'head motion':
                this.edit_head_motion_action(index)
                break;

            case 'interface':
                this.edit_interface_action(index)
                break;
                

            case 'speak':
                this.edit_speak_action(index)
                break;
                
            case 'wait':
                this.edit_wait_action(index)
                break;
            default:
                break;
        }
    },
    del_action(index){
        console.log(index)
        this.acts.act_edit.act.actions.splice(index,1)
    },
    move_action(index, direction){
        if(direction == 1){
            var temp
            if(index!=this.acts.act_edit.act.actions.length-1){
                temp = this.acts.act_edit.act.actions[index]
                this.acts.act_edit.act.actions[index] = this.acts.act_edit.act.actions[index+1]
                this.acts.act_edit.act.actions[index+1] = temp
            }
        }else{
            if(index!=0){
                temp = this.acts.act_edit.act.actions[index]
                this.acts.act_edit.act.actions[index] = this.acts.act_edit.act.actions[index-1]
                this.acts.act_edit.act.actions[index-1] = temp
            }

        }
        this.update_action_table()
    },

    edit_navigation_action(index){
            console.log('creating action ')

        if(this.acts.act_edit.act.actions[index].action_args.length >0){
            console.log('creating action ')

            this.acts.act_edit.action_edit.index = index
            this.acts.act_edit.action_edit.navigation_dialog.wait = this.acts.act_edit.act.actions[index].action_args[1]
            this.acts.act_edit.action_edit.navigation_dialog.selected_point= {}
            this.acts.act_edit.action_edit.navigation_dialog.selected_point.type= this.acts.act_edit.act.actions[index].action_args[2]
            this.acts.act_edit.action_edit.navigation_dialog.selected_point.name= this.acts.act_edit.act.actions[index].action_args[3]
            this.acts.act_edit.action_edit.navigation_dialog.selected_point.point = {}
            if(this.acts.act_edit.action_edit.navigation_dialog.selected_point.type == 'unangled'){
                this.acts.act_edit.action_edit.navigation_dialog.angled_point = false
                this.acts.act_edit.action_edit.navigation_dialog.selected_point.point.x= this.acts.act_edit.act.actions[index].action_args[4]
                this.acts.act_edit.action_edit.navigation_dialog.selected_point.point.y= this.acts.act_edit.act.actions[index].action_args[5]
            }else{
                this.acts.act_edit.action_edit.navigation_dialog.angled_point = true
                this.acts.act_edit.action_edit.navigation_dialog.selected_point.point.position = {}
                this.acts.act_edit.action_edit.navigation_dialog.selected_point.point.position.x= this.acts.act_edit.act.actions[index].action_args[4]
                this.acts.act_edit.action_edit.navigation_dialog.selected_point.point.position.y= this.acts.act_edit.act.actions[index].action_args[5]
                this.acts.act_edit.action_edit.navigation_dialog.selected_point.point.position.z= this.acts.act_edit.act.actions[index].action_args[6]
                this.acts.act_edit.action_edit.navigation_dialog.selected_point.point.orientation = {}
                this.acts.act_edit.action_edit.navigation_dialog.selected_point.point.orientation.x= this.acts.act_edit.act.actions[index].action_args[7]
                this.acts.act_edit.action_edit.navigation_dialog.selected_point.point.orientation.y= this.acts.act_edit.act.actions[index].action_args[8]
                this.acts.act_edit.action_edit.navigation_dialog.selected_point.point.orientation.z= this.acts.act_edit.act.actions[index].action_args[9]
                this.acts.act_edit.action_edit.navigation_dialog.selected_point.point.orientation.w= this.acts.act_edit.act.actions[index].action_args[10]
            }
            this.acts.act_edit.action_edit.navigation_dialog.show = true
        }else{
            console.log('creating action ')
            this.acts.act_edit.action_edit.index = index
            this.acts.act_edit.action_edit.navigation_dialog.wait = 'dont_wait'
            this.acts.act_edit.action_edit.navigation_dialog.selected_point = {}
        }
        console.log(this.acts.act_edit.action_edit)
        this.acts.act_edit.action_edit.navigation_dialog.show = true

    },
    go_to_point(){
      if(this.acts.act_edit.action_edit.navigation_dialog.selected_point.name){
        if(this.acts.act_edit.action_edit.navigation_dialog.selected_point.type == 'unangled'){
          this.$store
            .dispatch(
              "Ros/take_action",
              `navigation/unangled_goal/${this.acts.act_edit.action_edit.navigation_dialog.selected_point.point.x}&${this.acts.act_edit.action_edit.navigation_dialog.selected_point.point.y}`,
              {root:true}
            )
            .then((res) => {
              console.log(res);
            });
        }else{
          this.$store
            .dispatch(
              "Ros/take_action",
              `navigation/angled_goal/${this.acts.act_edit.action_edit.navigation_dialog.selected_point.point.position.x}&${this.acts.act_edit.action_edit.navigation_dialog.selected_point.point.position.y}&${this.acts.act_edit.action_edit.navigation_dialog.selected_point.point.position.z}&${this.acts.act_edit.action_edit.navigation_dialog.selected_point.point.orientation.x}&${this.acts.act_edit.action_edit.navigation_dialog.selected_point.point.orientation.y}&${this.acts.act_edit.action_edit.navigation_dialog.selected_point.point.orientation.z}&${this.acts.act_edit.action_edit.navigation_dialog.selected_point.point.orientation.w}`
              ,{root:true}
            )
            .then((res) => {
              console.log(res);
            });

        }
      }
    },
    save_navigation_action(){
        console.log(this.acts.act_edit.action_edit.navigation_dialog.selected_point.name )
        if(this.acts.act_edit.action_edit.navigation_dialog.selected_point.name){
            this.acts.act_edit.action_edit.navigation_dialog.show =false
            this.acts.act_edit.act.actions[this.acts.act_edit.action_edit.index].category = 'navigation'
            this.acts.act_edit.act.actions[this.acts.act_edit.action_edit.index].action_args = []
            this.acts.act_edit.act.actions[this.acts.act_edit.action_edit.index].action_args[0] = 'navigation'
            this.acts.act_edit.act.actions[this.acts.act_edit.action_edit.index].action_args[1] = this.acts.act_edit.action_edit.navigation_dialog.wait
            this.acts.act_edit.act.actions[this.acts.act_edit.action_edit.index].action_args[2] = this.acts.act_edit.action_edit.navigation_dialog.selected_point.type
            this.acts.act_edit.act.actions[this.acts.act_edit.action_edit.index].action_args[3] = this.acts.act_edit.action_edit.navigation_dialog.selected_point.name
            if(this.acts.act_edit.action_edit.navigation_dialog.selected_point.type == 'angled'){
                console.log('saving angled goal ')
                this.acts.act_edit.act.actions[this.acts.act_edit.action_edit.index].action_args[4] = this.acts.act_edit.action_edit.navigation_dialog.selected_point.point.position.x
                this.acts.act_edit.act.actions[this.acts.act_edit.action_edit.index].action_args[5] = this.acts.act_edit.action_edit.navigation_dialog.selected_point.point.position.y
                this.acts.act_edit.act.actions[this.acts.act_edit.action_edit.index].action_args[6] = this.acts.act_edit.action_edit.navigation_dialog.selected_point.point.position.z
                this.acts.act_edit.act.actions[this.acts.act_edit.action_edit.index].action_args[7] = this.acts.act_edit.action_edit.navigation_dialog.selected_point.point.orientation.x
                this.acts.act_edit.act.actions[this.acts.act_edit.action_edit.index].action_args[8] = this.acts.act_edit.action_edit.navigation_dialog.selected_point.point.orientation.y
                this.acts.act_edit.act.actions[this.acts.act_edit.action_edit.index].action_args[9] = this.acts.act_edit.action_edit.navigation_dialog.selected_point.point.orientation.z
                this.acts.act_edit.act.actions[this.acts.act_edit.action_edit.index].action_args[10] = this.acts.act_edit.action_edit.navigation_dialog.selected_point.point.orientation.w
            }else{
                console.log('saving unangled goal ')
                this.acts.act_edit.act.actions[this.acts.act_edit.action_edit.index].action_args[4] = this.acts.act_edit.action_edit.navigation_dialog.selected_point.point.x
                this.acts.act_edit.act.actions[this.acts.act_edit.action_edit.index].action_args[5] = this.acts.act_edit.action_edit.navigation_dialog.selected_point.point.y
            }
        }else{
            this.acts.act_edit.action_edit.navigation_dialog.show = false
            this.del_action(this.acts.act_edit.action_edit.index)
        }
    },

    edit_emoji_action(index){

        this.acts.act_edit.action_edit.index = index
        if(this.acts.act_edit.act.actions[index].action_args.length >0){
            this.acts.act_edit.action_edit.emoji_dialog.emoji_choise = this.acts.act_edit.act.actions[index].action_args[1]
            this.acts.act_edit.action_edit.emoji_dialog.emoji_color = '#' + this.acts.act_edit.act.actions[index].action_args[2] + 'FF'
            this.acts.act_edit.action_edit.emoji_dialog.emoji_repeat = parseInt(this.acts.act_edit.act.actions[index].action_args[3])
            this.acts.act_edit.action_edit.emoji_dialog.emoji_speed = parseInt(this.acts.act_edit.act.actions[index].action_args[4])
            this.acts.act_edit.action_edit.emoji_dialog.emoji_return_default = this.acts.act_edit.act.actions[index].action_args[5] == '1'? true : false
        }
        this.acts.act_edit.action_edit.emoji_dialog.show = true
    },
    reset_emoji_color(){
        this.acts.act_edit.action_edit.emoji_dialog.emoji_color = this.acts.act_edit.action_edit.emoji_dialog.emoji_default_color
    },
    set_emoji() {
      this.$store
        .dispatch(
          "Ros/take_action",
          `interactive/set_eyes/${this.acts.act_edit.action_edit.emoji_dialog.emoji_choise}/${this.acts.act_edit.action_edit.emoji_dialog.emoji_color.slice(
            1,
            -2
          )}/${this.acts.act_edit.action_edit.emoji_dialog.emoji_repeat}/${this.acts.act_edit.action_edit.emoji_dialog.emoji_speed}/${
            this.acts.act_edit.action_edit.emoji_dialog.emoji_return_default ? "1" : "0"
          }`,
          { root: true }
        )
        .then((res) => {
          console.log(res);
        });
    },
    save_emoji_action(){
        console.log(this.acts.act_edit.act.actions[this.acts.act_edit.action_edit.index])
        if(this.acts.act_edit.action_edit.emoji_dialog.emoji_choise != ''){
            this.acts.act_edit.act.actions[this.acts.act_edit.action_edit.index].category = 'eyes emoji'
            this.acts.act_edit.act.actions[this.acts.act_edit.action_edit.index].action_args = []
            this.acts.act_edit.act.actions[this.acts.act_edit.action_edit.index].action_args[0] = 'eyes emoji'
            this.acts.act_edit.act.actions[this.acts.act_edit.action_edit.index].action_args[1] = this.acts.act_edit.action_edit.emoji_dialog.emoji_choise
            this.acts.act_edit.act.actions[this.acts.act_edit.action_edit.index].action_args[2] = this.acts.act_edit.action_edit.emoji_dialog.emoji_color.slice(1,-2)
            this.acts.act_edit.act.actions[this.acts.act_edit.action_edit.index].action_args[3] = this.acts.act_edit.action_edit.emoji_dialog.emoji_repeat
            this.acts.act_edit.act.actions[this.acts.act_edit.action_edit.index].action_args[4] = this.acts.act_edit.action_edit.emoji_dialog.emoji_speed
            this.acts.act_edit.act.actions[this.acts.act_edit.action_edit.index].action_args[5] = this.acts.act_edit.action_edit.emoji_dialog.emoji_return_default? '1':'0'
            this.acts.act_edit.action_edit.emoji_dialog.show =false
        }else{  
            this.acts.act_edit.action_edit.emoji_dialog.show = false
            this.del_action(this.acts.act_edit.action_edit.index)
        }
    },
    

    edit_led_ring_action(index){

        this.acts.act_edit.action_edit.index = index
        if(this.acts.act_edit.act.actions[index].action_args.length >0){
            this.acts.act_edit.action_edit.led_ring_dialog.led_flow = this.acts.act_edit.act.actions[index].action_args[1]
            this.acts.act_edit.action_edit.led_ring_dialog.led_color = '#' + this.acts.act_edit.act.actions[index].action_args[2] + 'FF'
            this.acts.act_edit.action_edit.led_ring_dialog.led_repeat = parseInt(this.acts.act_edit.act.actions[index].action_args[3])
            this.acts.act_edit.action_edit.led_ring_dialog.led_speed = parseInt(this.acts.act_edit.act.actions[index].action_args[4])
            this.acts.act_edit.action_edit.led_ring_dialog.led_return_default = this.acts.act_edit.act.actions[index].action_args[5] == '1'? true : false
        }
        this.acts.act_edit.action_edit.led_ring_dialog.show = true
    },
    reset_led_ring_color(){
        this.acts.act_edit.action_edit.led_ring_dialog.led_color = this.acts.act_edit.action_edit.emoji_dialog.emoji_default_color
    },
    set_led_ring_flow() {
      this.$store
        .dispatch(
          "Ros/take_action",
          `interactive/set_ring_flow/${this.acts.act_edit.action_edit.led_ring_dialog.led_flow}/${this.acts.act_edit.action_edit.led_ring_dialog.led_color.slice(
            1,
            -2
          )}/${this.acts.act_edit.action_edit.led_ring_dialog.led_repeat}/${this.acts.act_edit.action_edit.led_ring_dialog.led_speed}/${
            this.acts.act_edit.action_edit.led_ring_dialog.led_return_default ? "1" : "0"
          }`,
          { root: true }
        )
        .then((res) => {
          console.log(res);
        });
    },
    save_led_ring_action(){
        console.log(this.acts.act_edit.act.actions[this.acts.act_edit.action_edit.index])
        if(this.acts.act_edit.action_edit.led_ring_dialog.led_flow != ''){
            this.acts.act_edit.act.actions[this.acts.act_edit.action_edit.index].category = 'led ring'
            this.acts.act_edit.act.actions[this.acts.act_edit.action_edit.index].action_args = []
            this.acts.act_edit.act.actions[this.acts.act_edit.action_edit.index].action_args[0] = 'led ring'
            this.acts.act_edit.act.actions[this.acts.act_edit.action_edit.index].action_args[1] = this.acts.act_edit.action_edit.led_ring_dialog.led_flow
            this.acts.act_edit.act.actions[this.acts.act_edit.action_edit.index].action_args[2] = this.acts.act_edit.action_edit.led_ring_dialog.led_color.slice(1,-2)
            this.acts.act_edit.act.actions[this.acts.act_edit.action_edit.index].action_args[3] = this.acts.act_edit.action_edit.led_ring_dialog.led_repeat
            this.acts.act_edit.act.actions[this.acts.act_edit.action_edit.index].action_args[4] = this.acts.act_edit.action_edit.led_ring_dialog.led_speed
            this.acts.act_edit.act.actions[this.acts.act_edit.action_edit.index].action_args[5] = this.acts.act_edit.action_edit.led_ring_dialog.led_return_default? '1':'0'
            this.acts.act_edit.action_edit.led_ring_dialog.show =false
        }else{  
            this.acts.act_edit.action_edit.led_ring_dialog.show = false
            this.del_action(this.acts.act_edit.action_edit.index)
        }
    },


    edit_led_strip_action(index){
        this.acts.act_edit.action_edit.index = index
        if(this.acts.act_edit.act.actions[index].action_args.length >0){
            this.acts.act_edit.action_edit.led_strip_dialog.led_color = '#' + this.acts.act_edit.act.actions[index].action_args[1] + 'FF'
        }
        this.acts.act_edit.action_edit.led_strip_dialog.show = true
    },
    reset_led_strip_color(){
        this.acts.act_edit.action_edit.led_strip_dialog.led_color = this.acts.act_edit.action_edit.emoji_dialog.emoji_default_color
    },
    set_led_strip() {
      this.$store
        .dispatch(
          "Ros/take_action",
          `interactive/set_strip_color/${this.acts.act_edit.action_edit.led_stip_dialog.led_color}`,
          { root: true }
        )
        .then((res) => {
          console.log(res);
        });
    },
    save_led_strip_action(){
        console.log(this.acts.act_edit.act.actions[this.acts.act_edit.action_edit.index])
        if(this.acts.act_edit.action_edit.led_strip_dialog.led_color != ''){
            this.acts.act_edit.act.actions[this.acts.act_edit.action_edit.index].category = 'led strip'
            this.acts.act_edit.act.actions[this.acts.act_edit.action_edit.index].action_args = []
            this.acts.act_edit.act.actions[this.acts.act_edit.action_edit.index].action_args[0] = 'led strip'
            this.acts.act_edit.act.actions[this.acts.act_edit.action_edit.index].action_args[1] = this.acts.act_edit.action_edit.led_strip_dialog.led_color.slice(1,-2)
            this.acts.act_edit.action_edit.led_strip_dialog.show =false
        }else{  
            this.acts.act_edit.action_edit.led_strip_dialog.show = false
            this.del_action(this.acts.act_edit.action_edit.index)
        }
    },

    edit_speak_action(index){
        this.acts.act_edit.action_edit.index = index
        if(this.acts.act_edit.act.actions[index].action_args.length >0){
            this.acts.act_edit.action_edit.speak_dialog.speak_file = this.acts.act_edit.act.actions[index].action_args[1]
        }
        this.acts.act_edit.action_edit.speak_dialog.show = true
    },
    playfile() {
      if (this.acts.act_edit.action_edit.speak_dialog.speak_file != "") {
        this.$store
          .dispatch(
            "Ros/take_action",
            `interactive/speak_push_to_queue/${this.acts.act_edit.action_edit.speak_dialog.speak_file}.mp3`,
            { root: true }
          )
          .then((res) => {
            console.log(res);
          });
      }
    },
    save_speak_action(){
        console.log(this.acts.act_edit.act.actions[this.acts.act_edit.action_edit.index])
        if(this.acts.act_edit.action_edit.speak_dialog.speak_file != ''){
            this.acts.act_edit.act.actions[this.acts.act_edit.action_edit.index].category = 'speak'
            this.acts.act_edit.act.actions[this.acts.act_edit.action_edit.index].action_args = []
            this.acts.act_edit.act.actions[this.acts.act_edit.action_edit.index].action_args[0] = 'speak'
            this.acts.act_edit.act.actions[this.acts.act_edit.action_edit.index].action_args[1] = this.acts.act_edit.action_edit.speak_dialog.speak_file
            this.acts.act_edit.action_edit.speak_dialog.show =false
        }else{  
            this.acts.act_edit.action_edit.speak_dialog.show = false
            this.del_action(this.acts.act_edit.action_edit.index)
        }
    },

    edit_wait_action(index){
        this.acts.act_edit.action_edit.index = index
        if(this.acts.act_edit.act.actions[index].action_args.length >0){
            this.acts.act_edit.action_edit.wait_dialog.time = parseInt(this.acts.act_edit.act.actions[index].action_args[1])
        }
        this.acts.act_edit.action_edit.wait_dialog.show = true
    },
    save_wait_action(){
        console.log(this.acts.act_edit.act.actions[this.acts.act_edit.action_edit.index])
        console.log(this.acts.act_edit.action_edit.wait_dialog.time)
        if(this.acts.act_edit.action_edit.wait_dialog.time != 0){
            this.acts.act_edit.act.actions[this.acts.act_edit.action_edit.index].category = 'wait'
            this.acts.act_edit.act.actions[this.acts.act_edit.action_edit.index].action_args = []
            this.acts.act_edit.act.actions[this.acts.act_edit.action_edit.index].action_args[0] = 'wait'
            this.acts.act_edit.act.actions[this.acts.act_edit.action_edit.index].action_args[1] = '' + this.acts.act_edit.action_edit.wait_dialog.time
            this.acts.act_edit.action_edit.wait_dialog.show =false
        }else{  
            this.acts.act_edit.action_edit.wait_dialog.show = false
            this.del_action(this.acts.act_edit.action_edit.index)
        }
    },

    edit_interface_action(index){
        this.acts.act_edit.action_edit.index = index
        if(this.acts.act_edit.act.actions[index].action_args.length >0){
            this.acts.act_edit.action_edit.interface_dialog.interface_view = this.acts.act_edit.act.actions[index].action_args[1]
        }
        this.acts.act_edit.action_edit.interface_dialog.show = true
    },
    set_interface() {
      if (this.acts.act_edit.action_edit.interface_dialog.interface_view != "") {
        this.$store
          .dispatch(
            "Ros/take_action",
            `interface/force_change_view_set/${this.acts.act_edit.action_edit.interface_dialog.interface_view}`,
            { root: true }
          )
          .then(() => {
          });
      }
    },
    save_interface_action(){
        console.log(this.acts.act_edit.act.actions[this.acts.act_edit.action_edit.index])
        if(this.acts.act_edit.action_edit.interface_dialog.interface_view != ''){
            this.acts.act_edit.act.actions[this.acts.act_edit.action_edit.index].category = 'interface'
            this.acts.act_edit.act.actions[this.acts.act_edit.action_edit.index].action_args = []
            this.acts.act_edit.act.actions[this.acts.act_edit.action_edit.index].action_args[0] = 'interface'
            this.acts.act_edit.act.actions[this.acts.act_edit.action_edit.index].action_args[1] = this.acts.act_edit.action_edit.interface_dialog.interface_view
            this.acts.act_edit.action_edit.interface_dialog.show =false
        }else{  
            this.acts.act_edit.action_edit.interface_dialog.show = false
            this.del_action(this.acts.act_edit.action_edit.index)
        }
    },

    edit_head_motion_action(index){
        this.acts.act_edit.action_edit.index = index
        if(this.acts.act_edit.act.actions[index].action_args.length >0){
            this.acts.act_edit.action_edit.head_motion_dialog.head_motion_name = this.acts.act_edit.act.actions[index].action_args[1]
        }
        this.acts.act_edit.action_edit.head_motion_dialog.show = true
    },
    play_head_motion() {
      if (this.acts.act_edit.action_edit.head_motion_dialog.head_motion_name != "") {
        this.$store
          .dispatch(
            "Ros/take_action",
            `interactive/head_play_motions_by_name/${this.acts.act_edit.action_edit.head_motion_dialog.head_motion_name}`,
            { root: true }
          )
          .then(() => {
          });
      }
    },
    save_head_motion_action(){
        console.log(this.acts.act_edit.act.actions[this.acts.act_edit.action_edit.index])
        if(this.acts.act_edit.action_edit.head_motion_dialog.head_motion_name != ''){
            this.acts.act_edit.act.actions[this.acts.act_edit.action_edit.index].category = 'head motion'
            this.acts.act_edit.act.actions[this.acts.act_edit.action_edit.index].action_args = []
            this.acts.act_edit.act.actions[this.acts.act_edit.action_edit.index].action_args[0] = 'head motion'
            this.acts.act_edit.act.actions[this.acts.act_edit.action_edit.index].action_args[1] = this.acts.act_edit.action_edit.head_motion_dialog.head_motion_name
            this.acts.act_edit.action_edit.head_motion_dialog.show =false
        }else{  
            this.acts.act_edit.action_edit.head_motion_dialog.show = false
            this.del_action(this.acts.act_edit.action_edit.index)
        }
    },
  },
};
</script>

<style scoped></style>
