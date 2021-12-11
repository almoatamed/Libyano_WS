import rospy
from action_handler_msgs.srv import action_srv
import os
import time
import threading
from std_msgs.msg import String


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
    

home = os.environ['HOME']
acts_file_path = home + '/catkin_ws/src/action_handler/scripts/act_manager/actions.txt'
def decode_acts():
    global acts_file_path    
    file = open(acts_file_path, 'r')
    acts = file.read()
    file.close()
    if acts:
        acts = acts.split('$')
        acts = {act.split(':')[0]:act.split(':')[1].split('|') for act in acts}
        return acts
    else:
        return {}

def encode_acts(acts):
    return '$'.join([':'.join([act,'|'.join(acts[act])]) for act in acts])
    
def get_acts():
    global acts_file_path
    file = open(acts_file_path, 'r')
    acts = file.read()
    file.close()
    return acts
    
def get_acts_names():
    global acts_file_path
    acts = decode_acts()
    return '|'.join(acts.keys())

    
def add_act(act):
    global acts_file_path, update_acts
    #printLine('adding act ', act)
    acts = decode_acts()
    act = act.replace('&','/')
    act = act.split(':')
    acts[act[0]] = act[1].split('|')
    acts = encode_acts(acts)
    file = open(acts_file_path, 'w+')
    file.write(acts)
    file.close()
    return 'Done'


def del_act(act_name):
    global acts_file_path, update_acts
    acts = decode_acts()
    #printLine('deleting act', act_name)
    if act_name in acts:
        acts.pop(act_name)
        acts = encode_acts(acts)
        file = open(acts_file_path, 'w+')
        file.write(acts)
        file.close()
        return 'Done'
    else:
        return 'not_found'
        
act_queue= [] 
pause = False

def wait_for_goal_end():
    #printLine('waiting for goal')
    time.sleep(3)
    if asq('navigation/goal_monitor_get_last_state') == 'running':
        time.sleep(0.25)
    return 

def perform_navigation(action_args):
    #printLine('performing navigation action ', action_args)
    if action_args[2] == 'angled':
        #printLine('angled action ', 'navigation/angled_goal/'+'&'.join(action_args[4:]))
        asq('navigation/angled_goal/'+'&'.join(action_args[4:]))
    else:
        #printLine('unngled action ', 'navigation/unangled_goal/'+'&'.join(action_args[4:]))
        asq('navigation/unangled_goal/'+'&'.join(action_args[4:]))
    if action_args[1] == 'wait':
        wait_for_goal_end()
    

def perform(action):
    action_args = action.split('/')
    if action_args[0] == 'navigation':
        perform_navigation(action_args)
        #printLine('navigation has been performed')
    elif action_args[0] == 'wait':
        #printLine('waiting ',action_args[1])
        sleep_time = float(action_args[1])/1000
        int_sleep_time = int(sleep_time)
        fraction_sleep_time = sleep_time - int_sleep_time
        for _ in range(int_sleep_time):
            if len(act_queue) == 0:
                break
            time.sleep(1)
        time.sleep(fraction_sleep_time)
    elif action_args[0] == 'interface':
        asq('interface/force_change_view_set/'+action_args[1])
    elif action_args[0] == 'eyes emoji':
        asq('interactive/set_eyes/'+ '/'.join(action_args[1:]))
        time.sleep(0.05)
    elif action_args[0] == 'led ring':
        asq('interactive/set_ring_flow/'+ '/'.join(action_args[1:]))
        time.sleep(0.05)
    elif action_args[0] == 'led strip':
        asq('interactive/set_strip_color/'+ action_args[1])
    elif action_args[0] == 'speak':
        asq('interactive/speak_push_to_queue/'+ action_args[1]+ '.mp3')
    elif action_args[0] == 'head motion':
        asq('interactive/head_play_motions_by_name/'+ action_args[1])
    else:
        asq('/'.join(action_args[1:]))

running_action = ''
def threaded_act_player():
    global act_queue, pause, running_action
    #printLine('starting Act Manager')
    while not rospy.is_shutdown(): 
        if act_queue and not pause:
            running_action = action = act_queue[0]
            #printLine('performing action ', action)
            # t_start= time.time()
            perform(action)
            printLine('performed act ', action)
            try:
                act_queue.pop(0)
            except IndexError:
                pass
            #printLine('action took ', time.time() - t_start)
        else:
            running_action = ''
            time.sleep(0.3)

thread = threading.Thread(target=threaded_act_player)
thread.start()


def toggle_pause(val):
    global pause
    if val == '1':
        pause = True
        stop()
    else:
        pause = False
    return 'Done'
    
def is_paused():
    global pause
    return pause

def clear_queue():
    global act_queue
    act_queue = []
    return 'Done'
    
def stop():
    asq('navigation/stop')
    asq('interactive/speak_set_stop')
    asq('interactive/set_eyes/clear/0/1')
    asq('interactive/set_strip_color/0/0/0')
    asq('interactive/set_ring_flow/off')
    return 'Done'
    
def stop_and_clear():
    clear_queue()
    stop()
    return 'Done'

def push_to_queue_by_act(act):
    global act_queue
    #printLine('pushing by action', act)
    act = act.replace('&','/')
    act_queue = act_queue + act.split('|')
    return 'Done'
    
    
def play_new_act_by_act(act):
    global act_queue
    #printLine('playing by action', act)
    act = act.replace('&','/')
    stop_and_clear()
    act_queue = act.split('|')
    return 'Done'

def push_to_queue_by_name(act_name):
    global act_queue
    acts = decode_acts()
    if act_name not in acts:
        printLine('act has not been found', act_name)
        return 'not_found'
    printLine('pushing by name',act_name, acts[act_name])
    act_queue= act_queue + acts[act_name]
    return 'Done'

        
def play_new_act_by_name(act_name):
    global act_queue
    acts = decode_acts()
    if act_name not in acts:
        return 'not_found'
    #printLine('playing by name',act_name, acts[act_name])
    stop_and_clear()
    act_queue = acts[act_name]
    return 'Done'
    
def get_queue_length():
    global act_queue
    return str(len(act_queue))
    
    
queue_len_pub = rospy.Publisher('/act/act_queue_length', String, queue_size=2)
string_msg= String()
def queue_len_pub_thread():
    global string_msg, queue_len_pub
    while not rospy.is_shutdown():
        time.sleep(0.1)
        queue_len_pub.publish(str(len(act_queue)))
queue_len_thread = threading.Thread(target=queue_len_pub_thread)
queue_len_thread.start()


running_action_pub = rospy.Publisher('/act/running_action', String, queue_size=2)
string_msg2= String()
def running_action_pub_function():
    global string_msg2, running_action_pub
    while not rospy.is_shutdown():
        time.sleep(0.1)
        running_action_pub.publish(str(running_action))
running_action_thread = threading.Thread(target=running_action_pub_function)
running_action_thread.start()