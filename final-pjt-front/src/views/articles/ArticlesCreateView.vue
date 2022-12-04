<template>
  <div style="margin-top: 20px !important;">
    <h1 class="mb-3">
      게시글 작성
    </h1>
    <div class="article12">
      <b-input v-model="title" placeholder="제목을 입력해주세요."></b-input>
      <b-input v-model="movie_title" placeholder="관련영화선택(Optional)" readonly></b-input>
      <b-button v-b-modal.modal1 style="float:left;">영화검색</b-button>
      <b-modal id="modal1" ok-title = "Cancel" cancel-title = "OK" cancel-variant="danger" ok-variant="outline-danger">
        <b-input-group>
          <b-form-input placeholder="검색할 제목을 입력 후 엔터" @keyup.enter="searchKeyword"></b-form-input>
            <b-input-group-append b-input-group-append >
          </b-input-group-append>
        </b-input-group>
        <div v-if="searchedList">
          <div>
            <b-dropdown text="아래에 영화를 선택해주세요." block variant="outline-danger" class="my-class">
              <div v-for="(movie, idx) in searchedList" :key="idx" @click="savenum(movie.id, movie.title)">
                <b-dropdown-item><img :src="`https://image.tmdb.org/t/p/w500/${movie.poster_url}`" width="80px" height="auto"></b-dropdown-item>
                <span><b-dropdown-item>{{movie.title}}</b-dropdown-item></span>
              </div>
            </b-dropdown>
          </div>
        </div>
      </b-modal>
      <b-form-textarea
          v-model="content"
          placeholder="내용을 입력해 주세요"
          rows="18"
          max-rows="18"
          style="overflow-y:scroll"
      ></b-form-textarea>
      <br>
      <b-button @click="createArticle()">등록</b-button>&nbsp;
      <b-button @click="cancel()">취소</b-button>
      <p></p>
    </div>  
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ArticlesCreateView',
  data() {
    return {
      title: null,
      content: null,
      pk: null,
      searchedList: null,
      movie_title: null,
    }
  },  
  methods: {
    createArticle() {
      axios({
        method: 'post',
        url: `${API_URL}/articles/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
        data: {
          title: this.title,
          content: this.content,
          pk: this.pk
        }
      })
        .then((res) => {
          this.$router.push({name: 'ArticleDetailView', params: { article_pk: res.data.id}})
        })
    },
    cancel() {
      this.$router.push({ name: 'ArticlesView' })
    },
    searchKeyword: function(event) {
      const keyword = event.target.value
      
      this.searchedList = this.$store.state.movies.filter((movie) => {
        return movie.title.includes(keyword)
      })
    },
    savenum(id, title) {
      this.pk = id
      this.movie_title = title
    },
  },
  computed:{
    isLogin() {
      return this.$store.getters.isLogin
    },
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
h1 {
  text-align: center;
  padding: 0;
  margin-bottom: 60px;
}
.article12 {
  width: 60%;
  margin: auto;
  margin-bottom: 30px;
  border: solid 1px black;
}
.my-class .dropdown-menu {
  max-height: 300px;
  overflow-y: auto;
}
</style>