import Vue from 'vue';
import Vuetify from 'vuetify/lib/framework';

Vue.use(Vuetify);

const vuetify = new Vuetify({
  theme: {
    themes: {
      light: {
        libyana: '#92278f',
        stream:'#0f0f33',
        background: '#ecf0f1',
      },
    },
  },

  rtl: false,
})

export default vuetify