const express = require('express')
const router = express.Router()
const store = require('../store/index.js');
const jwt_auth = require('./middleware/jwt_auth');
const Voucher = require('../database/models/voucher')

var connection_flag;
var mode;
var status;
var map;
var page;
//############################ store  ##########################################
store.get('Ros/get_ros', (flag) => {
    if (flag) {
        connection_flag = true;
    } else {
        connection_flag = false;
    }
});
store.get('Ros/get_mode', (robot_mode) => {
    mode = robot_mode
});
store.get('Ros/get_status', (robot_status) => {
    status = robot_status
});
var currentlocation;
store.get('Ros/get_current_location', (currentlocationres) => {
    currentlocation = currentlocationres;
});

//############################ Routes ##########################################

router.get('/connection', (req, res) => {
    return res.status(200).json({ connection: connection_flag });
});

router.get('/status', (req, res) => {
    return res.status(200).json({ status });
});

router.get('/currentlocation', (req, res) => {
    return res.status(200).json({ currentlocation });
});

router.get('/mode', (req, res) => {
    return res.status(200).json({ mode });
});

const time_gap = 5
var last_check = new Date().getTime()/1000.0
router.get('/voucher_check', (req, res) => {
    var time =  new Date().getTime()/1000.0
    if(time - last_check > time_gap){
        store.dispatch('Ros/check_vouchers').then((voucher) => {
            last_check = time
            console.log('voucher checking succeed', voucher)
            return res.status(200).json({ message: 'valid',   voucher })
        }).catch(err => {
            console.log('voucher checking failed', err)
            return res.status(205).json(err)
        })    
    }else{
        console.log('voucher checking failed')
        return res.status(205).json({message: 'failed'})
    }
    
})

router.get('/cash_reader_cancel', (req, res) =>{
    store.dispatch('Ros/cash_reader_cancel').then(()=>{
        console.log('cashreader action cancelled')
        return res.status(200).json({ message: 'cancelled'})
    }).catch(()=>{
        return res.status(500).json({message: 'failed'})
    })
})

router.post('/takein', (req, res) => {
    console.log('take in request ', req.body)
    val = req.body.val
    Voucher.find().where('val').equals(val).where('used').equals(false).exec((err, voucher) => {
        console.log('voucher exists',voucher.length)
        if (err) {
            return res.status(500).json({ message: 'error while trying to fetch voucher card', err })
        } else {
            if (voucher.length > 0) {
                console.log('taking in action')
                store.dispatch('Ros/take_action', 'cash_reader/cash_reader_takein/'+req.body.channel).then((result) => {
                    return res.status(200).json({ message: result })
                }).catch(() => {
                    return res.status(200).json({ message: 'failed' })
                })
            }else{
                return res.status(200).json({message: 'empty'})
            }
        }
    })
})

router.post('/relay',(req, res)=>{
    console.log('relay request ', req.body)
    store.dispatch('Ros/take_action', `control/set_relay/${req.body.number}/${req.body.value}.0`).finally(()=>{
        return res.status(200).json({message: 'done'})
    })
})

router.post('/action', (req, res) => {
    store.dispatch('Ros/take_action', req.body.action).then((result) => {
        return res.status(200).json({ message: result })
    }).catch(() => {
        return res.status(500).json({ message: 'failed' })
    })
})
module.exports = router