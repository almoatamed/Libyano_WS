<template>
  <v-container fluid>
    <img
      :src="require('../../assets/roaming/map10.png')"
      usemap="#image-map"
      style="  display: block; margin-left: auto; margin-right: auto;"
    />
    <map name="image-map">
    <area target="" alt="asia" title="asia" @click="dialog3 = true" coords="628,121,649,127,709,113,799,81,824,94,908,93,1005,133,1001,143,927,187,923,172,919,161,891,165,876,177,888,182,886,198,858,225,859,238,840,223,838,232,840,249,835,265,806,274,813,290,804,300,771,275,753,281,740,308,715,272,703,264,694,270,659,293,646,273,636,250,632,231,619,226,646,215,626,204,614,181,616,162,630,148,632,128" shape="poly">
    <area target="" alt="asiaLabel" title="asiaLabel" @click="dialog3 = true" coords="930,58,996,93" shape="rect">
    <area target="" alt="europe" title="europe" @click="dialog2 = true" coords="618,113,595,116,579,134,565,148,565,162,580,167,566,182,552,171,545,127,541,136,535,166,527,183,531,200,543,202,529,213,530,226,548,224,568,212,585,218,605,215,615,206,606,199,599,183,596,169,605,152,618,147" shape="poly">
    <area target="" alt="europeLabel" title="europeLabel" @click="dialog2 = true" coords="568,61,694,104" shape="rect">
    <area target="" alt="africa" title="africa" @click="dialog = true" coords="539,235,577,234,619,245,627,256,637,277,647,297,663,303,665,312,655,319,650,328,646,338,646,354,667,354,670,369,661,387,642,371,632,385,612,409,596,409,575,366,582,341,573,328,568,312,531,315,510,295,508,269,521,250" shape="poly">
    <area target="" alt="africaLabel" title="africaLabel" @click="dialog = true" coords="635,401,711,427" shape="rect">
    <area target="" alt="australia" title="australia" @click="dialog7 = true" coords="872,323,905,337,911,347,917,386,915,407,904,425,880,410,829,411,823,387,846,369,864,351" shape="poly">
    <area target="" alt="australiaLabel" title="australiaLabel" @click="dialog7 = true" coords="821,424,928,457" shape="rect">
    <area target="" alt="northamerica" title="northamerica" @click="dialog5 = true" coords="169,109,237,117,277,127,309,129,326,126,341,136,331,149,327,166,347,174,358,187,362,178,364,153,375,152,383,160,392,166,397,160,418,184,424,203,408,199,400,192,399,209,355,247,358,261,343,251,324,254,317,267,326,276,339,269,350,291,360,303,352,305,320,288,298,276,275,257,249,191,217,164,185,163,163,172,154,154,149,134,152,121" shape="poly">
    <area target="" alt="northamericaLabel" title="northamericaLabel" @click="dialog5 = true" coords="373,235,465,279" shape="rect">
    <area target="" alt="southamerica" title="southamerica" @click="dialog6 = true" coords="367,302,382,296,464,339,454,375,438,399,443,410,424,420,405,424,388,455,390,472,380,472,366,455,373,427,379,368,363,354,355,329" shape="poly">
    <area target="" alt="southamericaLabel" title="southamericaLabel" @click="dialog6 = true" coords="183,377,283,426" shape="rect">
    <area target="" alt="northpole" title="northpole" @click="dialog4 = true" coords="259,86,358,53,397,55,467,49,517,60,503,74,504,99,495,122,462,137,448,159,421,133,402,90,364,85,360,101,387,116,402,134,392,151,370,142,371,127,344,110,334,97,316,101,311,107,302,115,280,120,248,110" shape="poly">
    <area target="" alt="help" title="help" @click="help = true" coords="1035,392,1091,464" shape="rect">
    <area target="" alt="australiaIsland" title="australiaIsland" @click="dialog7 = true" coords="948,407,984,451" shape="rect">
    </map>
    <v-dialog v-model="dialog" max-width="750px">
      <v-card class="mx-auto" max-width="750" outlined>
        <v-card-title class="text-h7 font-weight-bold grey lighten-2">
          {{ translate("Africa") }}
        </v-card-title>

        <v-card-text style="padding-top:10px;">
          <v-simple-table fixed-header>
            <thead style="background-color:#92278f; color:white;">
              <tr>
                <td>{{ translate("Operator") }}</td>
                <td>{{ translate("Network Service Status") }}</td>
                <td>{{ translate("Incoming Call") }}</td>
                <td>{{ translate("Outgoing Call to Libya") }}</td>
                <td>{{ translate("Outgoing Local Call") }}</td>
                <td>{{ translate("SMS") }}</td>
              </tr>
            </thead>
            <tbody v-for="roam in africa" :key="roam.country">
              <tr v-if="roam.country">
                <td
                  colspan="6"
                  style="font-weight:700; text-align:center; color:#92278f"
                  class="text-h6"
                >
                  {{ translate(roam.country) }}
                </td>
              </tr>
              <tr>
                <td>{{ translate(roam.operator) }}</td>
                <td>{{ translate(roam.netstatus) }}</td>
                <td>{{ translate(roam.mtc) }}</td>
                <td>{{ translate(roam.moclib) }}</td>
                <td>{{ translate(roam.mocloc) }}</td>
                <td>{{ translate(roam.sms) }}</td>
              </tr>
            </tbody>
          </v-simple-table>
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-btn text @click="dialog = false">
            Close
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-dialog v-model="dialog2" max-width="750px">
      <v-card class="mx-auto" max-width="750" outlined>
        <v-card-title class="text-h7 font-weight-bold grey lighten-2">
          {{ translate("Europe") }}
        </v-card-title>

        <v-card-text style="padding-top:10px;">
          <v-simple-table fixed-header>
            <thead style="background-color:#92278f; color:white;">
              <tr>
                <td>{{ translate("Operator") }}</td>
                <td>{{ translate("Network Service Status") }}</td>
                <td>{{ translate("Incoming Call") }}</td>
                <td>{{ translate("Outgoing Call to Libya") }}</td>
                <td>{{ translate("Outgoing Local Call") }}</td>
                <td>{{ translate("SMS") }}</td>
              </tr>
            </thead>
            <tbody v-for="roam in europe" :key="roam.country">
              <tr v-if="roam.country">
                <td
                  colspan="6"
                  style="font-weight:700; text-align:center; color:#92278f"
                  class="text-h6"
                >
                  {{ translate(roam.country) }}
                </td>
              </tr>
              <tr>
                <td>{{ translate(roam.operator) }}</td>
                <td>{{ translate(roam.netstatus) }}</td>
                <td>{{ translate(roam.mtc) }}</td>
                <td>{{ translate(roam.moclib) }}</td>
                <td>{{ translate(roam.mocloc) }}</td>
                <td>{{ translate(roam.sms) }}</td>
              </tr>
            </tbody>
          </v-simple-table>
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-btn text @click="dialog2 = false">
            Close
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-dialog v-model="dialog3" max-width="750px">
      <v-card class="mx-auto" max-width="750" outlined>
        <v-card-title class="text-h7 font-weight-bold grey lighten-2">
          {{ translate("Asia") }}
        </v-card-title>

        <v-card-text style="padding-top:10px;">
          <v-simple-table fixed-header>
            <thead style="background-color:#92278f; color:white;">
              <tr>
                <td>{{ translate("Operator") }}</td>
                <td>{{ translate("Network Service Status") }}</td>
                <td>{{ translate("Incoming Call") }}</td>
                <td>{{ translate("Outgoing Call to Libya") }}</td>
                <td>{{ translate("Outgoing Local Call") }}</td>
                <td>{{ translate("SMS") }}</td>
              </tr>
            </thead>
            <tbody v-for="roam in asia" :key="roam.country">
              <tr v-if="roam.country">
                <td
                  colspan="6"
                  style="font-weight:700; text-align:center; color:#92278f"
                  class="text-h6"
                >
                  {{ translate(roam.country) }}
                </td>
              </tr>
              <tr>
                <td>{{ translate(roam.operator) }}</td>
                <td>{{ translate(roam.netstatus) }}</td>
                <td>{{ translate(roam.mtc) }}</td>
                <td>{{ translate(roam.moclib) }}</td>
                <td>{{ translate(roam.mocloc) }}</td>
                <td>{{ translate(roam.sms) }}</td>
              </tr>
            </tbody>
          </v-simple-table>
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-btn text @click="dialog3 = false">
            Close
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-dialog v-model="dialog4" max-width="750px">
      <v-card class="mx-auto" max-width="750" outlined>
        <v-card-title class="text-h7 font-weight-bold grey lighten-2">
          {{ translate("North Pole, Not coming that soon -.- ") }}
        </v-card-title>

        <v-divider></v-divider>

        <v-card-actions>
          <v-btn text @click="dialog4 = false">
            Close
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-dialog v-model="dialog5" max-width="750px">
      <v-card class="mx-auto" max-width="750" outlined>
        <v-card-title class="text-h7 font-weight-bold grey lighten-2">
          {{ translate("North America") }}
        </v-card-title>

        <v-card-text style="padding-top:10px;">
          <v-simple-table fixed-header>
            <thead style="background-color:#92278f; color:white;">
              <tr>
                <td>{{ translate("Operator") }}</td>
                <td>{{ translate("Network Service Status") }}</td>
                <td>{{ translate("Incoming Call") }}</td>
                <td>{{ translate("Outgoing Call to Libya") }}</td>
                <td>{{ translate("Outgoing Local Call") }}</td>
                <td>{{ translate("SMS") }}</td>
              </tr>
            </thead>
            <tbody v-for="roam in america" :key="roam.country">
              <tr v-if="roam.country">
                <td
                  colspan="6"
                  style="font-weight:700; text-align:center; color:#92278f"
                  class="text-h6"
                >
                  {{ translate(roam.country) }}
                </td>
              </tr>
              <tr>
                <td>{{ translate(roam.operator) }}</td>
                <td>{{ translate(roam.netstatus) }}</td>
                <td>{{ translate(roam.mtc) }}</td>
                <td>{{ translate(roam.moclib) }}</td>
                <td>{{ translate(roam.mocloc) }}</td>
                <td>{{ translate(roam.sms) }}</td>
              </tr>
            </tbody>
          </v-simple-table>
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-btn text @click="dialog5 = false">
            Close
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-dialog v-model="dialog6" max-width="750px">
      <v-card class="mx-auto" max-width="750" outlined>
        <v-card-title class="text-h7 font-weight-bold grey lighten-2">
          {{ translate("South America") }}
        </v-card-title>

        <v-card-text style="padding-top:10px;">
          <v-simple-table fixed-header>
            <thead style="background-color:#92278f; color:white;">
              <tr>
                <td>{{ translate("Operator") }}</td>
                <td>{{ translate("Network Service Status") }}</td>
                <td>{{ translate("Incoming Call") }}</td>
                <td>{{ translate("Outgoing Call to Libya") }}</td>
                <td>{{ translate("Outgoing Local Call") }}</td>
                <td>{{ translate("SMS") }}</td>
              </tr>
            </thead>
            <tbody v-for="roam in south_america" :key="roam.country">
              <tr v-if="roam.country">
                <td
                  colspan="6"
                  style="font-weight:700; text-align:center; color:#92278f"
                  class="text-h6"
                >
                  {{ translate(roam.country) }}
                </td>
              </tr>
              <tr>
                <td>{{ translate(roam.operator) }}</td>
                <td>{{ translate(roam.netstatus) }}</td>
                <td>{{ translate(roam.mtc) }}</td>
                <td>{{ translate(roam.moclib) }}</td>
                <td>{{ translate(roam.mocloc) }}</td>
                <td>{{ translate(roam.sms) }}</td>
              </tr>
            </tbody>
          </v-simple-table>
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-btn text @click="dialog6 = false">
            Close
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-dialog v-model="dialog7" max-width="750px">
      <v-card class="mx-auto" max-width="750" outlined>
        <v-card-title class="text-h7 font-weight-bold grey lighten-2">
          {{ translate("Australia, Coming Soon!") }}
        </v-card-title>

        <v-divider></v-divider>

        <v-card-actions>
          <v-btn text @click="dialog7 = false">
            Close
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-dialog v-model="help" max-width="750px">
      <v-card class="mx-auto" max-width="750" outlined>
                      <v-row style="background-color: #0f0f33;">
                <v-col md="10">
                  <v-card-title
                    class="text-h7 white--text"
                    style="font-weight:700;"
                  >
                    {{
                      translate(
                        "Help"
                      )
                    }}
                  </v-card-title>
                </v-col>
                <v-col md="2" class="text-center mt-3"
                  ><v-icon
                    @click="help = false"
                    large
                    color="orange lighten-3"
                    >mdi-close-circle</v-icon
                  ></v-col
                >
              </v-row>
              <v-card-text
                class="text--primary"
                style="padding-top:60px; margin-bottom:20px; height:220px; font-size:18px; text-align:center;"
              >
                {{
                  translate(
                    "Roaming Service allows you to use your Libyana SIM abroad, according to the host country’s billing** fees. For information on these fees click on each continent to view its host countries. ** Billing is LYD per 60 seconds."
                  )
                }}
              </v-card-text>
        <v-divider></v-divider>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script>
import lang from "../../lang/index";
export default {
  methods: {
    translate: lang.translate,
  },

  data() {
    return {
      dialog: false,
      dialog2: false,
      dialog3: false,
      dialog4: false,
      dialog5: false,
      dialog6: false,
      dialog7: false,
      help: false,
      africa: [
        {
          flag: "../../assets/flags/Flag_of_Algeria.svg",
          country: "Algeria",
          operator: "Wataniya",
          netstatus: "Postpaid+Prepaid",
          mtc: "5.81",
          moclib: "14.22",
          mocloc: "4.54",
          sms: "3.03",
        },
        {
          operator: "DJEZZY",
          netstatus: "Postpaid",
          mtc: "5.81",
          moclib: "11.37",
          mocloc: "4.60",
          sms: "2.36",
        },
        {
          country: "Egypt",
          operator: "Etisalat Misr ",
          netstatus: "Postpaid+Prepaid",
          mtc: "2.40",
          moclib: "37.33",
          mocloc: "6.23",
          sms: "3.93",
        },
        {
          operator: "Vodafone",
          netstatus: "Postpaid+Prepaid",
          mtc: "2.40",
          moclib: "7.87",
          mocloc: "4.54",
          sms: "3.93",
        },
        {
          operator: "Orange",
          netstatus: "Postpaid+Prepaid",
          mtc: "2.40",
          moclib: "8.59",
          mocloc: "4.66",
          sms: "0.36",
        },
        {
          country: "South Africa",
          operator: "Cell C",
          netstatus: "Postpaid",
          mtc: "3.00",
          moclib: "6.18",
          mocloc: "3.90",
          sms: "0.48",
        },
        {
          operator: "Telkom South Africa",
          netstatus: "Postpaid",
          mtc: "4.80",
          moclib: "13.31",
          mocloc: "13.31",
          sms: "1.09",
        },
        {
          operator: "VODACOM PTY LTD",
          netstatus: "Postpaid",
          mtc: "5.70",
          moclib: "5.75",
          mocloc: "5.75",
          sms: "0.42",
        },
        {
          country: "Tunisia",
          operator: "Tunisie Telecom",
          netstatus: "Postpaid+Prepaid",
          mtc: "5.70",
          moclib: "9.68",
          mocloc: "5.81",
          sms: "0.79",
        },
        {
          operator: "Orange",
          netstatus: "Postpaid+Prepaid",
          mtc: "5.70",
          moclib: "9.68",
          mocloc: "9.44",
          sms: "1.51",
        },
        {
          operator: "Ooredoo",
          netstatus: "Postpaid+Prepaid",
          mtc: "5.70",
          moclib: "8.47",
          mocloc: "5.14",
          sms: "0.79",
        },
      ],
      america: [
        {
          country: "United States",
          operator: "AT&T",
          netstatus: "Postpaid",
          mtc: "5.10",
          moclib: "5.01",
          mocloc: "5.25",
          sms: "1.17",
        },
        {
          operator: "Union Wireless",
          netstatus: "Postpaid",
          mtc: "9.36",
          moclib: "12.94",
          mocloc: "7.58",
          sms: "1.98",
        },
        {
          country: "Canada",
          operator: "Rogers Fido",
          netstatus: "Postpaid",
          mtc: "8.10",
          moclib: "12.71",
          mocloc: "7.52",
          sms: "2.22",
        },
      ],
      europe: [
        {
          country: "France",
          operator: "Orange",
          netstatus: "Postpaid+Prepaid",
          mtc: "3.08",
          moclib: "7.38",
          mocloc: "7.38",
          sms: "1.03",
        },
        {
          operator: "Bouygues",
          netstatus: "Postpaid",
          mtc: "3.85",
          moclib: "17.85",
          mocloc: "7.74",
          sms: "1.69",
        },
        {
          country: "Germany",
          operator: "Telekom Deutschland",
          netstatus: "Postpaid+Prepaid",
          mtc: "3.60",
          moclib: "13.98",
          mocloc: "8.71",
          sms: "1.57",
        },
        {
          operator: "Vodafone",
          netstatus: "Postpaid",
          mtc: "3.60",
          moclib: "5.51",
          mocloc: "5.51",
          sms: "0.36",
        },
        {
          country: "Italy",
          operator: "Telecom Italia TI",
          netstatus: "Postpaid+Prepaid",
          mtc: "2.40",
          moclib: "5.20",
          mocloc: "3.27",
          sms: "0.12",
        },
        {
          operator: "Wind",
          netstatus: "Postpaid+Prepaid",
          mtc: "2.40",
          moclib: "19.72",
          mocloc: "7.44",
          sms: "1.63",
        },
        {
          operator: "Vodafone",
          netstatus: "Postpaid+Prepaid",
          mtc: "2.40",
          moclib: "5.51",
          mocloc: "5.51",
          sms: "0.36",
        },
        {
          country: "Malta",
          operator: "Vodafone",
          netstatus: "Postpaid+Prepaid",
          mtc: "4.33",
          moclib: "5.57",
          mocloc: "5.57",
          sms: "0.61",
        },
        {
          operator: "GoMobile",
          netstatus: "Postpaid",
          mtc: "4.33",
          moclib: "6.59",
          mocloc: "4.84",
          sms: "0.18",
        },
        {
          country: "Spain",
          operator: "Vodafone",
          netstatus: "Postpaid+Prepaid",
          mtc: "4.20",
          moclib: "6.35",
          mocloc: "6.35",
          sms: "0.42",
        },
        {
          operator: "Vodafone",
          netstatus: "Postpaid+Prepaid",
          mtc: "4.20",
          moclib: "9.92",
          mocloc: "5.08",
          sms: "2.06",
        },
        {
          country: "United Kingdom",
          operator: "Three",
          netstatus: "Postpaid+Prepaid",
          mtc: "3.60",
          moclib: "10.45",
          mocloc: "3.96",
          sms: "1.13",
        },
        {
          operator: "Orange(EE)",
          netstatus: "Postpaid+Prepaid",
          mtc: "3.60",
          moclib: "31.64",
          mocloc: "5.93",
          sms: "2.03",
        },
        {
          operator: "O2(Telefonica)",
          netstatus: "Postpaid",
          mtc: "3.60",
          moclib: "17.06",
          mocloc: "5.93",
          sms: "1.92",
        },
        {
          operator: "Vodafone",
          netstatus: "Postpaid",
          mtc: "3.60",
          moclib: "5.25",
          mocloc: "5.25",
          sms: "0.55",
        },
      ],
      asia: [
        {
          country: "Cyprus",
          operator: "Prime Tel",
          netstatus: "Postpaid+Prepaid",
          mtc: "4.20",
          moclib: "13.31",
          mocloc: "6.66",
          sms: "0.91",
        },
        {
          country: "Jordan",
          operator: "Umniah",
          netstatus: "Postpaid+Prepaid",
          mtc: "3.12",
          moclib: "22.04",
          mocloc: "10.21",
          sms: "2.90",
        },
        {
          country: "Saudi Arabia",
          operator: "Mobily",
          netstatus: "Postpaid+Prepaid",
          mtc: "3.36",
          moclib: "3.96",
          mocloc: "2.94",
          sms: "0.68",
        },
        {
          operator: "Mobily",
          netstatus: "Postpaid+Prepaid",
          mtc: "3.36",
          moclib: "3.96",
          mocloc: "2.94",
          sms: "0.57",
        },
        {
          operator: "Zain",
          netstatus: "Postpaid+Prepaid",
          mtc: "8.10",
          moclib: "33.90",
          mocloc: "6.89",
          sms: "2.26",
        },
        {
          country: "Turkey",
          operator: "Vodafone",
          netstatus: "Postpaid+Prepaid",
          mtc: "3.60",
          moclib: "5.75",
          mocloc: "5.81",
          sms: "0.61",
        },
        {
          operator: "Avea (TT)",
          netstatus: "Postpaid+Prepaid",
          mtc: "3.60",
          moclib: "10.71",
          mocloc: "6.35",
          sms: "0.73",
        },
        {
          operator: "Turkcell",
          netstatus: "Postpaid+Prepaid",
          mtc: "3.60",
          moclib: "6.35",
          mocloc: "5.14",
          sms: "0.36",
        },
        {
          country: "United Arab Emirates",
          operator: "Etisalat",
          netstatus: "Postpaid+Prepaid",
          mtc: "10.68",
          moclib: "29.50",
          mocloc: "15.64",
          sms: "2.95",
        },
        {
          operator: "Thuraya (Satellite)",
          netstatus: "Postpaid",
          mtc: "18.00",
          moclib: "22.15",
          mocloc: "22.04",
          sms: "5.60",
        },
      ],
    };
  },
};
</script>
