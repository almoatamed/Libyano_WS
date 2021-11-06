import rospy
import os
from mcu_msgs.msg import mcu_input
import time
import threading

file_name = __file__.split('/')[-1][:-3]
if file_name == '__init__' or file_name == '__init__.':
    file_name = __file__.split('/')[-2]
def printLine(*args):
    '''
        prints information on the console screen
    '''
    global name
    print(file_name+': '+'\n      - '+'\n      - '.join([str(arg) for arg in list(args)]))
    
x_min = -45
x_max = 45
y_min = -15
y_max = 15

current_x = 0.0
current_y = 0.0

last_time = time.time()
last_speed = 700

home = os.environ['HOME']
motions_file_path = home +'/catkin_ws/src/action_handler/scripts/interactive/head/head_motions.txt'
def decode_motion():
    global motions_file_path
    file = open(motions_file_path, 'r')
    motions = file.read()
    file.close()
    if motions:
        motions =  [motion.split(':') for motion in motions.split('$')]
        motions = {motion[0]:[[float(val) for val in vals.split('&')] for vals in motion[1].split('|')] for motion in motions}
        printLine('motions', motions)
        return motions
    else:
        return {}

def encode_motions(motions):
    encoding =  '$'.join([':'.join([motion, '|'.join(['&'.join([str(val) for val in vals]) for vals in motions[motion]]) ]) for motion in motions])
    printLine('encoding', encoding)
    return encoding


def add_motion(motion):
    motions = decode_motion()
    motion = motion.split(':')
    motions[motion[0]] = [[float(motion_val) for motion_val in motion_vals.split('&')] for motion_vals in motion[1].split('|')]
    file = open(motions_file_path, 'w+')
    file.write(encode_motions(motions))
    return 'done'

def get_motions_names():
    motions= decode_motion()
    return '|'.join(motions.keys())
    
motions_queue = []
def clear_motions_queue():
    global motions_queue
    motions_queue = []

def move_head_home():
    play_angled_movement(0,0,700,0)
    
def push_angled_movement(x,y,speed,delay):
    global motions_queue
    motions_queue.append([
        float(val) for val in [x,y,speed,delay]
    ])
    return 'done'

def play_angled_movement(x,y,speed,delay):
    global motions_queue
    motions_queue = [[float(val) for val in [x,y,speed,delay]]]
    return 'done'

def push_motion_by_name(name):
    global motions_queue
    motions = decode_motion()
    if name not in motions:
        return 'not_found'
    motions_queue += motions[name]
    return 'done'

def play_motions_by_name(name):
    global motions_queue
    motions = decode_motion()
    if name not in motions:
        return 'not_found'
    motions_queue = motions[name]
    return 'done'
    
def push_motions_by_motion(motion):
    global motions_queue
    motion = motion.split('|')
    motion = [[float(val) for val in m.split('&')] for m in motion]
    motions_queue = motions_queue + motion
    return 'done'
    
def play_motions_by_motion(motion):
    global motions_queue
    motion = motion.split('|')
    motion = [[float(val) for val in m.split('&')] for m in motion]
    motions_queue = motion
    return 'done' 


mcu_topic = rospy.get_param('/mcu/mcu_input_topic','/mcu/interactive/input')
queue_size = int(rospy.get_param('/global/queue_size', '10'))
pub = rospy.Publisher(mcu_topic, mcu_input,queue_size=queue_size)
mcu_msg = mcu_input()
mcu_msg.Element = 23
def threaded_motion_player():
    global motions_queue
    while not rospy.is_shutdown():
        if len(motions_queue) > 0:
            motion = motions_queue.pop(0)
            mcu_msg.values = [float(val) for val in motion[:-1]]
            printLine('publishign motion', motion)
            mcu_msg.Part_and_function = 11
            pub.publish(mcu_msg)
            time.sleep(float(motion[-1])/1000+0.05)
        else:
            time.sleep(0.2)

thread = threading.Thread(target=threaded_motion_player)
thread.start()

def relative_move(x,y,speed):
    global current_x, current_y, last_speed, motions_queue
    motions_queue = []
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


