<template>
  <div
    id="moviecard"
    @click="goDetail"
    style="cursor:pointer"
  >
  <b-card
      id="card"
      :title="`${ movie.title }`"
      :img-src="`${ movie.poster_url}`"
      img-alt="Image"
      img-width="100%"
      img-height="593.32"
      class="border-0">
      <b-card-text>
    <p
        style="font-family:'NanumMyeongjoExtraBold'; color:gray; font-size:18px;" class="ecl"
    > {{ movie.description }} </p>
    </b-card-text>
    </b-card>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'MovieCard',
  props: {
    movie: Object,
  },
  methods: {
    goDetail() {
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/accounts/addvisited/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
        data: {
          pk: this.movie.id
        }
      })
      this.$router.push({name:"MovieDetailView", params: {moviePk: this.movie.id}})
    }
  },
}
</script>

<style>
#moviecard {
  border: 2px solid black;
  border-radius: 8px;
  margin-bottom: 10px;
}

#moviecard:hover {
  /* background-color: #CCCCCC; */
  /* background-color: #F23D3D; */
  opacity: 0.6;
  transition: all 0.3s;
}

.ecl {
  font-family:'NanumMyeongjoBold';
  padding: 5px;
  font-size: 30px;
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 4;
  -webkit-box-orient: vertical;
  word-break:keep-all;
  text-align: center;
}
</style>