#!/usr/bin/env python

# This node predicts the Simulatiun state of charging based on the location on regarded to the odom frame
# ...

import rospy
from std_msgs.msg import String
from nav_msgs.msg import Odometry


# fake charging state checker
def is_charging(data):
    # print(data.pose.pose.position)
    global X, X_high, X_low, Y, Y_high, Y_low, pub, counter
    if (X_low<data.pose.pose.position.x<X_high) and (Y_low<data.pose.pose.position.y<Y_high):
        if counter == 50:
            counter = 0 
            # print('charging...')
        else:
             counter +=1
        pub.publish('1')
    else:
        if counter == 50:
            counter = 0 
            # print('not charging...')
        else:
             counter +=1
        pub.publish('0')


if __name__=='__main__':
    try:
        # print counter
        counter = 0

        # specific, lower, and higher x charging pose
        X_high = -4.79
        X_low = -4.83
        X = -4.815

        # specific, lower, and higher y charging pose
        Y_low = 1.4
        Y_high = 1.8
        Y = 1.48

        # Creating publisher
        print('Creating publishers')
        pub = rospy.Publisher("charging", String, queue_size=10)

        # initializing node
        print('initializing node')
        rospy.init_node('fake_charging', anonymous=True)

        # publish fake Charging state based based on a Static pose
        print('subscribing to /odoms')
        rospy.Subscriber('odom', Odometry ,is_charging)
        
        # block till shutdown
        print('spinning ...')
        rospy.spin()

    except rospy.ROSInterruptException:
        pass

    # shutdown
    print('Shutting Down ...')
        
