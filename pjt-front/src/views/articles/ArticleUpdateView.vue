<template>
  <div>
    <h1>
      게시글 수정
    </h1>
    <div class="article">
      <b-input v-model="article.title">{{article.title}}</b-input>
      <b-input v-model="article.movie" readonly>{{article.movie}}</b-input>
      <b-form-textarea
          v-model="article.content"
          rows="19"
          max-rows="19"
          style="overflow-y:scroll"
      >{{article.content}}</b-form-textarea>
      <br>
      <b-button @click="UpdateArticle()">등록</b-button>&nbsp;
      <b-button @click="cancel()">취소</b-button>
      <p></p>
    </div>  
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ArticleUpdateView',
  data() {
    return {
      pk: this.$route.params.article_pk,
      article: {"username":null, "title": null, "content": null, "created_at": null, "movie":null}
    }
  },  
  methods: {
    getArticle() {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/articles/${this.pk}`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          this.article = res.data
        })
        .catch(() => {
          this.$router.push({name:"NotFound404"})
        })
    },
    UpdateArticle() {
      axios({
        method: 'put',
        url: `${API_URL}/articles/${this.pk}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
        data: {
          title: this.article.title,
          content: this.article.content,
          movie: this.article.movie
        }
      })
        .then((res) => {
          this.$router.push({name: 'ArticleDetailView', params: { article_pk: res.data.id}})
        })
    },
    cancel() {
      this.$router.push({ name: 'ArticlesView' })
    },
  },
  computed:{
    isLogin() {
      return this.$store.getters.isLogin
    }
  },
  created() {
    if (this.isLogin === false) { 
      alert('로그인이 필요한 서비스 입니다.')
      this.$router.push({ name: 'LogInView' })
    } else {
      this.getArticle()
    }
  }
}
</script>

<style>
h1 {
  margin-bottom: 60px;
}
.article {
  width: 60%;
  margin: auto;
  margin-bottom: 30px;
  border: solid 1px black;
}
</style>