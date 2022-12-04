import Vue from 'vue'
import VueRouter from 'vue-router'

import MovieOnelinesView from '../views/MovieOnelinesView.vue'
import MovieTotalView from '../views/MovieTotalView.vue'
import MovieRecommendView from '../views/MovieRecommendView.vue'
import MovieDetailView from '../views/MovieDetailView'
import MovieSearchView from '../views/MovieSearchView'

import ArticlesView from '../views/articles/ArticlesView'
import ArticlesCreateView from '../views/articles/ArticlesCreateView'
import ArticleDetailView from '../views/articles/ArticleDetailView'
import ArticleUpdateView from '../views/articles/ArticleUpdateView'
import NotFound404 from '../views/NotFound404'

import SignUpView from '../views/accounts/SignUpView'
import LogInView from '../views/accounts/LogInView'
import ProfileView from '../views/accounts/ProfileView'

import TwoView from '../views/two/TwoView'
import TwoFailView from '../views/two/TwoFailView'
import TwoRankView from '../views/two/TwoRankView'

import AndView from '../views/AndView'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Main',
  },

  {
    path: '/movies',
    name: 'MovieOnelinesView',
    component: MovieOnelinesView
  },
  {
    path: '/movies/total',
    name: 'MovieTotalView',
    component: MovieTotalView
  },
  {
    path: '/movies/recommend',
    name: 'MovieRecommendView',
    component: MovieRecommendView
  },
  {
    path: '/movies/search',
    name: 'MovieSearchView',
    component: MovieSearchView
  },
  {
    path: '/movies/:moviePk',
    name: 'MovieDetailView',
    component: MovieDetailView
  },

  {
    path: '/articles',
    name: 'ArticlesView',
    component: ArticlesView
  },
  {
    path: '/articles/create',
    name: 'ArticlesCreateView',
    component: ArticlesCreateView
  },
  {
    path: '/articles/:article_pk',
    name: 'ArticleDetailView',
    component: ArticleDetailView
  },
  {
    path: '/articles/:article_pk/update',
    name: 'ArticleUpdateView',
    component: ArticleUpdateView
  },

  {
    path: '/and',
    name: 'AndView',
    component: AndView
  },

  {
    path: '/two',
    name: 'TwoView',
    component: TwoView
  },
  {
    path: '/two/fail',
    name: 'TwoFailView',
    component: TwoFailView
  },
  {
    path: '/two/rank',
    name: 'TwoRankView',
    component: TwoRankView
  },
  

  {
    path: '/signup',
    name: 'SignUpView',
    component: SignUpView
  },
  {
    path: '/login',
    name: 'LogInView',
    component: LogInView
  }, 
  {
    path: '/profile/:userName',
    name: 'ProfileView',
    component: ProfileView
  },

  {
    path: '/404',
    name: 'NotFound404',
    component: NotFound404,
  },
  {
    path: '*',
    redirect: '/404',
  }
]


const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router