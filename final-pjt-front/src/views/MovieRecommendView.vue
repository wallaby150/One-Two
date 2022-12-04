<template>
  <div>
    <p class="componentName"
    ><span style="color:red">R</span>ecommend</p>

    <div class="visitedMovies">
      <MovieRecommendCard
        v-for="(movie, idx) in movies"
        :key="idx"
        :movie="movie"
        class="imgDiv d-flex flex-wrap"
      />
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import MovieRecommendCard from '@/components/MovieRecommendCard'

export default {
  name: 'MovieRecommend',

  components: {
    MovieRecommendCard
  },

  data() {
    return {
      movies: null
    }
  },
  computed:{
    isLogin() {
      return this.$store.getters.isLogin
    }
  },
  methods:{
    getRecommend() {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/recommend/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          this.movies = res.data
        })
    }
  },
  created() {
    if (this.isLogin === false) { 
      alert('로그인이 필요한 서비스 입니다.')
      this.$router.push({ name: 'LogInView' })
    } else{
      this.getRecommend()
      this.$store.dispatch('oneOn')
      this.$store.dispatch('twoOff')      
    }     
  }
}
</script>

<style>
.visitedMovies {
  /* width: 80vw; */
  /* height: 40vw; */
  /* display: flex; */
  width: 45vw;
  display: grid;
  grid-template-columns: 3fr 3fr 3fr 3fr 3fr;
  margin-bottom: 3vw;
  margin-top: 3vw;
}

.imgDiv {
  justify-content: flex-start;
  width: 100% !important;
  height: 100% !important;
  /* display:flex; */
  flex-wrap: nowrap !important;
}
.imgDiv > img{
  height:13vw;
  margin-bottom: 1vw;
}

.imgDiv > p{
  width: 100%;
}


</style>