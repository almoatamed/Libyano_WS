export default {
    namespaced: true,
    actions:{
        check({dispatch}, error){
            var err = error.toJSON()
            console.log('checking error')
            let rjct  = {err:err}
            if(err.message == 'Network Error'){
                dispatch('Notify/notify', { group: 'main', text: 'please check the connection with the Robot.', title: 'Network Error', type:'error'}, {root:true});
                rjct.to = 'noNetwork';
            }
            else if (err.message == 'Request failed with status code 404'){
                dispatch('Notify/notify', { group: 'main', text: 'this page does not exist.', title: 'Page Not Found', type:'error'}, {root:true});
                rjct.to = 'notFound';
            }
            else{
                dispatch('Notify/notify', { group: 'main', text: 'please contact the robot maintainers.', title: 'Robot Server Error', type:'error'}, {root:true});
                rjct.to = 'RobotServerError';
            }
            return rjct
        }
    }
}