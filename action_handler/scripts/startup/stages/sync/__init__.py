import time
import threading
import rospy


file_name = __file__.split('/')[-1][:-3]
if file_name == '__init__' or file_name == '__init__.':
    file_name = __file__.split('/')[-2]
def printLine(*args):
    '''
        prints information on the console screen
    '''
    global name
    print(file_name+': '+'\n      - '+'\n      - '.join([str(arg) for arg in list(args)]))
    
running_state = False
def is_running():
    global running_state
    return running_state

remote_interface = 'loading'
def get_remote_interface():
    global remote_interface
    return remote_interface

main_interface = 'loading'
def get_main_interface():
    global main_interface
    return main_interface

next_stage = 'power_stage'
def get_next_stage():
    global next_stage
    return next_stage

confirmation = None
def confirm(val):
    global confirmation
    confirmation = val

def start():
    global running_state
    running_state = True
    thread = threading.Thread(target=run)
    thread.start()
    return 'started'

def is_cancelled():
    global running_state, next_stage, remote_interface,confirmation
    if confirmation == 'end':
        running_state = False
        next_stage = 'power_stage'
        time.sleep(1)
        

def pick_map():
    global confirmation, remote_interface
    remote_interface = 'loading_existing_map'
    confirmation = 'is_picked'
    while not rospy.is_shutdown() and confirmation == 'is_picked':
        print(confirmation)
        time.sleep(1)
    is_cancelled()


def confirm_location():
    global confirmation, remote_interface
    remote_interface = 'confirm_position'
    confirmation = 'is_confirmed'
    while not rospy.is_shutdown() and confirmation == 'is_confirmed':
        print(confirmation)
        time.sleep(1)
    is_cancelled()

def run():
    global running_state, confirmation, remote_interface, next_stage
    running_state = True
    pick_map()
    ##printLine('running state', running_state)
    if running_state:
        confirm_location()
    remote_interface = 'loading'
    running_state = False
    time.sleep(1)
    
obj = {
    'confirm': confirm
}
        
        
    
    
    