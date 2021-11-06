// state managment controller
const store = require('./store/index.js')

// express engine 
const express = require('express')

// ######################## Connecting to ros and initializing store ########################3
store.dispatch('Ros/set_voucher_checker')

store.dispatch('Ros/connect').then(()=>{
    console.log('connected and configured successfully');
}).catch(()=>{
    console.log('error occured')
})

// ######################## Database ########################3

// database controller
const db = require('./database/index')


// ######################## Routers ########################3
// requiring reouterd
const routes_auth = require('./router/auth')
const routes_ros = require('./router/ros')
const router_seeder = require('./router/seeder.js')
const router_test = require('./router/testing')

const app = express();

// Body Parser Middleware
app.use(express.json());
app.use(express.urlencoded({ extended: false }));

// routers
app.use('/api/auth', routes_auth)
app.use('/api/ros', routes_ros)
app.use('/api/seed',router_seeder)
app.use('/api/test',router_test)

// ######################## starting server ########################3


// working port
const port = 3421;
app.listen(port, ()=>{
    // console.log('started the server')
})

module.exports = app;  