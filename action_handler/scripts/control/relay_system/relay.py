import rospy
from mcu_msgs.msg import mcu_input

file_name = __file__.split('/')[-1][:-3]
if file_name == '__init__' or file_name == '__init__.':
    file_name = __file__.split('/')[-2]
def printLine(*args):
    '''
        prints information on the console screen
    '''
    global name
    print(file_name+': '+'\n      - '+'\n      - '.join([str(arg) for arg in list(args)]))
    
topic = rospy.get_param('mcu/interactive/input_topic','mcu/interactive/input')
pub = rospy.Publisher(topic, mcu_input,queue_size=int(rospy.get_param('/global/queue_size', '10')))
msg = mcu_input()
msg.Element = 21

def set_relay(number, value):
    printLine(number,value)
    msg.Part_and_function = int(number)
    msg.values = [float(value)]
    pub.publish(msg)
    return 'done'