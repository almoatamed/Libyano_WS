import Vue from 'vue';
import Vuetify from 'vuetify/lib/framework';

Vue.use(Vuetify);

const vuetify = new Vuetify({
  theme: {
    themes: {
      light: {
        bar_color: '#0F0F33',
        btn_color:'#BB66CC',
      },
    },
  },
})

export default vuetify