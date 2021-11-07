# import subprocess
import os
import rospy
from action_handler_msgs.srv import action_srv

main_device  = '17:00:26:2B:0F:1D'


file_name = __file__.split('/')[-1][:-3]
if file_name == '__init__' or file_name == '__init__.':
    file_name = __file__.split('/')[-2]
def printLine(*args):
    '''
        prints information on the console screen
    '''
    global name
    print(file_name+': '+'\n      - '+'\n      - '.join([str(arg) for arg in list(args)]))
    
def asq(action):
    action_service_name = rospy.get_param('/action/action_service_name','/action')
    rospy.wait_for_service(action_service_name)
    try: 
        take_action = rospy.ServiceProxy(action_service_name,action_srv)
        resp = take_action(action)
        return resp.result
    except rospy.ServiceException as e:
        #printLine('An error occured while trying to take an action ', e)
        return "failed"

def connect(device):
    # try:
    #     subprocess.check_output(['hci','connect',main_device])
    #     return 'Done'
    # except subprocess.CalledProcessError:
    #     return 'failed'
    asq('bluetooth/disconnect')
    home = os.environ['HOME']
    os.system(home+'/catkin_ws/src/action_handler/scripts/bluetooth/connect.sh '+device)
    return 'done'

def connect_default(device):
    dev = asq('bluetooth/get_default')
    if dev == 'empty':
        return 'no_default'
    else:
        home = os.environ['HOME']
        os.system(home+'/catkin_ws/src/action_handler/scripts/bluetooth/connect.sh '+dev)
        return 'done'
