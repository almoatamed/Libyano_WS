#!/usr/bin/env python
import rospy
from std_msgs.msg import String 
from geometry_msgs.msg import Twist
from actionlib_msgs.msg import GoalID

def mode_cb(data):
    global mode, premode 
    if data.data !=  mode:
        premode = mode 
        mode = data.data

def stop():
    global goal_cancel_publisher, cmd_vel_pub
    goal_id= GoalID()
    goal_cancel_publisher.publish(goal_id)
    twist = Twist()
    cmd_vel_pub.publish(twist)

def stop_cb(data):
    global mode, premode, mode_pub
    if data.data == '1':
        mode_pub.publish('stp')
        if mode != 'chg':
            stop()
    elif data.data == '0':
        # if premode != 'stp' and mode == 'stp':
        #     mode_pub.publish(premode)
        # else:
        mode_pub.publish('stpcancel')     

if __name__=='__main__':

    # parameters 
    premode = ''
    mode = ''
    change_mode_topic = '/change_mode'
    goal_cancel_topic = '/move_base/cancel'
    vel_topic = '/cmd_vel'

    mode_pub = rospy.Publisher(change_mode_topic, String, queue_size=10)
    goal_cancel_publisher = rospy.Publisher(goal_cancel_topic,GoalID,queue_size=10)
    cmd_vel_pub = rospy.Publisher(vel_topic, Twist, queue_size=10)

    rospy.init_node('stop')

    rospy.Subscriber('/stop', String, stop_cb)
    rospy.Subscriber('/mode', String, mode_cb)
    rospy.spin()
