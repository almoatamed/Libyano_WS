const express = require('express')
const router = new express.Router();
const User = require('../database/models/user')
const jwt_auth = require('./middleware/jwt_auth');

router.get('/find',(req,res)=>{
    User.find({username:'a'}).then(data=>{
        // console.log(data);
        res.status(200).json(data);
    })
})
router.get('/arabic', (req,res)=>{
    res.json({
        message:'السلام عليكم'
    })
})
router.get('/auth',jwt_auth.auth,(req,res)=>{
    User.findOne({username:'admin'}).then(data=>{
        // console.log(data);
        res.json(data);
    })
})
module.exports = router;