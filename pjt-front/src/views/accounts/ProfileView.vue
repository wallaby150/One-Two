<template>
  <div class="profileDiv">
    <p
      class="componentName"
      style="letter-spacing:2px"
    >
      <span style="font-family:'NanumMyeongjobold';">"{{userName}}"</span>
      <span>님의</span>
      <span style="color:red">  P</span>rofile
    </p>
    <p class="recent"> - 최근 찾아본 영화 - </p>
    <div v-if="userData.id === this.$store.state.userid" class="visitedMovies">
      <div
        v-for="movie in visited"
        :key="movie.id+9999"
        class="imgDiv 
        d-flex flex-wrap"
        >
        <!-- <p>{{movie.id}}</p> -->
          <router-link :to=" { name: 'MovieDetailView', params: {moviePk: movie.id} } ">
          <img
            :src='movie.poster_url'
            class="visitedImg"
          >
          </router-link>
      </div>

    </div>
    
    <div class="contents">
      <p>✍ {{userName}}님의 한줄평 : </p>
        <ul
          v-for="(comment, idx) in myComment"
          :key="idx+9876"
          style="margin-bottom:8px;"
          >
          <span class="oneline">"{{ comment.content }}"</span>
          <span class="star"> _ {{oneLineMovies[idx]}}, {{star[comment.grade]}}</span>
        </ul>
      
      <span>🎇{{userName}}의 최고 점수 :</span><span style="font-size:20px; color:red;"> {{userData.score}}</span>
      <br>
      <br>
      <span>💖 '좋아요' 한 영화 : </span>
      <p
        v-for="(movie, idx) in likeMovie"
        :key="idx"
        style="margin:10px;"
      >
        <router-link :to=" { name: 'MovieDetailView', params: {moviePk: movie.id} } "
          class="likemovies"
        >• {{movie.title}}</router-link>
      </p>

      <div class="followBox">
        <b-button v-b-modal.modal-scrollable1 style="background-color:white; color:black" class="follow">팔로잉 : {{following}}</b-button>
        <b-modal id="modal-scrollable1" ok-title = "Cancel" cancel-title = "OK" cancel-variant="danger" ok-variant="outline-danger" scrollable :title="`팔로잉 ${following}명`">
        <p class="my-4" v-for="(following,i) in myFollow" :key="i">
          <router-link :to=" { name: 'ProfileView', params: {userName: following.username} } ">{{following.username}}</router-link>
          </p>
      </b-modal>
        <b-button v-b-modal.modal-scrollable2 style="background-color:white; color:black" class="follow">팔로워 : {{follower}}</b-button>
        <b-modal id="modal-scrollable2" ok-title = "Cancel" cancel-title = "OK" cancel-variant="danger" ok-variant="outline-danger" scrollable :title="`팔로워 ${follower}명`">
        <p class="my-4" v-for="(follower,i) in myFollower" :key="i">
          <router-link :to=" { name: 'ProfileView', params: {userName: follower.username} } ">{{follower.username}}</router-link>
        </p>
      </b-modal>
      </div>
     <br>

    <div v-if="userData.id !== this.$store.state.userid" class="followDiv">
      <button v-if="is_followed" @click="userFollow" class="follow" >언팔로우</button>
      <button v-if="!is_followed" @click="userFollow" class="follow" >팔로우</button>
    </div>
    <router-view :key="$route.fullPath"/>
  </div>
    </div>



</template>

<script>
import axios from 'axios'

export default {
  name: 'ProfileView',
  data() {
    return {
      userData: {"id": 0,},
      userName: this.$route.params.userName,
      follower: null,
      following: null,
      is_followed: null,
      visited: [],
      likeMovie: null,
      myComment: null,
      myFollow: null,
      myFollower: null,
      movieTitles: null,
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
  computed:{
    isLogin() {
      return this.$store.getters.isLogin
    },
    oneLineMovies() {
      const movies = this.myComment
      const data = this.$store.state.movies
      const movieTitles = []

      for (const movie of movies){
        for (const datum of data){
          if (datum.id === movie.movie) {
            movieTitles.push(datum.title)
          }
        }
      }
      return movieTitles
    }
  },
  methods:{
    getProfile() {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/accounts/profile/${this.userName}`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          this.userData = res.data
          this.following = this.userData.followings.length
          this.checkFollow()
          this.visitedMovie()
          this.getLikeMovie()
          this.getMyComment()
          this.getFollowList()
          this.getFollowerList()
        })
    },
    checkFollow() {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/accounts/${this.userData.id}/checkfollow/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          this.is_followed = res.data.is_followed
          this.follower = res.data.followers_count
        })
    },
    visitedMovie() {
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/accounts/visited/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
        data: {
          pk: this.userData.id
        }
      })
        .then((res) => {
          this.visited = res.data
        })
    },
    userFollow() {
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/accounts/${this.userData.id}/follow/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          this.is_followed = res.data.is_followed
          this.follower = res.data.followers_count
        })
    },
    getLikeMovie() {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/movies/like_movie_list/',
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
        data: {
          pk: this.userData.id
        }
      })
        .then((res) => {
          this.likeMovie = res.data.reverse()
        })
    },
    getMyComment() {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/movies/one_line_comments/mylist/',
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
        data: {
          pk: this.userData.id
        }
      })
        .then((res) => {
          this.myComment = res.data
        })
    },
    getFollowList() {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/followinglist/',
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
        data: {
          pk: this.userData.id
        }
      })
        .then((res) => {
          this.myFollow = res.data
        })
    },
    getFollowerList() {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/followerlist/',
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
        data: {
          pk: this.userData.id
        }
      })
        .then((res) => {
          this.myFollower = res.data
        })
    },
  },
  created() {
    if (this.isLogin === false) { 
      alert('로그인이 필요한 서비스 입니다.')
      this.$router.push({ name: 'LogInView' })
      } else {
        this.getProfile()
    }
    this.$store.dispatch('oneOff')
    this.$store.dispatch('twoOff')  
  },
  beforeRouteUpdate(to, from, next) {
    this.userName = to.params.userName
    this.getProfile()
    next()
  }
}
</script>
this.$store.state.movies.filter(myComment.id)[0].title
<style>
.visitedMovies {
  margin-left: 30vw;
  margin-right: 30vw;
  width: 40vw;
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr 1fr;
  margin-top: 1vw;
  margin-bottom: 3vw;
}

.imgDiv {
  justify-content: flex-start;
  width: 100%;
  height: 100%;
  flex-wrap: nowrap;
}

.visitedImg {
  width: 100%;
  height: 100%;
}

.modal-body > p > a {
  text-decoration: none;
  color: black;
}

.profileDiv {
  padding-top: 145px;
}

.componentName {
  font-size: 33px;
  margin-bottom: 30px;
}

.recent {
  font-size: 25px;  
  margin-bottom:0;
}

.contents {
  text-align: start;
  width:50%;
  margin-left:auto;
  margin-right:auto;
}

.likemovies {
  text-decoration-line: none;
  margin-left: 20px;
}

.oneline {
 font-family: 'NanumMyeongjoextrabold';
 color: rgb(77, 77, 77);
  font-size: 20px;
  margin:0
}

.follow {
  border: 1px solid !important;
  /* color: rgb(69, 69, 212) !important; */
  color: #F23D3D !important;
  margin: 10px;
}

.followBox {
  display: flex;
  justify-content: center;
  margin:20px;
}
.followDiv {
  display: flex;
  justify-content: center;
}
.followDiv > button {
  color:white !important;
  background-color: red !important;
}
</style>