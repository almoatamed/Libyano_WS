const Voucher = require('../models/voucher')

function fixed_rand_str(length) {
    val = Math.floor(Math.random() * (10 ** length)).toString()
    while (val.length < length) {
        val = '0' + val
    }
    return val
}

module.exports = {
    main() {
        return new Promise((resolve, reject) => {
            try {
                for (let i = 0; i < 100; i++) {
                    voucher = new Voucher({
                        secret: fixed_rand_str(13),
                        serial: fixed_rand_str(10),
                        val: i % 2 ? 10 : 5,
                        used: false
                    })
                    console.log(voucher)
                    voucher.save().then(() => { })
                }
                resolve({ message: 'Done' })
            } catch (error) {
                reject(error)
            }
        })
    },
    load(voucher) {
        return new Promise((resolve, reject) => {
            voucher.forEach(voucher => {
                Voucher.findOne({ serial: voucher.Serial }).then(v => {
                    if(!v){
                        console.log(v)
                        card = new Voucher({
                            secret: voucher.PIN,
                            serial: voucher.Serial,
                            val: voucher.Value,
                            used: false
                        })
                        console.log(card)
                        card.save().then(() => { })
                    }
                })
            })
            resolve({ message: 'Done' })
        })
    }
}