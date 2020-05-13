<template>
<div class="maincontainer">
<div>
      <b-modal id="adduser_order" style="top: -15px;" size="lg" ref="adduser_order" centered
        title="Confirm Order" hide-footer>
        <adduser_order :selected_order="selected_order"></adduser_order>
      </b-modal>
    </div>

    <div>
        <main id="maindiv" style="height:100%;">
            <section>
                <div class="pagetitle d-flex justify-content-between">
                    <h4> Orders details</h4>
                </div>
            </section>

            <section>


                <div v-if="itemsloader" class="text-center text-danger my-2">
                  <b-spinner class="align-middle"></b-spinner>
                  <strong>Loading...</strong>
                </div>

                <div class="row pl-3 mt-3" >
                        <div class="col-sm-4" style="padding-top:0px;padding-bottom:0px;" v-for="item in orders" :key="item">
                            <b-card class="border">
                                <h2> {{ item.item_name }} </h2>
                                <div class="textoverflow" style="height:30px;">
                                      <span> Description :  {{ item.item_description }} </span>
                                </div>
                                <div class="textoverflow" style="height:30px;">
                                      <span> Category :  {{ item.type }} </span>
                                </div>
                                 <div class="textoverflow" style="height:30px;">
                                      <span style="margin-bottom:0px;"> Stock : {{ item.available_qty }} </span>
                                 </div>
                                  <div class="textoverflow" style="height:30px;">
                                      <span style="margin-bottom:0px;">Item_price :  {{ item.single_qty_price }} </span>
                                 </div>

                                 <div>
                                    <b-button style="color:white !important;float:right;" size="sm" variant="outline-primary"  @click = "gotoorder(item.order_id, item.single_qty_price, item.available_qty)"> GO TO ORDER </b-button>
                                  </div>

                            </b-card>
                         </div>
                 </div>

            <b-pagination  v-if="!itemsloader" v-model="currentPage" :total-rows="totalcount" :per-page="perPage" first-number
              aria-controls="detailstable" @change="get_alertmgmt_details" align="center" first-text="First" prev-text="Prev"
              next-text="Next" last-text="Last">
            </b-pagination>
            </section>
        </main>
        <div>
            <b-modal id="alertadd" ref="alertadd" title="Alert  Add" centered  hide-footer>
                    <alertadd :editdata="res_data"></alertadd>
            </b-modal>
        </div>
    </div>


</div>
</template>

<script>
import adduser_order from './adduser_order'
import Vue from 'vue';
import Swal from 'vue-sweetalert2';
import VueSwal from 'vue-swal'
Vue.use(Swal)


export default {
  name: 'DefaultContainer',

  components: {
    adduser_order:adduser_order
  },

  data () {
    return {
        totalcount:0,
        perPage:9,
        currentPage:1,
        itemsloader:false,
        res_data:{},
        selected_order:{}
    }
  },

  computed: {

  },
  methods:{

    gotoorder(order_id, item_price, stockqty){
      this.selected_order = {
          "id" : 0,
          "order_id" : order_id,
          "item_price": item_price,
          "available_qty": stockqty
      }
      this.$refs.adduser_order.show();
    },

    editalert(alertmgmt_id){
      try{
			  var self = this;
				this.axios.get(this.appConfig.api_url_get + this.appConfig.get_alertmgmt_by_id +"/"+alertmgmt_id).then((res) => {
            this.$refs.adduser_order.show();
            this.selected_order_id = res.data;
         })
			}
			catch (e) {
					console.log(e)
		  }
    },

    deletepop(alertmgmt_id){
      swal({
            title: "Are you sure ??",
            icon: "warning",
            buttons: true,
            dangerMode: true,
        })
        .then((willDelete) => {
          if (willDelete) {
            this.deletealert(alertmgmt_id);
          }
        });
    },

    closepopup(){
      this.$refs.adduser_order.hide();
      this.get_details(1)
    },

    get_details(page){
			try{
        var self = this;
        this.itemsloader = true;
        self.orders = [];
        self.currentPage = page;
				this.axios.get(this.appConfig.api_url_get + this.appConfig.get_available_orders +"/"+page+"/9").then((res) => {
            this.itemsloader = false;
            self.orders = res.data.data;
            self.totalcount = res.data.total_count;
         })
			}
			catch (e) {
				console.log(e)
			}
    }
  },

  mounted(){
    document.getElementById("maindiv").style.height=window.innerHeight+"px";
  },

  created(){
    if(window.localStorage['userid'] !=undefined){
      this.currentPage = 1;
      this.get_details(this.currentPage);
    }
    else{
      this.$router.push('/')
    }
  }
}

</script>

<style>
   .input{
          border: 1px solid #E8DCD4;
          padding: 10px;
          border-radius: 5px;
          width:100%;
   }

  .btn{
      padding:10px;
      background: #00a1f1;
      color: white;
   }

   .textoverflow{
        width: 95%;
        word-break: break-all;
        text-overflow: ellipsis;
        overflow: hidden;
        white-space: nowrap;
   }

</style>
