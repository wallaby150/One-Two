<template>
  <div>
    <p class="componentName"
    ><span style="color:red">T</span>otal Movies</p>
    <b-card-group
    class="card border-0">
    <MovieCard
      v-for="movie in randomMovies"
      :key="movie.id"
      :movie="movie"
    />
    </b-card-group>
  </div>
</template>

<script>
// import axios from 'axios'
import _ from 'lodash'
import MovieCard from '@/components/MovieCard'

export default {
  name: 'MovieTotalView',
  components: {
    MovieCard
  },
  data() {
    return {
      movies: null,
    }
  },
  methods: {
    getMovies() {
      this.$store.dispatch('getMovies')
    }
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    },
    randomMovies() {
      return _.shuffle(this.$store.state.movies)
    }
  },
  created(){
    if (this.isLogin === true) { 
      if (this.$store.state.movies.length === 0){
        this.getMovies()
      }
    } else {
      alert('로그인이 필요한 서비스 입니다.')
      this.$router.push({ name: 'LogInView' })
    }
    this.$store.dispatch('oneOn')
    this.$store.dispatch('twoOff')        
  }
}
</script>

<style>
.componentName {
  font-size: 33px;
  margin-bottom: 30px;
}
</style>