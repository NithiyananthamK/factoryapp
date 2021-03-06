import Vue from 'vue'
import Router from 'vue-router'

// Containers
const DefaultContainer = () => import('@/containers/DefaultContainer')

// Views
const orders = () => import('@/components/factoryapp/orderslist')
const Login = () => import('@/views/Login')
const add_order = () => import('@/components/factoryapp/add_order')
const products = () => import('@/components/factoryapp/order_page')
const adduser_order = () => import('@/components/factoryapp/adduser_order')
const myorders = () => import('@/components/factoryapp/myorders')
const alluser_orders = () => import('@/components/factoryapp/alluser_orders')
const change_orderstatus = () => import('@/components/factoryapp/change_orderstatus')

Vue.use(Router)

export default new Router({
  mode: 'hash',
  linkActiveClass: 'open active',
  scrollBehavior: () => ({ y: 0 }),
  routes: [
    {
      path: '/home',
      name: '',
      component: DefaultContainer,

      children: [
        {
          path: '/home',
          name: 'myorders',
          component: myorders
        },
        {
          path: '/orders',
          name: 'orders',
          component: orders
        },
        {
          path: '/add_order',
          name: 'add_order',
          component: add_order
        },
        {
          path: '/products',
          name: 'products',
          component: products
        },
        {
          path: '/adduser_order',
          name: 'adduser_order',
          component: adduser_order
        },
        {
          path: '/myorders',
          name: 'myorders',
          component: myorders
        },
        {
          path: '/alluser_orders',
          name: 'alluser_orders',
          component: alluser_orders
        },
        {
          path: '/change_orderstatus',
          name: 'change_orderstatus',
          component: change_orderstatus
        }

      ]
    },
    {
      path: '/',
      name: 'Login',
      component: Login
    },
  ]
})
