#!/usr/bin/env python
from __future__ import print_function
import rospy
import os 
import sys
from action_handler_msgs.srv import action_srvResponse,action_srv


try:
    system_type = os.environ['SYSTEM_TYPE']
    if system_type not in ['J', 'R']:
        raise KeyError
except KeyError:
    system_type = 'G'
    

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
                                 
try:
    system_type = os.environ['SYSTEM_TYPE']
    if system_type not in ['J', 'R']:
        raise KeyError
except KeyError:
    system_type = 'G'
    
file_name = __file__.split('/')[-1][:-3]
if file_name == '__init__' or file_name == '__init__.':
    file_name = __file__.split('/')[-2]
def printLine(*args):
    '''
        prints information on the console screen
    '''
    global name
    print(file_name+': '+'\n      - '+'\n      - '.join([str(arg) for arg in list(args)]))
    
node_name = 'action_handler_' + system_type
anonymous = False
rospy.init_node(node_name, anonymous=anonymous)

home = os.environ['HOME']
distribution_path = home+'/catkin_ws/src/action_handler/scripts/distribution.txt'
file = open(distribution_path,'r')
distribution = file.read()
category_dictionary = {i[0]:i[1] for i in [j.split(':') for j in distribution.split('\n')]}
file.close()

actions = {}
if system_type != 'G':
    if system_type == category_dictionary['navigation']:
        import scripts.navigation
        actions['navigation'] = scripts.navigation.Actions
        printLine('import navigation controller')
    if system_type == category_dictionary['act']:
        import scripts.act_manager
        actions['act'] = scripts.act_manager.Actions
        printLine('import act manager')
    if system_type == category_dictionary['control']:
        import scripts.control
        actions['control'] = scripts.control.Actions
        printLine('import control')
    if system_type == category_dictionary['system']:
        import scripts.system
        actions['system'] = scripts.system.Actions
        printLine('import system')
    if system_type == category_dictionary['cash_reader']:
        import scripts.cash_reader
        actions['cash_reader'] = scripts.cash_reader.Actions
        printLine('import cash_reader')
        
    if system_type == category_dictionary['bluetooth']:
        import scripts.bluetooth
        actions['bluetooth'] = scripts.bluetooth.Actions
        printLine('import bluetooth')
        
    if system_type == category_dictionary['startup']:
        import scripts.startup
        actions['startup'] = scripts.startup.Actions
        printLine('import startup')
        
    if system_type == category_dictionary['interactive']:
        import scripts.interactive
        actions['interactive'] = scripts.interactive.Actions
        printLine('import interactive')
        
    if system_type == category_dictionary['global_actions']:
        import scripts.global_actions
        actions['global_actions'] = scripts.global_actions.Actions
        printLine('import global actions')
        
    if system_type == category_dictionary['interface']:
        import scripts.interface
        actions['interface'] = scripts.interface.Actions
        printLine('import interface controller')
        
else:
    printLine('Loading G Actions')
    import scripts.navigation
    actions['navigation'] = scripts.navigation.Actions
    import scripts.control
    actions['control'] = scripts.control.Actions
    import scripts.system
    actions['system'] = scripts.system.Actions
    import scripts.cash_reader
    actions['cash_reader'] = scripts.cash_reader.Actions
    import scripts.bluetooth
    actions['bluetooth'] = scripts.bluetooth.Actions
    import scripts.startup
    actions['startup'] = scripts.startup.Actions
    import scripts.interactive
    actions['interactive'] = scripts.interactive.Actions
    import scripts.global_actions
    actions['global_actions'] = scripts.global_actions.Actions
    import scripts.interface
    actions['interface'] = scripts.interface.Actions
    import scripts.act_manager
    actions['act'] = scripts.act_manager.Actions
    
def action_handler(req):
    req = req.action.split('/')
    category = req[0]
    action = req[1]
    if category in actions:
        if action in actions[category]:
            # printLine('Initiating action of '+str(req))
            if len(req)>2:
                args = tuple(arg for arg in req[2:])
                return action_srvResponse(actions[category][action](*args))
            else: 
                return action_srvResponse(actions[category][action]())
        else:
            printLine('action has not been found')
            return 'failed'
    else:
        printLine('category has not been found')
        return 'failed'
    
        


if __name__ == "__main__":
    
    printLine('starting Action Handler')

    ###############################################
    #parameters#
    ###############################################
    action_service_name = rospy.get_param('/action/action_service_name', '/action')+'_'+system_type
    rospy.Service(action_service_name,action_srv, action_handler)
    rospy.spin()