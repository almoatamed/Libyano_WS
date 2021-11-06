import time
import threading 
import rospy
from action_handler_msgs.srv import action_srv


choice = 'no_choice'
running_state = False

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
        printLine('An error occured while trying to take an action ', e)
        return "failed"

def set_choice(selected_choice):
    global choice
    print('a choice has been made', choice)
    if selected_choice == 'end':
        res = asq('navigation/get_current_map')
        if not res:
            return 'no_map_set'
    choice = selected_choice

next_stage = 'chose_existing_map'
def run():
    global choice, remote_interface, next_stage, running_state
    choice = 'no_choice'
    remote_interface = 'choices'
    while choice == 'no_choice' and not rospy.is_shutdown():
        print('No Choice has been selected yet')
        time.sleep(1)
    next_stage = choice
    remote_interface = 'loading'
    time.sleep(2)
    running_state = False

def start():
    global running_state 
    running_state = True
    thread = threading.Thread(target=run)
    thread.start()
    return "started"
    
remote_interface = 'loading'
def get_remote_interface():
    global remote_interface
    return remote_interface

main_interface = 'loading'
def get_main_interface():
    global main_interface
    return main_interface

def is_running():
    global running_state
    return running_state

def get_next_stage():
    global next_stage
    return next_stage

obj = {
    'start': start,
    'is_running': is_running,
    'get_remote_interface': get_remote_interface,
    'get_main_interface': get_main_interface,
    'set_choice':set_choice
}

