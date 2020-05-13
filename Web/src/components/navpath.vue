<template>
  <b-breadcrumb :items="items" ref = "pathRef" style="background-color:#f6f7f9"></b-breadcrumb>
</template>

<script>

import Vue from 'vue'

export default {
   props: ['pathData'],
data() {
try{
      return {
        items: [

        ]
      }
}
    catch (e) {
       console.log(e)
     }
    },
components: {

},
methods: {
    
},
created()
{
try{
  var self = this;
  self.items = [];
  self.items=this.pathData;
}
    catch (e) {
       console.log(e)
     }
}
};
</script>
