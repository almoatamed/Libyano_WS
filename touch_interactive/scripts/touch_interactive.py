#!/usr/bin/env python
import rospy
from status_msgs.msg import status
from std_msgs.msg import String
def status_cb(msg):
    global pub
    if len(list(msg.sensors.touch)) > 0:
        if ord(msg.sensors.touch[0]) == 1:
            pub.publish('grt')

if __name__ == "__main__":

    print('starting touch interactive')
    rospy.init_node('touch_interactive')
    rospy.Subscriber('/status',status,status_cb)
    pub = rospy.Publisher('/mode/change_mode',String,queue_size=10)
    rospy.spin()