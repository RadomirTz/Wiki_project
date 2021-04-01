<template>
        <div>
        
            <div style='box-shadow: 0 0 5px 2px #00404C;font-family: Noto Sans, sans-serif; padding-left: 30px; padding:20px;border-radius:10px;background-color:rgba(0, 42, 50, 0.95); margin-top:90px; margin-left:100px; margin-right:100px;color: #BABABA;'>
                <h1 style='font-size:30px;'>Что это за сайт? | Главная</h1>
                <p>Приветствую, данный сайт создан по тематике аниме 'DeathNote'.</p>
                <p>Здесь можно найти всю информацию о этом аниме, а также посмотреть его</p>
                <p>Мы будем очень рады, если ты посмотришь наш перечень товаров <a href='http://localhost:8080/#/merch'>тут</a></p>
                <p>Чтобы перейти на страницу просмотра нажми <a href='http://localhost:8080/#/view'>сюда</a></p>
                <p >Приятного пользования нашим сайтом<img id='ryuk' width='90px' height='90px' src='https://i.yapx.ru/LZTAg.png'></p>
                <a href='#'>Мы в вк</a>
                <br>
                <a href='#'>Мы в инсте</a>
                <br>        
                <a href='#'>Наш дискорд канал</a>

            </div>
        </div>
</template>

<script>
import axios from 'axios'
export default {
    data() {
        return {
            articles: [],
        };
    },
    methods: {
        getArticles() {
            const path = 'http://localhost:5000/articles';

            axios.get(path)
            .then((res) => {
                this.articles = res.data.articles;
            })
            .catch((error)  => {
                console.error(error);
            });
        },
    },
    created() {
        this.getArticles();
    },
};
</script>

<style>
    #column_top{
    border-bottom: 1px solid #f5f5f5;
    background-color: #fff;
    }
    .header{
            border-bottom: 1px solid #f5f5f5;
            background-color: #fff;
    }
    body{
        background-image: url('https://i.yapx.ru/LYHV6.png');
        background-size: 100%;
    }

    @keyframes ryuk_anim {
        0%{
            transform: none;
        }
        100%{
            transform: rotate(360deg);
        }
    }
    #ryuk:hover{
        animation: ryuk_anim 1s infinite;
    }
    a{
        color: #00d6d6; font-family: DejaVu Sans Mono, monospace;
        transition: 0.5s;
        text-decoration: none;
    }
    a:hover{
        color:#047a7a;
        font-size: 110%;
        text-decoration: none;
    }
    #name{
    text-shadow: 0 0 0.5px #f5f5f5, 0 0 1px #0a0a0a, 0 0 2px #f5f5f5, 0 0 3px #0a0a0a, 0 0 4px #ffffff, 0 0 5px #0a0a0a, 0 0 100px #ffffff, 0 0 10px #ffffff; font-family: Sedan;font-style: normal;font-weight: normal;font-size: 28px;color: #FFFDFD;
    }
    #name:hover{
        font-size: 200%;
        text-decoration: none;
    }
</style>