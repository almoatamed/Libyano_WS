#!/usr/bin/env python
import rospy
import os
import json

try:
    system_type = os.environ['SYSTEM_TYPE']
    if system_type not in ['J', 'R']:
        raise KeyError
except KeyError:
    system_type = 'G'
    
server_computers = ['G', 'R']

if system_type not in server_computers:
    exit()
    

home = os.environ['HOME']
distribution_path = home+'/catkin_ws/src/action_handler/scripts/distribution.json'
file = open(distribution_path,'r')
category_dictionary = json.load(file)
file.close()

file_name = __file__.split('/')[-1][:-3]
if file_name == '__init__' or file_name == '__init__.':
    file_name = __file__.split('/')[-2]
def printLine(*args):
    '''
        prints information on the console screen
    '''
    global name
    print(file_name+': '+'\n      - '+'\n      - '.join([str(arg) for arg in list(args)]))
    


action_service_name = rospy.get_param('/action/action_service_name','/action')
node_name = 'action_server'
anonymous = False
rospy.init_node(node_name, anonymous=anonymous)


from action_handler_msgs.srv import action_srvResponse,action_srv

def action_service_query(action,dev):
    global action_service_name
    action_query = action_service_name + '_' + dev
    rospy.wait_for_service(action_query)
    try: 
        take_action = rospy.ServiceProxy(action_query,action_srv)
        resp = take_action(action)
        return resp.result
    except rospy.ServiceException as e:
        #printLine('An error occured while trying to take an action ', e)
        return "failed"
    
def action_server(raw_req):
    try:
        dev_split = raw_req.action.split('&^')
        if len(dev_split) > 1:
            return action_srvResponse(action_service_query(dev_split[1],dev_split[0]))
        else:
            req = dev_split[0].split('/')
            if system_type == 'G':
                return action_srvResponse(action_service_query(dev_split[0],'G'))
            else:
                category = req[0]
                dev = category_dictionary[category]
                return action_srvResponse(action_service_query(dev_split[0],dev))
    except Exception as e:
        #printLine('Error while processing action',e)
        return 'failed'
        
if __name__ == "__main__":
        
    #printLine('starting Action Handler')

    ###############################################
    #parameters#
    ###############################################
    rospy.Service(action_service_name,action_srv,action_server )
    rospy.spin()