<template>
    <div style='box-shadow: 0 0 5px 2px #00404C;font-family: Noto Sans, sans-serif; padding-left: 30px; padding:20px;height:100%;border-radius:10px;background-color:rgba(0, 42, 50, 0.95); margin-top:90px; margin-left:100px; margin-right:100px;color: #BABABA;'>
        <div>
            <h1 style='font-size:25px;'>Вики <input style='border-radius: 5px;font-size:20px;margin-left:450px; width: 80px; height:20px;' v-model='title' placeholder="Имя"><input style='border-radius: 5px;margin-left:10px; font-size:20px;width: 80px; height:20px;' v-model='image' placeholder="Фото"><button  v-on:click="addWiki" style='margin-left:10px;border-color: black; background-color: #001e24;' type="button" class="btn btn-primary">Добавить</button><button  v-on:click="titles=title, images=image" style='margin-left:10px;border-color: black; background-color: #001e24;' type="button" class="btn btn-primary">Подтвердить</button></h1>
        </div>
        
        <br>
        <div  v-for="(article, index) in articles" :key="index">
                <h1 style='font-size:20px;'><a :href='path+"/"+article.title'><img width='50px' height="50px" style='border-radius: 10px; margin-right: 10px;' :src='article.image' >{{article.title}}</a></h1> 

        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
  data() {
    return {
        ara: 'fsfsf',
      articles: [],
      wikis: [],
      path: 'http://localhost:8080/#/wiki'
    };
  },
    methods: {
        getArticles() {
        const path = 'http://localhost:5000/wiki';
        axios.get(path)
            .then((res) => {
            this.articles = res.data.articles;
            })
            .catch((error) => {
            // eslint-отключение следующей строки
            console.error(error);
            });
        },
        addWiki(){
            let gd = 'da'
            axios.post('http://localhost:5000/wiki', {
                'images':  this.images,
                'titles':  this.titles
            })
            .then(function (response) {
                console.log(response);
            })
            .catch(function (error) {
                console.log(error);
            });
        },
    },
    created() {
        this.getArticles();
    },
};
</script>