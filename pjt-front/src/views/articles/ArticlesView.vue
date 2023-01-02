<template>
  <div id="article">
    <p class="componentName"
    ><span style="color:red">C</span>ommunity</p>
    <paginate
      name="articles"
      :list="articles"
      ref="paginator"
      class="paginate-list"
      :per="10"
    >
    <div>
      <table class="table table-striped">
        <thead>
          <tr>
            <th scope="col" class="num1">글번호</th>
            <th scope="col" class="num2">제목</th>
            <th scope="col" class="num3">이름</th>
            <th scope="col" class="num4">날짜</th>
            </tr>
        </thead>
        <tbody>
          <tr v-for="(item, idx) in paginated('articles')" :key="idx">
            <th scope="row" class="num5">{{ item.id }}</th>
            <td class="num6"><router-link :to=" { name: 'ArticleDetailView', params: { article_pk: item.id } } ">{{ item.title }}</router-link></td>
            <td class="num7"><router-link :to=" { name: 'ProfileView', params: { userName: item.username } } ">{{ item.username }}</router-link></td>
            <td class="num8">{{ item.created_at }}</td>
          </tr>
        </tbody>
      </table>
    </div>
    <router-view/>
    <div class="btn-container">
      <b-button variant="outline-danger"
        @click="createArticle"
        class="my"
      >
      글쓰기</b-button>
    </div>
      </paginate>
    <div class="lower">
      <paginate-links
        for="articles"
        :show-step-links="true"
        :limit="5"
      ></paginate-links>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ArticlesView',
  data() {
    return{
      articles: [1],
      paginate: ["articles"],
      movie: null,
    }
  },

  methods: {
    getArticles() {
      axios({
        method: 'get',
        url: `${API_URL}/articles`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          this.articles = res.data.reverse()
        })
    },
    createArticle() {
      this.$router.push({ name: 'ArticlesCreateView' })
      }
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
    else {
      this.getArticles()
    }
    this.$store.dispatch('oneOn')
    this.$store.dispatch('twoOff')      
  } 
}
</script>

<style>
@charset "UTF-8";
#article {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  font-size: 15px;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px; }

ul {
  list-style-type: none;
  padding: 0; }

li {
  display: inline-block;
  margin: 0 10px; }

.paginate-list {
  width: 60%;
  margin: 0 auto;
  text-align: left; 
  display: grid;
  border: none !important;
  }
  .paginate-list li {
    display: block; }
    .paginate-list li:before {
      content: '⚬ ';
      font-weight: bold;
      color: slategray; }

.paginate-links.articles {
  user-select: none; }
  .paginate-links.articles a {
    cursor: pointer; }
  .paginate-links.articles li.active a {
    font-weight: bold; }
  .paginate-links.articles li.next:before {
    content: ' | ';
    margin-right: 13px;
    color: #ddd; }
  .paginate-links.articles   li.disabled a {
    color: #ccc;
    cursor: no-drop; }
.table thead tr th.num1{
    width: 7%;
    text-align: center;
  }
.table thead tr th.num2{
    width: 53%;
    padding-left: 14px;
  }
.table thead tr th.num3{
    width: 20%;
    text-align: center;
  }
.table thead tr th.num4{
    width: 10%;
    text-align: center;
  }
.table tbody tr th.num5{
  text-align: center;
}
.table tbody tr td.num7{
  text-align: center;
}
.table tbody tr td.num8{
  text-align: center;
}
.table tr > td > a {
  text-decoration: none;
  color: black;
}
.table tr > td > a:hover {
  color: black;
  text-decoration: underline;
}
.my {
  display: inline-block;
  right:0;
  transition: 1s;
}

.my:hover,
.my:focus{
  background-color: red !important;
  box-shadow: 0 0 3px rgb(255, 210, 210),0 0 10px rgb(255, 168, 168),0 0 20px rgb(247, 130, 130);
}

.lower {
  margin: auto;
}

.btn-container{
  display: grid;
  justify-content: end;

}

.componentName {
  font-family: "NanumSquareRegular";
  font-size: 33px;
  margin-bottom: 30px;
}
</style>