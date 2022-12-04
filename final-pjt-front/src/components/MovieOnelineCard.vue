<template>
  <div id="movieonelinecard" @click="goDetail" style="cursor:pointer">
    <b-card
      id="card"
      :title="`${ movie.title }`"
      :img-src="`${ movie.poster_url}`"
      img-alt="Image"
      img-width="100%"
      img-height="593.32"
      class="border-0">
      <b-card-text>
        <div v-if="onelines">
          <div
            style="font-family:'NanumMyeongjoExtraBold'; color:gray;"
          >
          <p
            class="title"
          >
            " {{randomOneline[0][0] | stringUnescape }} "
          </p>
          <p style="font-size:14px;">{{randomOneline[0][2]}}, {{randomOneline[0][1]}}</p>
          </div>
        </div>
      </b-card-text>
    </b-card>
  </div>
</template>

<script>
import _ from 'lodash'
import axios from 'axios'

export default {
  name: 'MovieOnelineCard',
  data() {
    return {
      onelines: [],
      id: null,
    }
  },
  props: {
    movie: Object,
  },

  methods: {
    goDetail() {
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/accounts/addvisited/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
        data: {
          pk: this.movie.id
        }
      })
      this.$router.push({name:"MovieDetailView", params: {moviePk: this.movie.id}})
    }
  },

  filters: {
    stringUnescape(rawText) {
      return _.unescape(rawText)
    }
  },
  
  computed: {
    randomOneline() {
      return _.shuffle(this.onelines)
    },
  },

  created() {
          if (this.movie.exp_reple) {
            const temp = this.movie.exp_reple.split('], [')
            const onelines = []
            for (const i of temp) {
              const line = i.split(`', '`)
              const oneline = []
              for (var j = 0; j < line.length; j++) {
                if (j === 0) {
                  if (line[j].includes(`[['`)) {
                    oneline.push(line[j].slice(3))
                  }
                  else {
                    oneline.push(line[j].slice(1))
                  }
                }
                else if (j === line.length-1) {
                  if (line[j].includes(`']]`)) {
                    oneline.push(line[j].slice(0,-3))
                  }
                  else {
                    oneline.push(line[j].slice(0,-1))
                  }
                }
                else {
                  oneline.push(line[j])
                }
              }
              onelines.push(oneline)
              }
            this.onelines = onelines
          }
  }
}
</script>

<style>
#movieonelinecard {
  border: 2px solid black;
  border-radius: 8px;
  margin-bottom: 10px;
}

#movieonelinecard:hover {
  opacity: 0.6;
  transition: all 0.3s;
}

.title {
  font-size: 20px;
  margin-top: 20px;
}

#card {
   width: 390px !important;
   height: 800px !important;
   object-fit: cover; 
}

.card-body {
  width:100% !important;
}
</style>