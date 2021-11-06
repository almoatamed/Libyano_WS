<template>
  <v-container fluid>
    <img
      :src="require('../assets/roaming/map.png')"
      usemap="#image-map"
      style="  display: block; margin-left: auto; margin-right: auto;"
    />
    <map name="image-map">
      <area
        target=""
        alt="africa"
        title="africa"
        @click="dialog = true"
        coords="517,306,568,299,584,316,600,324,606,317,641,322,645,340,653,362,667,379,676,390,695,386,694,397,680,415,668,427,661,438,662,455,692,462,684,504,648,502,638,511,620,534,595,539,584,513,572,483,580,448,568,433,562,410,545,401,529,408,505,406,484,386,480,369,480,346,505,315"
        shape="poly"
      />
      <area
        target=""
        alt="europe"
        title="europe"
        @click="dialog2 = true"
        coords="634,144,608,145,597,145,586,153,576,169,555,190,553,204,562,209,562,224,552,236,541,229,532,211,531,182,531,163,524,169,520,181,520,199,514,213,504,237,504,256,506,274,506,295,516,298,531,297,555,274,582,298,603,294,619,272,624,263,608,254,599,246,608,239,600,230,599,205,612,198,628,187"
        shape="poly"
      />
      <area
        target=""
        alt="asia"
        title="asia"
        @click="dialog3 = true"
        coords="638,151,665,160,674,167,688,161,730,150,769,131,797,129,867,103,896,111,1011,117,1115,140,1139,170,1128,179,1042,236,980,251,943,288,948,299,923,321,923,336,911,340,904,345,881,356,879,367,880,382,869,387,821,347,788,388,718,333,721,349,711,363,677,377,660,347,648,319,649,295,627,298,620,287,668,279,654,265,628,264,616,241,615,207,638,189,636,167"
        shape="poly"
      />
      <area
        target=""
        alt="antartica"
        title="antartica"
        @click="dialog4 = true"
        coords="269,65,305,62,438,61,490,71,467,98,470,117,449,150,389,200,355,134,316,114,284,101,274,117,280,132,308,149,326,165,334,170,327,180,317,188,297,184,278,185,264,182,290,152,266,149,253,146,253,126,246,119,216,134,207,152,175,152,160,138,133,135,147,111"
        shape="poly"
      />
      <area
        target=""
        alt="america"
        title="america"
        @click="dialog5 = true"
        coords="38,138,126,149,172,159,200,162,222,161,235,160,236,149,231,141,238,130,241,138,243,148,252,158,264,153,275,157,267,164,257,172,251,181,243,187,233,200,240,212,251,214,269,225,287,190,312,197,329,203,343,221,356,232,364,257,333,268,276,315,280,336,271,336,251,323,234,326,223,339,232,359,246,354,255,349,268,373,276,388,265,389,239,374,196,357,153,307,141,312,139,254,81,202,45,201,30,218,17,222,8,193,2,163,16,145"
        shape="poly"
      />
      <area
        target=""
        alt="southamerica"
        title="southamerica"
        @click="dialog6 = true"
        coords="285,402,310,384,338,391,370,410,412,438,421,444,408,478,397,499,393,531,391,549,346,552,331,565,321,576,321,590,324,615,309,617,293,600,304,480,283,459,277,436,279,423"
        shape="poly"
      />
      <area
        target=""
        alt="australia"
        title="australia"
        @click="dialog7 = true"
        coords="961,422,998,435,1045,443,1045,457,1001,454,977,447,995,465,1006,489,1024,507,1015,540,1005,564,1090,539,1103,552,1077,581,1068,582,988,552,972,539,932,537,910,540,901,516,899,499,945,469"
        shape="poly"
      />
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
                  style="font-weight:700; text-align:center;"
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
                  style="font-weight:700; text-align:center;"
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
                  style="font-weight:700; text-align:center;"
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
          {{ translate("Antarctica, Not coming that soon -.- ") }}
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
                  style="font-weight:700; text-align:center;"
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
                  style="font-weight:700; text-align:center;"
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
  </v-container>
</template>

<script>
import lang from "../lang/index";
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
      south_america:[],
      africa: [
        {
          flag: "../assets/flags/Flag_of_Algeria.svg",
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
