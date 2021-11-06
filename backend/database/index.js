const mongoose  = require('mongoose');
const app = require('..');

const dbURI = 'mongodb://127.0.0.1:27017/robot';
mongoose.connect(dbURI, {useNewUrlParser: true, useUnifiedTopology: true});
const db = mongoose.connection
db.on('error', err => {
    console.error(err)
});
db.once('open', ()=>{
    console.log('Database initiated')
});

module.exports = db