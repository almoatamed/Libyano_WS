<template>
  <v-container fluid>
    <img
      src='../assets/map.png'
      max-height="520"
      max-width="1250"
      usemap="#image-map"
      style="  display: block; margin-left: auto; margin-right: auto;"
    />

    <map name="image-map">
      <area
        target=""
        alt="egypt"
        title="egypt"
        @click="dialog = true"
        coords="691,255,692,281,735,282,717,256,705,257"
        shape="poly"
      />
      <area
        target=""
        alt="usa"
        title="usa"
        @click="dialog2 = true"
        coords="158,184,258,191,271,194,278,208,277,218,282,222,290,206,294,218,299,222,320,216,347,202,353,209,337,219,319,230,308,243,290,254,293,269,280,254,236,258,226,266,216,258,204,258,194,248,182,252,165,247,149,239,138,216"
        shape="poly"
      />
      <area
        target=""
        alt="saudi"
        title="saudi"
        @click="dialog3 = true"
        coords="762,298,766,293,774,296,781,294,790,290,799,289,808,287,808,280,796,280,790,275,781,264,771,263,761,261,752,256,743,255,740,262,729,264"
        shape="poly"
      />
      <area
        target=""
        alt="turkey"
        title="turkey"
        @click="dialog4 = true"
        coords="699,223,721,223,738,224,752,224,762,236,702,240,696,236,693,227"
        shape="poly"
      />
    </map>

    <v-dialog v-model="dialog" max-width="344px">
      <v-card class="mx-auto" max-width="344" outlined>
        <v-list-item three-line>
          <v-list-item-content>
            <div class="text-overline mb-4">
              ROAMING WITH LIBYANA
            </div>
            <v-list-item-title class="text-h5 mb-1">
              Egypt
            </v-list-item-title>
            <v-list-item-subtitle
              >Provided with Etisalat Misr</v-list-item-subtitle
            >
          </v-list-item-content>

          <v-list-item-avatar tile size="80">
            <v-img src='../assets/Flag_of_Egypt.svg'></v-img
          ></v-list-item-avatar>
        </v-list-item>

        <v-card-actions>
          <v-btn text @click="dialog = false">
            Close
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-dialog v-model="dialog2" max-width="344px">
      <v-card class="mx-auto" max-width="344" outlined>
        <v-list-item three-line>
          <v-list-item-content>
            <div class="text-overline mb-4">
              ROAMING WITH LIBYANA
            </div>
            <v-list-item-title class="text-h5 mb-1">
              United States of America
            </v-list-item-title>
            <v-list-item-subtitle
              >Provided with AT&T</v-list-item-subtitle
            >
          </v-list-item-content>

          <v-list-item-avatar tile size="80">
            <v-img src='../assets/Flag_of_the_United_States.svg' max-width="80px" max-height="80px"></v-img
          ></v-list-item-avatar>
        </v-list-item>

        <v-card-actions>
          <v-btn text @click="dialog2 = false">
            Close
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-dialog v-model="dialog3" max-width="344px">
      <v-card class="mx-auto" max-width="344" outlined>
        <v-list-item three-line>
          <v-list-item-content>
            <div class="text-overline mb-4">
              ROAMING WITH LIBYANA
            </div>
            <v-list-item-title class="text-h5 mb-1">
              Saudi Arabia
            </v-list-item-title>
            <v-list-item-subtitle
              >Provided with Mobily, STC and Zain</v-list-item-subtitle
            >
          </v-list-item-content>

          <v-list-item-avatar tile size="80">
            <v-img src='../assets/Flag_of_Saudi_Arabia.svg'></v-img
          ></v-list-item-avatar>
        </v-list-item>

        <v-card-actions>
          <v-btn text @click="dialog3 = false">
            Close
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-dialog v-model="dialog4" max-width="344px">
      <v-card class="mx-auto" max-width="344" outlined>
        <v-list-item three-line>
          <v-list-item-content>
            <div class="text-overline mb-4">
              ROAMING WITH LIBYANA
            </div>
            <v-list-item-title class="text-h5 mb-1">
              Turkey
            </v-list-item-title>
            <v-list-item-subtitle
              >Provided with Vodafone & Turkcell</v-list-item-subtitle
            >
          </v-list-item-content>

          <v-list-item-avatar tile size="80">
            <v-img src='../assets/Flag_of_Turkey.svg'></v-img
          ></v-list-item-avatar>
        </v-list-item>

        <v-card-actions>
          <v-btn text @click="dialog4 = false">
            Close
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      dialog: false,
      dialog2: false,
      dialog3: false,
      dialog4: false,
      goback_timeout: null,
    }
  },
  methods:{
    change_mode(){
      this.$store.dispatch('Ros/change_mode','grtcancel', {root:true}).then(()=>{}).catch(err=>{
        console.error('Error while trying to change mode from interface', err)
      })
    },
    reset_goback_timeout(){
      clearTimeout(this.goback_timeout)
      console.log('resetting time out on services')
      this.goback_timeout = setTimeout(()=>{
        this.reset_goback_timeout()
        this.change_mode();
      },this.timeout_val)
    }
  },
  created(){
    this.goback_timeout = setTimeout(()=>{
      this.reset_goback_timeout()
      this.change_mode();
    },this.timeout_val)
    window.addEventListener('click', this.reset_goback_timeout)
  },
  beforeDestroy(){
    console.log('destroying services')
    clearTimeout(this.goback_timeout)
    window.removeEventListener('click', this.reset_goback_timeout)
  },
  computed:{
    timeout_val(){
      return this.$store.getters['Interface/get_timeout_val']
    }
  }
};
</script>
