<template>
  <div>
    <p class="componentName"
    ><span style="color:red">Two </span>Rank</p>
    <div v-if="rankdata">
      <p class="rank1">1위 : {{ rankdata[0].username }}&nbsp;&nbsp;<span class="rankscore1">{{rankdata[0].score}}</span>점</p>
      <p class="rank2">2위 : {{ rankdata[1].username }}&nbsp;&nbsp;<span class="rankscore2">{{rankdata[1].score}}</span>점</p>
      <p class="rank3">3위 : {{ rankdata[2].username }}&nbsp;&nbsp;<span class="rankscore3">{{rankdata[2].score}}</span>점</p>
      <p class="rank4">4위 : {{ rankdata[3].username }}&nbsp;&nbsp;<span class="rankscore4">{{rankdata[3].score}}</span>점</p>
      <p class="rank5">5위 : {{ rankdata[4].username }}&nbsp;&nbsp;<span class="rankscore5">{{rankdata[4].score}}</span>점</p>
    </div>
    <br>  
    <br>  
    <br>  
    <p class="componentName"
    ><span style="color:red">T</span>otal Rank</p>
    <div v-for="(data,index) in rankdata" :key="index">
      <p>{{index+1}}위 : {{ data.username }} &nbsp;&nbsp;&nbsp;{{data.score}}점</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'TwoRankView',
  data() {
    return {
      rankdata: null
    }  
  },
  computed:{
    isLogin() {
      return this.$store.getters.isLogin
    }
  },
  methods: {
    getRank() {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/two/ranking/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          this.rankdata = res.data
        })
    }
  },
  created() {
    if (this.isLogin === false) { 
      alert('로그인이 필요한 서비스 입니다.')
      this.$router.push({ name: 'LogInView' })
    } else{
      this.getRank()
      this.$store.dispatch('oneOff')
      this.$store.dispatch('twoOn')
    }     
  }
}
</script>

<style>

.rank1 {
  font-size: 48px;
}
.rank2 {
  font-size: 40px;
}
.rank3 {
  font-size: 30px;
}
.rank4 {
  font-size: 25px;
}
.rank5 {
  font-size: 20px;
}

.rankscore1 {
  color: red;
}
.rankscore2 {
  color: rgb(211, 24, 24);
}
.rankscore3 {
  color: rgb(170, 39, 39);
}
.rankscore4 {
  color: rgb(139, 39, 39);
}
.rankscore5 {
  color: rgb(44, 21, 21);
}
</style>