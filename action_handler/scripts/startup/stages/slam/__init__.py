import threading
import time
import rospy
import os
from slamware_ros_sdk.msg import RobotBasicState
from slamware_ros_sdk.srv import SyncGetStcm
from action_handler_msgs.srv import action_srv
from geometry_msgs.msg import Pose

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
    
current_pose = None
current_pose_sub = None
def current_pose_cb(msg):
    global current_pose
    current_pose = msg 

def save_map_file(name):
    home = os.environ['HOME']
    try:
        os.mkdir(home+'/catkin_ws/src/public/maps/'+name)
    except Exception as e:
        print(e)
    rospy.wait_for_service('slamware_ros_sdk_server_node/sync_get_stcm')
    service = rospy.ServiceProxy('slamware_ros_sdk_server_node/sync_get_stcm',SyncGetStcm)
    resp = service()
    file = open(home+'/catkin_ws/src/public/maps/'+name+'/map.stcm', 'wb+')
    file.write(resp.raw_stcm)
    file.close()
    file = open(home+'/catkin_ws/src/public/maps/'+name+'/pose.txt', 'w+')
    file.write('&'.join([
        str(current_pose.position.x),
        str(current_pose.position.y),
        str(current_pose.position.z),
        str(current_pose.orientation.x),
        str(current_pose.orientation.y),
        str(current_pose.orientation.z),
        str(current_pose.orientation.w)
        ]))
    file.close()
    
    
def save_map():
    global confirmation, remote_interface, current_pose_sub
    remote_interface = 'slam_save_scanned_map'
    confirmation = 'is_saved'
    while not rospy.is_shutdown() and confirmation == 'is_saved':
        time.sleep(1)
    name = confirmation 
    remote_interface = 'loading'
    current_pose_sub = rospy.Subscriber('/current_pose', Pose, current_pose_cb)
    while not rospy.is_shutdown() and not current_pose:
        time.sleep(1)
    current_pose_sub.unregister()
    save_map_file(name)
    is_cancelled()
    if not running_state:
        return 
    save_map_file(name)
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
    'get_manual_controls': get_manual_controls
}

