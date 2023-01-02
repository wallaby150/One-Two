<template>
  <div>
    <div v-if="isBest">
      <p class="componentName"
        style="font-size:40px;"
      >
      <span style="color:red">"</span>대단해요!<span style="color:red">"</span></p>
      <p>최고점수를 갱신했어요!</p>
      <p class="componentName"
      >
      최종점수 : <span style="color:red">{{$route.params.score}}</span> 점</p>
      <img src="@/assets/best.gif" alt="" style="margin-left:auto; margin-right:auto">
    </div>
    <div v-if="!isBest">
      <p class="componentName"
        style="font-size:40px;"
      >
      <span style="color:red">"</span>틀렸습니다!<span style="color:red">"</span></p>
      <br>

      <p class="componentName"
      >
      최종점수 : <span style="color:red">{{$route.params.score}}</span> 점</p>
      <video src="@/assets/fail.mp4" loop="" autoplay="" muted="">  
      </video>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'TwoFailView',
  data() {
    return {bestRecord : 0}
  },
  computed:{
    isLogin() {
      return this.$store.getters.isLogin
    },
    userName() {
      return this.$store.state.username
    },
    isBest() {
      return (this.bestRecord <= this.$route.params.score)
    },
  },
  methods: {
    getProfile() {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/accounts/profile/${this.userName}`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
    .then((res) => {
      this.bestRecord = res.data.score
    })
  }},
  created() {
    if (this.isLogin === false) { 
      alert('로그인이 필요한 서비스 입니다.')
      this.$router.push({ name: 'LogInView' })    }     
    this.getProfile()
    this.$store.dispatch('oneOff')
    this.$store.dispatch('twoOn')  
  }
}
</script>

<style>

</style>