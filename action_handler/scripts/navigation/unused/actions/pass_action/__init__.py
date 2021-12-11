import rospy

status = 'cancelled'
rate = rospy.Rate(1)


def start():
    global status
    status = 'running'
    
def cancel():
    global status
    status = 'cancelled'
    