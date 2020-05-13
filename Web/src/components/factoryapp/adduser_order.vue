<template>
  <div style="background: #E7F0F4;min-height:100%">
    <div class="row">

      <div class="col-sm-4">
        <label class="float-left" style="margin-bottom: 3px;">Order Qty<label style="color:red">*</label></label>
        <b-form-input v-model="order_qty" placeholder="Enter order qty" v-on:keyup="calculate_totalamt(order_qty)"></b-form-input>
      </div>

      <div class="col-sm-4">
        <label class="float-left" style="margin-bottom: 3px;">Delivery Address<label style="color:red">*</label></label>
        <b-form-input v-model="del_address" placeholder="Enter Address"></b-form-input>
      </div>

      <div class="col-sm-4">
        <label class="float-left" style="margin-bottom: 3px;">Delivery city<label style="color:red">*</label></label>
        <b-form-input v-model="del_city" placeholder="Enter City"></b-form-input>
      </div>
    </div>

    <div class="row">


      <div class="col-sm-4">
        <label class="float-left" style="margin-bottom: 3px;">Delivery state<label style="color:red">*</label></label>
        <b-form-input v-model="del_state" placeholder="Enter State"></b-form-input>
      </div>

      <div class="col-sm-4">
        <label class="float-left" style="margin-bottom: 3px;">Delivery Zipcode<label style="color:red">*</label></label>
        <b-form-input v-model="del_zipcode" placeholder="Enter Zipcode"></b-form-input>
      </div>

    </div>

    <div class="col-sm-12 text-end" >
      <span><b>STOCK : {{available_qty}}</b></span>
    </div>

    <div class="col-sm-12 text-end" >
      <span><b>TOTAL AMOUNT TO PAY : {{total_amounttopay}}</b></span>
    </div>

    <div class="col-sm-12 text-end" v-if="isBusy">
      <v-btn class="float-right" disabled style="background: #00a1f1;color:white;margin-top: -10px;">buynow</v-btn>
    </div>

    <div class="col-sm-12 text-end" v-if="!isBusy">
      <v-btn class="float-right" style="cursor:pointer;background: #00a1f1;color:white;margin-top:-10px" @click="save_order">buynow</v-btn>
    </div>

  </div>
</template>

<script>
import Multiselect from 'vue-multiselect'
  export default {
    props: ['selected_order'],
    components: {
      Multiselect
    },

    data: () => ({
      selected_id:"",
      selected_order_id: "",
      selected_item_price:"",
      available_qty:"",
      selectedCategory: null,
      category: [
        {
          "category": "Food",
          "value": "Food"
        },
        {
          "category": "Ingredients",
          "value": "Ingredients"
        }
      ],
      order_qty:"",
      del_address:"",
      del_city:"",
      del_state:"",
      del_zipcode:"",
      total_amounttopay:"0.0",
      isBusy:false,
    }),

    created() {
      try {
        var self = this;
        self.selected_id = this.selected_order.id;
        self.selected_order_id = this.selected_order.order_id;
        self.selected_item_price = parseFloat(this.selected_order.item_price);
        self.available_qty = this.selected_order.available_qty
        if (this.selected_id != 0) {
          self.isBusy = false;
          self.getdatabyid(self.selected_id)
        }
      } catch (e) {
        console.log(e)
      }
    },

    mounted(){

    },

    methods: {
      calculate_totalamt(qty){
        var self = this;
        if(qty == ""){
          qty = 0;
        }
        self.total_amounttopay = parseFloat(parseFloat(qty) * parseFloat(self.selected_item_price)).toFixed(1);
      },

      hidepopup() {
        this.$refs.showxml.hide()
      },

      getdatabyid(id) {
        var self = this;
        this.axios.get(this.appConfig.api_url_get + this.appConfig.get_orderderdata_byid + '/' + id).then((data) => {
            this.selected_order_id = data.data.order_id;
            this.order_qty = data.data.ordered_qty;
            this.del_address = data.data.delivery_address;
            this.del_city = data.data.delivery_city;
            this.del_state = data.data.delivery_state;
            this.del_zipcode = data.data.delivery_postalcode;
            self.calculate_totalamt(data.data.ordered_qty);
        })

      },

      save_order() {
        var self = this;
        self.modal = "add_data";
        if (this.order_qty == "") {
          swal({
            title: "Enter order Qty",
            icon: "warning",
            timer: 2000,
            showConfirmButton: false
          });
        } else if (this.del_address == "") {
          swal({
            title: "Enter Delivery address",
            icon: "warning",
            timer: 2000,
            showConfirmButton: false
          });
        } else if (this.del_city == "") {
          swal({
            title: "Enter Delivery City",
            icon: "warning",
            timer: 2000,
            showConfirmButton: false
          });
        } else if (this.del_state == "") {
          swal({
            title: "Enter Delivery State",
            icon: "warning",
            timer: 2000,
            showConfirmButton: false
          });
        }
        else if (this.del_zipcode == "") {
          swal({
            title: "Enter Delivery Zipcode",
            icon: "warning",
            timer: 2000,
            showConfirmButton: false
          });
        }
        else if (this.order_qty > this.available_qty || this.order_qty == 0) {
          swal({
            title: "Please Enter the qty below Available Qty",
            icon: "warning",
            timer: 2000,
            showConfirmButton: false
          });
        }else {
          self.isBusy = true;
          const path = this.appConfig.api_url_post + this.appConfig.confirm_userorder
          let payload = {
            "id":parseInt(this.selected_id),
            "order_id": this.selected_order_id,
            "order_qty": this.order_qty,
            "item_price":this.selected_item_price,
            "created_by":parseInt(window.localStorage['userid']),
            "del_address":this.del_address,
            "del_city":this.del_city,
            "del_state":this.del_state,
            "del_zipcode":this.del_zipcode,
          }

          this.axios.post(path, payload).then((res) => {
            if (res.data.Errorcode == 9999) {
              swal({
                title: "Saved Successfully",
                icon: "success",
                timer: 2000,
                showConfirmButton: false
              });
              self.isBusy = false;
              this.$root.$emit('bv::hide::modal', self.modal)
              this.$parent.$options.parent.$parent.closepopup()
            }
          })
        }
      },
    },
  }
</script>

<style>
 .dropdowns{
          border: 1px solid #E8DCD4;
          padding: 10px;
          border-radius: 5px;
          width:100%;
          color:#2f353ad1;
          background: white;
   }
   .resumable-drop,.supportresumable-drop{
    border: 2px dashed #E8DCD4;
}
.resumable-drop:hover,.supportresumable-drop:hover {
    border: 2px dashed rgb(184, 174, 169);
}
.uploadbtn{
   background-color: #7CB342 !important;
   color: white !important;
}
.progressdiv{
    padding: 0px 12px;
}
.modal-title{
  font-weight: bold;
}
#add_data___BV_modal_content_{
  background: #E7F0F4;
}
</style>
