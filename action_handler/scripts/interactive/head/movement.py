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
    

mcu_topic = rospy.get_param('/mcu/mcu_input_topic','/mcu/interactive/input')
queue_size = int(rospy.get_param('/global/queue_size', '10'))

pub = rospy.Publisher(mcu_topic, mcu_input,queue_size=queue_size)
mcu_msg = mcu_input()
mcu_msg.Element = 23

x_min = -45
x_max = 45
y_min = -15
y_max = 15

current_x = 0.0
current_y = 0.0

last_time = time.time()
last_speed = 700


def relative_move(x,y,speed):
    global current_x, current_y, last_speed
    last_speed = speed
    try:
        x = float(x)
        y = float(y)
        speed = float(speed)
    except Exception as e:
        printLine("error while trying to move head",e)
        return 'failed'
    last_speed = speed
    if time.time() - last_time < float(last_speed/1000):
        return 'too_soon'
    if x+current_x > x_max or x+current_x < x_min or current_y+y > y_max or y+current_y < y_min:
        return 'out_of_boundries'    
    current_y = current_y + y
    current_x = current_x + x
    print(current_x,current_y)
    mcu_msg.values = [current_x,current_y, speed]
    mcu_msg.Part_and_function = 11
    pub.publish(mcu_msg)
    return 'succeed'

def move(x='0',y='0',speed='700'):
    global mcu_msg, current_y, current_x
    try:
        x = float(x)
        y = float(y)
        speed = float(speed)
    except Exception as e:
        printLine("error while trying to move head",e)
        return 'failed'
    if x > x_max or x < x_min or y > y_max or y < y_min:
        return 'out_of_boundries'    
    current_x = x
    current_y = y
    mcu_msg.values = [x,y,speed]
    mcu_msg.Part_and_function = 11
    pub.publish(mcu_msg)
    return 'succeed'

def home():
    global mcu_msg, current_x, current_y
    current_y = 0.0
    current_x = 0.0
    mcu_msg.Part_and_function = 12
    pub.publish(mcu_msg)
    return 'succeed'

home()