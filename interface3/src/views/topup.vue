<template>
  <v-container fluid style="margin-top:5%">
    <v-row justify="center">
      <!------------------------Five Dinars Card -------------------------->
      <v-col md="4">
        <v-card class="mx-auto" max-width="400">
          <v-img
            class="white--text align-end"
            height="200px"
            :src="translateMedia('five_lyd')"
            contain
          >
          </v-img>

          <v-card-subtitle class="pb-0">
          {{translate('Five Libyan Dinars')}}
          </v-card-subtitle>

          <v-card-text class="text--primary">
            <div>{{translate('Top-Up of 5 LYD for your mobile credit!')}}</div>
          </v-card-text>

          <v-card-actions style="padding-bottom:10px;">
            <v-btn color="#ffc74a" :loading='taking_in_loading' :disabled='taking_in' block @click="reveal[5]=true;get(5)">
              {{translate('Request')}}
            </v-btn>
          </v-card-actions>

          <v-expand-transition>
            <v-card
              v-if="reveal[5]"
              class="transition-fast-in-fast-out v-card--reveal"
              outlined
              dark
              color="#92278f"
              style="
                position: absolute;
                top: 0%;
                height:100%;
                "
            >
              <v-card-title>Five LYD</v-card-title>
              <v-card-title
                class="text-h4 font-weight-bold"
                style="text-align:center; padding-top:30px;"
                >{{translate('Please Insert a 5 Dinar bill!')}}</v-card-title
              >
              <v-card-text class="text-h4 font-weight-bold" style="text-align:center; padding-top:10px">
                {{timer}}
              </v-card-text>
              <v-card-actions>
                <v-btn color="#ffc74a" @click="cancel()" :disabled='request_cancel_button' :loading='request_cancel_button' light block>
                  {{translate('Cancel')}}
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-expand-transition>
        </v-card>
      </v-col>

      <!------------------------Ten Dinars Card -------------------------->

      <v-col md="4">
        <v-card class="mx-auto" max-width="400">
          <v-img
            class="white--text align-end"
            height="200px"
            :src="translateMedia('ten_lyd')"
            contain
          >
          </v-img>

          <v-card-subtitle class="pb-0">
            {{translate('Ten Libyan Dinars')}}
          </v-card-subtitle>

          <v-card-text class="text--primary">
            <div>{{translate('Top-Up of 10 LYD for your mobile credit!')}}</div>
          </v-card-text>

          <v-card-actions style="padding-bottom:10px;">
            <v-btn color="#ffc74a" :loading='taking_in_loading' :disabled='taking_in' block @click="reveal[10]=true;get(10)">
              {{translate('Request')}}
            </v-btn>
          </v-card-actions>

          <v-expand-transition>
            <v-card
              v-if="reveal[10]"
              class="transition-fast-in-fast-out v-card--reveal"
              style="
                position: absolute;
                top: 0%;
                height:100%;
                "
              outlined
              dark
              color="#92278f"
            >
              <v-card-title>Ten LYD</v-card-title>
              <v-card-title
                class="text-h4 font-weight-bold"
                style="text-align:center; padding-top:30px; padding-left:60px;"
                >{{translate('Please Insert a 10 Dinar bill!')}}</v-card-title
              >
              <v-card-text class="text-h4 font-weight-bold" style="text-align:center; padding-top:10px">
                {{timer}}
              </v-card-text>
              <v-card-actions>
                <v-btn color="#ffc74a" @click="cancel()" :disabled='request_cancel_button' :loading='request_cancel_button' light block>
                  {{translate('Cancel')}}
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-expand-transition>
        </v-card>
      </v-col>

    <!------------------ Popups for Money request ------------------>
      <v-dialog v-model="dialog.show" max-width="400px" persistent>
        <v-card class="mx-auto" max-width="400" outlined dark color="#92278f">
          <v-card-title>{{dialog.title}}</v-card-title>
          <v-card-text class="text-h5 font-weight-bold"
            >{{dialog.text}}
          </v-card-text> 
          <v-card-actions>
            <v-btn color="#ffc74a" @click="close_dialog()" light>
              {{dialog.action_name}}
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-row>
  </v-container>
</template>

<style>
.v-card--reveal {
  bottom: 0;
  opacity: 1 !important;
  position: absolute;
  width: 100%;
}
</style>

<script>
export default {
  data() {
    return {
      dialog: {
        show: false,
        title: "",
        text: "",
        action_name: "cancel"
      },
      channel_dictionary: {
        1: 0,
        5: 1,
        10: 2,
      },
      reveal: {
        5: false,
        10: false,
      },
      taking_in:false,
      taking_in_loading: false,
      time_out_holder: null,
      request_cancel_button: false,
      timer:0,
      timer_interval_holder:null,
      goback_timeout: null,
    };
  },
  methods: {
translateMedia(src){
      return this.$store.getters['Interface/get_media'][src]
    },
    translate(phrase){
      var t_phrase = this.$store.getters['Interface/get_content'][phrase]
      if(!t_phrase){
        return phrase
      }else{
        return t_phrase
      }
    },
    close_dialog(){
      clearTimeout(this.time_out_holder);
      this.dialog.show = false;
      this.dialog.text = "";
      this.dialog.title = "";
    },
    cancel() {
      clearInterval(this.timer_interval_holder)
      this.reveal[5] = false;
      this.reveal[10] = false;
      if(this.taking_in == true){
        this.taking_in_loading = true
      }
      this.$store.dispatch("Voucher/cash_reader_cancel", null, { root: true })
    },
    get(val) {
      console.log(`getting ${val} from cash reader`)
      for (const currency in this.reveal) {
        if (currency != val) {
          console.log(`hiding ${currency}`)
          this.reveal[currency] = false;     
        }
      }
      this.request_cancel_button = true
      setTimeout(()=>{this.request_cancel_button = false}, 2e3)

      this.timer = 40
      this.timer_interval_holder = setInterval(() => {
        if(this.timer != 0){
          this.timer -=1
        }
      }, 1000);
      this.taking_in = true;
      this.$store
        .dispatch(
          "Voucher/takein",
          { channel: this.channel_dictionary[val], val },
          { root: true }
        )
        .then(res=>{
          console.log('Dispatched Take in request successfully which resulted in ', res)
          setTimeout(()=>{this.taking_in = false;this.taking_in_loading =false},3000)
          clearInterval(this.timer_interval_holder)
          this.reveal[5] = false;
          this.reveal[10] = false;
          if(res.data.message == 'stacked' || res.data.message == 'cancelled'){
            null
          }else if(res.data.message == 'failed'){
            this.dialog.show = true;
            this.dialog.title = "something went wrong";
            this.dialog.text = "it seems that an error occured, please try again!";
            this.time_out_holder = setTimeout(()=>{
              this.dialog.show = false;
              this.dialog.text = "";
              this.dialog.title = "";
            },10e3)
          }else if(res.data.message == 'empty'){
            this.dialog.show = true;
            this.dialog.title = "sorry we sold out!";
            this.dialog.text = `it seems the we are out of ${val} LYD vouchers`;
            this.time_out_holder = setTimeout(()=>{ 
              this.dialog.show = false;
              this.dialog.text = "";
              this.dialog.title = "";
            },10e3)
          }else if(res.data.message == 'timeout'){
            this.dialog.show = true;
            this.dialog.title = "Timeout";
            this.dialog.text = "you have not inserted a bill in the given time!";
            this.time_out_holder = setTimeout(()=>{
              this.dialog.show = false;
              this.dialog.text = "";
              this.dialog.title = "";
            },10e3)
          }else{
            this.dialog.show = true;
            this.dialog.title = "Currenncy Insertion Error";
            this.dialog.text = "it seems that an proper currency was inserted, or an error occured while inserting it, please try again properly!";
            this.time_out_holder = setTimeout(()=>{
              this.dialog.show = false;
              this.dialog.text = "";
              this.dialog.title = "";
            },10e3)
          }
        }).catch(err=>{
          console.log('Error occured while dispatching take in request', err)
          setTimeout(()=>{this.taking_in = false;this.taking_in_loading =false},3000)
          clearInterval(this.timer_interval_holder)
          this.reveal[5] = false;
          this.reveal[10] = false;
          this.dialog.show = true;
          this.dialog.title = "something went wrong";
          this.dialog.text = "it seems that an internal error occured, please try again!";
          this.time_out_holder = setTimeout(()=>{
            this.dialog.show = false;
            this.dialog.text = "";
            this.dialog.title = "";
          },10e3)
        })
    },
  },

  created(){
    this.$store.dispatch('Voucher/launch',null,{root:true}).then(res=>{
      console.log('Dispatched Cash Reader Relay Launch successfully ', res)
    }).catch(err=>{
      console.log('Failed to Dispatched Cash Reader Relay Launch', err)
    })
  },

  beforeDestroy(){
    console.log('destroying topup')
    if(this.taking_in == true){
      this.$store.dispatch("Voucher/cash_reader_cancel", null, { root: true }).finally(()=>{
        this.$store.dispatch('Voucher/stop',null,{root:true}).then(res=>{
          console.log('Dispatched Cash Reader Relay Stop successfully ', res)
        }).catch(err=>{
          console.log('Failed to Dispatched Cash Reader Relay Stop ', err)
        })
      })
    }else{
      this.$store.dispatch('Voucher/stop',null,{root:true}).then(res=>{
        console.log('Dispatched Cash Reader Relay Stop successfully ', res)
      }).catch(err=>{
        console.log('Failed to Dispatched Cash Reader Relay Stop ', err)
      })
    }
  },

  computed:{
  }
};
</script>
