<template>
  <div class="app">
    <v-navigation-drawer permanent expand-on-hover:false fixed style="background-color:#C8C8D4">
      <v-list class="profilecontainer d-flex position-relative" style="height:220px">
        <v-list-item class="d-flex align-items-center justify-content-center p-0">
          <img class="navbar-brand-full" src="./../../static/food2.png" width="100%" alt="DOSM">
        </v-list-item>

      </v-list>
      <div class="divider"></div>
      <!-- <v-divider style="border-color: #00a1f1;margin-bottom: 0px"></v-divider> -->

      <v-list class="ml-1" nav>
        <v-list-item class="active" @click="tabsNav('myorders',$event)" link>
          <v-list-item-icon>
            <v-icon>mdi-food</v-icon>
          </v-list-item-icon>
          <v-list-item-title class="ml-2">MY ORDERS</v-list-item-title>
        </v-list-item>


        <v-list-item @click="tabsNav('products',$event)" link>
          <v-list-item-icon>
            <v-icon>mdi-food-variant</v-icon>
          </v-list-item-icon>
          <v-list-item-title class="ml-2">AVAILABLE PRODUCTS</v-list-item-title>
        </v-list-item>

        <v-list-item  v-if="user_role=='Admin'" @click="tabsNav('orders',$event)">
          <v-list-item-icon>
            <v-icon>mdi-food-fork-drink</v-icon>
          </v-list-item-icon>
          <v-list-item-title class="ml-2">ORDERS</v-list-item-title>
        </v-list-item>

      </v-list>

      <div class="text-center" style="position: absolute;bottom: 20px;left: 13%;">
        <div class="my-2" style="margin-left:35px">
          <v-btn style="background: #555663;color:white;border-bottom: 4px solid #282568;border-radius:0;" @click="logout">LOG OUT</v-btn>
        </div>
      </div>
    </v-navigation-drawer>
    <router-view></router-view>
  </div>
</template>

<script>
import nav from '@/_nav'
import { Header as AppHeader, SidebarToggler, Sidebar as AppSidebar, SidebarFooter, SidebarForm, SidebarHeader, SidebarMinimizer, SidebarNav, Aside as AppAside, AsideToggler, Footer as TheFooter, Breadcrumb } from '@coreui/vue'
import DefaultHeaderDropdownAccnt from './DefaultHeaderDropdownAccnt'


export default {
  name: 'DefaultContainer',
  components: {
    AsideToggler,
    AppHeader,
    AppSidebar,
    AppAside,
    TheFooter,
    Breadcrumb,
    DefaultHeaderDropdownAccnt,
    SidebarForm,
    SidebarFooter,
    SidebarToggler,
    SidebarHeader,
    SidebarNav,
    SidebarMinimizer
  },
  data () {
    return {
      nav: nav.items,
      dashmnth:1,
      dashyer:"",
      MonthList:[],
      isDefaultset:1,
      userid:"",
      newcount:"",
      user_role:window.localStorage['user_role']
    }
  },
  computed: {
    name () {
      return this.$route.name
    },
    list () {
      return this.$route.matched.filter((route) => route.name || route.meta.label )
    },
  },
  methods:{
    logout(){
      this.$router.push('/')
      window.localStorage.clear();
    },
    getcartcount(){
      var self = this;
      self.userid = window.localStorage['userid']
      this.axios.get(this.appConfig.api_url_get + this.appConfig.getcartcount + '/' + self.userid).then((data) => {

        this.newcount = data.data
        setTimeout(()=>{
          this.getcartcount()
      },4000);
      })
    },
    getFileMonths(){
      this.axios.get(this.appConfig.api_url_get + this.appConfig.getAllFileMonths).then((data) => {
           var data1=data.data.data;
            this.MonthList=[];
             data1.forEach(element => {
              this.MonthList.push({'text':element.Month_year,'value':element.Month_year})
              });
              this.dashyer=unescape(localStorage.dataMonth);
          })
    },
    MonthChangedropdown(e){

      if(e!= window.localStorage.dataMonth){
        console.log('Reload date: '+window.localStorage.dataMonth);
        Console.log('Reloaded for no date in local storage')
        window.localStorage.setItem("dataMonth",escape(this.dashyer));
                window.location.reload();
        }
        else{
          this.isDefaultset=0;

        }
    },
    viewcart(){
      this.$router.push('/viewcart')
    },
    tabsNav(type,elemnt){

      $('.v-list-item').removeClass('active');
      $(elemnt.currentTarget).addClass('active');
      switch (type) {

        case "orders":
          this.$router.push('/'+type)
          break;

        case "products":
          this.$router.push('/'+type)
          break;

       case "myorders":
        this.$router.push('/'+type)
        break;

        default:
          break;
      }
    }
  },
  created(){
    var self = this;
    $(elemnt.currentTarget).addClass('active');
    self.user_role = window.localStorage['user_role'];
  }
}
</script>


<style scoped>
.fa-bell{
  font-size: 1rem;
}
.monthdiv{
  background: white;
    width: 100%;
    min-width: 100%;
    height: 46px;
    border-bottom: 1px solid #c8ced3;
    padding-top: 7px;
}
.breadcrumb-item span {
    padding-left: 40px;
    margin-bottom: 0.5rem;
    font-weight: 600;
    line-height: 1.2;
}
.headertxt{
  color: black;
  padding-left: 10px;
}
.tabslist{
  background-color: #314c8a;
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -ms-flex-wrap: wrap;
  flex-wrap: wrap;
  padding: 0.75rem 1rem;
  margin-bottom: 1.5rem;
  list-style: none;
  border-radius: 0;
  position: fixed;
  width: 100%;
  z-index: 99;
}
.tabs-item{
  padding-left: 40px;
  cursor: pointer;
}
.tabs-item span{
  color:#fff !important;
  font-size: 14px;
  font-weight: 600;
  text-transform: uppercase !important;
}
.tabs-item span.active{
  font-size: 15px;
  color: #fce4ec !important;
}
.main,.container-fluid{
  background: #fff;
}
.wrapper {
  margin-top:3.5rem !important;
  height:100%;
  position:relative;
  display:inline-table;
}
.app-body,.app{
  background-color: #fff;
  display: inline-table;
}
.cartdiv{
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: rgb(0, 161, 241);
  width:40px;
  height: 40px;
  margin-right: 15px;
  box-shadow: 2px 4px 9px #757575;
}
.cartdiv:hover {
    box-shadow: 2px 3px 10px #525050;
}
.cartimg{
  height: 42%;
    margin-top: 10px;
    margin-left: -3px;
    width: 65%;
}
.profilecontainer{
  border-radius: 0;
}
.v-list-item.active{
  background-color: #98A8B7;
}
.divider{
  background-image: url("./../../public/strip.png");
  max-height:10px;
  height:10px;
  width:100%;
  background-repeat: repeat-x;
  background-size: cover;
}

</style>
