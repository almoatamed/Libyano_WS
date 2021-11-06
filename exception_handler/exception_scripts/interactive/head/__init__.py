import rospy
from status_msgs.msg import status
from mcu_msgs.msg import mcu_input
import time

pub = rospy.Publisher(rospy.get_param('/mcu/interactive/input_topic', '/mcu/interactive/input'),mcu_input, queue_size=10)
msg = mcu_input()
msg.Element = 23
msg.Part_and_function = 13

timeout = 10
timeflag = time.time()

def servo_error(current_status):
    for servo in current_status.controllers.servos:
        if ord(servo.stat) != 0x00:
            return True
    return False



def run(current_status):
    global msg, timeout, timeflag, pub
    if servo_error(current_status) and time.time() - timeflag > timeout:
        timeflag = time.time()
        pub.publish(msg)

