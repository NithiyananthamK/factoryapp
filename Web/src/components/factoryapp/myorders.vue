<template>
  <div class="maincontainer">
    <div>
      <b-modal id="adduser_order" style="top: -15px;" size="lg" ref="adduser_order" centered
        title="Edit Order" hide-footer>
        <adduser_order :selected_order="selected_order"></adduser_order>
      </b-modal>
    </div>

    <h4> My Orders </h4>

    <div class="titleline"></div>


    <section style="background:#f5f5f5;">
      <div class="">
        <div>
          <b-table striped :sticky-header="true" :busy="isBusy" hover :items="items" :fields="fields">
            <template v-slot:table-busy>
              <div class="text-center text-danger my-2">
                <b-spinner class="align-middle"></b-spinner>
                <strong>Loading...</strong>
              </div>
            </template>

            <template v-slot:cell(Actions)="{ item }">
              <i data-toggle="tooltip" data-placement="top" title="Edit" style="font-size:18px !important;cursor:pointer;"
                class="v-icon notranslate mdi mdi-pencil theme--light" @click="edit_data(item['Order Id'], item['Id'], item['Item Price'], item['Available Qty'])"></i>
              <i data-toggle="tooltip" data-placement="top" title="Delete" style="font-size:18px !important;cursor:pointer;"
                class="v-icon notranslate mdi mdi-delete theme--light" @click="deletepop(item['Id'])"></i>
            </template>
          </b-table>

          <p v-if="items.length == 0 && !isBusy" class="pb-3 text-center font-weight-bold">No available orders found</p>

          <b-pagination v-show="items.length != 0" v-model="currentPage" :total-rows="totalcount" :per-page="perPage"
            first-number aria-controls="detailstable" @change="pageChange" align="center" first-text="First"
            prev-text="Prev" next-text="Next" last-text="Last">
          </b-pagination>
        </div>
      </div>
    </section>

  </div>
</template>

<script>
import adduser_order from './adduser_order'
import Vue from 'vue'
import VueSwal from 'vue-swal'
  export default {
    data() {
      return {
        isAdd:false,
        dataid:"",
        fields:['Order Id', 'Item name', 'Order type', 'Ordered Qty', 'Total amount to pay', 'Delivery Address',  'Actions'],
        items: [],
        isBusy:true,
        currentPage:1,
        perPage:10,
        totalcount:0,
        data_set:[],
        created_by:window.localStorage['userid'],
        selected_order:{}
      }
  },

  components:{
    adduser_order:adduser_order
  },

  mounted() {
    this.getdata(1);
  },

  methods: {

    closepopup(){
        this.$refs.adduser_order.hide();
        this.getdata(1)
      },

      updatedata(){
        //this.items=[]
        //this.getdata(this.page );
      },

      edit_data(order_id, id, item_price, stockqty){
        this.selected_order = {
          "id" : id,
          "order_id" : order_id,
          "item_price": item_price,
          "available_qty": stockqty
      }
      this.$refs.adduser_order.show();
      },

      deletepop(id){
        swal({
              title: "Are you sure ??",
              icon: "warning",
              buttons: true,
              dangerMode: true,
          })
          .then((willDelete) => {
            if (willDelete) {
              this.delete_data(id);
            }
            // else {
            //   swal("Your imaginary file is safe!");
            // }
          });
      },

      delete_data(id){
        var self = this;
        this.axios.get(this.appConfig.api_url_get + this.appConfig.delete_order +'/'+ id).then((data) => {
        if(data.data.Errorcode=='9999'){
          swal("Deleted!", {
                  icon: "success",timer: 2000,showConfirmButton: false
                });
          const index = self.items.findIndex(item => item.Actions === id) // find the post index
           if (~index) // if the post exists in array
             self.items.splice(index, 1) //delete the post
             self.getdata(self.currentPage)
        }
        else{

        }
      })
      },

      getdata(page){
        var self = this;
        self.isBusy = true;
        this.page = page;
        let created_by = self.created_by
        this.axios.get(this.appConfig.api_url_get + this.appConfig.getuser_orders +'/'+ page+'/10/'+created_by).then((data) => {
          self.items = [];
          self.data_set = data.data.data
          this.totalcount = data.data.total_count
          for(var i=0;i<self.data_set.length;i++){
            self.items.push({
              "Id":self.data_set[i].id,
              "Order Id": self.data_set[i].order_id,
              "Item name": self.data_set[i].item_name,
              "Order type": self.data_set[i].type,
              "Ordered Qty": self.data_set[i].ordered_qty,
              "Total amount to pay": self.data_set[i].amount_to_pay,
              "Delivery Address": self.data_set[i].delivery_address+","+self.data_set[i].delivery_city+","+self.data_set[i].delivery_state+","+self.data_set[i].delivery_postalcode,
              "Actions":self.data_set[i].id,
              "Item Price":self.data_set[i].item_price,
              "Available Qty":self.data_set[i].available_qty
            })
        }
        this.isBusy = false;
        })
      },

      addNewSurvey () {
        var self = this;
        self.dataid = 0;
        this.$refs.add_order.show()
      },

      pageChange(page) {
        var self = this;
        this.items = [];
        this.isBusy = true,
        this.getdata(page)
      }
    },

    created() {
      if(window.localStorage['userid'] !=undefined){
          var self = this;
          self.created_by = window.localStorage['userid']
          self.getdata(1);
        }
      else{
        this.$router.push('/');
      }
    }
  }

</script>
<style scoped>
.danger {
    background-color: #ef0606d4;
}

.table th, .table td {
    padding: 0.60rem !important;
    vertical-align: top;
    border-top: 1px solid #c8ced3;
}

</style>>
