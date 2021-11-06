const events = require('events');

class Store extends events{
    build(skeleton){
        var self = this;
        self.models = {...skeleton.models};
        for( const model_name in self.models){

            for( const mutation_name in self.models[model_name].mutations)
            self.on([model_name,mutation_name ].join('/'),(arg)=>{
                self.models[model_name].mutations[mutation_name](self.models[model_name].state,arg);
                self.emit('__update'+mutation_name.slice(4));
            });

        }
    }

    dispatch(name, arg){
        var self = this;

        var model_name = name.split('/')[0]
        var action_name = name.split('/')[1]
        try {
            // console.log('dispatching, ', model_name, action_name)
            return self.models[model_name].actions[action_name](this,arg)            
        } catch (error) {
            return new Promise((reject)=>reject(error))
        }
    }

    commit(name, arg){
        this.emit(name,arg);
    }

    get(getter_name,cb){
        var self = this;
        var model_name = getter_name.split('/')[0]
        var getter_name = getter_name.split('/')[1]
        self.on('__update'+getter_name.slice(4),()=>{
            cb(self.models[model_name].getters[getter_name](self.models[model_name].state));
        });
        setTimeout(() => {
            cb(self.models[model_name].getters[getter_name](self.models[model_name].state));
        }, 10); 
    }

}

module.exports = Store