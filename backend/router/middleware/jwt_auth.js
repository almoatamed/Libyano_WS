const jwt = require('jsonwebtoken');
const env = require('../../env');

function auth(req,res,next){
    const token = req.headers.authorization;
    if(!token) {res.status(403).json({message: 'not authorized'});}
    else{
        jwt.verify(token, env.jwt.secret, (err, value)=>{
            if(err) {res.status(421).json({message:'invalid token',err});}
            else{
                req.user = value.data;
                next();
            }
        })
    }
}

module.exports = {auth};