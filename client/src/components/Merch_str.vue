<template>
    <div style='box-shadow: 0 0 5px 2px #00404C;font-family: Noto Sans, sans-serif; padding-left: 30px; padding:20px;height:100%;border-radius:10px;background-color:rgba(0, 42, 50, 0.95); margin-top:90px; margin-left:100px; margin-right:100px;color: #BABABA;'>
        <h1 style='font-size: 30px;'><a href='http://localhost:8080/#/merch'><button style='margin-left:10px;border-color: black; background-color: #001e24;font-size:10px' type="button" class="btn btn-primary">←</button></a>  {{title}}</h1>
        <div style='width:1000px;'>
            <p style=''><img :src='this.image' width='30%' height='30%'></p>
            <p>{{about}}</p>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    
    data() {
        var paramsString = document.location.hash;
        var params_2 = paramsString.replace('#','')
        return {
            id: '',
            title: '',
            image: '',
            cost: '',
            path_piece: params_2,
            paths: '',
            about: ''
        };
    },
    methods: {
        getItem(){
            let headers = new Headers();
            headers.append('Access-Control-Allow-Origin', 'http://localhost:8080');
            headers.append('Access-Control-Allow-Credentials', 'true');
            axios.defaults.headers.common['header1'] = headers // for POST requests
            var path = 'http://localhost:5000/';
            path += this.path_piece.replace('', '');
            axios.get(path)
                .then((res) => {
                this.title = res.data.item_title;
                this.image = res.data.item_image;
                this.cost = res.data.item_cost;
                this.about = res.data.item_about;
                },
                )
                .catch((error) => {
                // eslint-отключение следующей строки
                console.error(error);
                });
        }
    },
    created() {
        this.getItem();
    },
};
</script>