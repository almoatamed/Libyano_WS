import rospy
from slamware_ros_sdk.msg import GoHomeRequest
from status_msgs.msg import status
import threading
import time



current_status = status()
current_status.power.charging_status = 0
def status_cb(msg):
    global current_status
    current_status = msg

sub = None
def start():
    global sub, current_status
    sub = rospy.Subscriber('/status', status, status_cb)
    thread = threading.Thread(target=run)
    thread.start()
    return 'running'

pub = rospy.Publisher('/slamware_ros_sdk_server_node/go_home',GoHomeRequest, queue_size=10)    

running_state = 'cancelled'
go_home_topic = '/slamware_ros_sdk_server_node/go_home'
msg = GoHomeRequest()
check_rate = rospy.Rate(2)
pub_time_out = 60.0
def run():
    global running_state, check_rate, pub, current_status
    running_state = 'running'
    t_start = 0
    pub.publish(msg)
    while running_state == 'running' and not rospy.is_shutdown():
        check_rate.sleep()
        if current_status.power.charging_status == 0 and time.time() - t_start >pub_time_out:
            t_start = time.time()
            pub.publish(msg)

def cancel():
    global sub, running_state
    running_state = 'cancelled'
    sub.unregister()
    