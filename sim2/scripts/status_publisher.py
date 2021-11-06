#!/usr/bin/env python

# This node is responsible for publishing the state of the robot for know it only publishes the state
# as string with field and value seperated by :, and the mutiple key value pairs are seperated by /

# Statuses published are 
# - Charging or not which should be 0 for no, and 1 for yes
# ...


import rospy
from common import joiner, splitter
from std_msgs.msg import String

# update the state of charging as a callback
def chchrg(data):
    # print('charging state',data.data)
    global CHARGING
    if data.data == "0":
        CHARGING = '0'
    elif data.data == "1":
        CHARGING = '1'

def battery_cb(data):
    global  BATTERY
    BATTERY = float(data.data)

if __name__=="__main__":
    print('starting status publisher')
    try:    
        # parameters
        CHARGING = '0'
        BATTERY = 90.0

        # create the status publisher
        pub = rospy.Publisher('status', String, queue_size=10)

        #initialize the node
        rospy.init_node('state_publisher',anonymous=True)

        # subscribe to the charging predicter
        rospy.Subscriber('charging', String, chchrg)
        rospy.Subscriber('battery', String, battery_cb)


        # create the publish rate
        rate = rospy.Rate(5)

        # main loop
        while not rospy.is_shutdown():
            # publish the status 
            if(CHARGING):
                pub.publish(joiner({'charging':CHARGING, 'battery':str(BATTERY)}))
            rate.sleep()
    except rospy.ROSInterruptException:
        pass

    # shut down procedure
    print('shutting down status publisher')