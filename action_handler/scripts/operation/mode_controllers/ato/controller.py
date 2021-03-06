from __future__ import print_function
print('starting mnl script')
import threading
import rospy
import json
import os 
from action_handler_msgs.srv import action_srv
from scripts.operation.mode_controllers.ato.story_controller import controller as story_ctl

############################################# Logging ##############################################

file_name = __file__.split('/')[-1][:-3]
if file_name == '__init__' or file_name == '__init__.':
    file_name = __file__.split('/')[-2]
def printLine(*args):
    '''
        prints information on the console screen
    '''
    print(file_name+': '+'\n      - '+'\n      - '.join([str(arg) for arg in list(args)]))

#################################### Action Server Query Proxy #####################################

def asq(action):
    action_service_name = '/action'
    rospy.wait_for_service(action_service_name)
    try:
        take_action = rospy.ServiceProxy(action_service_name, action_srv)
        resp = take_action(action)
        return resp.result
    except rospy.ServiceException as e:
        return 'failed'
    

##################################### Controlling Configuration ######################################

home = os.environ['HOME']
interrupt_config_json_path = home + '/catkin_ws/src/action_handler/scripts/operation/mode_controllers/ato/interrupt_config.json'

interrupt_config = {}

def load_interrupt_config_json():
    global interrupt_config
    file = open(interrupt_config_json_path, 'r')
    interrupt_config = json.load(file)
    obj['interrupt_config'] = interrupt_config
    file.close()


def update_interrupt_config_json():
    global interrupt_config
    obj['interrupt_config'] = interrupt_config
    file  = open(interrupt_config_json_path, 'w+')
    file.write(json.dumps(interrupt_config))
    file.close()


def validate_config_from_request(request):
    global interrupt_config 
    try:
        for interrupter in request:
            if type(request[interrupter]['enabled']) != bool or interrupter not in interrupt_config:
                return False
        return True
    except KeyError:
        return False
    
#api
def change_interrupt_config_json(json_string):
    global interrupt_config
    request = json.loads(json_string)
    if validate_config_from_request(request):
        interrupt_config = request
        update_interrupt_config_json()
        return 'Done'
    else:
        return "failed"

#api
def get_interrupt_config():
    global interrupt_config
    return json.dumps(interrupt_config)

################################ interrupt validation and handling #################################
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
    obj['interrupt_queue'] = interrupt_queue
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

###################################### Mode operation Control ######################################


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
    'interrupt_queue': {},
    'interrupt_config': interrupt_config,
    'stop': stop,
    'start': start,
}

load_interrupt_config_json()

############################### Importing Interrupters and Handlers ################################

from scripts.operation.mode_controllers.ato.interrupters.power import power as power_interrupter
from scripts.operation.mode_controllers.ato.interrupters.screen import screen as screen_interrupter 
interrupters = {
    'power': power_interrupter,
    'screen': screen_interrupter,
}


from scripts.operation.mode_controllers.ato.handlers import charger as charger_handler
from scripts.operation.mode_controllers.ato.handlers import serve as serve_handler
interrupt_hanlders = {
    'charger': charger_handler,
    'serve': serve_handler
}

story_ctl.init(obj)
charger_handler.init(obj)
power_interrupter.init(obj)
screen_interrupter.init(obj)
serve_handler.init(obj)

#api
def get_interrupt_queue():
    return json.loads(interrupt_queue)

try:
    from scripts.operation.mode_controllers.ato.interrupters.facial_detection import face_detection as face_detection_interrupter 
    interrupters['facial_detection'] =  face_detection_interrupter
    face_detection_interrupter.init(obj)
    face_detection_interrupter.start()
except ImportError:
    printLine('Error while trying to import facial detection models')
    pass
