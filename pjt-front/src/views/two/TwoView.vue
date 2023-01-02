<template>
  <div >
    <p class="componentName"
    ><span style="color:red">Two </span>: Game</p>
    <span class="description">"더 많은 사람들이 평가한 영화는 어느 쪽일까요???"</span>
    <p class="scoreBar">
      <span class="score">score : </span>
      <span class="score" style="color:#F20505; font-size:40px;">{{score}}</span>
    </p>
    <div class="container">
      <div
        @click="select(`left`)"
        style="cursor:pointer;
        margin:auto;"
        class="leftMovie moviecard"
        @mouseover="hoverLeft"
        @mouseout="hoverOut"
      >
        <img :src="`${ Movie1.poster_url} `" class="poster">
        <p
          class="movieName"
        >{{Movie1.title}}</p>
        <p>평점 수 :  <span style="color:#F20505; font-weight:700;">{{Movie1.audience}}</span></p>
      </div>
      <span style="font-size:100px; margin:auto; color:#F20505; " class="mx-5">{{choice}}</span>
      <div
        @click="select(`right`)"
        style="cursor:pointer;
        margin:auto;"
        class="rightMovie moviecard"
        @mouseover="hoverRight"
        @mouseout="hoverOut"
      >
        <img :src="`${ Movie2.poster_url} `" class="poster">
        <p
          class="movieName"
        >{{Movie2.title}}</p>
        <p>평점 수 :  <span style="color:#F20505; font-weight:700;">??????</span></p>
        <!-- <p>{{Movie2.audience}}</p> -->
      </div>
    </div>
  </div>
</template>

<script>
import _ from 'lodash'
import axios from 'axios'

export default {
  name: 'TwoView',
  data() {
    return{
      idx : 0,
      score : 0,
      choice : '?'
    }
  },

  methods: {
    select(dir) {
      const ansLeft = this.Movie1.audience > this.Movie2.audience
      if (ansLeft) {
        if (dir !== 'left') {
          this.scoreSave()
          this.$router.push({ name: 'TwoFailView', params: {score: this.score}})
        }
      }
      else {
        if (dir !== 'right') {
          this.scoreSave()
          this.$router.push({ name: 'TwoFailView', params: {score: this.score} })
        }
      }
      this.idx ++
      this.score ++
    },
    hoverLeft() {
      this.choice = ' > '
    },
    hoverRight() {
      this.choice = ' < '
    },
    hoverOut() {
      this.choice = ' ? '
    },
    scoreSave() {
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/two/fail/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
        data: {
          score: this.score
        }
      })
    }
  },

  computed:{
    isLogin() {
      return this.$store.getters.isLogin
    },
    randomMovies() {
      return _.shuffle(this.$store.state.movies)
    },
    Movie1() {
      return this.randomMovies[this.idx]
    },
    Movie2() {
      return this.randomMovies[this.idx+1]
    },
  },
  mounted() {
    // console.log(this.isLogin)
    if (this.isLogin === false) { 
      alert('로그인이 필요한 서비스 입니다.')
      this.$router.push({ name: 'LogInView' })    }
    this.$store.dispatch('oneOff')
    this.$store.dispatch('twoOn')
  }
}
</script>

<style>
.leftMovie:hover {
  opacity: 0.6;
  transition: all 0.3s;
}
.rightMovie:hover {
  opacity: 0.6;
  transition: all 0.3s;
}

.container {
  display: flex;
  justify-content: center;
}

.title {
  margin:10px;
}

.score {
  font-size: 30px;
  font-family:'NanumMyeongjoBold';
}

.description {
 font-family:'NanumMyeongjoBold';
  background-color: #F20505;
  color: white;
  padding: 5px;
}

.scoreBar {
  position: relative;
  left: 28%
}

.poster {
  width: 25vw;
  height: 34vw;
  border-radius: 7px;
}

.moviecard {
  border: 2px solid #F20505;
  border-radius: 8px;
  width: 25.3vw;
}

.movieName {
  font-family:'NanumMyeongjoBold';
  padding: 5px;
  font-size: 30px;
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 1;
  -webkit-box-orient: vertical;
  word-break:keep-all;
  text-align: center;
}
</style>