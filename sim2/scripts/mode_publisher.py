#!/usr/bin/env python 
import rospy
from common import joiner, splitter
from std_msgs.msg import String
from geometry_msgs.msg import Twist
import time

###################
# modes are nav for navigation, 
# chg for charging, trk for tracking, 
# grt for greeting, lbt for low battery
# stp for stop, sth for stay home
###################

# responsible for prioritizing, or cancelling modes
def prioritize(inmode):
    global priorities, mode, premode
    if inmode != mode:
        if inmode == mode+'cancel':
            premode == mode 
            mode = 'nav'
        elif (priorities[mode] > priorities[inmode]):
            mode = mode
            premode = premode
        else:
            premode = mode
            mode = inmode

# callback for status subscription
def status_cb(data):
    global status
    status = splitter(data.data)

# responsible for mode subscription
def change_mode_cb(data):
    prioritize(data.data)

# make the robot move forward little bit
def go_forward():
    pass
    global cmd_vel_pub
    twist = Twist()
    twist.linear.x = 0.14
    cmd_vel_pub.publish(twist)
    time.sleep(2.5)
    twist = Twist()
    cmd_vel_pub.publish(twist)

# mian call 
if __name__ == '__main__':

    # starting node
    print('starting mode publisher')

    # parameters
    ###################################
    # node name
    node_name = 'mode_publisher'

    # topic names
    mode_topic = 'mode'
    premode_topic = 'premode'
    change_mode_topic = 'change_mode' 
    charging_topic = 'charging'
    status_topic = '/status'
    cmd_vel_topic = '/cmd_vel'

    # static parameters
    priorities = {
        'nav': 0,
        'trk': 0,
        'grt': 0,
        'chg': 2,
        'lbt': 2,
        'sth': 3,
        'stp': 1,
    }

    # dynamic parameters
    status = {}
    mode = 'nav'
    premode = ''
    ###################################

    # creating publishers
    cmd_vel_pub = rospy.Publisher(cmd_vel_topic, Twist, queue_size=10)
    mode_pub = rospy.Publisher(mode_topic,String, queue_size=10)
    premode_pub = rospy.Publisher(premode_topic,String, queue_size=10)

    # initializing node
    rospy.init_node(node_name)

    # subscribing to topics
    rospy.Subscriber(change_mode_topic,String, change_mode_cb)
    rospy.Subscriber(status_topic,String, status_cb)

    # main loop
    rate = rospy.Rate(5)
    while(not rospy.is_shutdown()):
        rate.sleep()
        mode_pub.publish(mode)
        premode_pub.publish(premode)

        # if the robot is charging and the mode indicate to move the move forward a little bit
        if 'charging' in status:
            if status['charging'] == '1' and mode not in ['chg','sth']:
                go_forward()