<template>
  <v-container fluid>
    <carousel-3d
      :autoplay="autoplay"
      :autoplay-timeout="2500"
      style="margin-top:5%;"
      :height="370"
      :width="500"
      :perspective="16"
      :space="450"
    >
      <slide :index="0" style="border: 0px; background-color:#ecf0f1;">
        <vue-flip v-model="flip[0]" width="500" height="370">
          <template v-slot:front>
            <v-card class="mx-auto rounded-0" min-width="500" min-height="370">
              <v-img
                :src="require('../assets/offers/mylibyana.svg')"
                height="200px"
              ></v-img>

              <v-card-title>
                {{ translate("MyLibyana Application") }}
              </v-card-title>

              <v-card-subtitle>
                {{
                  translate(
                    "Download MyLibyana from Appstore or Playstore and get 1 Giga + 15 minutes free."
                  )
                }}
              </v-card-subtitle>

              <v-card-actions>
                <v-btn  color="orange lighten-3" block elevation="6"  @click="flipCard(0)">
                  {{ translate("Learn More") }}
                </v-btn>
              </v-card-actions>
            </v-card>
          </template>
          <template v-slot:back>
            <v-card class="mx-auto rounded-0" min-width="500" min-height="370">
              <v-card-title class="text-h7 white--text" style="background-color: #0f0f33;">
                {{ translate("All Libyana’s services and offers at the press - of a button #foryourcomfort") }}
              </v-card-title>

              <v-card-text class="text--primary" style="padding-top:30px; height:220px;">
                {{
                  translate(
                    "Through 'MyLibyana' app you can benefit from all services, access all offers, and get the latest of Libyana’s updates in one place. The application is available in Arabic and English."
                  )
                }}
              </v-card-text>

              <v-divider></v-divider>

              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="primary" text @click="cancelFlipCard(0)">
                  {{ translate("Close") }}
                </v-btn>
              </v-card-actions>
            </v-card>
          </template>
        </vue-flip>
      </slide>

      <slide :index="1" style="border: 0px; background-color:#ecf0f1;">
        <vue-flip v-model="flip[1]" width="500" height="370">
          <template v-slot:front>
            <v-card class="mx-auto rounded-0" min-width="500" min-height="370">
              <v-img
                :src="require('../assets/offers/sallefny2.png')"
                height="200px"
              ></v-img>

              <v-card-title>
                {{ translate("Sallefny") }}
              </v-card-title>

              <v-card-subtitle>
                {{
                  translate("dial *121# and don’t let the credit limit you.")
                }}
              </v-card-subtitle>

              <v-card-actions>
                <v-btn  color="orange lighten-3" block elevation="6"  @click="flipCard(1)">
                  {{ translate("Learn More") }}
                </v-btn>
              </v-card-actions>
            </v-card>
          </template>
          <template v-slot:back>
            <v-card class="mx-auto rounded-0" min-width="500" min-height="370">
              <v-card-title class="text-h7 white--text" style="background-color: #0f0f33;">
                {{ translate("Sallefny, don't stop your calls!") }}
              </v-card-title>

              <v-card-text class="text--primary" style="padding-top:30px; height:240px;">
                {{
                  translate(
                    "With the credit loan service, you can borrow credit from Libyana and use it to make calls, subscribe to Internet packages, and benefit from all other Libyana services."
                  )
                }}
              </v-card-text>

              <v-divider></v-divider>

              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="primary" text @click="cancelFlipCard(1)">
                  {{ translate("Close") }}
                </v-btn>
              </v-card-actions>
            </v-card>
          </template>
        </vue-flip>
      </slide>

      <slide :index="2" style="border: 0px; background-color:#ecf0f1;">
        <vue-flip v-model="flip[2]" width="500" height="370">
          <template v-slot:front>
            <v-card class="mx-auto rounded-0" min-width="500" min-height="370">
              <v-img
                :src="require('../assets/offers/cus_srvc.svg')"
                height="200px"
              ></v-img>

              <v-card-title>
                {{ translate("Call Center") }}
              </v-card-title>

              <v-card-subtitle>
                {{ translate("150 we’re there because we care.") }}
              </v-card-subtitle>

              <v-card-actions>
                <v-btn  color="orange lighten-3" block elevation="6"  @click="flipCard(2)">
                  {{ translate("Learn More") }}
                </v-btn>
              </v-card-actions>
            </v-card>
          </template>
          <template v-slot:back>
            <v-card class="mx-auto rounded-0" min-width="500" min-height="370">
              <v-card-title class="text-h7 white--text" style="background-color: #0f0f33;">
                {{ translate("150 we’re there because we care.") }}
              </v-card-title>

              <v-card-text class="text--primary" style="padding-top:30px; height:240px;">
                {{
                  translate(
                    "Our customer service team is always ready to help you 24/7, just call 150 or message us on our facebook page."
                  )
                }}
              </v-card-text>

              <v-divider></v-divider>

              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="primary" text @click="cancelFlipCard(2)">
                  {{ translate("Close") }}
                </v-btn>
              </v-card-actions>
            </v-card>
          </template>
        </vue-flip>
      </slide>

      <slide :index="3" style="border: 0px; background-color:#ecf0f1;">
        <vue-flip v-model="flip[3]" width="500" height="370">
          <template v-slot:front>
            <v-card class="mx-auto rounded-0" min-width="500" min-height="370">
              <v-img
                :src="require('../assets/placeholder.svg')"
                height="200px"
              ></v-img>

              <v-card-title>
                {{ translate("My Points Program") }}
              </v-card-title>

              <v-card-subtitle>
                {{
                  translate(
                    "Collect more points as you use services and replace those points for free (minutes, SMS, and Internet) from Libyana."
                  )
                }}
              </v-card-subtitle>

              <v-card-actions>
                <v-btn  color="orange lighten-3" block elevation="6"  @click="flipCard(3)">
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
              <v-card-title class="text-h7 white--text" style="background-color: #0f0f33;">
                {{ translate("Use more services and get more points") }}
              </v-card-title>

              <v-card-text style="padding-top:10px;">
                <v-simple-table fixed-header>
                  <thead>
                    <tr style="background-color:#92278f; color:white;">
                      <td  style="width: 20%;">
                        {{ translate("Package Validity") }}
                      </td>
                      <td style="width: 20%;"></td>
                      <td class="text-center" style="width: 60%;">
                        {{ translate("Gift Package") }}
                      </td>
                      <td style="width: 20%;"></td>
                      <td  style="width: 20%;">
                        {{ translate("Required Points") }}
                      </td>
                    </tr>
                    <tr>
                      <td
                        style="background-color:#92278f; color:white; width: 20%;"
                      ></td>
                      <td style="width: 20%; background-color:#e8e8e8">{{ translate("Internet") }}</td>
                      <td style="width: 20%; background-color:#e8e8e8">
                        {{ translate("Text Messages (Libyana-Libyana)") }}
                      </td>
                      <td style="width: 20%; background-color:#e8e8e8">{{ translate("Minutes (Libyana-Libyana)") }}</td>
                      <td
                        style="background-color:#92278f; color:white; width: 20%;"
                      ></td>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="(pkg,i) in pointsprg" :key="i">
                      <td>{{ translate(pkg.valid) }}</td>
                      <td>{{ translate(pkg.internet) }}</td>
                      <td>{{ translate(pkg.text) }}</td>
                      <td>{{ translate(pkg.min) }}</td>
                      <td>{{ translate(pkg.points) }}</td>
                    </tr>
                  </tbody>
                </v-simple-table>
              </v-card-text>

              <v-card-text style="padding-top:10px;">
                {{
                  translate(
                    "To view your points or see the available packages dial *333# or use MyLibyana app."
                  )
                }}
              </v-card-text>

              <v-divider></v-divider>

              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="primary" text @click="cancelFlipCard(3)">
                  {{ translate("Close") }}
                </v-btn>
              </v-card-actions>
            </v-card>
          </template>
        </vue-flip>
      </slide>

      <slide :index="4" style="border: 0px; background-color:#ecf0f1;">
        <vue-flip v-model="flip[4]" width="500" height="370">
          <template v-slot:front>
            <v-card class="mx-auto rounded-0" min-width="500" min-height="370">
              <v-img
                :src="require('../assets/offers/sadara.png')"
                height="200px"
              ></v-img>

              <v-card-title>
                {{ translate("You are the lead") }}
              </v-card-title>

              <v-card-subtitle>
                {{
                  translate(
                    "With Libyana you’re always in the lead."
                  )
                }}
              </v-card-subtitle>

              <v-card-actions>
                <v-btn  color="orange lighten-3" block elevation="6" @click="flipCard(4)">
                  {{ translate("Learn More") }}
                </v-btn>
              </v-card-actions>
            </v-card>
          </template>
          <template v-slot:back>
            <v-card class="mx-auto rounded-0 overflow-y-auto" width="500" height="370">
              <v-card-text>
                <div  class="text--primary" style="font-size:16px;">
                {{ translate("You are the lead offers special packages to Libyana’s most loyal customers that includes special monthly internet packages as well as free minutes to spend on the network.") }}
              </div>
              </v-card-text>

              <v-card-text class="text--primary" style="padding-top:10px; font-weight:700;">
                {{ translate("The Special Offers:") }}
              </v-card-text>
              <v-card-text style="padding-top:10px;">
                <v-simple-table fixed-header>
                  <thead style="background-color:#92278f; color:white;">
                    <tr>
                      <td >{{translate("Technology") }}</td>
                      <td >{{translate("Free Minutes") }}</td>
                      <td >{{translate("Package Capacity") }}</td>
                      <td >{{translate("Package Price") }}</td>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="(pkg,i) in specialOffers" :key="i">
                      <td>{{ translate(pkg.tech) }}</td>
                      <td>{{ translate(pkg.mins) }}</td>
                      <td>{{ translate(pkg.capacity) }}</td>
                      <td>{{ translate(pkg.price) }}</td>
                    </tr>
                  </tbody>
                </v-simple-table>
              </v-card-text>

              <v-divider></v-divider>

              <v-card-text class="text--primary" style="padding-top:30px; font-weight:700;">
                {{ translate("All Night Special Offers:") }}
              </v-card-text>
              <v-card-text style="padding-top:10px;">
                <v-simple-table fixed-header>
                  <thead style="background-color:#92278f; color:white;">
                    <tr>
                      <td >{{translate("Technology") }}</td>
                      <td >{{translate("Package Capacity") }}</td>
                      <td >{{translate("Package Price") }}</td>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="(pkg,i) in allnight_SpecialOffers" :key="i">
                      <td>{{ translate(pkg.tech) }}</td>
                      <td>{{ translate(pkg.capacity) }}</td>
                      <td>{{ translate(pkg.price) }}</td>
                    </tr>
                  </tbody>
                </v-simple-table>
              </v-card-text>

              <v-divider></v-divider>

              <v-card-subtitle style="margin-top:30px;font-size:16px;" class="text--primary">{{ translate("Additionally, You’re the lead offer includes double quota for the weekly and biweekly internet packages:") }}</v-card-subtitle>

              <v-card-text class="text--primary" style="padding-top:١0px; font-weight:700;">
                {{ translate("Weekly") }}
              </v-card-text>
              <v-card-text style="padding-top:10px;">
                <v-simple-table fixed-header>
                  <thead style="background-color:#92278f; color:white;">
                    <tr>
                      <td >{{translate("Subscription Method") }}</td>
                      <td >{{translate("Package Capacity") }}</td>
                      <td >{{translate("Package Price") }}</td>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="(pkg,i) in weekly_SpecialOffers" :key="i">
                      <td>{{ translate(pkg.sub) }}</td>
                      <td>{{ translate(pkg.price) }}</td>
                      <td>{{ translate(pkg.capacity) }}</td>
                    </tr>
                  </tbody>
                </v-simple-table>
              </v-card-text>
              
              <v-divider></v-divider>

              <v-card-text class="text--primary" style="padding-top:١0px; font-weight:700;">
                {{ translate("Bi-Weekly") }}
              </v-card-text>
              <v-card-text style="padding-top:10px;">
                <v-simple-table fixed-header>
                  <thead style="background-color:#92278f; color:white;">
                    <tr>
                      <td >{{translate("Subscription Method") }}</td>
                      <td >{{translate("Package Capacity") }}</td>
                      <td >{{translate("Package Price") }}</td>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="(pkg,i) in biweekly_SpecialOffers" :key="i">
                      <td>{{ translate(pkg.sub) }}</td>
                      <td>{{ translate(pkg.price) }}</td>
                      <td>{{ translate(pkg.capacity) }}</td>
                    </tr>
                  </tbody>
                </v-simple-table>
              </v-card-text>
              
              <v-divider></v-divider>

              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="primary" text @click="cancelFlipCard(4)">
                  {{ translate("Close") }}
                </v-btn>
              </v-card-actions>
            </v-card>
          </template>
        </vue-flip>
      </slide>
    </carousel-3d>
  </v-container>
</template>

<script>
import { Carousel3d, Slide } from "vue-carousel-3d";
import lang from "../lang/index";
import VueFlip from "vue-flip";
export default {
  components: {
    Carousel3d,
    Slide,
    "vue-flip": VueFlip,
  },

  methods: {
    translate: lang.translate,
    flipCard(index) {
      this.cancelFlipCard()
      console.log("flipping card ", index);
      this.flip[index] = true;
      this.autoplay = false;
      this.timeout = setTimeout(() => {
        this.cancelFlipCard()
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
      flip: [false, false, false, false, false],
      autoplay: true,
      timeout: null,
      pointsprg: [
        {
          valid: "One Week",
          internet: "500 MB",
          text: "15",
          min: "70",
          points: "200",
        },
        {
          valid: "One Week",
          internet: "1 GB",
          text: "25",
          min: "150",
          points: "500",
        },
        {
          valid: "Two Weeks",
          internet: "2 GB",
          text: "40",
          min: "250",
          points: "750",
        },
        {
          valid: "Two Weeks",
          internet: "3 GB",
          text: "50",
          min: "300",
          points: "1000",
        },
        {
          valid: "One Month",
          internet: "10 GB",
          text: "200",
          min: "1000",
          points: "2000",
        },
        {
          valid: "One Month",
          internet: "20 GB",
          text: "500",
          min: "2000",
          points: "4000",
        },
        {
          valid: "Two Weeks",
          internet: "Unlimited",
          text: "Unlimited",
          min: "Unlimited",
          points: "8000",
        },
        {
          valid: "One Month",
          internet: "Unlimited",
          text: "Unlimited",
          min: "Unlimited",
          points: "12000",
        },
        {
          valid: "Two Months",
          internet: "Unlimited",
          text: "Unlimited",
          min: "Unlimited",
          points: "15000",
        },
      ],
      specialOffers: [
        {
        tech: "4G",
        mins: "100",
        capacity: "21 GB",
        price: "30 ",
        },
        {
        tech: "4G",
        mins: "200",
        capacity: "30 GB",
        price: "40 ",
        },
        {
        tech: "4G",
        mins: "500",
        capacity: "85 GB",
        price: "75 ",
        },
        {
        tech: "4G",
        mins: "1000",
        capacity: "200GB",
        price: "150 ",
        },
      ],
      allnight_SpecialOffers: [
        {
        tech: "4G",
        capacity: "1 TB",
        price: "10 ",
        },
      ],
      weekly_SpecialOffers: [
        {
          sub: "*777*1#",
          price: "1 ",
          capacity: "5̶0̶ ̶M̶B̶ - 100 MB"
        },
        {
          sub: "*777*3#",
          price: "3 ",
          capacity: "2̶0̶0̶ ̶M̶B̶ - 400 MB"
        },
        {
          sub: "*777*4#",
          price: "4 ",
          capacity: "4̶0̶0̶ ̶M̶B̶ - 800 MB"
        },
      ],
      biweekly_SpecialOffers: [
        {
          sub: "*777*8#",
          price: "8 ",
          capacity: "1̶ ̶G̶B̶ - 2 GB"
        },
        {
          sub: "*777*12#",
          price: "12 ",
          capacity: "2̶ ̶G̶B̶ - 4 GB"
        },
        {
          sub: "*777*16#",
          price: "16 ",
          capacity: "3̶ ̶G̶B̶ - 6 GB"
        },
      ],
    };
  },
};
</script>
