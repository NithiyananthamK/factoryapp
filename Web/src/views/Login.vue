<template>
  <div class="app align-items-center">
    <div class="container-fluid banner-bg">
      <div class="container">
        <div class="row h-100" style="margin-top: 100px;">
          <div class="col-md-5">
            <div class="d-flex flex-column align-items-center justify-content-center h-100">
              <img src="./../../public/food_factory.png" style="width:100%">
              <div class="bannerline mt-3"></div>
              <div class="mt-3 w-100">

                <div class="bannerlogotxt">
                  <div>F</div>
                  <div>O</div>
                  <div>O</div>
                  <div>D</div>
                  <div>F</div>
                  <div>A</div>
                  <div>C</div>
                  <div>T</div>
                  <div>O</div>
                  <div>R</div>
                  <div>Y</div>

                </div>
              </div>
            </div>
          </div>
          <div class="col-md-7">
            <div class="d-flex align-items-center justify-content-center h-100">
              <b-row class="justify-content-end">
                <b-col md="7">
                  <b-card-group class="loginbg">
                    <b-card no-body class="">
                      <b-card-body>
                        <b-form v-if="!show_signup">
                          <div style="text-align: center">
                            <h1>LOGIN</h1>
                          </div>
                          <hr style="width:100%;text-align:left;margin-left:0">
                          <!-- <p class="text-muted">Sign In to your account</p> -->
                          <b-input-group class="mb-3">
                            <b-input-group-prepend>
                              <b-input-group-text><i class="icon-user"></i></b-input-group-text>
                            </b-input-group-prepend>
                            <b-form-input type="text" class="form-control" placeholder="Username"
                              autocomplete="username email" @keyup.enter="login_user" v-model="userName" />
                          </b-input-group>
                          <b-input-group class="mb-3">
                            <b-input-group-prepend>
                              <b-input-group-text><i class="icon-lock"></i></b-input-group-text>
                            </b-input-group-prepend>
                            <b-form-input type="password" class="form-control" placeholder="Password"
                              autocomplete="current-password" @keyup.enter="login_user" v-model="password" />
                          </b-input-group>
                          <b-row>
                            <b-col cols="6" v-if="showloading">
                              <b-button variant="primary" disabled>
                                <b-spinner small type="grow"></b-spinner>
                                Loading...
                              </b-button>
                            </b-col>
                          </b-row>
                            <!-- <b-row>
                              <b-col cols="12" class="p-0 text-right">
                                <p class="m-0 px-4">forgot password ?</p>
                              </b-col>
                            </b-row> -->
                          <b-row>
                            <b-col cols="12" v-if="!showloading">
                              <b-button style="background: #4472c4;width: 100%;color: white !important;border: 0px solid #0CC0C0;border-bottom: 4px solid #2855a4;border-radius: 7px;height: 45px;"
                                @click="login_user">Login</b-button>
                            </b-col>
                          </b-row>

                          <b-row>
                            <b-col cols="4"></b-col>
                            <b-col cols="4">
                              <b-button size="sm" style="background: #4472c4;width: 100%;color: white !important;border: 0px solid #0CC0C0;border-bottom: 4px solid #2855a4;border-radius: 7px;"
                                @click="signup()">Sign up</b-button>
                            </b-col>
                            <b-col cols="4"></b-col>
                          </b-row>

                          <!-- <div class="clr5"></div> -->
                          <!-- <b-row> -->
                          <!-- <b-col cols="12"> -->
                          <span v-show="isinvalid" class="text-danger">You have entered an invalid username or password.
                            Please
                            enter the correct credentials again.</span>
                          <!-- </b-col> -->
                          <!-- </b-row> -->
                        </b-form>


                        <b-form v-if="show_signup">
                          <div style="text-align: center">
                            <h1>SIGN UP</h1>
                          </div>
                          <hr style="width:100%;text-align:left;margin-left:0">

                          <b-input-group class="mb-3">
                            <b-input-group-prepend>
                              <b-input-group-text><i class="icon-user"></i></b-input-group-text>
                            </b-input-group-prepend>
                            <b-form-input type="text" class="form-control" placeholder="Name"
                               @keyup.enter="login_user" v-model="name" />
                          </b-input-group>

                          <b-input-group class="mb-3">
                            <b-input-group-prepend>
                              <b-input-group-text><i class="icon-user"></i></b-input-group-text>
                            </b-input-group-prepend>
                            <b-form-input type="text" class="form-control" placeholder="Email"
                                v-model="email" />
                          </b-input-group>

                          <b-input-group class="mb-3">
                            <b-input-group-prepend>
                              <b-input-group-text><i class="icon-lock"></i></b-input-group-text>
                            </b-input-group-prepend>
                            <b-form-input type="password" class="form-control" placeholder="Create Password"
                               v-model="crtpassword" />
                          </b-input-group>

                          <b-input-group class="mb-3">
                            <b-input-group-prepend>
                              <b-input-group-text><i class="icon-lock"></i></b-input-group-text>
                            </b-input-group-prepend>
                            <b-form-input type="password" class="form-control" placeholder="Confirm Password"
                               v-model="cnfmpassword" />
                          </b-input-group>

                          <b-form-radio-group style="display: flex; justify-content: center;"
                            v-model="selected_role"
                            :options="options"
                            class="mb-3"
                            value-field="item"
                            text-field="name"
                          ></b-form-radio-group>

                          <b-row>
                            <b-col cols="6" v-if="showloading">
                              <b-button variant="primary" disabled>
                                <b-spinner small type="grow"></b-spinner>
                                Loading...
                              </b-button>
                            </b-col>
                          </b-row>

                          <b-row>
                            <b-col cols="12" v-if="!showloading">
                              <b-button style="background: #4472c4;width: 100%;color: white !important;border: 0px solid #0CC0C0;border-bottom: 4px solid #2855a4;border-radius: 7px;height: 45px;"
                                @click="signup_user()">Sign up</b-button>
                            </b-col>
                          </b-row>

                          <b-row>
                            <b-col cols="3"></b-col>
                            <b-col cols="6">
                              <b-button size="sm" style="background: #4472c4;width: 100%;color: white !important;border: 0px solid #0CC0C0;border-bottom: 4px solid #2855a4;border-radius: 7px;"
                                @click="gotologin()">Back to login</b-button>
                            </b-col>
                            <b-col cols="3SSSS"></b-col>
                          </b-row>

                          <!-- <div class="clr5"></div> -->
                          <!-- <b-row> -->
                          <!-- <b-col cols="12"> -->
                          <span v-show="isinvalid" class="text-danger">You have entered an invalid username or password.
                            Please
                            enter the correct credentials again.</span>
                          <!-- </b-col> -->
                          <!-- </b-row> -->
                        </b-form>



                      </b-card-body>
                    </b-card>
                  </b-card-group>
                </b-col>
              </b-row>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Vue from 'vue';
 import Swal from 'vue-sweetalert2';
 Vue.use(Swal)

export default {
  name: 'Login',
  data(){
    return {
      userName:"",
      password:"",
      isinvalid:0,
      showloading:false,
      slide: 0,
      sliding: null,
      show_signup:false,
      selected_role: 'Admin',
        options: [
          { item: 'Admin', name: 'Admin' },
          { item: 'User', name: 'User' },
        ],
      crtpassword:"",
      cnfmpassword:"",
      email:"",
      name:""
    }
  },
  methods:{
    authenticateUser(){

    },

    signup(){
      var self = this;
      self.show_signup = true;

    },

    gotologin(){
      var self = this;
      self.show_signup = false;
    },

    signup_user(){
      var self = this;
      if(self.crtpassword != self.cnfmpassword){
        swal({
                title: "Password and Confirm password doesn't match",
                icon: "warning",
                timer: 2000,
                showConfirmButton: false
              });
      }
      else{
        self.showloading = true;
        const path = this.appConfig.api_url_post + this.appConfig.signup;
            let payload = {
              "name":self.name,
              "email": self.email,
              "password": self.crtpassword,
              "role": self.selected_role
            }
            this.axios.post(path, payload).then((res) => {
              if (res.data.Errorcode == 9999) {
                self.showloading = false;
                swal({
                  title: "Successfully Registered",
                  icon: "success",
                  timer: 2000,
                  showConfirmButton: false
                });
                self.showloading = false;
                self.show_signup = false;
              }
              else{
                swal({
                  title: "Registration failed",
                  icon: "danger",
                  timer: 2000,
                  showConfirmButton: false
                });
              }
            })
          }
    },

    login_user(){
      var self =this;
      this.isinvalid=0;
      self.showloading = true;
      const path = this.appConfig.api_url_post + this.appConfig.login;
          let payload = {
            "email": self.userName,
            "password": self.password,
          }
          this.axios.post(path, payload).then((res) => {
            if (res.data.Errorcode == 9999) {
              self.showloading = false;
              window.localStorage.setItem('islogedin',1);
              window.localStorage.setItem('userid',res.data.user_id);
              window.localStorage.setItem('user_role',res.data.user_role);
              self.$router.push('/home');
            }
            else{
              self.showloading = false;
              this.isinvalid=1;
            }
          })
    },
     onSlideStart(slide) {
        this.sliding = true
      },
      onSlideEnd(slide) {
        this.sliding = false
      },
    InsightFullpopup() {
      this.$swal({
        title: '<strong>Insightful BI</strong>',
        html: '<div>'+
                '<div class="row">'+
                  '<div class="col-md-6" style="cursor: pointer;">'+
                      '<a href="http://10.251.48.105:5601/app/maps#/map/f00b66b0-8d5f-11ea-92fb-193614c3d112" target="_blank"><div class="d-flex align-items-center insightdiv"><img src="./../../static/insight1.png" style="width:95%;"/></div></a>'+
                  '</div>'+
                   '<div class="col-md-6" style="cursor: pointer;">'+
                      '<a href="/#/mstr" target="_blank"><div class="d-flex align-items-center insightdiv"><img src="./../../static/insight2.png" style="width:95%;"/></div></a>'+
                  '</div>'+
                '</div>'+
              '</div>',
        showCloseButton: true,
        showCancelButton: false,
        showConfirmButton: false
      });
    }
    },
  created() {
		if(localStorage.islogedin ==1){
      this.$router.push('/home')
    }
	},
}
</script>

<style>
.btn{
      color: black !important;
   }
.aligncard{
  padding: 0px;
}
.bulletHeader{
  color:#5615a7;
  font-size: 16pt;
  font-weight: 600;
}
.blueline{
  background-color:#5615a7;
  width:100%;
  height:2px;
}
.greyline{
  background-color:grey;
  width:95%;
  height:2px;
  margin: 0 20px;
}
.bulletimg{
  height:80px;
}
.bulletcontainer{
  background-color: #fff;
}
.greytext{
  color:grey !important;
}
.bluetext{
  color: #010080 !important;
}
.bcalender{
  width:100px;
  font-size: 8pt;
  float: right;
}
.btitle{
  width: calc(100% - 100px);
  text-transform: uppercase;
}
.bbody p{
    display: block;
    display: -webkit-box;
    max-width: 100%;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;
    overflow: hidden;
    text-overflow: ellipsis;
}
.bluebtn{
  color:#fff;
  display: inline;
  float:right;
  background-color: #010080;
  font-size: 11pt;
  font-weight: 600;
  padding: 5px 20px;
}
.footerlist li{
  color: #fff;
  margin: 5px;
  font-weight: 600;
  list-style: none;
}
.footerContactus{
color: #fff;
font-weight: 600;
}
.address{
  font-size: 9pt;
}
.footerbg{
background-image:url("./../../public/footer-bg.png");
background-repeat:repeat-x;
height:100%
}
.banner-bg{
  background-image: url("./../../public/banner-bg.png");
  min-height: 100%;
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  position: relative;
}
.bannerline{
  background-color:#494544;
  width:100%;
  height:2px;
}
.bannerlogotxt{
  color:#494544;
  width: 100%;
  text-align: center;
  display: flex;
  flex-flow: row nowrap;
  justify-content: space-between;
  font-weight: 600;
  font-size: 19pt;
}
.midcardtxt{
  color: rgb(5, 5, 131);
  font-size: 10pt;
  font-weight: 600;
}
.aligncard .card-body{
  display: flex;
  align-items: center;
  justify-content: center;
}
.loginbg{
  background-image:url('./../../public/login-bg.png');
  background-repeat: repeat;
  background-size: 100% auto
}
.loginbg .card{
  background-color: transparent;
  border: 1px solid #5f6e90;
  border-radius: 0;
}
.insightdiv{
  border: 2px solid grey;
  padding: 1rem;
}
</style>
