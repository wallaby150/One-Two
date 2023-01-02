<template>
  <div>
    <h1 style="margin:20px">LogIn</h1>

    <div class="formdiv">
      <form @submit.prevent="logIn">
        <div class="mb-3">
          <label for="username" class="form-label">Username :</label>
          <input type="text" class="form-control" id="username" v-model="username">
        </div>
        <div class="mb-3">
          <label for="password" class="form-label">Password : </label>
          <input type="password" class="form-control" id="password" v-model="password">
        </div>
        <div align="right">
          <button type="submit" class="submitbutton">LogIn</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: 'LogInView',
  data() {
    return {
      username: null,
      password: null,
    }
  },
  computed:{
    isLogin() {
      return this.$store.getters.isLogin
    }
  },
  methods: {
    logIn() {
      const username = this.username
      const password = this.password

      const payload = {
        username: username,
        password: password,
      }
      this.$store.dispatch('logIn', payload)
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
