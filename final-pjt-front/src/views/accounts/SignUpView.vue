<template>
  <div>
    <h1 style="margin:20px;">SignUp</h1>

    <div class="formdiv">
      <form @submit.prevent="signUp">
        <div class="mb-3">
          <label for="username" class="form-label">Username :</label>
          <input type="text" class="form-control" id="username" v-model="username">
        </div>
        <div class="mb-3">
          <label for="password1" class="form-label">Password : </label>
          <input type="password" class="form-control" id="password1" v-model="password1">
        </div>
        <div class="mb-3">
          <label for="password2" class="form-label">Password confirmation : </label>
          <input type="password" class="form-control" id="password2" v-model="password2">
        </div>
        <div align="right">
          <button type="submit" class="submitbutton">SignUp</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SignUpView',
  computed:{
    isLogin() {
      return this.$store.getters.isLogin
    }
  },
  data() {
    return {
      username: null,
      password1: null,
      password2: null,
    }
  },
  methods: {
    signUp() {
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2

      const payload = {
        username: username,
        password1: password1,
        password2: password2,
      }

      this.$store.dispatch('signUp', payload)

    }
  },
  created() {
    if (this.isLogin === true) { 
      this.$router.push({ name: 'MovieView'})
    }     
    this.$store.dispatch('oneOff')
    this.$store.dispatch('twoOff')  
  }
}
</script>

<style>
  .formdiv {
    width: 30vw;
    text-align: start;
    border: red solid 1px;
    padding: 10px;
    border-radius: 8px;
    margin-left: auto;
    margin-right: auto;
  }
  .submitbutton {
    padding: 7px;
    border: red solid 1px;
    border-radius: 8px;
    background: white;
    position: relative;
  }
</style>