const store_scaleton = require('./skeleton');
const Store = require('./store')

const store = new Store()

store.build(store_scaleton);

module.exports = store;