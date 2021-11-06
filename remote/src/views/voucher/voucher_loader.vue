<template>
  <div id="root">
    <v-container>
      <div class="text-h4">Voucher Loading Manager</div>
      <v-divider class="py-2"></v-divider>
      <v-card rounded="xl" elevation="6" :dark="isDark">
        <v-form ref="voucherForm" v-model="valid">
          <v-container fluid>
            <v-row>
              <v-col cols="12">
                <v-file-input
                  counter
                  v-model="file.obj"
                  show-size
                  truncate-length="15"
                  @change="check()"
                ></v-file-input>
                <p v-if="file.error" class="pl-6 red--text text--lighten-3">
                  {{ file.error_dictionary[file.error_type] }}
                </p>
                <p v-if="file.loaded" class="pl-6 green--text text--lighten-3">
                  The Vouchers Has Been Stored in Database Successfully
                </p>
              </v-col>
            </v-row>
          </v-container>

          <v-container fluid
            v-if="file.is_valid_vouchers"
          >
            <v-row>
              <v-col>
                  <div class="text-h6">Valid Vouchers</div>
              </v-col>
              <v-col cols="12">
                <v-data-table
                  dense
                  :headers="file.headers"
                  :items="file.valid_vouchers"
                  item-key="Serial"
                ></v-data-table>
              </v-col>
            </v-row>
          </v-container>

          <v-container fluid
            v-if="file.is_rejected_vouchers"
          >
            <v-row>
              <v-col>
                  <div class="text-h6">Rejected Vouchers</div>
              </v-col>
              <v-col cols="12">
                <v-data-table
                  dense
                  :headers="file.headers"
                  :items="file.rejected_vouchers"
                  item-key="Serial"
                ></v-data-table>
              </v-col>
            </v-row>
          </v-container>
          
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn
              :disabled="!file.is_valid_vouchers"
              :loading="file.loading"
              text
              color="primary"
              @click="load()"
            >
              Load
            </v-btn>
            <v-spacer></v-spacer>
            <v-btn
              :disabled="file.loading || file.saving"
              :loading="file.loading || file.saving"
              text
              color="primary"
              @click="clear()"
            >
              Clear
            </v-btn>
            <v-spacer></v-spacer>
          </v-card-actions>
        </v-form>
      </v-card>
    </v-container>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  data() {
    const defaultForm = Object.freeze({
      obj: {},
      error: false,
      error_dictionary: {
        not_csv: "Please chose and open either CSV file or xlsx file",
        not_valid: "The CSV file is not valid",
        no_file: "Please chose Valid file",
        over_size: "The File size should be less then 30kB",
      },
      error_type: null,
      loaded: false,
      loading: false,
      headers:[
        {text:'Serial Number', value:'Serial'},
        {text:'PIN', value:'PIN'},
        {text:'Value', value:'Value'}
      ],
      saving: false,
      valid: false,
      valid_vouchers: [],
      rejected_vouchers: [],
      is_valid_vouchers:false,
      is_rejected_vouchers:false,
    });

    return {
      file: Object.assign({}, defaultForm),
      defaultForm,
      valid: true,
    };
  },

  computed: {
    ...mapGetters("Theme", ["isDark"]),
    disabled() {
      return false;
    },
  },

  methods: {
    resetForm() {
      this.file = Object.assign({}, this.defaultForm);
      this.$refs.voucherForm.reset();
    },
    check() {
      var self = this
      self.file.valid_vouchers = []
      self.file.rejected_vouchers = []
      self.file.loaded = false
      self.file.error = false
      if (this.file.obj) {
        console.log(this.file);
        if (!this.file.obj.name) {
          this.clear();
          this.file.error_type = "no_file";
          this.file.error = true;
          return;
        } else {
          console.log("a file has been chosen");
          var extention = this.file.obj.name.split(".");
          extention = extention[extention.length - 1];
          console.log(extention);
          if (extention == "csv") {
            if (this.file.obj.size > 30e3) {
              this.clear();
              this.file.error_type = "over_size";
              this.file.error = true;
              return;
            } else {
              const reader = new FileReader();
              reader.onload = () => {
                var rows = reader.result.split('\n')
                rows = rows.map(function(row){
                  return row.split(',')
                })
                var head = rows[0]
                rows = rows.slice(1,rows.length-1)
                var vouchers = []
                rows.forEach(row => {
                  var voucher = {}
                  row.forEach((el,index)=>{
                    voucher[head[index]] = el
                  })
                  vouchers.push(voucher)
                });
                vouchers.forEach((el)=>{
                  if(el.PIN.length !=13 ){
                    self.file.rejected_vouchers.push(el)
                  }else if(parseInt(el.Value) == 5){
                    self.file.valid_vouchers.push(el)
                  }else if(parseInt(el.Value) == 10){
                    self.file.valid_vouchers.push(el)
                  }else{
                    self.file.rejected_vouchers.push(el)
                  }
                  
                })
                self.file.is_valid_vouchers = self.file.valid_vouchers.length>0?true:false
                self.file.is_rejected_vouchers = self.file.rejected_vouchers.length>0?true:false
                console.log(vouchers)
              };
              reader.readAsText(this.file.obj);
            }
          } 
            // else if (extention == "xlsx") {
            //   const reader = new FileReader();
            //   reader.onload = () => {
            //     var bstr = reader.result
            //     const wb = XLSX.read(bstr, { password:"17082021" });
            //     /* Get first worksheet */
            //     const wsname = wb.SheetNames[0];
            //     const ws = wb.Sheets[wsname];
            //     /* Convert array of arrays */
            //     const data = XLSX.utils.sheet_to_json(ws, { header: 1 }); 
            //     console.log(data)
            // };
            //   reader.readAsText(this.file.obj);
            // }
           else {
            this.clear();
            this.file.error_type = "not_csv";
            this.file.error = true;
            return;
          }
        }
      }
    },
    clear() {
      this.resetForm();
    },
    load(){
      this.$store.dispatch('Ros/postVouchers',this.file.valid_vouchers, {root:true}).then(()=>{
        this.clear()
        this.file.loaded = true
      })
    }
  },
  created() {},
};
</script>
<style></style>
