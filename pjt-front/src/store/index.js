import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '@/router'

Vue.use(Vuex)


const API_URL = 'http://127.0.0.1:8000'


export default new Vuex.Store({
  plugins: [
    createPersistedState()
  ],
  state: {
    token: null,
    movies: [],
    username: null,
    userid: null,
    oneToggle: false,
    twoToggle: false,
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    }
  },
  mutations: {
    GET_MOVIES(state, movies) {
      state.movies = movies
    }
    ,
    SAVE_TOKEN(state, token) {
      state.token = token
    },
    DELETE_TOKEN(state) {
      state.token = null
      state.movies = []
      state.username = null
    },
    SAVE_USER(state, userdata) {
      state.username = userdata.name
      state.userid = userdata.id
    },
    ONE_ON(state) {
      state.oneToggle = true
    },
    ONE_OFF(state) {
      state.oneToggle = false
    },
    TWO_ON(state) {
      state.twoToggle = true
    },
    TWO_OFF(state) {
      state.twoToggle = false
    },
  },


  actions: {
    getMovies(context) {
      axios({
        method: 'get',
        url: `${API_URL}/movies/total/`,
        headers: {
          Authorization: `Token ${context.state.token}`
        }
      })
        .then((res) => {
          context.commit('GET_MOVIES', res.data)
        })
    },
    signUp(context, payload) {
      axios({
        method: 'post',
        url: `${API_URL}/restauth/signup/`,
        data: {
          username: payload.username,
          password1: payload.password1,
          password2: payload.password2,
        }
      })
        .then((res) => {
          context.commit('SAVE_TOKEN', res.data.key)
          axios({
            method: 'get',
            url: `${API_URL}/movies/check/`,
            headers: {
              Authorization: `Token ${res.data.key}`
            }
          })
          .then((res) => {
            context.commit('SAVE_USER', res.data)
            router.push({ name: 'MovieOnelinesView' })
            context.dispatch('getMovies')
          })
        })
        .catch(() => {
            alert('이미 존재하는 이름이거나, 잘못된 비밀번호 양식입니다.')
        }
        )
    },
    logIn(context, payload) {
      axios({
        method: 'post',
        url: `${API_URL}/restauth/login/`,
        data: {
          username: payload.username,
          password: payload.password,
        }
      })
        .then((res) => {
          context.commit('SAVE_TOKEN', res.data.key)
          axios({
            method: 'get',
            url: `${API_URL}/movies/check/`,
            headers: {
              Authorization: `Token ${res.data.key}`
            }
          })
          .then((res) => {
            context.commit('SAVE_USER', res.data)
            router.push({ name: 'MovieOnelinesView' })
            context.dispatch('getMovies')
          })
        })
        .catch(() => {
          alert('잘못 입력하셨습니다.')
        })
    },
    logOut(context) {
      axios({
        method: 'post',
        url: `${API_URL}/restauth/logout/`,
      })
        .then(() =>
          context.commit('DELETE_TOKEN'),
          router.push({ name: 'Main' })
        )
    },
    oneOn(context) {
      context.commit('ONE_ON')
    },
    oneOff(context) {
      context.commit('ONE_OFF')
    },
    twoOn(context) {
      context.commit('TWO_ON')
    },
    twoOff(context) {
      context.commit('TWO_OFF')
    },
  },
  modules: {
  }
})
