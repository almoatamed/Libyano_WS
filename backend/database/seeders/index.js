const user_seeders = require('./user')


module.exports = {
    async run(){
        await user_seeders.main();
        return Promise.resolve();
    }
}

