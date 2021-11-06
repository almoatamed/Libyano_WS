const express = require('express');
const router = new express.Router();
const seeder = require('../database/seeders/index')
const user_seeder  = require('../database/seeders/user')
const voucher_seeder = require('../database/seeders/voucher')
router.get('/',(req,res)=>{
    seeder.run().then(()=>{
        res.status(200).json({done:true});
    }).catch(err=>{
        res.status(500).json({message:'failed'})
    });
})

router.get('/user',(req,res)=>{
    user_seeder.main().then((user)=>{
        res.status(200).json(user);
    }).catch(err=>{res.status(500).json(err)});
})

router.get('/vouchers',(req,res)=>{
    voucher_seeder.main().then((msg)=>{
        res.status(200).json(msg);
    }).catch(err=>{res.status(500).json(err)});
})
router.post('/load_vouchers',(req,res)=>{ 
    console.log('voucher load request', req.body.vouchers.length)
    voucher_seeder.load(req.body.vouchers).then((msg)=>{
        res.status(200).json(msg);
    }).catch(err=>{res.status(500).json(err)});
})
module.exports = router;