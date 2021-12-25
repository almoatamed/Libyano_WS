import rospy
import threading
import time 
import rospy
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
        #printLine('error while taking action', e)
        return 'failed'
    
parent = {}
def init(obj):
    global parent 
    #printLine('server handler is initiallized', obj)
    parent = obj
    
current_request = None
running = False
def handle(request):
    global current_request 
    #printLine('serving a request', request)
    current_request = request
    if not running:
        thread = threading.Thread(target=run)
        thread.start()
        
def run():
    global running 
    if not (asq('interface/get_set') == 'main' and asq('interface/get_route') != 'slide-show'):
        asq('interface/change_route/language')
    parent['pause']('serving')
    running = True
    while not rospy.is_shutdown():
        time.sleep(1)
        if parent['status'] == 'halt':
            break
        elif not (asq('interface/get_route') != 'slide-show' and asq('interface/get_set') == 'main'):
            break
    running = False
    parent['remove_interrupt'](current_request)
    parent['continue']('serving')