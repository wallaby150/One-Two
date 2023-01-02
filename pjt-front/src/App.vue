<template>
  <div id="app">
    <div v-if="isLogin">
      <div class="mainNav">     
        <div class="subNav">
          
          <router-link :to=" { name: 'MovieOnelinesView' } ">
            <img src="@/assets/logo.png" id="logo" >
          </router-link>

          <div id="helloNav">
            <router-link :to=" { name: 'MovieSearchView' } ">
              <img id="searchIcon" src="@/assets/mag.png" >
            </router-link>
            <span>
              Hello,
            </span>
            <router-link
              :to=" { name: 'ProfileView', params: { userName: nowUser } } "
              style="text-decoration : none;">
              {{this.nowUser}} 
            </router-link>
            <button
              @click = "logOut"
              class = "logOutButton"
            >
              Logout
            </button>          
          </div>    

          <nav id="oneTwoNav">
            <router-link :to=" { name: 'MovieOnelinesView' } " class="menu">One</router-link>
            <router-link :to=" { name: 'AndView' } " class="menu and"> & </router-link>
            <router-link :to=" { name: 'TwoView' } " class="menu">Two</router-link>
          </nav>

          <div
            v-show = "oneToggle" 
            class="nav-bar"       
          >
            <router-link :to=" { name: 'MovieRecommendView' } " class="menu"> Recommend </router-link>
            <router-link :to=" { name: 'MovieTotalView' } " class="menu"> Total </router-link>
            <router-link :to=" { name: 'ArticlesView' } " class="menu"> Community </router-link>
          </div>
          <div
            v-show="twoToggle"
            class="nav-bar2"
          >
            <router-link :to=" { name: 'TwoView' } " class="menu"> Play </router-link>
            <router-link :to=" { name: 'TwoRankView' } " class="menu"> Ranking </router-link>
          </div>
        </div>
      </div>
      
      <router-view
       style="margin-top: 4rem;"
      />
    </div>
    <div v-if="!isLogin">
        <router-link :to=" { name: 'Main' } ">
          <img src="@/assets/logo.png" style="margin:20px; margin-top:90px;">
        </router-link>        <br>
        <router-link :to=" { name: 'LogInView' } ">
          <button class="mainbutton">LogIn</button>
        </router-link>
        <router-link :to=" { name: 'SignUpView' } ">
          <button class="mainbutton">SignUp</button>
        </router-link>
        <router-view/>
    </div>
  </div>
</template>


<script>
export default {
  name:'App',
  computed:{
    isLogin() {
      return this.$store.getters.isLogin
    },
    nowUser() {
      return this.$store.state.username
    },
    oneToggle() {
      return this.$store.state.oneToggle
    },
    twoToggle() {
      return this.$store.state.twoToggle
    }
  },


  methods: {
    logOut() {
      this.$store.dispatch('logOut')
    }
  },
}  
</script>


<style>
@font-face {
  font-family: 'NanumSquareLight';
  src: url('assets/NanumSquareNeo-aLt.ttf') format('truetype');
}
@font-face {
  font-family: 'NanumSquareRegular';
  src: url('assets/NanumSquareNeo-bRg.ttf') format('truetype');
}
@font-face {
  font-family: 'NanumSquareBald';
  src: url('assets/NanumSquareNeo-cBd.ttf') format('truetype');
}
@font-face {
  font-family: 'NanumSquareExtraBold';
  src: url('assets/NanumSquareNeo-dEb.ttf') format('truetype');
}
@font-face {
  font-family: 'NanumMyeongjo';
  src: url('assets/NanumMyeongjo.ttf') format('truetype');
}
@font-face {
  font-family: 'NanumMyeongjoBold';
  src: url('assets/NanumMyeongjoBold.ttf') format('truetype');
}
@font-face {
  font-family: 'NanumMyeongjoExtraBold';
  src: url('assets/NanumMyeongjoExtraBold.ttf') format('truetype');
}

   
#app {
  font-family: "NanumSquareRegular";
  /* font-family: Avenir, Helvetica, Arial, sans-serif; */
  text-align: center;
  color: black;

}

nav {
  /* display: flex; */
  justify-content: end;
  font-size: 40px
}

nav a {
  color: black;
  padding-right: 0.8rem
}

nav a.router-link-exact-active {
  /* color:  ; */
}
nav a.router-link-active {
  color: #F20505;
}

#logo {
  width: 14rem;
  /* float: left; */
  /* position: relative; */
  position: absolute;
  /* margin-left : auto; */
  margin-top : 25px;
  left: 200px;
  top: 20px
  /* text-align: start !important; */
  /* margin-left: 20px;
  margin-top: 20px;
  margin-right: 20px;
  margin-bottom: 10px; */
}

#searchIcon {
  width: 1.4rem;
  margin-right: 5px;
  /* float:none;
  margin-left: 20px;
  margin-top: 20px;
  margin-right: 20px;
  margin-bottom: 10px;
  position: absolute; */
}

.mainbutton {
  background-color: #F20505;
  color: white;
  /* color: blACK; */
  border: 0px;
  margin : 10px;
  padding : 10px;
  font-size: 20px;
  border-radius: 5px;
}

.logOutButton{
  background-color: #F20505;
  color: white;
  /* color: blACK; */
  border: 0px;
  border-radius: 5px;
}

.account {
  /* display: flex; */
  /* justify-content: end; */
  /* margin-left: auto; */
  /* float:right; */
}

.menu {
  text-decoration : none;
}

#helloNav {
  position: absolute;
  right: 220px;
  /* top: 3%; */
  top: 60px;
}

#oneTwoNav {
  position: absolute;
  right:200px;
  top: 85px;
}

#mainNav {
  /* margin-bottom: 10px; */
  
  height: 10%;
}

.nav-bar{
  display: flex;
  justify-content: right;
  margin-right: 310px;
  margin-top: 120px ;
  color: black;
}

.nav-bar > a {
  color: gray;
}
.nav-bar2{
  display: flex;
  justify-content: right;
  margin-right: 215px;
  margin-top: 120px ;
  color: black;
}
.nav-bar2 > a {
  color: gray;
}

a {
  margin-left: 5px;
  margin-right: 5px;
}

.and:hover {
  cursor:default;
  color: black;
}

</style>
