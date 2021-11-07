import time
import threading 
from slamware_ros_sdk.msg import RobotBasicState, ClearMapRequest
import rospy
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
    

def action_service_query(action):
    action_service_name = rospy.get_param('/action/action_service_name','/action')
    rospy.wait_for_service(action_service_name)
    try: 
        take_action = rospy.ServiceProxy(action_service_name,action_srv)
        resp = take_action(action)
        return resp.result
    except rospy.ServiceException as e:
        #printLine('An error occured while trying to take an action ', e)
        return "failed"


confirmation = False
running_state = False

def confirm(val):
    global confirmation 
    confirmation = val

def is_running():
    return running_state


robot_basic_state = RobotBasicState()
def robot_basic_state_cb(msg):
    global robot_basic_state, confirmation
    if confirmation == 'no_messages':
        #printLine('received message')
        confirmation = 'yeah'
    robot_basic_state = msg
    
sub = None

def remove_dc_cord():
    global remote_interface, robot_basic_state
    remote_interface = 'remove_dc_cord'
    while robot_basic_state.is_dc_in:
        #printLine('Dc Cord is in ', robot_basic_state.is_dc_in)
        time.sleep(1)
    remote_interface = 'loading'

def is_placed_properly():
    global confirmation, remote_interface
    action_service_query('navigation/switch/manual')
    remote_interface = 'confirm_initial_position'
    time.sleep(3)
    confirmation = 'is_placed_properly'
    while confirmation == 'is_placed_properly':
        #printLine('waiting for confirmation')
        time.sleep(1)
    remote_interface = 'loading'
    
def is_the_robot_in_charging_spot():
    global confirmation, remote_interface
    action_service_query('navigation/switch/pass')
    remote_interface = 'is_the_robot_charging'
    time.sleep(2)
    confirmation = 'is_the_robot_charging'
    while confirmation == 'is_the_robot_charging':
        #printLine('waiting for confirmation')
        time.sleep(1)
    remote_interface = 'loading'
    if confirmation != 'no':
        #printLine('robot is charging')
        return True
    else:
        return False

def set_zero_pose():
    #printLine('setting zero pose')
    pose_pub = rospy.Publisher('/slamware_ros_sdk_server_node/set_pose',Pose,queue_size=1)
    time.sleep(0.3)
    home_pub = rospy.Publisher('/slamware_ros_sdk_server_node/set_home_pose',Pose,queue_size=1)
    time.sleep(0.3)
    clear_map_pub = rospy.Publisher('/slamware_ros_sdk_server_node/clear_map',ClearMapRequest,queue_size=1)
    time.sleep(0.3)
    msg = ClearMapRequest()
    clear_map_pub.publish(msg)
    time.sleep(0.3)
    msg = Pose()
    msg.orientation.w =1.0
    pose_pub.publish(msg)
    time.sleep(0.3)
    msg.position.x = -0.3
    home_pub.publish(msg)
    time.sleep(0.3)
    pose_pub.unregister()
    home_pub.unregister()
    clear_map_pub.unregister()
    #printLine('finished publishing zero pose')
    
def go_home():
    global remote_interface, robot_basic_state
    set_zero_pose()
    action_service_query('navigation/switch/go_home')
    timeout = 60
    t_start = time.time()
    flag = True
    while not robot_basic_state.is_charging:
        print('robot is not chargin yet', robot_basic_state.is_charging)
        time.sleep(1)
        if time.time() - t_start > timeout:
            flag = False
            break
    return flag
    

def run():
    global confirmation, sub, robot_basic_state, running_state
    time.sleep(3)    
    sub = rospy.Subscriber('/slamware_ros_sdk_server_node/robot_basic_state', RobotBasicState, robot_basic_state_cb)
    confirmation = 'no_messages'
    print('changing navigation mode', action_service_query('navigation/switch/pass'))
    time.sleep(2)
    while not rospy.is_shutdown() and confirmation == 'no_messages':
        printLine(confirmation)
        time.sleep(1)
    print(robot_basic_state)
    print('Dc cord state: ',robot_basic_state.is_dc_in)
    print('charger state: ',robot_basic_state.is_charging)
    
    if robot_basic_state.is_dc_in:
        remove_dc_cord()    
    is_charging = False
    if robot_basic_state.battery_percentage == 100:
        print('robot is 100 percent charged')
        is_charging = is_the_robot_in_charging_spot()
    elif not robot_basic_state.is_charging and not is_charging:
        flag = False
        while not flag:
            is_placed_properly()
            flag = go_home()
        
    action_service_query('navigation/switch/pass')
    sub.unregister()
    sub = None
    time.sleep(1)
    running_state = False
    
def start():
    global running_state
    running_state = True
    thread = threading.Thread(target=run)
    thread.start()
    return 'Done'
    
remote_interface = 'loading'
def get_remote_interface():
    global remote_interface
    return remote_interface

main_interface= 'loading'
def get_main_interface():
    global main_interface
    return main_interface

next_stage = 'choices_stage'
def get_next_stage():
    global next_stage
    return next_stage

obj = {
    'confirm':confirm,
    'run': run,
    'get_remote_interface': get_remote_interface,
    'get_main_interface': get_main_interface,
    'is_running': is_running,
    'next_stage': get_next_stage,
}