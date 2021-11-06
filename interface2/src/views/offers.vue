<template>
  <v-container fluid>
    <carousel-3d
      :autoplay="true"
      :autoplay-timeout="2500"
      style="margin-top:5%"
      :height="370"
      :width="500"
      :perspective="16"
      :space="450"
    >
      <slide :index="0" style="border: 0px;">
        <v-card class="mx-auto rounded-0" min-width="500" min-height="370">
          <v-img
            src='../assets/mylibyana.svg'
            height="200px"
          ></v-img>

          <v-card-title>
            MyLibyana 
          </v-card-title>

          <v-card-subtitle>
            #Easier with My Libyana <br/> MyLibyana and get 1giga + 15minutes FREE.
          </v-card-subtitle>

          <v-card-actions>
            <v-btn color="orange lighten-2" text @click="dialog = true">
              Learn More
            </v-btn>
          </v-card-actions>
        </v-card>
      </slide>

      <slide :index="1" style="border: 0px;">
        <v-card class="mx-auto rounded-0" min-width="500" min-height="370">
          <v-img
            src="../assets/sallefny.png"
            height="200px"
          ></v-img>

          <v-card-title>
            Sallefny
          </v-card-title>

          <v-card-subtitle>
            Out of credit? don't worry Libyana got your back dial *121#
          </v-card-subtitle>

          <v-card-actions>
            <v-btn color="orange lighten-2" text @click="dialog2 = true">
              Learn More
            </v-btn>
          </v-card-actions>
        </v-card>
      </slide>

      <slide :index="2" style="border: 0px;">
        <v-card class="mx-auto rounded-0" min-width="500" min-height="370">
          <v-img
            src='../assets/cus_srvc.svg'
            height="200px"
          ></v-img>

          <v-card-title>
            Customer Service
          </v-card-title>

          <v-card-subtitle>
            150 We're there because we care.
          </v-card-subtitle>

          <v-card-actions>
            <v-btn color="orange lighten-2" text @click="dialog3 = true">
              Learn More
            </v-btn>
          </v-card-actions>
        </v-card>
      </slide>
    </carousel-3d>

    <v-dialog v-model="dialog" max-width="500px">
      <v-card>
        <v-card-title class="text-h5 grey lighten-2">
Discover, control and enjoy MyLibyana
        </v-card-title>

        <v-card-text style="padding-top:20px;">
Through "MyLibyana" app for Android and IOS, you can manage all your services such as checking your balance,
 recharging and accessing everything directly and effectively, you also won’t miss any of Libyana’s updates, 
The application is available in Arabic and English interface.
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary" text @click="dialog = false">
            Close
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-dialog v-model="dialog2" max-width="500px">
      <v-card>
        <v-card-title class="text-h5 grey lighten-2">
          Sallefny, don't stop your calls!
        </v-card-title>

        <v-card-text>
With the credit loan service, subscribers can borrow credit from Libyana. 
Where this balance can be used to make local and international calls, 
in addition to subscribing to Internet packages, 
and to benefit from all other Libyana services 
(Validity Extending, credit transfer, subscription to added services .... and other services).
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary" text @click="dialog2 = false">
            Close
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-dialog v-model="dialog3" max-width="500px">
      <v-card>
        <v-card-title class="text-h5 grey lighten-2">
          150 We're there because we care.
        </v-card-title>

        <v-card-text>
Our customer service team is always ready to help you 24/7, call 150 or message us on our facebook page.
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary" text @click="dialog3 = false">
            Close
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script>
import { Carousel3d, Slide } from "vue-carousel-3d";

export default {
  components: {
    Carousel3d,
    Slide,
  },

  data() {
    return {
      dialog: false,
      dialog2: false,
      dialog3: false,
      goback_timeout: null,
    };
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
    console.log('destroying offers')
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
