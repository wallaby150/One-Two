<template>
  <div class= "bigtitle">
    <p class="componentName"
      @click="gopush()"
      style="cursor: pointer;"
    ><span style="color:red">C</span>ommunity</p>
    <b-card-group columns>
      <b-card class="bcard">
        <b-card-title class="head">
          <div align="left" class="mx-4 mt-2">
            <h4 style="font-weight:bold;">{{article.title}}</h4>
          </div>
          <router-link :to=" { name: 'ProfileView', params: { userName: article.username } } ">{{article.username}}</router-link>
          <div align="right">
            <p class="mx-4" style="font-size:15px;">{{article.created_at}}</p>
          </div>
        </b-card-title>
        <b-card-text>
          <div align="left">
            <p v-if="moviedata" class="mb-4">
              <img :src="`https://image.tmdb.org/t/p/w500/${moviedata.poster_url}`" width="170px">
            </p>
          </div>
          <div align="left" class="my-5">
            <pre style="max-width:1800px; font-size:15px; font-family: 'NanumSquareRegular';">{{article.content}}</pre>
          </div>
          <div v-if="isLiked" style="margin-top : 200px;">
            <button class="filter-button" @click="[isLiked = !isLiked, liked()]">
              <slot><img src="../../assets/redheart.png" width="17px"></slot>
            </button>
          </div>
          <div v-if="!isLiked" style="margin-top : 200px;">
            <button class="filter-button" @click="[isLiked = !isLiked, liked()]">
              <slot><img src="../../assets/blankheart.png" width="17px"></slot>
            </button>
          </div>
          <p style="color:red; font-size:14px; padding-right:6px;">{{likeCount}}</p>
          <div v-if="isYours" align="right" class="redbtn">
            <router-link :to=" { name: 'ArticleUpdateView', params: { article_pk: this.articlePk } } "><b-button pill style="font-size:80%; background-color:#F20505; border-color: #F20505;">수정</b-button></router-link>
            <b-button pill @click="deleteArticle" style="font-size:80%; background-color:#F20505; border-color: #F20505;"> 삭제</b-button>
          </div>
          <router-view/>
        </b-card-text>
        <b-input-group>
          <b-form-input v-model="content" placeholder="댓글을 입력해주세요." @keyup.enter="createComment"></b-form-input>
          <b-input-group-append >
          <b-button squared variant="outline-danger" @click="createComment">등록</b-button>
          </b-input-group-append>
        </b-input-group>
        <div>
        <hr>
        <CommentItem v-for="(comment, idx) in comments"
        :key="idx"
        :comment="comment"
        @delete-comment="deleteComment"
        />
        </div>
      </b-card>
    </b-card-group>

  <router-view/>

  </div>
</template>

<script>
import axios from 'axios'
import CommentItem from '@/components/CommentItem'

export default {
  name: 'ArticleDetailView',
  components: {
    CommentItem
  },
  data() {
    return {
      articlePk: this.$route.params.article_pk,
      article: {"username":null, "title": null, "content": null, "created_at": null, "movie":null},
      comments: null,
      content: null,
      moviedata: null,  
      isLiked: null,
      likeCount: 0,
    }
  },
  computed:{
    isLogin() {
      return this.$store.getters.isLogin
    },
    isYours() {
      return this.$store.state.username === this.article.username
    },
  },

  methods:{
    getArticle() {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/articles/${this.articlePk}`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          if (res.data.like_users.includes(this.$store.state.userid)){
            this.isLiked = true
          } else {
            this.isLiked = false
          }
          this.article = res.data
          this.likeCount = this.article.like_users.length
          if (res.data.movie){
            this.getMovie()
          }
        })
        .catch(() => {
          this.$router.push({name:"NotFound404"})
        })
    },
    getComments() {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/articles/${this.articlePk}/comments`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          this.comments = res.data
        })
    },
    deleteArticle() {
      axios({
        method: 'delete',
        url: `http://127.0.0.1:8000/articles/${this.articlePk}`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then(() => {
          this.$router.push({name:"ArticlesView"})
        })
    },

    createComment() {
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/articles/${this.articlePk}/comments/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
        data: {
          content: this.content,
        }
      })
        .then(() => {
          this.getComments()
          this.content = null

        })
    },

    deleteComment(comment) {
      const idx = this.comments.indexOf(comment)
      this.comments.splice(idx, 1)
    },

    liked() {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/articles/${this.articlePk}/like/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          if (res.data.is_liked == false){
            this.likeCount --
          } else {
            this.likeCount ++
          }
        })
    },
    getMovie() {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/${this.article.movie}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          this.moviedata = res.data
        })
    },
    gopush() {
      this.$router.push({name:'ArticlesView'})
    }
  },

  created(){
    if (this.isLogin === true) { 
      this.getArticle()
      this.getComments()
    } else {
      alert('로그인이 필요한 서비스 입니다.')
      this.$router.push({ name: 'LogInView' })
    }
    this.$store.dispatch('oneOn')
    this.$store.dispatch('twoOff')      
  },
}
</script>

<style>
.filter-button {
  border: none;
  background-color: white;
}

.bcard {
  display: grid;
  grid-template-columns: 6fr;
  justify-content: start;
  width: 70%;
}
.head {
  background-color:rgb(247, 247, 247);
  padding: 4px;
}


.card > .card-body > .card-title > a {
  float: left;
  text-decoration: none;
  color: black;
  margin-left: 1.7rem;
  font-size: 15px;
  font-weight: bold;
}

pre {
  white-space: pre-wrap; 
}

.componentName {
  font-size: 33px;
  margin-bottom: 30px;
}

</style>