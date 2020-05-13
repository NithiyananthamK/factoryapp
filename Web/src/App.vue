<template>
  <router-view></router-view>
</template>

<script>
export default {
  name: 'app'
}
</script>

<style lang="scss">
  @import 'assets/scss/style';
  $fa-font-path: '~font-awesome/fonts/';
   $simple-line-font-path: '~simple-line-icons/fonts/';
   .modal-backdrop{
    opacity: .5;
  }
</style>
