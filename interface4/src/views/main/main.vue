
<template>
  <v-container fluid id="root" fill-height class="pa-0 ma-0" :style="appStyle">
    <!-- Confirm Before Leaving Dialog -->
    <v-dialog v-model="done" max-width="750">
      <v-card class="mx-auto" max-width="750" outlined>
        <v-card-title
          class="text-h7 white--text"
          style="font-weight: 700; background-color: #0f0f33"
          >{{ translate("Libyano Robot") }}</v-card-title
        >
        <v-card-text
          class="text--primary"
          style="
            padding-top: 60px;
            margin-bottom: 20px;
            font-size: 18px;
            text-align: center;
          "
        >
          {{
            translate(
              "Thank you for using Libyano Robot! Its been my pleasure to serve you!"
            )
          }}
        </v-card-text>
        <v-card-text
          class="text--primary"
          style="
            padding-top: 10px;
            margin-bottom: 20px;
            font-size: 18px;
            text-align: center;
          "
        >
          {{
            translate(
              "If you're done using Libyano, please tap on the 'Yes' button. If you would still like to explore Libyano, Tap on the 'No' button."
            )
          }}
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions class="d-flex justify-center">
          <v-btn color="error" large width="160" @click="rateWindow()">
            {{ translate("Yes") }}
          </v-btn>
          <v-btn color="primary" large width="160" @click="done = false">
            {{ translate("No") }}
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <!-- Rate Before Leaving -->
    <v-dialog v-model="rate" max-width="750">
      <v-card class="mx-auto" max-width="750" outlined>
        <v-card-title
          class="text-h7 white--text"
          style="font-weight: 700; background-color: #0f0f33"
          >{{ translate("Libyano Robot") }}</v-card-title
        >
        <v-card-text
          class="text--primary"
          style="
            padding-top: 60px;
            margin-bottom: 20px;
            font-size: 18px;
            text-align: center;
            font-weight: 700;
          "
        >
          {{
            translate(
              "Thank you for using Libyano Robot! Its been my pleasure to serve you!"
            )
          }}
        </v-card-text>
        <v-rating
          length="5"
          size="54"
          value="3"
          color="#92278f"
          background-color="#CE93D8"
          class="d-flex justify-center mb-6"
        ></v-rating>

        <v-divider></v-divider>

        <v-card-actions class="d-flex justify-center">
          <v-btn
            color="orange lighten-3"
            dark
            large
            width="160"
            @click="rate_cb"
            style="font-weight: 700"
          >
            {{ translate("Done") }}
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <!-- Main Bar -->
    <v-app-bar
      v-if="interactive"
      app
      flat
      extended
      extension-height="140px;"
      color="background"
      src="../../assets/bar/banner2.svg"
    >
      <v-container>
        <v-row>
          <v-img
            @click="goBack"
            :src="
              $route.path
                .split('/')
                .slice(0, $route.path.split('/').length - 1)
                .join('/')
                ? translateMedia('./assets/bar/back.svg')
                : translateMedia('./assets/close-circle.svg')
            "
            style="margin-top: 120px"
            max-width="60px"
            max-height="60px"
          ></v-img>
          <v-spacer></v-spacer>
          <v-spacer></v-spacer>
          <v-img
            src="../../assets/bar/dima_m3ana.svg"
            max-width="260"
            max-height="100"
            style="margin-top: 140px"
            class="ms-16"
          ></v-img>
          <v-spacer></v-spacer>
          <v-spacer></v-spacer>
          <v-img
            @click="set_lang('en')"
            src="../../assets/bar/en.svg"
            style="margin-top: 120px"
            max-width="60px"
            max-height="60px"
          ></v-img>
          <v-img
            @click="set_lang('ar')"
            src="../../assets/bar/ar.svg"
            style="margin-top: 120px"
            max-width="60px"
            max-height="60px"
            class="ms-3"
          ></v-img>
        </v-row>
      </v-container>
    </v-app-bar>

    <router-view></router-view>

    <v-footer v-if="interactive_footer" app height="100" color="stream">
      <v-container>
        <v-row justify="space-between">
          <v-col md="3" style="margin-top: -2px" @click="libyanoVidPlay()">
            <v-img
              src="../../assets/bar/libyano.svg"
              style="width: 300px; margin-left: -70px"
            ></v-img>
          </v-col>
          <v-col md="3" style="display: flex; margin-top: -2px">
            <v-img
              src="../../assets/bar/stream.svg"
              max-width="90px"
              max-height="70px"
              style="margin-left: 40px"
            ></v-img>
            <v-img
              src="../../assets/bar/libyana.svg"
              max-width="70px"
              max-height="70px"
              style="margin-left: 40px"
            ></v-img>
            <v-img
              src="../../assets/huawei.svg"
              max-width="70px"
              max-height="70px"
              style="margin-left: 40px"
            ></v-img>
          </v-col>
        </v-row>
        <v-dialog v-model="libyanoVid" width="720">
          <video id="libyanoVid" autoplay>
            <source src="../../assets/vid/libyano.mp4" type="video/mp4" />
            Your browser does not support the video tag.
          </video>
        </v-dialog>
      </v-container>
    </v-footer>
  </v-container>
</template>

<script>
export default {
  methods: {
    translate(phrase) {
      var t_phrase = this.$store.getters["Interface/get_content"][phrase];
      if (!t_phrase) {
        return phrase;
      } else {
        return t_phrase;
      }
    },
    libyanoVidPlay() {
      this.libyanoVid = true;
    },
    rateWindow() {
      this.done = false;
      this.$store.dispatch("Interface/perform_event_acts", "on_rating", {
        root: true,
      });
      this.rate = true;
    },
    rate_cb() {
      this.rate = false;
      this.$router.push({ name: "slide-show" });
    },
    set_lang(lang) {
      this.$store.dispatch("Interface/set_lang", lang, { route: true });
    },
    reset_timeout() {
      console.log("resetting time out");
      clearTimeout(this.timeout_handler);
      this.timeout_handler = setTimeout(() => {
        if (this.$route.name != "slide-show") {
          this.$router.push({ name: "slide-show" });
        }
      }, 180e3);
    },
    goBack() {
      var path = this.$route.path.split("/");
      path = path.slice(0, path.length - 1).join("/");
      if (!path) {
        this.done = true;
      } else {
        this.$router.push(path);
      }
    },
    translateMedia(src) {
      return this.$store.getters["Interface/get_media"][src];
    },
  },
  computed: {
    interactive() {
      return this.$store.getters["Interactive/get_interactive"];
    },

    interactive_footer() {
      return this.$store.getters["Interactive/get_interactive_footer"];
    },

    lang() {
      return this.$store.getters["Interface/get_lang"];
    },
    rtl() {
      return this.$vuetify.rtl;
    },
  },
  watch: {
    libyanoVid() {
      var myVideo = document.getElementById("libyanoVid");
      if (this.libyanoVid == false) {
        myVideo.pause();
      } else {
        myVideo.load();
      }
    },
    lang() {
      if (this.lang != this.current_lang) {
        this.current_lang = this.lang;
        if (this.current_lang == "ar") {
          this.appStyle.fontFamily = "Tajawal";
          this.$vuetify.rtl = true;
          console.log("Font and RTL Activated");
        } else {
          this.appStyle.fontFamily = "Montserrat";
          this.$vuetify.rtl = false;
        }
      }
    },
  },
  created() {
    this.reset_timeout();
    window.addEventListener("click", this.reset_timeout);
  },
  data() {
    return {
      done: false,
      rate: false,
      libyanoVid: false,
      appStyle: {
        backgroundColor: "#ecf0f1",
        fontFamily: "Montserrat",
      },
      timeout_handler: null,
      current_lang: "",
    };
  },
};
</script>

<style>
::-webkit-scrollbar {
  display: none;
}
.goback_left {
  position: absolute;
  top: 3%;
  left: 8%;
  z-index: 1000;
  width: 100px;
  height: 100px;
}
.goback_right {
  position: absolute;
  top: 3%;
  right: 8%;
  z-index: 1000;
  width: 100px;
  height: 100px;
}
</style>