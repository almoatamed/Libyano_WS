import rospy
from geometry_msgs.msg import Twist 

running_state = 'cancelled'


cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
def cmd_vel_req_cb(msg):
    if running_state == 'running' and not rospy.is_shutdown():
        cmd_vel_pub.publish(msg)
        
rate = rospy.Rate(1)
cmd_vel_req_sub = None
def start():
    global running_state, cmd_vel_req_sub
    running_state = 'running'
    cmd_vel_req_sub = rospy.Subscriber('/navigate/cmd_vel_req', Twist, cmd_vel_req_cb)
    return 'running'

def cancel():
    global running_state, cmd_vel_req_sub
    running_state = 'cancelled'
    try:
        cmd_vel_req_sub.unregister()
    except:
        pass
