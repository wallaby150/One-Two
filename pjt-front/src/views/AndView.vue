<template>
  <div>
    <p><img src="@/assets/whynot.png" alt="" style="margin: auto; margin-top:300px;"></p>
    <p style="font-size:40px;">- by ggu</p>
    <div style="margin-top:2000px;">
      <p><img src="@/assets/ggu1.png" alt="" style="margin-left:auto; margin-right:auto"></p>
      <p><img src="@/assets/ggu2.png" alt="" style="margin-left:auto; margin-right:auto"></p>
      <p><img src="@/assets/ggu3.png" alt="" style="margin-left:auto; margin-right:auto"></p>
      <p><img src="@/assets/ggu4.png" alt="" style="margin-left:auto; margin-right:auto"></p>
      <p><img src="@/assets/ggu5.png" alt="" style="margin-left:auto; margin-right:auto"></p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AndView',
  data() {
    return {
    }  
  },
  computed:{
    isLogin() {
      return this.$store.getters.isLogin
    }
  },
  methods: {
  },
  created() {
    if (this.isLogin === false) { 
      alert('로그인이 필요한 서비스 입니다.')
      this.$router.push({ name: 'LogInView' })
    } else{
      this.$store.dispatch('oneOff')
      this.$store.dispatch('twoOff')
    }     
  }
}
</script>

<style>
</style>