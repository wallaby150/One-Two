<template>
  <div
    id="movierecommendcard"
    @click="goDetail"
    style="cursor:pointer;"
  >
    <img
      :src=" `https://image.tmdb.org/t/p/w500${movie.poster_path}`"
      class="visitedImg"    
    >
    <p> {{movie.title}} </p>
    <p
        style="font-family:'NanumMyeongjoExtraBold'; color:gray; font-size:18px;"
    >평점 : {{movie.vote_average }} </p>
  </div>
</template>

<script>
export default {
  name: 'MovieRecommendCard',
  props: {
    movie: Object,
  },
  methods: {
    goDetail() {
      window.open(`https://www.themoviedb.org/movie/${this.movie.id}?language=ko`, '_blank')
}
  },
}
</script>

<style>
#movierecommendcard {
  border: 2px solid black;
}

#movierecommendcard:hover {
  /* background-color: #CCCCCC; */
  /* background-color: #F23D3D; */
  opacity: 0.6;
  transition: all 0.3s;
}

.visitedImg {
  width: 100%; 
  height: 100%;
}
</style>