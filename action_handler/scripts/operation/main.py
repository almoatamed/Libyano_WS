from __future__ import print_function
print('starting main operation script')
import rospy
import threading
from std_msgs.msg import String
import json
import os


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
mode_json_file = home + '/catkin_ws/src/action_handler/scripts/operation/modes.json'
modes = {}

#api
def load_modes_config():
    global modes 
    modes_file = open(mode_json_file, 'r')
    modes = json.load(modes_file)
    modes_file.close()

load_modes_config()
printLine(modes)
running_mode = ''

is_running  = False 
def start():
    global is_running
    if not is_running and not rospy.is_shutdown():
        is_running = True
        thread = threading.Thread(target=run)
        thread.start()

from scripts.operation.mode_controllers.mnl import controller as mnl
from scripts.operation.mode_controllers.ato import controller as ato

operators = {
    "mnl": mnl.obj,
    'ato': ato.obj
}

def stop():
    global is_running, operators
    is_running = False

mode_pub = rospy.Publisher('/mode', String, queue_size=10)
rate = rospy.Rate(5)
string_msg = String()
def run():
    global running_mode, modes, string_msg
    running_mode = modes['default_mode']
    printLine('starting with defautl running mode', running_mode, modes['modes'][running_mode])
    operators[running_mode][modes['modes'][running_mode]['on_proceed']]()
    while not rospy.is_shutdown() and is_running:
        string_msg.data = running_mode
        rate.sleep()
        mode_pub.publish(string_msg)

start()

#api
def switch(in_mode):
    global running_mode, modes, operators
    printLine('attempting to switch mode to ' + in_mode)
    if is_running and not rospy.is_shutdown():
        if in_mode == running_mode+'cancel':
            printLine('current mode is cancelling')
            premode = running_mode
            operators[running_mode][modes['modes'][running_mode]['on_halt']]()
            running_mode = modes['modes'][running_mode]['retract_mode']
            resp = operators[running_mode][modes['modes'][running_mode]['on_proceed']]()
            if resp == 'done': 
                printLine('switching succeed')
                return "done"
            else: 
                printLine('switching failed')
                running_mode = premode
                operators[running_mode][modes['modes'][running_mode]['on_proceed']]()
                return resp
        else:
            if in_mode in modes['modes'][running_mode]["flags"]:
                if modes['modes'][running_mode]["flags"][in_mode]:
                    premode = running_mode
                    operators[running_mode][modes['modes'][running_mode]['on_halt']]()
                    running_mode = in_mode
                    resp = operators[running_mode][modes['modes'][running_mode]['on_proceed']]()
                    if resp == 'done': 
                        printLine('switching succeed')
                        return "done"
                    else: 
                        printLine('switching failed')
                        running_mode = premode
                        operators[running_mode][modes['modes'][running_mode]['on_proceed']]()
                        return resp
                else:
                    printLine('mode is not permitted to switch')
                    return 'not_permitted'
            else:
                printLine('mode is not permitted to switch')
                return 'not_permitted'

#api
def get_is_running():
    global is_running
    return is_running
#api
def get_status():
    global operators, running_mode
    return operators[running_mode]['status']()
#api
def get_running_mode():
    global running_mode
    return running_mode