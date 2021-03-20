<template>
    <div style='box-shadow: 0 0 5px 2px #00404C;font-family: Noto Sans, sans-serif; padding-left: 30px; padding:20px;height:100%;border-radius:10px;background-color:rgba(0, 42, 50, 0.95); margin-top:90px; margin-left:100px; margin-right:100px;color: #BABABA;'>
        <h1>{{title.substring(1, title.length-1)}}</h1>
        <div style=' position: absolute; margin-left: 800px'>
            <img :src='image' height='30%' width='30%' style='border-radius: 10px;'>
            <p style='margin-left: 30px'>{{title.substring(1, title.length-1)}}</p>
        </div>
        <textarea cols='70' rows='10'style='background-color:rgba(0, 42, 50, 0)' v-model='texts'>{{text}}</textarea>
        <br>
        <h1><button style='border-color: black; background-color: #001e24;' class='btn btn-primary' v-on:click="text_other=texts">1</button>
        <button v-on:click="redText" type='button' style='border-color: black; background-color: #001e24;' class='btn btn-primary' >Редактировать Описание</button></h1>

    </div>
</template>

<script>
import axios from 'axios'
export default {

  data() {
    var paramsString = document.location.hash;
    var params_2 = paramsString.replace('#','')
    return {
        ara: 'fsfsf',
      articles: '',
      arab: params_2.replace('/',''),
      id: '',
      title: '',
      image: '',
      text: '',
      text_other: '',
      need: ''
    };
  },
  
    methods: {
        getArt() {
            var path = 'http://localhost:5000/';
            path += this.arab.replace('wiki', '');
            axios.get(path)
                .then((res) => {
                this.id = res.data.article_id;
                this.title = res.data.article_name;
                this.image = res.data.article_image.substring(1, res.data.article_image.length-1);
                this.text = res.data.article_text.substring(1, res.data.article_text.length-1);
                })
                .catch((error) => {
                // eslint-отключение следующей строки
                console.error(error);
                });
        },
        redText () {
            var path = 'http://localhost:5000/';
            path += this.arab;
            this.need = path
            axios.post(path, {
                'text': this.text_other,
            })
            .then(function (response) {
                console.log(response);
            })
            .catch(function (error) {
                console.log(error);
            });
        }
    },
    created() {
        this.getArt();
    },
}
</script>
<style>
textarea:focus{
    border: 0;
    outline: 0;
    outline-offset: 0;
    color: #BABABA;
    background-color:#002a32;
}
textarea{
    border: 0;
    outline: 0;
    outline-offset: 0;
    color: #BABABA;
    background-color:#002a32;
}
</style>