import rospy
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import Twist 
import time
import threading
from slamware_ros_sdk.msg import MoveToRequest

running_state = 'cancelled'

cmd_vel_pub = rospy.Publisher('/slamware_ros_sdk_server_node/cmd_vel_no_limit', Twist, queue_size=10)
t_pub = 0
last_cmd_vel= Twist()
def cmd_vel_req_cb(msg):
    global last_cmd_vel, t_pub
    if running_state == 'running' and not rospy.is_shutdown():
        last_cmd_vel = msg
        t_pub = time.time()
        cmd_vel_pub.publish(msg)

def threaded_check():
    global last_cmd_vel
    while not rospy.is_shutdown() and running_state == 'running':
        if (last_cmd_vel.linear.x != 0 or last_cmd_vel.angular.z != 0 ) and time.time() - t_pub > 1:
           last_cmd_vel = Twist()
           cmd_vel_pub.publish(last_cmd_vel)
        time.sleep(1)
    
goal_pub= rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=10)
def goal_req_cb(msg):
    if running_state == 'running' and not rospy.is_shutdown():
        msg.header.stamp = rospy.Time.now()
        goal_pub.publish(msg)
        
unangled_goal_pub = rospy.Publisher('/slamware_ros_sdk_server_node/move_to', MoveToRequest, queue_size=1)
def unangled_goal_req_cb(msg):
    if running_state == 'running' and not rospy.is_shutdown():
        unangled_goal_pub.publish(msg)    
        

rate = rospy.Rate(1)
cmd_vel_req_sub = None
goal_req_sub = None
unangled_goal_req_sub = None
def start():
    global running_state, cmd_vel_req_sub, goal_req_sub, unangled_goal_req_sub
    running_state = 'running'
    cmd_vel_req_sub = rospy.Subscriber('/navigation/cmd_vel_req', Twist, cmd_vel_req_cb)
    goal_req_sub = rospy.Subscriber('/navigation/goal_req', PoseStamped, goal_req_cb)
    unangled_goal_req_sub = rospy.Subscriber('/navigation/unangled_goal_req',MoveToRequest,unangled_goal_req_cb)
    thread = threading.Thread(target=threaded_check)
    thread.start()
    return 'running'

def cancel():
    global running_state, cmd_vel_req_sub, goal_req_sub, unangled_goal_req_sub
    running_state = 'cancelled'
    try:
        cmd_vel_req_sub.unregister()
    except:
        pass
    try:
        goal_req_sub.unregister()
    except:
        pass
    try:
        unangled_goal_req_sub.unregister()
    except:
        pass