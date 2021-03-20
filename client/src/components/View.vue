<template>
    <div style='box-shadow: 0 0 5px 2px #00404C;font-family: Noto Sans, sans-serif; padding-left: 30px; padding:20px;height:100%;border-radius:10px;background-color:rgba(0, 42, 50, 0.95); margin-top:90px; margin-left:100px; margin-right:100px;color: #BABABA;'>
        <h1 style='font-size:25px'>DeathNote | Просмотр </h1>
        <video width='800px' height='500px' controls='controls' poster='https://r270104.kujo-jotaro.com/death-note/1.480.b9415bf64b43e619.mp4?hash1=ae1ea91271edd432d4551905e9afde6e&hash2=5ba3deaabcec3a258463534a1ce987e3'>
            <source :src='url'>
        </video>
        <div>
            <h1><button  v-on:click="addWiki" style='margin-left:10px;border-color: black; background-color: #001e24;' type="button" class='btn btn-primary'>1 серия</button><button  v-on:click="addWiki" style='margin-left:10px;border-color: black; background-color: #001e24;' type="button" class='btn btn-primary'>2 серия</button><button  v-on:click="addWiki" style='margin-left:10px;border-color: black; background-color: #001e24;' type="button" class='btn btn-primary'>3 серия</button><button  v-on:click="addWiki" style='margin-left:10px;border-color: black; background-color: #001e24;' type="button" class='btn btn-primary'>4 серия</button><button  v-on:click="addWiki" style='margin-left:10px;border-color: black; background-color: #001e24;' type="button" class='btn btn-primary'>5 серия</button><button  v-on:click="addWiki" style='margin-left:10px;border-color: black; background-color: #001e24;' type="button" class='btn btn-primary'>6 серия</button><button  v-on:click="addWiki" style='margin-left:10px;border-color: black; background-color: #001e24;' type="button" class='btn btn-primary'>7 серия</button><button  v-on:click="addWiki" style='margin-left:10px;border-color: black; background-color: #001e24;' type="button" class='btn btn-primary'>7 серия</button><button  v-on:click="addWiki" style='margin-left:10px;border-color: black; background-color: #001e24;' type="button" class='btn btn-primary'>8 серия</button><button  v-on:click="addWiki" style='margin-left:10px;border-color: black; background-color: #001e24;' type="button" class='btn btn-primary'>9 серия</button><button  v-on:click="url=url1" style='margin-left:10px;border-color: black; background-color: #001e24;' type="button" class='btn btn-primary'>10 серия</button></h1>
            <h1><button  v-on:click="addWiki" style='margin-left:10px;border-color: black; background-color: #001e24;' type="button" class='btn btn-primary'>11 серия</button><button  v-on:click="addWiki" style='margin-left:10px;border-color: black; background-color: #001e24;' type="button" class='btn btn-primary'>12 серия</button><button  v-on:click="addWiki" style='margin-left:10px;border-color: black; background-color: #001e24;' type="button" class='btn btn-primary'>13 серия</button><button  v-on:click="addWiki" style='margin-left:10px;border-color: black; background-color: #001e24;' type="button" class='btn btn-primary'>14 серия</button><button  v-on:click="addWiki" style='margin-left:10px;border-color: black; background-color: #001e24;' type="button" class='btn btn-primary'>15 серия</button><button  v-on:click="addWiki" style='margin-left:10px;border-color: black; background-color: #001e24;' type="button" class='btn btn-primary'>16 серия</button><button  v-on:click="addWiki" style='margin-left:10px;border-color: black; background-color: #001e24;' type="button" class='btn btn-primary'>17 серия</button><button  v-on:click="addWiki" style='margin-left:10px;border-color: black; background-color: #001e24;' type="button" class='btn btn-primary'>17 серия</button><button  v-on:click="addWiki" style='margin-left:10px;border-color: black; background-color: #001e24;' type="button" class='btn btn-primary'>18 серия</button><button  v-on:click="addWiki" style='margin-left:10px;border-color: black; background-color: #001e24;' type="button" class='btn btn-primary'>19 серия</button></h1>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {

  data() {
    return {
        url1: 'https://r56.kujo-jotaro.com/death-note/10.480.8397fda20ab88f24.mp4?hash1=6924fae39b8f95e8ddcf06f02c28a5fd&hash2=63115801513aa02cb4d8f2dbaea229b5',
        url: 'https://r270104.kujo-jotaro.com/death-note/1.480.b9415bf64b43e619.mp4?hash1=ae1ea91271edd432d4551905e9afde6e&hash2=5ba3deaabcec3a258463534a1ce987e3'
    };
  },
  
    methods: {
    }
}
</script>
