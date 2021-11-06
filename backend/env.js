const jwt = require('jsonwebtoken')

module.exports = {
    bcrypt:{
        rounds: 10
    },
    jwt:{
        secret: 'dontMissWithMe',
        expiresIn: '48h'
    }
}