<template>
  <div style="">
    <p class="componentName"
    ><span style="color:red">One</span>Lines</p><div>
  </div>
  <b-card-group
    class="card border-0">
    <MovieOnelineCard
      v-for="movie in randomMovies"
      :key="movie.id"
      :movie="movie"
    />
  </b-card-group>
    <!-- <p>{{ movies }}</p> -->
  </div>
</template>

<script>
import _ from 'lodash'
import axios from 'axios'
import MovieOnelineCard from '@/components/MovieOnelineCard'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'MovieOnelinesView',
  components: {
    MovieOnelineCard
  },
  data() {
    return {
      movies: null,
    }
  },
  methods: {
    getMovies() {
      axios({
        method: 'get',
        url: `${API_URL}/movies/`,
        headers: {
          Authorization: `Token ${this.token}`
        }
      })
        .then((res) => {
          this.movies = res.data
        })
    },
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    },
    randomMovies() {
      return _.shuffle(this.movies)
    },
    token() {
      return this.$store.state.token
    }
  },

  created(){
    if (this.isLogin === true) { 
      this.getMovies()
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
.card {
  width: 85%;
  display: inline-flex;
  justify-content: space-around;
  align-items: center;
  margin: auto;
  border: 0 !important;
}

.componentName {
  font-size: 33px;
  margin-bottom: 30px;
}
</style>