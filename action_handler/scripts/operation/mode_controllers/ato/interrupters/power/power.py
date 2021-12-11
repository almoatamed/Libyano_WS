import time 
import threading 
import rospy
from action_handler_msgs.srv import action_srv
from slamware_ros_sdk.msg import RobotBasicState

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
    action_service_name = '/action'
    rospy.wait_for_service(action_service_name)
    try:
        take_action = rospy.ServiceProxy(action_service_name, action_srv)
        resp = take_action(action)
        return resp.result
    except rospy.ServiceException as e:
        printLine('error while taking action', e)
        return 'failed'


parent = {}
def init(obj):
    global parent
    parent = obj


request = {
    'interrupter': 'power',
    'handler':'charger', 
    'args': {
        'basic_status': RobotBasicState()
    }
}

current_status = None
printed_flag = False
def platform_basic_state_cb(state_message):
    global current_status, request, printed_flag
    current_status = state_message
    if not printed_flag:
        printed_flag = True
        printLine(request)
    request['args']['basic_status'] = current_status

platform_basic_state  = rospy.get_param('/platform/basic_state', '/slamware_ros_sdk_server_node/robot_basic_state')
rospy.Subscriber(platform_basic_state, RobotBasicState,platform_basic_state_cb)
    
def validate_interrupt():
    if asq('interface/get_set') == 'main' and asq('interface/get_route') != 'slide-show':
        return False
    else:
        return True

running = False
def run():
    global running
    while not rospy.is_shutdown() and running:
        time.sleep(2)
        try:
            if  parent['status'] != 'halt' or not current_status:
                time.sleep(5)
            elif float(current_status.battery_percentage) <= 15.0 and ( current_status.is_charging == 0 and current_status.is_dc_in == 0):
                parent['interrupt_request'](request)
        except KeyError as e:
            printLine('Error whiel trying to request power interrupt', e)
    
    
def start():
    global running
    if not running:
        running = True
        thread = threading.Thread(target=run)
        thread.start()

def stop():
    global running 
    running = False
    
start()