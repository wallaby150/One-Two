<template>
  <div>
    <p class="componentName"
    ><span style="color:red">S</span>earch</p>
    <br>
    <select v-model="selected">
      <option v-for="(SWF,idx) in SWFList" :key="idx+100" :value="SWF.value">{{ SWF.text }}</option>
    </select>
    <div v-if="selected==='1'">
      <input
      type="text"
      @input ="onInputKeyword"
    >
    <b-card-group
    class="card border-0">
    <MovieCard
      v-for="movie in searchedList"
      :key="movie.id"
      :movie="movie"
    />
    </b-card-group>
    </div>
    <div v-else-if="selected==='2'">
      <input
      type="text"
      @input ="onInputOneLine"
    >
    <b-card-group
    class="card border-0">
    <MovieCard
      v-for="movie in searchedonelines"
      :key="movie.id"
      :movie="movie"
    />
    </b-card-group>
    </div>
  </div>
</template>

<script>
import MovieCard from '@/components/MovieCard'

export default {
  name: 'MovieSearchView',
  components: {
    MovieCard
  },
  data() {
    return {
      selected: 0,
      searchedList: null,
      searchedonelines: null,
      SWFList:[
        {
          text : "-선택-",
          value : "0"
        },
        {
          text : "제목",
          value : "1"
        },
        {
          text : "키워드",
          value : "2"
        }
      ]
    }
  },
  computed:{
    isLogin() {
      return this.$store.getters.isLogin
    }
  },
  methods: {
    onInputKeyword: function(event) {
      const keyword = event.target.value
      
      this.searchedList = this.$store.state.movies.filter((movie) => {
        return movie.title.includes(keyword)
      })
    },
    onInputOneLine: function(event) {
      const keyword = event.target.value
      
      this.searchedonelines = this.$store.state.movies.filter((movie) => {
        return movie.exp_reple.includes(keyword)
      })
    }
  },
  created() {
    if (this.isLogin === false) { 
      alert('로그인이 필요한 서비스 입니다.')
      this.$router.push({ name: 'LogInView' })    }     
    this.$store.dispatch('oneOn')
    this.$store.dispatch('twoOff')      
  }
}
</script>

<style>
#moviecard {
  border: 2px solid black;
  border-radius: 8px;
  margin-bottom: 10px;
}
</style>