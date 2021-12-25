from __future__ import print_function
import rospy
import threading 
from geometry_msgs.msg import Pose
from status_msgs.msg import goal_monitor_msg
from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import Path
from slamware_ros_sdk.msg import MoveToRequest

file_name = __file__.split('/')[-1][:-3]
if file_name == '__init__' or file_name == '__init__.':
    file_name = __file__.split('/')[-2]
def printLine(*args):
    '''
        prints information on the console screen
    '''
    global name
    print(file_name+': '+'\n      - '+'\n      - '.join([str(arg) for arg in list(args)]))

current_pose = None
def current_pose_cb(msg):
    global current_pose
    current_pose = msg
    
goal_msg = None
process_flag = False
def unangled_goal_cb(msg):
    global goal_msg, process_flag
    # ##printLine('Unangled goal was received', msg)
    goal_msg = msg
    process_flag = True
    
def angled_goal_cb(msg):
    # ##printLine('Angled goal was received', msg)
    global goal_msg, process_flag
    goal_msg = msg
    process_flag = True
    
global_path_queue = []
queue_length = 13
def global_path_cb(msg):
    global global_path_queue
    global_path_queue.append(msg)
    if len(global_path_queue) >queue_length:
        global_path_queue = global_path_queue[-queue_length:]


running_state = 'cancelled'
global_path_sub = None
current_pose_sub = None
angled_goal_sub = None
unangled_goal_sub = None
def start():
    global running_state, global_path_sub, current_pose_sub, angled_goal_sub, unangled_goal_sub
    if running_state != 'running':
        running_state = 'running'
        ##printLine('starting')
        global_path_sub = rospy.Subscriber('/slamware_ros_sdk_server_node/global_plan_path', Path, global_path_cb)
        angled_goal_sub = rospy.Subscriber('/move_base_simple/goal',PoseStamped,angled_goal_cb)
        unangled_goal_sub = rospy.Subscriber('/slamware_ros_sdk_server_node/move_to',MoveToRequest,unangled_goal_cb)
        current_pose_sub = rospy.Subscriber('/current_pose',Pose,current_pose_cb)
        thread = threading.Thread(target=run)
        thread.start()

goal_monitor = goal_monitor_msg()
goal_monitor_pub = rospy.Publisher('/navigation/goal_monitor', goal_monitor_msg,queue_size=1)
rate = rospy.Rate(2)
def run():
    global goal_monitor_pub, rate, goal_monitor, process_flag, goal_msg, global_path_queue
    while not rospy.is_shutdown() and running_state == 'running':
        rate.sleep()
        if process_flag:
            # ##printLine('processing')
            goal_monitor = goal_monitor_msg()
            if type(goal_msg) == PoseStamped:
                # ##printLine('angled goal is being processed')
                goal_monitor.is_angled = True
                goal_monitor.pose.x = goal_msg.pose.position.x
                goal_monitor.pose.y = goal_msg.pose.position.y
                goal_monitor.pose.z = goal_msg.pose.position.z
                goal_monitor.orientation.x = goal_msg.pose.orientation.x
                goal_monitor.orientation.y = goal_msg.pose.orientation.y
                goal_monitor.orientation.z = goal_msg.pose.orientation.z
                goal_monitor.orientation.w = goal_msg.pose.orientation.w
            else:
                # ##printLine('unangled goal is being processed')
                goal_monitor.is_angled = False
                goal_monitor.pose.x = goal_msg.location.x
                goal_monitor.pose.y = goal_msg.location.y
                goal_monitor.pose.z = goal_msg.location.z
            if len(global_path_queue) == queue_length:
                # ##printLine('global_path_queue is valid in length')
                if all([len(path.poses) >0 for path in global_path_queue]):
                    # ##printLine('global_path_queue is directing currectly',len(global_path_queue[1].poses))
                    if abs(global_path_queue[-1].poses[-1].pose.position.x - goal_monitor.pose.x) < 0.3  and abs(global_path_queue[-1].poses[-1].pose.position.y - goal_monitor.pose.y) < 0.3:
                        goal_monitor.state = 'running'
                    else:
                        continue
                elif all([len(path.poses) == 0 for path in global_path_queue]):
                    # ##printLine('global_path_queue is empty',len(global_path_queue[1].poses))
                    if current_pose:
                        # print('line comparing position', abs(current_pose.position.x - goal_monitor.pose.x),abs(current_pose.position.y - goal_monitor.pose.y))
                        if abs(current_pose.position.x - goal_monitor.pose.x) < 0.3  and abs(current_pose.position.y - goal_monitor.pose.y) < 0.3:
                            # ##printLine('succeed')
                            goal_monitor.state = 'succeed'
                        else:
                            goal_monitor.state = 'false'
                    else:
                        continue
                else:
                    continue
            else:
                continue
        goal_monitor_pub.publish(goal_monitor)

def get_current_goal_state():
    global goal_monitor
    return goal_monitor.state
            
                    
def cancel():
    global running_state, global_path_sub, unangled_goal_sub, angled_goal_sub, current_pose_sub
    running_state = 'cancelled'
    try:
        global_path_sub.unregister()
    except:
        pass
    try:
        unangled_goal_sub.unregister()
    except:
        pass
    try:
        angled_goal_sub.unregister()
    except:
        pass    
    try:
        current_pose_sub.unregister()
    except:
        pass

def is_running():
    global running_state
    return running_state

start()