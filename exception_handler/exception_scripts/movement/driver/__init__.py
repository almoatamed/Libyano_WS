from status_msgs.msg import status
import rospy
from mcu_msgs.msg import mcu_input
import time

file_name = __file__.split('/')[-1][:-3]
if file_name == '__init__' or file_name == '__init__.':
    file_name = __file__.split('/')[-2]
def printLine(*args):
    '''
        prints information on the console screen
    '''
    global name
    print(file_name+': '+'\n      - '+'\n      - '.join([str(arg) for arg in list(args)]))
    
pub = rospy.Publisher(rospy.get_param('/mcu/movement/operation_control_topic', '/mcu/movement/operation_state_control'),mcu_input,queue_size=10)
msg = mcu_input()
msg.Element = 2

timeout = 10
timeflag = time.time()

def error(current_status):
    # print(current_status.driver)
    if current_status.driver.axis0.error != "0x0d" or \
       current_status.driver.axis0.encoder.error != "0x00" or \
       current_status.driver.axis0.motor.error != "0x00" or \
       current_status.driver.axis1.error != "0x0d" or \
       current_status.driver.axis1.encoder.error != "0x00" or \
       current_status.driver.axis1.motor.error != "0x00"\
    :
        return True
    else:
        #printLine('no errors')
        return False
    

def run(current_status):
    global timeflag, timeout, pub
    if error(current_status) and time.time() - timeflag > timeout:
        #printLine('Error on Driver')
        timeflag = time.time()
        pub.publish(msg)
