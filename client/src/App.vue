<template>
  <div id="app">
    <title>DeathNote | Русскоязычное вики</title>
    <nav class="navbar navbar-expand-md navbar-dark fixed-top " style='background-color: #002a32; '>
    <link rel="preconnect" href="https://fonts.gstatic.com">
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans:wght@700&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Shadows+Into+Light&display=swap" rel="stylesheet">
    <a id='name' class="navbar-brand" href="#">DeathNote</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarCollapse">
      <ul class="navbar-nav mr-auto">
        <li class="nav-item ">
          <a class="nav-link" href="http://localhost:8080/#/">Главная </a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="http://localhost:8080/#/wiki">Вики</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="http://localhost:8080/#/merch">Мерч</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="http://localhost:8080/#/view">Просмотр</a>
        </li>
      </ul>
    </div>
    </nav>
    <router-view/>
  </div>
</template>


<script>
export default {
  name: 'App',
};
</script>

<style>
@import url('/style.css');
#app {
  margin-top: 30px;
}


</style>
