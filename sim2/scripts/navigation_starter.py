#!/usr/bin/env python
# used to establish the node
import rospy 
# used to read the status of robot
from std_msgs.msg import String
# used to do the ros command
import os 

# splits the string in the required form 
def splitter(data):
    obj = {}
    for i in data.split('/'):
        obj[i.split(':')[0]] = i.split(':')[1]
    return obj

# joins the string from the regular form
def joiner(data):
    return '/'.join([i+':'+data[i] for i in data])

# this callback is used to start the robot navigation 
def starter(data):
    global breaker, charging, counter

    state = splitter(data.data)

    if counter == 20:
        print('status',state)
        counter = 0
    else:
        counter +=1

    if state['charging'] == '1':
        breaker = charging = True

if __name__ == "__main__":
    
    # parameters
    print('creating parameters')
    breaker = False
    charging = False
    counter = 0

    #initialize node
    print('initializing node')
    rospy.init_node('starter',anonymous=True)

    
    # subscribe to the robot status to check if its charging
    print('subscribing to status')
    sub = rospy.Subscriber('/status', String,starter)

    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        if breaker:
            break
        rate.sleep()
    
    # shutdown procedure
    print('shutting down navigation starter...')

    sub.unregister()
    if(charging):
        print('starting navigation stack ... ')
        os.system('roslaunch sim2 navigation_rviz.launch')
    else:
        print('Error')