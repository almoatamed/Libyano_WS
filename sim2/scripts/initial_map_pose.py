#!/usr/bin/env python

import rospy
from tf2_msgs.msg import TFMessage
from geometry_msgs.msg import PoseWithCovarianceStamped
from geometry_msgs.msg import PoseStamped
import sys


def cb(data):
    global p, breaker
    for t in data.transforms:
        if t.header.frame_id == 'map' and t.child_frame_id == 'odom':
            print('found one')
            p.pose.pose.orientation.w = 1
            # p.pose.pose.position.x = -4.8 + t.transform.translation.x
            # p.pose.pose.position.y = 1.7 + t.transform.translation.y
            p.pose.pose.position.x = -2.9
            p.pose.pose.position.y = 1.5
            p.header.frame_id = 'map'
            p.header.stamp = rospy.Time.now()
            print(p)
            breaker = True


if __name__ == "__main__":
    breaker = False
    p = PoseWithCovarianceStamped()

    pub = rospy.Publisher('/initialpose', PoseWithCovarianceStamped,queue_size=10)

    rospy.init_node('location_initializer')
    sub = rospy.Subscriber("tf", TFMessage, cb)
    rate = rospy.Rate(20)
    while not rospy.is_shutdown():
        if breaker:
            break
        rate.sleep()
    print(sys.argv)
    print('starting shutdown initial map pose')
    pub.publish(p)
    print('Finished ... ')