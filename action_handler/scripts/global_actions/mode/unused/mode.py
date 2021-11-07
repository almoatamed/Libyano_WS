import rospy
from common.csv import readCSV
from std_msgs.msg import String
import os 
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
    
home = os.environ['HOME']
csv_path = home+'/catkin_ws/src/mode_and_status_publishers/csv/modes.csv'
modes = {}
def process_csv():
    global modes
    modes = readCSV(csv_path)
    printLine(*modes)
    for mode in modes:
        temp = {}
        for flag in modes[mode]['mode_flag'].split('/'):
            flag = flag.split(':')
            temp[flag[0]] = flag[1]
        modes[mode]['mode_flag'] = temp
    
current_mode = None
def mode_cb(msg):
    global current_mode 
    current_mode = msg.data
sub = rospy.Subscriber('/mode', String, mode_cb)

change_mode_pub = rospy.Publisher('/mode/change_mode', String, queue_size=1)
retry_count = 3
def cancel_current_mode():
    global retry_count, change_mode_pub, current_mode
    i = 0
    while i < retry_count:
        i+=1
        premode = current_mode
        change_mode_pub.publish(current_mode + 'cancel')
        time.sleep(1)
        if premode == current_mode:
            continue
        else:
            return 'succeed'
    return 'failed'


def try_to_change_mode(target_mode):
    global retry_count, change_mode_pub, current_mode
    i = 0
    while i < retry_count:
        i+=1
        premode = current_mode
        change_mode_pub.publish(target_mode)
        time.sleep(1)
        if premode == current_mode:
            continue
        else:
            return 'succeed'
    return 'failed'

def switch(target_mode):
    global current_mode, modes
    # #printLine('targetmode is ',target_mode, 'available modes are', *[mode for mode in modes])
    if current_mode == target_mode:
        return 'already_running'
    elif target_mode == current_mode + 'cancel':
        return cancel_current_mode()
    elif target_mode not in modes:
        return 'target_mode_not_found'
    else:
        return try_to_change_mode(target_mode)

def get_current_mode():
    global current_mode
    return current_mode

process_csv()