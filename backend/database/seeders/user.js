const User = require('../models/user');
const env = require('../../env');
const bcrypt = require('bcrypt');

module.exports = {   
    main(){
        return new Promise((resolve,reject)=>{
            User.findOne({username:'admin'}).then(user=>{
                if(!user){
                    bcrypt.hash('admin',env.bcrypt.rounds, (err, hash)=>{
                        if(err) {
                            // console.log(err)
                            reject(err)
                        } else {
                            const new_user = User({
                                username: 'admin',
                                password: hash
                            });
                            new_user.save().then((user => {
                                // console.log('seeded the administrative user',user.username);
                                resolve(user)
                            })).catch(err=>{
                                // console.log('error occured while trying to save administrative user');
                                reject(err)
                            });
                        }
                    })
                }else {
                    reject({message:'User seed already exists'})
                }
            }).catch(err=>{
                console.error(err)
                reject(error)
            });
        })
    }
}