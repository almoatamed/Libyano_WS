<template>
  <div id="root">
    <v-container>
      <div class="text-h4">Voice Manager</div>
      <v-divider class="py-2"></v-divider>
      <v-card  elevation="6"  :dark="isDark">
        <v-form ref="SoundForm" v-model="valid">
          <v-container fluid>
            <v-row>
              <v-col cols="12">
                <v-text-field
                  :disabled='disabled' :loading="loading"
                  v-model="form.name"
                  :rules="name_rules"
                  color="purple darken-2"
                  label="File name"
                  required
                ></v-text-field>
              </v-col>
              <v-col cols="12">

                <v-select
                  :dark='isDark'
                  :disabled='disabled' :loading="loading"
                  :rules="lang_rules"
                  :items="form.langs"
                  v-model="form.lang"
                  label="Language"
                  color="purple darken-2"
                  required
                ></v-select>
              </v-col>
              <!-- <v-col cols="12" sm="6">
                <v-text-field
                  v-model="form.last"
                  :rules="rules.name"
                  color="blue darken-2"
                  label="Last name"
                  required
                ></v-text-field>
              </v-col> -->
              <v-col cols="12">
                <v-textarea v-model="form.content" color="teal" 
                  :disabled='disabled' :loading="loading" :rules="text_rules">
                  <template v-slot:label>
                    <div>Text</div>
                  </template>
                </v-textarea>
              </v-col>
              <v-col cols="12">
                <!-- <v-select
                  v-model="sound"
                  :disabled='loading'
                  :loading='loading'
                  :items="sounds"
                  color="pink"
                  label="File"
                  required
                ></v-select> -->
              
                <v-menu
                offset-y
                >
                  <template
                  v-slot:activator="{attrs,on}"
                  >
                    <v-btn
                    icon
                    v-bind ='attrs'
                    v-on='on'
                    >
                      <v-icon>mdi-file</v-icon>
                    </v-btn>
                  </template>
                  <v-list :dark="isDark" dense min-width="180">

                    <v-list-item-group>

                      <v-list-item v-for="sound in sounds" link :key="sound[0]" @click="set_sound(sound)"> 
                        <v-list-item-content >
                          <v-list-item-title > {{sound[0]}}</v-list-item-title>
                        </v-list-item-content>
                      </v-list-item>

                    </v-list-item-group>

                  </v-list>
                </v-menu>
              </v-col>
              <!-- <v-col cols="12" sm="6">
                <v-slider
                  v-model="form.age"
                  :rules="rules.age"
                  color="orange"
                  label="Age"
                  hint="Be honest"
                  min="1"
                  max="100"
                  thumb-label
                ></v-slider>
              </v-col> -->
              <!-- <v-col cols="12">
                <v-checkbox v-model="form.terms" color="green">
                  <template v-slot:label>
                    <div @click.stop="">
                      Do you accept the
                      <a href="#" @click.prevent="terms = true">terms</a>
                      and
                      <a href="#" @click.prevent="conditions = true">conditions?</a>
                    </div>
                  </template>
                </v-checkbox>
              </v-col> -->
            </v-row>
          </v-container>
          <v-card-actions>
            <v-btn :disabled="play_loading" :loading='play_loading' text @click="play"> Play </v-btn>
            <v-spacer></v-spacer>
            <v-btn :disabled="play_loading" :loading='play_loading' text @click="queue"> Queue </v-btn>
            <v-spacer></v-spacer>
            <v-btn :disabled="disabled || save_loading" :loading='save_loading' text color="primary" @click="save">
              Save
            </v-btn>
            <v-spacer></v-spacer>
            <v-btn :disabled="!(sound != 'temp' && sound != '')" :loading='loading' text @click="del"> del </v-btn>
          </v-card-actions>
        </v-form>
        <!-- <v-dialog v-model="terms" width="70%">
          <v-card>
            <v-card-title class="text-h6"> Terms </v-card-title>
            <v-card-text v-for="n in 5" :key="n">
              {{ content }}
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn text color="purple" @click="terms = false"> Ok </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
        <v-dialog v-model="conditions" width="70%">
          <v-card>
            <v-card-title class="text-h6"> Conditions </v-card-title>
            <v-card-text v-for="n in 5" :key="n">
              {{ content }}
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn text color="purple" @click="conditions = false"> Ok </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog> -->
      </v-card>
    </v-container>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  data() {
    const defaultForm = Object.freeze({
        name: '', 
        content: '',
        langs:['en', 'ar','fr'],
        lang:'ar'
    });

    return {
      form: Object.assign({}, defaultForm),
      sounds: [['temp','']],
      sound: '',
      valid: true,
      loading: false,
      save_loading: false,
      play_loading: false,
      defaultForm,
    };
  },

  computed: {
    ...mapGetters("Theme", ["isDark"]),
    name_rules(){
        var Rules = [
            v => ((v || '').length <= 50) || 'Name must be less then 50 characters',
            v => ((v || '').indexOf(' ') < 0) || 'Name cannot conatin spaces',
            v => !!v || 'Name is Required'
        ]
        return Rules
    },
    text_rules(){
      return [
            v => !!v || 'Text is Required'
      ]
    },
    lang_rules(){
      return [
            v => !!v || 'Language is Required'
      ]
    },
    disabled(){
      if(this.sound !='temp' || this.loading){
        return true
      }else{
        return false
      }
    },
  },

  methods: {
    resetForm() {
      this.form = Object.assign({}, this.defaultForm);
      this.$refs.SoundForm.reset();
    },
    set_sound(sound){
      if(sound[0] == 'temp'){
        this.sound = 'temp'
        this.resetForm()
      }else{
        this.form.name = sound[0]
        this.form.content = sound[1]
        this.form.lang = 'en'
        this.sound = sound[0]
      }
    },
    fetch_sounds(){
      var self = this
      this.loading = true
      this.save_loading = true
      this.play_loading = true
      self.sounds = [['temp','']] 
      this.$store.dispatch('Voice/fetch_sounds', null, {root: true}).then(resp=>{
        console.log('dispatched fetch sounds',resp)
        resp = resp.message
        if(!resp){
          self.sounds = [['temp','']] 
        }else{
          resp = resp.split('%')
          resp.forEach(el => {
          self.sounds.push(el.split('&')) 
          });
        }
        self.loading = false
        self.save_loading = false
        self.play_loading = false
      }).catch(err =>{
        console.error(err)
        self.loading = false
        self.save_loading = false
        self.play_loading = false
      })
    },
    save() {
      if(this.$refs.SoundForm.validate()){
          this.loading = true
          this.save_loading = true
          this.play_loading = true
          this.$store.dispatch('Voice/save_file',{lang:this.form.lang,name:this.form.name, content:this.form.content},{root:true}).then(resp=>{
            console.log('Dispatched Save Voice ',resp)
            setTimeout(()=>{
              this.fetch_sounds()
            },2000)
          }).catch(err=>{
            console.error('Error whiel Saving voice ',err)
            this.fetch_sounds()
          })
      }
    },
    play(){
      
      if(this.$refs.SoundForm.validate()){
          this.loading = true
          this.save_loading = true
          this.play_loading = true
          if(this.sound == 'temp'){
            this.$store.dispatch('Voice/play_temp',{content:this.form.content,lang:this.form.lang},{root:true}).then(resp=>{
              console.log('Dispatched play temp',resp)
              this.loading = false
              this.save_loading = false
              this.play_loading = false
            }).catch(err=>{
              console.error('Error while playing temp',err)
              this.loading = false
              this.save_loading = false
              this.play_loading = false
            })
          }else if(this.sound != ''){
            this.$store.dispatch('Voice/play_saved_file',this.form.name,{root:true}).then(resp=>{
              console.log('Dispatched play temp',resp)
              this.loading = false
              this.save_loading = false
              this.play_loading = false
            }).catch(err=>{
              console.error('Error while playing temp',err)
              this.loading = false
              this.save_loading = false
              this.play_loading = false
            })
          }
      }
    },
    queue(){
      if(this.$refs.SoundForm.validate()){
          if(this.sound != 'temp'){
            this.$store.dispatch('Ros/take_action',`interactive/speak_push_to_queue/${this.form.name}.mp3`,{root:true}).then(()=>{
              console.log('queued')
            }).catch(err=>{
              console.log('error while trying to push',err)
            })
          }
      }
    },
    del(){     
      if(this.$refs.SoundForm.validate()){
          this.loading = true
          this.save_loading = true
          this.play_loading = true
          this.$store.dispatch('Voice/del_file',this.form.name,{root:true}).then(resp=>{
            console.log('Dispatched del Voice ',resp)
            setTimeout(()=>{
              this.fetch_sounds()
              this.set_sound(['temp',''])
            },2000)
          }).catch(err=>{
            console.error('Error whiel Del voice ',err)
            this.fetch_sounds()
          })
      }
    }
  },
  created(){
    this.fetch_sounds()
  }
};
</script>
<style></style>
