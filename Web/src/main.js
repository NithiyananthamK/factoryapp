// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import 'core-js/es6/promise'
import 'core-js/es6/string'
import 'core-js/es7/array'
// import cssVars from 'css-vars-ponyfill'
import Vue from 'vue'
import BootstrapVue from 'bootstrap-vue'
import App from './App'
import router from './router'
import { apipath } from '../config/apipath'
import VueSweetalert2 from 'vue-sweetalert2'
import 'sweetalert2/dist/sweetalert2.min.css'
import axios from 'axios'
import VueAxios from 'vue-axios'
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'
import '@mdi/font/css/materialdesignicons.css'
Vue.prototype.appConfig = apipath

Vue.config.productionTip = false
Vue.use(Vuetify)
Vue.use(BootstrapVue)
Vue.use(VueSweetalert2)
Vue.use(VueAxios, axios)


Vue.use(Vuetify)
export default new Vuetify({
  icons: {
    iconfont: 'md',
  },
})

const options = {
  confirmButtonColor: '#41b882',
  cancelButtonColor: '#ff7674'
}

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: {
    App
  },
  created() {
    if(!(window.location.hash).includes('mstr')){
      if(localStorage.islogedin !=1){
        this.$router.push('/')
      }
  }
  },
})
