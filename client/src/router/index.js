import Vue from 'vue';
import Router from 'vue-router';
import Ping from '@/components/Ping';
import Wiki from '@/components/Wiki';
import Articles from '@/components/Articles';
import Shop from '@/components/Shop';
import Merch from '@/components/Merch';
import View from '@/components/View';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/ping',
      name: 'Ping',
      component: Ping,
    },
    {
      path: '/',
      name: 'Articles',
      component: Articles,
    },
    {
      path: '/wiki',
      name: 'Wiki',
      component: Wiki,
    },
    {
      path: '/wiki/:str',
      name: 'wikis',
      component: Shop,
    },
    {
      path: '/merch',
      name: 'merch',
      component: Merch,
    },
    {
      path: '/view',
      name: 'view',
      component: View,
    },
    
    
  ],
});
