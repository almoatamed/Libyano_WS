const express = require('express')
const router = express.Router()
const User = require('../database/models/user')
const bcrypt = require('bcrypt')
const env = require('../env')
const jwt = require('jsonwebtoken')

function generate(data){
    return jwt.sign({data}, env.jwt.secret, {expiresIn:'48h'})
}

router.post('/login',(req,res)=>{  
    try{
        // console.log('/api/auth/login: login request received,  ',req.body)
        User.findOne({username: req.body.username}).then((user)=>{
            // console.log('/api/auth/login: Database result are, ', user)
            if(!user) {
                // console.log('/api/auth/login: the provided username does not exist, ',user.username)
                res.status(404).json({message:'user not found'})}
            else {
                // console.log('/api/auth/login: User has been found')
                bcrypt.compare( req.body.password, user.password, (err,match)=>{
                    if(err) {
                        res.status(500).json({message: 'error while comparing password.', err})
                        // console.log('/api/auth/login: error while comparing the password, ', err)
                    }
                    else {
                        // console.log('/api/auth/login: password comparision succeed, ', match)
                        if(match){
                            res.status(200).json({token: generate({
                                username:user.username,
                                _id: user._id,
                            })});
                        }else{
                            res.status(403).json({message: 'password do not match'})
                        }
                    }
                })
            }
        }).catch(err=>{
            console.error(err)
            res.status(500).json({message:'error while accessing database', error:err})
        })
    }catch(e){
        res.status(500).json({message: 'server internal error',error:e})
    }
})

module.exports = router