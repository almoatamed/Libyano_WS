<template>
  <v-app >

    <!-- Dispaly Voucher -->
    <v-dialog v-model="voucher.dialog.show" max-width="400px" persistent>
      <v-card class="mx-auto" max-width="400" outlined dark color="#92278f">
        <v-card-title
          >{{ voucher.dialog.messages[voucher.dialog.counter].title }}
        </v-card-title>
        <v-card-text
          v-if="voucher.dialog.counter == 0"
          class="text-h5 font-weight-bold"
        >
          <p>
            {{ voucher.dialog.messages[0].text[0] }}
          </p>
        </v-card-text>

        <v-card-text class="text-h5 font-weight-bold" v-else>
          <p>
            {{ voucher.dialog.messages[0].text[0] }}
          </p>
          <p>
            {{ voucher.dialog.messages[0].text[0] }}
          </p>
          <p>{{ translate("Secret") }}: {{ voucher.card.secret }}</p>
          <p>Serial: {{ voucher.card.serial }}</p>
          <p>Val: {{ voucher.card.val }}</p>
        </v-card-text>
        <v-card-actions>
          <v-btn color="#ffc74a" @click="close_dialog()" light>
            {{ voucher.dialog.messages[voucher.dialog.counter].action }}
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-main>
      <router-view></router-view>
    </v-main>

  </v-app>
</template>

<script>
export default {
  name: "App",

  methods: {
    translate(phrase) {
      var t_phrase = this.$store.getters["Interface/get_content"][phrase];
      if (!t_phrase) {
        return phrase;
      } else {
        return t_phrase;
      }
    },
    close_dialog() {
      this.voucher.dialog.counter += 1;
      if (this.voucher.dialog.counter == 2) {
        clearTimeout(this.voucher.timeout);
        this.$store.dispatch("Voucher/clear", null, { root: true });
        this.voucher.continue = true;
        this.voucher.dialog.show = false;
        this.voucher.card = {};
      }
    },
  },

  computed: {
    voucher_show() {
      return this.$store.getters["Voucher/show"];
    },
    voucher_message() {
      return this.$store.getters["Voucher/message"];
    },
  },
  watch: {
    voucher_show() {
      if (this.voucher_show) {
        this.voucher.card = this.voucher_message;
        this.voucher.dialog.counter = 0;
        this.voucher.dialog.show = true;
        this.voucher.continue = false;
        this.voucher.timeout = setTimeout(() => {
          this.$store.dispatch("Voucher/clear", null, { root: true });
          this.voucher.continue = true;
          this.voucher.dialog.show = false;
          this.voucher.card = {};
        }, 60e3);
      }
    },
  },
  created() {
    var self = this

    // Voucher Card Dialog Display Periodic check
    setInterval(()=>{
      if(self.voucher.continue){
        self.$store.dispatch('Voucher/check',null,{root:true}).then(()=>{}).catch(()=>{})
      }
    },500)

    //  Interface Category Check Periodically
    setInterval(()=>{
      self.$store.dispatch('Ros/take_action','interface/get_set',{root:true}).then((set)=>{
        // try {
          if(!this.$route.matched.some(e=>e.name == set)){
            this.$router.push({name:this.sets_defualt_routes[set]})
          }
        // } catch (error) {
        //   console.log(error)          
        // }
      }).catch(()=>{})
    },250)

    //  Interface current rout update
    setInterval(()=>{
      self.$store.dispatch('Ros/take_action',`interface/set_current_route_name/${this.$route.name}`,{root:true}).then(()=>{
      }).catch((err)=>{
        console.log('Failed to update current route on interface controller', err)
      })
    },250)
  },
  data() {
    return {
      voucher: {
        dialog: {
          messages: [
            {
              title: "You Have Succeed",
              text: ["Please Press continue to get you voucher!"],
              action: "get",
            },
            {
              title: "Voucher Card",
              text: ["Please use the shown Voucher Card!", "", "", ""],
              action: "Received",
            },
            {},
          ],
          counter: 0,
          show: false,
          timeout: {},
        },
        card: {},
        continue: true,
      },
      sets_defualt_routes:{
        main: 'slide-show', 
        bootup: 'bootup',
      }
    };
  },
};
</script>
<style>
@import url("./assets/css/font.css");
</style>
