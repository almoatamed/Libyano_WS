#!/usr/bin/env python 
import rospy
from std_msgs.msg import String

change_mode_topic = '/mode/change_mode'

change_mode_pub = rospy.Publisher(change_mode_topic, String, queue_size=10)

def run(status):
    mode = status.mode
    if float(status.power.battery) <= 15.0 and status.power.charging_status == 0 and mode not in ['lbt','sth']:
        change_mode_pub.publish('lbt')
    elif status.power.charging_status == 1 and float(status.power.battery) < 85.0 and mode not in ['chg','sth']:
        change_mode_pub.publish('chg')
    elif float(status.power.battery) >= 85.0 and status.power.charging_status == 1 and mode == 'chg':
        change_mode_pub.publish('chgcancel')