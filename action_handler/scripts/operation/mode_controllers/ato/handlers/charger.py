import rospy
import threading 
import time
from action_handler_msgs.srv import action_srv

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
    parent  = obj 
    

current_request = None
running = False
def handle(request):
    global current_request, running
    current_request = request
    if not running:
        thread = threading.Thread(target = run)    
        thread.start()
    
threashold = 80
def run():
    global running
    parent['pause']('charging')
    running = True
    while not rospy.is_shutdown():
        if parent['status'] == 'halt':
            break
        elif (current_request['args']['basic_status'].is_charging == 0 or current_request['args']['basic_status'].is_dc_in == 0) and float(current_request['args']['basic_status'].battery_percentage) <= threashold:
            asq('interface/change_view_set/bootup')
            asq('navigation/go_home')
            time.sleep(30)
        else:
            asq('interface/change_view_set/main')
            if float(current_request['args']['basic_status'].battery_percentage) > threashold:
                break
        time.sleep(2)
    running = False
    parent['remove_interrupt'](current_request)
    parent['continue']('charging')
        