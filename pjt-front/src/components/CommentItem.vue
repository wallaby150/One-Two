<template>
  <div>
    <div align="left" class="routestyle">
      <router-link :to=" { name: 'ProfileView', params: { userName: comment.username } } ">{{comment.username}}</router-link>
      <span class="mx-4">{{comment.content}}</span>
      <span class="goright">
        <div v-if="isYours">
           <img src ="../assets/delete.png" height="25.19px" @click="deleteComment" style="cursor: pointer;">
        </div>
      </span>
    </div>
    <hr>
    <router-view/>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name:'CommentItem',
  data() {
    return {
      username:null,
      
    }
  },
  props: {
    comment: Object,
  },
  methods: {
    deleteComment() {
      this.$emit('delete-comment', this.comment)
      axios({
        method: 'delete',
        url: `http://127.0.0.1:8000/articles/comments/${this.comment.id}`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
    },
  },
  computed:{
    isYours() {
      return this.$store.state.username === this.comment.username
    },
    isLogin() {
      return this.$store.getters.isLogin
    },
  },
}
</script>

<style>
.routestyle > a {
  text-decoration: none;
  color: black;
  font-weight: bold;
}

p {
  margin-left:5px;
}

.routestyle {
  display: grid;
  grid-template-columns: 0.5fr 11fr 0.5fr;
}
</style>