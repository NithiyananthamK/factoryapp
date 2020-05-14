<template>
  <div class="maincontainer">
    <div>
      <b-modal id="add_data" style="top: -15px;" size="lg" ref="change_orderstatus" centered
        title="Change order status" hide-footer>
        <change_orderstatus :dataid="dataid"></change_orderstatus>
      </b-modal>
    </div>

    <h4> Available Orders </h4>

    <div class="titleline"></div>

    <button @click="addNewSurvey()" type="button" class="v-btn v-btn--contained theme--light v-size--default"
      style="background: rgb(0, 161, 241); color: white;margin-left: 87%;margin-bottom: 1%;margin-top:3%;">
      <span class="v-btn__content">ADD ORDER</span>
    </button>

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

            <template v-slot:cell(Status)="{ value }">
              <span
                :style="`border-radius: 7px; font-size: 12px; padding: 5px;background: ${getColor(value)};color: white`">
                {{ getText(value) }}</span>
            </template>

            <template v-slot:cell(Actions)="{ item }">
              <b-button v-if="item['Status'] != 4" size="sm" variant="outline-dark" @click="change_status(item['Id'])">CHANGE STATUS</b-button>
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
import change_orderstatus from './change_orderstatus'
import Vue from 'vue'
import VueSwal from 'vue-swal'
  export default {
    data() {
      return {
        isAdd:false,
        dataid:"",
        fields:['Order Id', 'Ordered user name', 'Item name', 'Order type', 'Ordered Qty', 'Total amount to pay', 'Status', 'Actions'],
        items: [],
        isBusy:true,
        currentPage:1,
        perPage:10,
        totalcount:0,
        data_set:[],
      }
  },

  components:{
    change_orderstatus:change_orderstatus
  },

  mounted() {
    this.getdata(1);
  },

  methods: {

    change_status(id){
      var self = this;
      self.dataid = id;
      this.$refs.change_orderstatus.show();
    },

    closepopup(){
       var self = this;
       this.$refs.change_orderstatus.hide();
    },

    getColor(status) {
      switch(status){
        case 1:
          return 'rgba(249, 9, 9, 0.76)'
          break;
        case 2:
          return 'rgb(249, 164, 9)'
          break;
        case 3:
          return 'rgb(9, 94, 249)'
          break;
        case 4:
          return '#0cad44'
          break;
        case 5:
          return '#293848'
          break;

      }
    },

    getText(status) {
      switch(status){
        case 1:
          return 'Ordered'
          break;
        case 2:
          return 'Packed'
          break;
        case 3:
          return 'Dispatched'
          break;
        case 4:
          return 'Delivered'
          break;
        case 5:
          return 'Returned'
          break;
      }
    },

      updatedata(){
        //this.items=[]
        //this.getdata(this.page );
      },

      edit_data(id){
        var self = this;
        self.dataid = id;
        this.$refs.add_order.show()
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
        this.axios.get(this.appConfig.api_url_get + this.appConfig.get_alluser_orders +'/'+ page+'/10').then((data) => {
          self.items = [];
          self.data_set = data.data.data
          this.totalcount = data.data.total_count
          for(var i=0;i<self.data_set.length;i++){
            self.items.push({
              "Id": self.data_set[i].id,
              "Order Id": self.data_set[i].order_id,
              "Ordered user name":self.data_set[i].ordered_user_name,
              "Item name": self.data_set[i].item_name,
              "Order type": self.data_set[i].type,
              "Ordered Qty": self.data_set[i].ordered_qty,
              "Total amount to pay": self.data_set[i].amount_to_pay,
              "Status": self.data_set[i].order_status,
              "Actions":self.data_set[i].id,
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
