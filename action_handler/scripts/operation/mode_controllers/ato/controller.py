from __future__ import print_function
print('starting mnl script')
import threading
import rospy
import json
import os 
from action_handler_msgs.srv import action_srv
from scripts.operation.mode_controllers.ato.story_controller import controller as story_ctl


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

from scripts.operation.mode_controllers.ato.interrupters.power import power as power_interrupter
from scripts.operation.mode_controllers.ato.interrupters.screen import screen as screen_interrupter 
from scripts.operation.mode_controllers.ato.interrupters.facial_detection import face_detection as face_detection_interrupter 
interrupters = {
    'power': power_interrupter,
    'screen': screen_interrupter,
    'facial_detection': face_detection_interrupter,
}

from scripts.operation.mode_controllers.ato.handlers import charger as charger_handler
from scripts.operation.mode_controllers.ato.handlers import serve as serve_handler
interrupt_hanlders = {
    'charger': charger_handler,
    'serve': serve_handler
}

home = os.environ['HOME']
interrupt_config_json_path = home + '/catkin_ws/src/action_handler/scripts/operation/mode_controllers/ato/interrupt_config.json'

interrupt_config = {}
#api
def load_interrupt_config_json():
    global interrupt_config
    file = open(interrupt_config_json_path, 'r')
    interrupt_config = json.load(file)
    file.close()

load_interrupt_config_json()

def global_interrupt_validation(request):
    global obj
    if any(request['interrupter'] == req['interrupter'] and request['handler'] == req['handler'] for req in interrupt_queue):
        return False
    elif not interrupt_config[request['interrupter']]['enabled']: 
        return False
    else:
        return True


def local_interrupt_validation(request):
    global interrupters
    return interrupters[request['interrupter']].validate_interrupt()


def validate_interrupt(request):
    if global_interrupt_validation(request) and local_interrupt_validation(request):
        return True
    else:
        return False

interrupt_queue = []
def handle_interrupt(request):
    global interrupt_queue
    interrupt_queue.append(request)
    thread = threading.Thread(target=interrupt_hanlders[request['handler']].handle,args=(request,))
    thread.start()

def remove_interrupt(request):
    global interrupt_queue
    for req in interrupt_queue:
        if request['handler'] == req['handler']:
            interrupt_queue.remove(req)
    
    
def interrupt_request(request):
    '''
    An interrupt request is of the form 
    {
        'interrupter': 'name_of_the_interrupter',
        'handler': 'name_of_the_handler',
        'arge': {
            ...
        }
    }        
    
    based on these two and based on the running interrupts list 
    a global and local (in the interrupter it self) validation conditions is checked 
    to make sure that it is proper to be handled, if not the request is ignored
    '''
    if validate_interrupt(request):
        handle_interrupt(request)



def start():
    global obj
    if story_ctl.stories['default_story'] == '':
        return 'no_default_story'
    obj['status'] = 'running'
    return 'done'


def stop():
    global obj
    obj['status'] = 'halt'
    story_ctl.stop()
    return True
    
    

obj = {
    'status': 'halt',
    'pause': story_ctl.pause_story,
    'continue': story_ctl.continue_story,
    'interrupt_request': interrupt_request,
    'remove_interrupt': remove_interrupt,
    'interrupt_queue': interrupt_queue,
    'interrupt_config': interrupt_config,
    'stop': stop,
    'start': start,
}

story_ctl.init(obj)
charger_handler.init(obj)
power_interrupter.init(obj)
screen_interrupter.init(obj)
face_detection_interrupter.init(obj)
serve_handler.init(obj)

#api
def get_interrupt_queue():
    return json.loads(interrupt_queue)


face_detection_interrupter.start()