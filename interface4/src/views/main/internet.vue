<template>
  <v-container fluid>
    <carousel-3d
      :autoplay="autoplay"
      :autoplay-timeout="2500"
      style="margin-top:1%;"
      :height="370"
      :width="500"
      :perspective="16"
      :space="450"
      ref="car3d"
    >
      <slide :index="0" style="border: 0px; background-color:#ecf0f1;">
        <vue-flip v-model="flip[0]" width="500" height="370">
          <template v-slot:front>
            <v-card class="mx-auto rounded-0" min-width="500" min-height="370">
              <v-img
                src="../../assets/internet/internet_for_all.png"
                height="200px"
                width="500px"
              ></v-img>

              <v-card-title class="frontTitle">
                {{ translate("Internet for all") }}
              </v-card-title>

              <v-card-subtitle>
                {{
                  translate(
                    "Choose your package and enjoy Libyana’s internet with different speed, capacity, and price tailored for your needs."
                  )
                }}
              </v-card-subtitle>

              <v-card-actions style="margin-top:-2%;">
                <v-btn
                  style="margin-left:auto; margin-right:auto; font-size:18px; font-weight:700;"
                  width="300"
                  color="orange lighten-3"
                  elevation="8"
                  @click="flipCard(0)"
                >
                  {{ translate("Learn More") }}
                </v-btn>
              </v-card-actions>
            </v-card>
          </template>
          <template v-slot:back>
            <v-card class="mx-auto rounded-0" min-width="500" min-height="370">
              <v-row style="background-color: #0f0f33;" class="mb-2">
                <v-col md="10"
                  ><v-card-title class="text-h7 white--text" style="font-weight:700;">
                    {{ translate("Internet for all your needs!") }}
                  </v-card-title></v-col
                >
                <v-col md="2" class="text-center mt-3"
                  ><v-icon
                    @click="cancelFlipCard(0)"
                    large
                    color="orange lighten-3"
                    >mdi-close-circle</v-icon
                  ></v-col
                >
              </v-row>
              <v-card-text style="padding-top:10px;">
                <v-simple-table fixed-header>
                  <thead style="background-color:#92278f; color:white;">
                    <tr>
                      <td>{{ translate("Package Type") }}</td>
                      <td>{{ translate("Package Capacity") }}</td>
                      <td>{{ translate("Package Price") }}</td>
                      <td>{{ translate("Download Speed") }}</td>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="pkg in all" :key="pkg.type">
                      <td>{{ translate(pkg.type) }}</td>
                      <td style="direction: ltr;">
                        {{ translate(pkg.capacity) }}
                      </td>
                      <td>{{ translate(pkg.price) }} {{ translate("LYD") }}</td>
                      <td style="direction: ltr;">
                        {{ translate(pkg.speed) }}
                      </td>
                    </tr>
                  </tbody>
                </v-simple-table>
              </v-card-text>

              <v-divider></v-divider>
            </v-card>
          </template>
        </vue-flip>
      </slide>

      <slide :index="1" style="border: 0px; background-color:#ecf0f1;">
        <vue-flip v-model="flip[1]" width="500" height="370">
          <template v-slot:front>
            <v-card class="mx-auto rounded-0" min-width="500" min-height="370">
              <v-img
                src="../../assets/internet/internet_all_night2.png"
                height="200px"
                width="500px"
              ></v-img>

              <v-card-title class="frontTitle">
                {{ translate("Internet all night") }}
              </v-card-title>

              <v-card-subtitle>
                {{ translate("Get more for less, off peak-period.") }}
              </v-card-subtitle>

              <v-card-actions>
                <v-btn
                  style="margin-left:auto; margin-right:auto; font-size:18px; font-weight:700;"
                  width="300"
                  color="orange lighten-3"
                  elevation="8"
                  @click="flipCard(1)"
                >
                  {{ translate("Learn More") }}
                </v-btn>
              </v-card-actions>
            </v-card>
          </template>
          <template v-slot:back>
            <v-card
              class="mx-auto rounded-0 overflow-y-auto"
              width="500"
              height="370"
            >
            <v-row  style="background-color: #0f0f33;" class="mb-2">
              <v-col md="10"><v-card-title class="text-h7 white--text" style="font-weight:700;">
                {{
                  translate(
                    "Stream, download, and play all night with Libyana’s discounted packages from 3 AM to 10 AM."
                  )
                }}
              </v-card-title></v-col>
                              <v-col md="2" class="text-center mt-3"
                  ><v-icon
                    @click="cancelFlipCard(1)"
                    large
                    color="orange lighten-3"
                    >mdi-close-circle</v-icon
                  ></v-col
                >
            </v-row>

              <v-card-text style="padding-top:10px;">
                <v-simple-table fixed-header>
                  <thead style="background-color:#92278f; color:white;">
                    <tr>
                      <td>{{ translate("Package Type") }}</td>
                      <td>{{ translate("Package Capacity") }}</td>
                      <td>{{ translate("Package Price") }}</td>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="pkg in allNight" :key="pkg.type">
                      <td>{{ translate(pkg.type) }}</td>
                      <td style="direction: ltr;">
                        {{ translate(pkg.capacity) }}
                      </td>
                      <td>{{ translate(pkg.price) }} {{ translate("LYD") }}</td>
                    </tr>
                  </tbody>
                </v-simple-table>
              </v-card-text>

              <v-divider></v-divider>
            </v-card>
          </template>
        </vue-flip>
      </slide>

      <slide :index="2" style="border: 0px; background-color:#ecf0f1;">
        <vue-flip v-model="flip[2]" width="500" height="370">
          <template v-slot:front>
            <v-card class="mx-auto rounded-0" min-width="500" min-height="370">
              <v-img
                src="../../assets/internet/extra_internet_packages.png"
                height="200px"
                width="500px"
              ></v-img>

              <v-card-title class="frontTitle">
                {{ translate("Internet extra!") }}
              </v-card-title>

              <v-card-subtitle>
                {{
                  translate(
                    "Extra quota for essential packages to spend on socials or streaming."
                  )
                }}
              </v-card-subtitle>
              <v-card-actions style="margin-top:-3%;">
                <v-btn
                  style="margin-left:auto; margin-right:auto; font-size:18px; font-weight:700;"
                  width="300"
                  color="orange lighten-3"
                  elevation="8"
                  @click="flipCard(2)"
                >
                  {{ translate("Learn More") }}
                </v-btn>
              </v-card-actions>
            </v-card>
          </template>
          <template v-slot:back>
            <v-card
              class="mx-auto rounded-0 overflow-y-auto"
              width="500"
              height="370"
            >
            <v-row style="background-color: #0f0f33;" class="mb-2">
              <v-col md="10"><v-card-title class="text-h7 white--text" style="font-weight:700;">
                {{ translate("Internet extra.") }}
              </v-card-title></v-col>
                              <v-col md="2" class="text-center mt-3"
                  ><v-icon
                    @click="cancelFlipCard(4)"
                    large
                    color="orange lighten-3"
                    >mdi-close-circle</v-icon
                  ></v-col
                >
            </v-row>
              <v-card-title class="text-h7" style="font-weight:700;">
                {{ translate("Extra Social ") }}
                <v-img
                  :src="require('../../assets/internet/facebook.svg')"
                  max-width="30px"
                  style="margin-left:10px;"
                ></v-img>
                <v-img
                  :src="require('../../assets/internet/snapchat.svg')"
                  max-width="30px"
                  style="margin-left:10px;"
                ></v-img>
                <v-img
                  :src="require('../../assets/internet/twitter.svg')"
                  max-width="30px"
                  style="margin-left:10px;"
                ></v-img>
                <v-img
                  :src="require('../../assets/internet/tiktok.svg')"
                  max-width="30px"
                  style="margin-left:10px;"
                ></v-img>
              </v-card-title>
              <v-card-text>
                {{
                  translate(
                    "Stay connected with the extra social package on all your social networks."
                  )
                }}
              </v-card-text>

              <v-card-text style="padding-top:10px;">
                <v-simple-table fixed-header>
                  <thead style="background-color:#92278f; color:white;">
                    <tr>
                      <td>{{ translate("Package Type") }}</td>
                      <td>{{ translate("Package Capacity") }}</td>
                      <td>{{ translate("Package Price") }}</td>
                      <td>{{ translate("Download Speed") }}</td>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="pkg in extraSocial" :key="pkg.type">
                      <td>{{ translate(pkg.type) }}</td>
                      <td style="direction: ltr;">
                        {{ translate(pkg.capacity) }}
                      </td>
                      <td>{{ translate(pkg.price) }} {{ translate("LYD") }}</td>
                      <td style="direction: ltr;">
                        {{ translate(pkg.speed) }}
                      </td>
                    </tr>
                  </tbody>
                </v-simple-table>
              </v-card-text>

              <v-divider></v-divider>

              <v-card-title class="text-h7" style="font-weight:700;">
                {{ translate("Extra Stream") }}
                <v-img
                  :src="require('../../assets/internet/netflix.svg')"
                  max-width="30px"
                  style="margin-left:10px;"
                ></v-img>
                <v-img
                  :src="require('../../assets/internet/spotify.svg')"
                  max-width="30px"
                  style="margin-left:10px;"
                ></v-img>
                <v-img
                  :src="require('../../assets/internet/soundcloud.svg')"
                  max-width="30px"
                  style="margin-left:10px;"
                ></v-img>
                <v-img
                  :src="require('../../assets/internet/youtube.svg')"
                  max-width="30px"
                  style="margin-left:10px;"
                ></v-img>
                <v-img
                  :src="require('../../assets/internet/shahid.svg')"
                  max-width="40px"
                  style="margin-left:10px;"
                ></v-img>
                <v-img
                  :src="require('../../assets/internet/anghami.svg')"
                  max-width="30px"
                  style="margin-left:10px;"
                ></v-img>
              </v-card-title>
              <v-card-text>
                {{
                  translate(
                    "Download, watch, and stream your favorite media with Extra Stream package."
                  )
                }}
              </v-card-text>

              <v-card-text style="padding-top:30px;">
                <v-simple-table fixed-header>
                  <thead style="background-color:#92278f; color:white;">
                    <tr>
                      <td>{{ translate("Package Type") }}</td>
                      <td>{{ translate("Package Capacity") }}</td>
                      <td>{{ translate("Package Price") }}</td>
                      <td>{{ translate("Download Speed") }}</td>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="pkg in extraStream" :key="pkg.type">
                      <td>{{ translate(pkg.type) }}</td>
                      <td style="direction: ltr;">
                        {{ translate(pkg.capacity) }}
                      </td>
                      <td>{{ translate(pkg.price) }} {{ translate("LYD") }}</td>
                      <td style="direction: ltr;">
                        {{ translate(pkg.speed) }}
                      </td>
                    </tr>
                  </tbody>
                </v-simple-table>
              </v-card-text>

              <v-divider></v-divider>

            </v-card>
          </template>
        </vue-flip>
      </slide>
    </carousel-3d>
  </v-container>
</template>

<script>
import { Carousel3d, Slide } from "vue-carousel-3d";
import lang from "../../lang/index";
import VueFlip from "vue-flip";
export default {
  components: {
    Carousel3d,
    Slide,
    "vue-flip": VueFlip,
  },
  mounted() {
    this.$el.addEventListener("touchstart", this.handleMousedown);
    this.$el.addEventListener("touchend", this.handleMouseup);
    this.$el.addEventListener("touchmove", this.handleMousemove);
  },
  methods: {
    handleMousedown(e) {
      console.log("touching down");
      this.mousedown = true;
      this.dragStartX = e.touches[0].clientX;
      this.dragStartY = e.touches[0].clientY;
    },
    handleMouseup() {
      this.mousedown = false;
      this.dragOffsetX = 0;
      this.dragOffsetY = 0;
    },
    handleMousemove(e) {
      if (!this.mousedown) {
        return;
      }

      const eventPosX = e.touches[0].clientX;
      const eventPosY = e.touches[0].clientY;
      console.log("eventPosX", e.touches[0].clientX);
      console.log("dragStartx", this.dragStartX);

      const deltaX = this.dragStartX - eventPosX;
      const deltaY = this.dragStartY - eventPosY;
      console.log("deltax", deltaX);

      this.dragOffsetX = deltaX;
      this.dragOffsetY = deltaY;
      console.log("dragOffsetx", this.dragOffsetX);

      // If the swipe is more significant on the Y axis, do not move the slides because this is a scroll gesture
      if (Math.abs(this.dragOffsetY) > Math.abs(this.dragOffsetX)) {
        return;
      }

      if (this.dragOffsetX > this.minSwipeDistance) {
        this.handleMouseup();
        this.$refs.car3d.goNext();
      } else if (this.dragOffsetX < -this.minSwipeDistance) {
        this.handleMouseup();
        this.$refs.car3d.goPrev();
      }
      // this.$refs.car3d.handleMousemove(e)
    },
    translate: lang.translate,
    flipCard(index) {
      this.cancelFlipCard();
      console.log("flipping card ", index);
      this.flip[index] = true;
      this.autoplay = false;
      this.timeout = setTimeout(() => {
        this.cancelFlipCard();
      }, 60000);
    },
    cancelFlipCard() {
      for (let index = 0; index < this.flip.length; index++) {
        this.flip[index] = false;
      }
      this.autoplay = true;
      clearTimeout(this.timeout);
    },
  },

  data() {
    return {
      // slide data
      viewport: 0,
      currentIndex: 0,
      total: 0,
      dragOffsetX: 0,
      dragStartX: 0,
      dragOffsetY: 0,
      dragStartY: 0,
      mousedown: false,
      zIndex: 998,
      minSwipeDistance: 10,

      //main page data
      flip: [false, false, false],
      autoplay: true,
      timeout: null,
      all: [
        {
          type: "Weekly",
          capacity: "100-800 MB",
          price: "1-4 ",
          speed: "512 Kbps",
        },
        {
          type: "Bi-Monthly",
          capacity: "2-6 GB",
          price: "8-16 ",
          speed: "2 Mbps",
        },
        {
          type: "Monthly",
          capacity: "5-50 GB",
          price: "10-50 ",
          speed: "4G",
        },
      ],
      extraSocial: [
        {
          type: "Weekly",
          capacity: "500 MB",
          price: "2 ",
          speed: "H+",
        },
        {
          type: "Bi-Monthly",
          capacity: "2 GB",
          price: "6 ",
          speed: "H+",
        },
      ],
      extraStream: [
        {
          type: "Weekly",
          capacity: "1 GB",
          price: "1 ",
          speed: "H+",
        },
        {
          type: "Bi-Monthly",
          capacity: "5 GB",
          price: "15 ",
          speed: "H+",
        },
        {
          type: "Monthly",
          capacity: "50 GB",
          price: "50 ",
          speed: "4G",
        },
      ],
      allNight: [
        {
          type: "Daily",
          capacity: "2 GB",
          price: "1 ",
        },
        {
          type: "Daily",
          capacity: "5 GB",
          price: "2 ",
        },
        {
          type: "Weekly",
          capacity: "30 GB",
          price: "10 ",
        },
        {
          type: "Weekly",
          capacity: "100 GB",
          price: "25 ",
        },
        {
          type: "Monthly",
          capacity: "200 GB",
          price: "40 ",
        },
        {
          type: "Monthly",
          capacity: "500 GB",
          price: "50 ",
        },
      ],
    };
  },
};
</script>

<style>
.frontText {
  font-size: 24px;
}
.v-card__subtitle {
  font-size: 16px;
}
.carousel-3d-slide {
  text-align: initial;
}
</style>
