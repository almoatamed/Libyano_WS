import rospy
from geometry_msgs.msg import PoseStamped

running_state = 'cancelled'

goal_pub= rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=10)
def goal_req_cb(msg):
    if running_state == 'running' and not rospy.is_shutdown():
        goal_pub.publish(msg)

rate = rospy.Rate(1)
cmd_vel_req_sub = None
goal_req_sub = None
def start():
    global running_state, cmd_vel_req_sub, goal_req_sub
    running_state = 'running'
    goal_req_sub = rospy.Subscriber('/navigate/goal_req', PoseStamped, goal_req_cb)
    return 'running'

def cancel():
    global running_state, cmd_vel_req_sub, goal_req_sub
    running_state = 'cancelled'
    try:
        goal_req_sub.unregister()
    except:
        pass
