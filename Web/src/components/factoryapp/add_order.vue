<template>
  <div style="background: #E7F0F4;min-height:100%">
    <div class="row">
      <div class="col-sm-4">
        <label class="float-left;" style="margin-bottom: 3px;">Order type<label style="color:red">*</label></label>
        <b-form-select v-if="dataid==0"
          v-model="selectedCategory"
          :options="category"
          class="mb-3"
          value-field="value"
          text-field="category"
          disabled-field="notEnabled">

          <template v-slot:first>
            <b-form-select-option :value="null" disabled>-- Please select an item --</b-form-select-option>
          </template>
        </b-form-select>

        <b-form-select v-if="dataid!=0" disabled
          v-model="selectedCategory"
          :options="category"
          class="mb-3"
          value-field="value"
          text-field="category"
          disabled-field="notEnabled">

          <template v-slot:first>
            <b-form-select-option :value="null" disabled>-- Please select an item --</b-form-select-option>
          </template>
        </b-form-select>

      </div>

      <div class="col-sm-4" v-if="dataid==0">
        <label class="float-left" style="margin-bottom: 3px;">Item name<label style="color:red">*</label></label>
        <b-form-input v-model="item_name" placeholder="Enter item name"></b-form-input>
      </div>

      <div class="col-sm-4" v-if="dataid!=0">
        <label class="float-left" style="margin-bottom: 3px;">Item name<label style="color:red">*</label></label>
        <b-form-input disabled v-model="item_name" placeholder="Enter item name"></b-form-input>
      </div>

      <div class="col-sm-4">
        <label class="float-left" style="margin-bottom: 3px;">Item description</label>
        <b-form-input v-model="item_desc" placeholder="Enter item description"></b-form-input>
      </div>
    </div>

    <div class="row">
      <div class="col-sm-4">
        <label class="float-left" style="margin-bottom: 3px;">Stock qty<label style="color:red">*</label></label>
        <b-form-input v-model="stock_qty" placeholder="Enter stock qty"></b-form-input>
      </div>

      <div class="col-sm-4">
        <label class="float-left" style="margin-bottom: 3px;">Item price<label style="color:red">*</label></label>
        <b-form-input v-model="item_price" placeholder="Enter price"></b-form-input>
      </div>

    </div>



    <div class="col-sm-12 text-end" v-if="isBusy">
      <v-btn class="float-right" disabled style="background: #00a1f1;color:white;margin-top: -10px;">Save</v-btn>
    </div>

    <div class="col-sm-12 text-end" v-if="!isBusy">
      <v-btn class="float-right" style="background: #00a1f1;color:white;margin-top:-10px" @click="save_order">Save</v-btn>
    </div>

  </div>
</template>

<script>
import Multiselect from 'vue-multiselect'
  export default {
    props: ['dataid'],
    components: {
      Multiselect
    },

    data: () => ({
      dataid: "",
      id:0,
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
      item_name:"",
      item_desc:"",
      item_price:"",
      stock_qty:"",
    }),

    created() {
      try {
        var self = this;
        self.dataid = this.dataid;
        if (this.dataid != "") {
          this.isBusy = false;
          this.getdatabyid(self.dataid);
        }
      } catch (e) {
        console.log(e)
      }
    },


    methods: {

      hidepopup() {
        this.$refs.showxml.hide()
      },

      getdatabyid(id) {
        var self = this;
        this.axios.get(this.appConfig.api_url_get + this.appConfig.get_order_byid + '/' + id).then((data) => {
          if (data.data.Errorcode == '9998') {
            this.$root.$emit('bv::hide::modal', self.modal)
          } else {
            self.id = id;
            self.selectedCategory = data.data.type;
            self.stock_qty = data.data.available_qty;
            self.item_price = data.data.single_qty_price;
            self.item_name = data.data.item_name;
            self.item_desc = data.data.item_description;
          }
        })

      },

      save_order() {
        var self = this;
        self.modal = "add_data";
        if (this.selectedCategory == null) {
          swal({
            title: "Select Item Category",
            icon: "warning",
            timer: 2000,
            showConfirmButton: false
          });
        } else if (this.stock_qty == "") {
          swal({
            title: "Enter Item Stock Qty",
            icon: "warning",
            timer: 2000,
            showConfirmButton: false
          });
        } else if (this.item_price == "") {
          swal({
            title: "Enter Item price",
            icon: "warning",
            timer: 2000,
            showConfirmButton: false
          });
        } else if (this.item_name == "") {
          swal({
            title: "Enter item Name",
            icon: "warning",
            timer: 2000,
            showConfirmButton: false
          });
        } else {
          const path = this.appConfig.api_url_post + this.appConfig.save_order
          let payload = {
            "id": this.id,
            "item_type": this.selectedCategory,
            "item_name": this.item_name,
            "item_desc": this.item_desc,
            "item_price": this.item_price,
            "stock_qty": this.stock_qty,
            "created_by":parseInt(window.localStorage['userid'])
          }

          this.axios.post(path, payload).then((res) => {
            if (res.data.Errorcode == 9999) {
              swal({
                title: "Saved Successfully",
                icon: "success",
                timer: 2000,
                showConfirmButton: false
              });
              this.$root.$emit('bv::hide::modal', self.modal)
              this.$parent.$options.parent.$parent.getdata(1)
            }
             else if (res.data.Errorcode == 999) {
              swal({
                title: "Updated Successfully",
                icon: "success",
                timer: 2000,
                showConfirmButton: false
              });
              this.$root.$emit('bv::hide::modal', self.modal)
              this.$parent.$options.parent.$parent.getdata(1)
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
