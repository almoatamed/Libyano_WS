from __future__ import print_function
import rospy 
import threading 
import time
from  action_handler_msgs.srv import action_srv
from std_msgs.msg import String
parent = {
    'status': 'halt'
}
def init(obj):
    global parent 
    parent = obj
    



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
    
running  = False
def start():
    global running 
    if not running: 
        running = True
        thread = threading.Thread(target = run)
        thread.start()

def validate_interrupt():
    return True

request = {
    'interrupter': 'screen',
    'handler': 'serve', 
    'args':{
        'route': '', 
        'set': ''
    }
}

interface  = '/'
def interface_cb(msg):
    global interface
    interface = msg.data.split('/')
    request['args']['rourte'] = interface[1]
    request['args']['set'] = interface[0]
rospy.Subscriber('/interface/set_slash_route', String, interface_cb)

def run():
    global parent, running 
    while not rospy.is_shutdown() and running:
        if parent['status'] == 'halt':
            time.sleep(5)
        elif interface[0] == 'main' and interface[1] != 'slide-show':
            parent['interrupt_request'](request)
        else:
            time.sleep(0.25)   

def stop():
    global running
    running = False
    
start()
        
    