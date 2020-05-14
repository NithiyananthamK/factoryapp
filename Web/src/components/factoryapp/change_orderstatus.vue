<template>
    <div style="background: #E7F0F4;">
         <b-form-radio-group
            v-model="selected_status"
            :options="options"
            class="mb-3"
            value-field="item"
            text-field="name"
            disabled-field="notEnabled"
          ></b-form-radio-group>

          <div class="col-sm-12">
                <div class="float-right">
                     <!-- <div type="button" class="btn" @click="save_alertmgmt()"> Save </div> -->
                      <b-button variant="outline-secondary" disabled v-if="showLoader">
                                  <b-spinner small type="grow"></b-spinner>
                                    Loading...
                                  </b-button>
                     <b-button  variant="outline-primary"  v-if="!showLoader" @click = "save_status">Save</b-button>
                 </div>
            </div>
    </div>
</template>

<script>

import Vue from 'vue';

import Swal from 'vue-sweetalert2';

Vue.use(Swal)


export default {
  name: 'DefaultContainer',
  components: {

  },
  data () {
    return {
      props: ['dataid'],
      activation_url:"",
      collectionname:"",
      entityname:"",
      showLoader:false,
      id:0,
      selected_status: '2',
      options: [
        { item: '2', name: 'Packed' },
        { item: '3', name: 'Dispatched' },
        { item: '4', name: 'Delivered' },
        { item: '5', name: 'Returned' }
      ]
    }
  },
  computed: {

  },

  methods:{
    save_status(){
			try{
            this.showLoader=true;
            var path=this.appConfig.api_url_post+this.appConfig.update_order_status;
            const payload={
              "id":this.dataid,
              "status":this.selected_status,
            }
            this.axios.post(path,payload)
            .then((res) => {
              if(res.data.Errorcode==9999){
                  this.showLoader=false;
                  swal({
                      title: "Order status updated successfully",
                      icon: "success",
                      timer: 2000,
                      showConfirmButton: false
                    });
                  this.$parent.$options.parent.$parent.closepopup()
                  this.$parent.$options.parent.$parent.getdata(1)
              }
              else{
                swal({
                      title: "Order status update failed",
                      icon: "danger",
                      timer: 2000,
                      showConfirmButton: false
                    });
                   this.$root.$emit('bv::hide::modal', self.modal)
              }
              this.showLoader=false;
            })
          }
          catch (e) {
            console.log(e)
          }
		  },
  },

  mounted(){
    document.getElementById("maindiv").style.height=window.innerHeight+"px";
  },

  created(){
    if(this.$attrs.dataid != undefined){
          this.dataid=this.$attrs.dataid;
    }
    else{
        this.id = 0;
				this.email="";
				this.mblenumber="";
    }
  }
}

</script>
<style>
.modal-title{
  font-weight: bold;
}
#alertadd___BV_modal_content_{
  background: #E7F0F4;
}
 .dropdowns{
          border: 1px solid #E8DCD4;
          padding: 10px;
          border-radius: 5px;
          width:100%;
          color:#2f353ad1;
          background: white;
   }
</style>


