module.exports = {

   apipath: {
      api_ip:"http://localhost:5000",
      api_url_get: "/get?url=",
      api_url_post: "/post?url=",
      api_upload: "/postupload?url=",
      api_url_post_upload: "/upload?url=",

      //user module
      login: "user/login",
      signup:"user/signup_user",

      //orders module
      get_available_orders:"orders/getall_orders",
      save_order:"orders/save_order",
      delete_order:"orders/delete_order",
      get_order_byid:"orders/get_order_byid",

      //User orders module
      confirm_userorder:"user_orders/confirm_userorder",
      getuser_orders:"user_orders/getuser_orders",
      get_orderderdata_byid:"user_orders/get_orderderdata_byid",


  }
 }

