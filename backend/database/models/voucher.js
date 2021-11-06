const mongoose  = require('mongoose')

const model = mongoose.Schema({
    secret: {
        type: String,
        required: true
    },
    serial: {
        type: String,
        required: true
    },
    val:{
        type: Number,
        required: true
    },
    used: {
        type: Boolean, 
        required: true
    }
});

module.exports = new mongoose.model('voucher', model)