<template>
  <div id="moviedetail">
    <img :src=" `${ movie.poster_url} `">

    <p class="title"> {{movie.title}} </p>
    <p>Reviews : {{movie.audience}}</p>
    <p>Release Date : {{movie.release_date}}</p>
    <p>Score : {{movie.score}}</p>
    <p>Genre : {{movie.genre}}</p>
    <div v-if="isLiked">
    <button class="filter-button" @click="[isLiked = !isLiked, liked()]">
      <slot><img src="../assets/redheart.png" width="17px"></slot>
    </button>
    </div>
    <div v-if="!isLiked">
    <button class="filter-button" @click="[isLiked = !isLiked, liked()]">
      <slot><img src="../assets/blankheart.png" width="17px"></slot>
    </button>
    </div>
    <br>

    <div v-if="expReples">
      <div
      v-for="expReple,idx in expReples"
      :key="idx"
      style="font-family:'NanumMyeongjoExtraBold';"
      >
        <p>" {{expReple[0]}} "</p>
        <p style="color:gray;">{{expReple[2]}} | {{expReple[1]}}</p>
        <hr style="width:50%; margin:auto; background-color: #F20505;">
        <br>
  
      </div>

    </div>

    <div v-if="oneLines">
      <div
      v-for="oneLine,idx in oneLines"
      :key="idx"
      style="font-family:'NanumMyeongjoExtraBold'; margin-bottom:20px;  border-radius: 5px;
"
      >
        <!-- <p>" {{oneLine.userName}} "</p> -->
        <!-- <span @click="">{{oneLine.username}} : </span> -->
                
        <span>
          <router-link :to=" { name: 'ProfileView', params: { userName: oneLine.username } } " style="text-decoration : none; color:gray;">{{oneLine.username}} </router-link>
        </span>
        <span>: "{{oneLine.content}}" _ {{star[oneLine.grade]}} </span>
        <span v-if="isCommentLiked">
          <button class="filter-button" @click="[isCommentLiked = !isCommentLiked, commentLiked(oneLine.id)]">
            <slot><img src="../assets/red_ddabong.png" width="18px"></slot>
          </button>
        </span>
        <span v-if="!isCommentLiked">
          <button class="filter-button" @click="[isCommentLiked = !isCommentLiked, commentLiked(oneLine.id)]">
            <slot><img src="../assets/black_ddabong.png" width="18px"></slot>
          </button>
        </span>
        <button
          v-if="isYours(oneLine)"
          @click="deleteOneline(oneLine)"
          class="createbutton"
        >
          X
        </button>
        <hr style="width:50%; margin:auto; background-color: #F20505;">

      </div>
    </div>
    <form @submit.prevent="createOneline">
      <label for="score"></label>
      <select v-model="grade">
        <option v-for="(star,idx) in starList" :key="idx" :value="star.value">{{ star.text }}</option>
      </select>
      <label for="content"></label>
      <input type="text" id="content" v-model="content" size=70 maxlength=60 placeholder="한줄평을 입력해주세요." style="margin:12px; margin-right:0px;">
      <input type="submit" value="create" class="createbutton">
    </form>


  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'MovieDetailView',
  data() {
    return {
      movie: {},
      movie_id: this.$route.params.moviePk,
      expReples: [],
      oneLines: [],
      content: null,
      grade: 0.5,
      isLiked: null,
      isCommentLiked: null,
      starList:[
        {text : "☆", value : 0.5},
        {text : "★", value : 1},
        {text : "★☆", value : 1.5},
        {text : "★★", value : 2},
        {text : "★★☆", value : 2.5},
        {text : "★★★", value : 3},
        {text : "★★★☆", value : 3.5},
        {text : "★★★★", value : 4},
        {text : "★★★★☆", value : 4.5},
        {text : "★★★★★", value : 5},
      ],
      star: {"0.5":"☆",
        "1":"★",
        "1.5":"★☆",
        "2":"★★",
        "2.5":"★★☆",
        "3":"★★★",
        "3.5":"★★★☆",
        "4":"★★★★",
        "4.5":"★★★★☆",
        "5":"★★★★★"
      }
    }
  },
  methods: {
    getMovie() {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/${this.$route.params.moviePk}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          this.movie = res.data
          if (res.data.like_users.includes(this.$store.state.userid)){
            this.isLiked = true
          } else {
            this.isLiked = false
          }
          if (res.data.exp_reple) {
            const temp = res.data.exp_reple.split('], [')
            const expReples = []
            for (const i of temp) {
              const line = i.split(`', '`)
              const expReple = []
              for (var j = 0; j < line.length; j++) {
                if (j === 0) {
                  if (line[j].includes(`[['`)) {
                    expReple.push(line[j].slice(3))
                  }
                  else {
                    expReple.push(line[j].slice(1))
                  }
                }
                else if (j === line.length-1) {
                  if (line[j].includes(`']]`)) {
                    expReple.push(line[j].slice(0,-3))
                  }
                  else {
                    expReple.push(line[j].slice(0,-1))
                  }
                }
                else {
                  expReple.push(line[j])
                }
              }
              expReples.push(expReple)
            }
            this.expReples = expReples
          }
          
        })
        .catch(() => {
          this.$router.push({name:"NotFound404"})
        })
    },
    getOnelines() {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/${this.movie_id}/one_line_comments/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          this.oneLines = res.data
          if (res.data[0].like_comment_users.includes(this.$store.state.userid)){
            this.isCommentLiked = true
          } else {
            this.isCommentLiked = false
          }

      })
    },
    isYours(oneLine) {
      return this.$store.state.username === oneLine.username
    },
    deleteOneline(oneLine) {
      const id = oneLine.id

      axios({
        method: 'delete',
        url: `http://127.0.0.1:8000/movies/one_line_comments/${id}/delete/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then(() => {
          const idx = this.oneLines.indexOf(oneLine)
          this.oneLines.splice(idx, 1)  
        })
    },
    createOneline() {
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/movies/${this.movie_id}/one_line_comments/create/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
        data: {
          content: this.content,
          grade: this.grade
        }
      })
        .then(() => {
          this.getOnelines()
          this.content = null
          this.grade = null

        })
        .catch(() => {
          if (!this.grade) {
            alert('평점을 남겨주세요.')
          } else if (!this.content.trim()) { 
            alert('한줄평을 입력해주세요.')
          }else {
            alert('기존의 한줄평을 삭제해주세요.')
          }
        })
    },
    liked() {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/${this.movie_id}/like/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
    },
    commentLiked(id) {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/one_line_comments/${id}/like/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
    }
  },

  computed:{
    isLogin() {
      return this.$store.getters.isLogin
    }
  },
  created(){
    if (this.isLogin === true) { 
      this.getMovie()
      this.getOnelines()
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
  .createbutton {
    color:white;
    background-color : red;
    border: 0px;
    border-radius: 5px;
    margin-left: 10px;
  }
</style>