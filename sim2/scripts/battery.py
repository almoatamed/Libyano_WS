#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from common import splitter, check_modes
import time

def mode_cb(data):
    global mode, premode
    if mode != data.data:
        premode = mode 
        mode = data.data

def status_cb(data):
    global status
    status = splitter(data.data)

if __name__ == "__main__":
    
    # parameters
    premode = '' 
    mode = 'nav'
    status = {}
    node_name = 'bettery_handler'

    change_mode_topic = '/change_mode'
    status_topic = '/status'
    mode_topic = '/mode'

    change_mode_pub = rospy.Publisher(change_mode_topic, String, queue_size=10)

    rospy.init_node(node_name)

    rospy.Subscriber(status_topic,String,status_cb)
    rospy.Subscriber(mode_topic, String, mode_cb)

    rate = rospy.Rate(1)


    while not rospy.is_shutdown():
        rate.sleep()
        if status:
            if float(status['battery']) <= 15.0 and status['charging'] == '0' and mode not in ['lbt','sth']:
                change_mode_pub.publish('lbt')
            elif  status['charging'] == '1' and float(status['battery']) < 85.0 and mode not in ['chg','sth']:
                change_mode_pub.publish('chg')
            elif float(status['battery']) >= 85.0 and status['charging'] == '1' and mode == 'chg':
                change_mode_pub.publish('chgcancel')

                
