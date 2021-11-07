import threading
import time
import rospy
from slamware_ros_sdk.msg import RobotBasicState, MoveToRequest
from status_msgs.msg import goal_monitor_msg
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
    action_service_name = rospy.get_param('/action/action_service_name','/action')
    rospy.wait_for_service(action_service_name)
    try: 
        take_action = rospy.ServiceProxy(action_service_name,action_srv)
        resp = take_action(action)
        return resp.result
    except rospy.ServiceException as e:
        #printLine('An error occured while trying to take an action ', e)
        return "failed"

confirmation = 'nothing'
def confirm(val):
    global confirmation
    confirmation = val
    return 'confirmed'

def is_cancelled():
    global confirmation, running_state
    if confirmation == 'end':
        running_state = False
        end()


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

def start():
    global running_state
    running_state = True
    thread = threading.Thread(target=run)
    thread.start()
    return 'Done'

def scan():
    global confirmation, remote_interface, manual_controls
    remote_interface = 'slam_start_scanning'
    manual_controls = 'point_goal|cmd_vel'
    confirmation = 'is_started'
    while not rospy.is_shutdown() and confirmation == 'is_started':
        time.sleep(1)
    is_cancelled()    
    if not running_state:
        return 
    print(asq('navigation/switch/manual'))
    time.sleep(2)
    remote_interface = 'slam_finish_scanning'
    confirmation = 'is_finished_scanning'
    while not rospy.is_shutdown() and confirmation == 'is_finished_scanning':
        time.sleep(1)
    is_cancelled()
    if not running_state:
        return 
    confirmation = 'wants_to_go_home'
    remote_interface = 'slam_wants_to_go_home'    
    while not rospy.is_shutdown() and confirmation == 'wants_to_go_home':
        time.sleep(1)
    is_cancelled()
    if not running_state:
        return 
    remote_interface = 'loading'
    
def go_home():
    global robot_basic_state, remote_interface
    asq('navigation/switch/go_home')
    time.sleep(2)
    confirmation = 'is_subscirbed'
    while not rospy.is_shutdown() and confirmation == 'is_subscribed':
        time.sleep(1)
    while not robot_basic_state.is_charging and not rospy.is_shutdown():
        time.sleep(1)
    

robot_basic_state = RobotBasicState()
def robot_basic_state_cb(msg):
    global robot_basic_state, confirmation
    robot_basic_state = msg
    if confirmation == 'is_subscribed':
        confirmation = 'yes'


##################################################### recorder ##############################################################


def goal_monitor_cb(msg):
    global current_goal_monitor, current_goal
    # printLine(msg,current_goal)
    if abs(current_goal.location.x - msg.pose.x) < 0.2 and abs(current_goal.location.y - msg.pose.y) < 0.2 :
        current_goal_monitor = msg

def location_matched():
    global current_goal_monitor, current_goal
    return abs(current_goal.location.x - current_goal_monitor.pose.x) < 0.2 and abs(current_goal.location.y - current_goal_monitor.pose.y) < 0.2

def check_goal():
    global current_goal_monitor, goal_queue
    if current_goal_monitor.state == 'succeed' and location_matched():  
        #printLine('adding new goal to sequance', current_goal)
        goal_queue.append(current_goal)
    
def point_goal_cb(msg):
    global current_goal
    #printLine('received new goal', msg)
    check_goal()
    current_goal = msg
    
goal_queue = []
current_goal = MoveToRequest()
current_goal_monitor = goal_monitor_msg()
recorder_state = False
goal_monitor_sub = None
point_goal_sub = None
def run_recording_goals():
    global current_goal, current_goal_monitor, goal_queue, point_goal_sub, goal_monitor_sub, recorder_state
    goal_monitor_sub = rospy.Subscriber('/navigation/goal_monitor',goal_monitor_msg, goal_monitor_cb)
    point_goal_sub = rospy.Subscriber('/slamware_ros_sdk_server_node/move_to',MoveToRequest, point_goal_cb)
    while not rospy.is_shutdown() and recorder_state:
        time.sleep(1)
    goal_monitor_sub.unregister()
    point_goal_sub.unregister()

def get_recorded_goals():
    global goal_queue
    #printLine('getting goal queue',*goal_queue)
    return '|'.join(['&'.join([str(pose.location.x),str(pose.location.y)]) for pose in goal_queue])

def start_recording_goals():
    global recorder_state, goal_queue
    #printLine('starting goal recorded')
    goal_queue = []
    recorder_state = True
    thread = threading.Thread(target=run_recording_goals)
    thread.start()

def stop_recording_goals():
    global recorder_state
    recorder_state = False




#############################################################################################################################

def build_track():
    global confirmation, remote_interface, running_state, manual_controls
    remote_interface = 'slam_start_tracking'
    confirmation = 'is_started'
    while not rospy.is_shutdown() and confirmation == 'is_started':
        time.sleep(1)
    is_cancelled()    
    if not running_state:
        return 
    asq('navigation/switch/manual')
    time.sleep(2)
    start_recording_goals()
    remote_interface = 'slam_finish_track'
    manual_controls = 'point_goal'
    confirmation = 'is_track_finished'
    while not rospy.is_shutdown() and confirmation == 'is_track_finished':
        time.sleep(1)
    stop_recording_goals()
    is_cancelled()    
    if not running_state:
        return 
    remote_interface = 'slam_wants_to_go_home'
    confirmation = 'wantas_to_go_home'
    while not rospy.is_shutdown() and confirmation == 'wants_to_go_home':
        time.sleep(1)
    is_cancelled()    
    if not running_state:
        return 
    remote_interface = 'loading'

def save_map_files():
    pass
    
def save_map():
    global confirmation, remote_interface
    remote_interface = 'slam_save_scanned_map'
    confirmation = 'is_saved'
    while not rospy.is_shutdown() and confirmation == 'is_saved':
        time.sleep(1)
    is_cancelled()
    if not running_state:
        return 
    save_map_files()
    remote_interface = 'loading'
    
    
sub = None
def run():
    global remote_interface, running_state, sub
    running_state = True
    asq('navigation/switch/pass')
    sub = rospy.Subscriber('/slamware_ros_sdk_server_node/robot_basic_state', RobotBasicState, robot_basic_state_cb)
    time.sleep(2)    
    scan()
    if running_state == True:
        go_home()
    if running_state == True:
        build_track()
    if running_state == True:
        go_home()
    if running_state == True:
        save_map()
    end()

def end():
    global sub, running_state, remote_interface
    try:
        sub.unregister()
    except Exception as err:
        print('Error while unregidtering sub', err)
    asq('navigation/switch/pass')
    remote_interface = 'loading'
    running_state = False
    time.sleep(2)

next_stage = 'power_stage'
def get_next_stage():
    global next_stage 
    return next_stage

manual_controls = 'point_goal'
def get_manual_controls():
    global manual_controls
    return manual_controls




obj = {
    'confirm': confirm, 
    'start':start,
    'get_next_stage':get_next_stage,
    'get_remote_interface':get_remote_interface,
    'get_main_interface': get_main_interface,
    'is_running': is_running,
    'get_recorded_goals': get_recorded_goals,
    'get_manual_controls': get_manual_controls
}

