#!/usr/bin/env python 
from __future__ import print_function
import rospy
import threading
from action_handler_msgs.srv import action_srv
from std_msgs.msg import String
from common.csv import readCSV
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

#printLine('starting Mode Controller')

def asq(action):
    action_service_name = rospy.get_param('/action/action_service_name','/action')
    rospy.wait_for_service(action_service_name)
    try: 
        take_action = rospy.ServiceProxy(action_service_name,action_srv)
        resp = take_action(action)
        return resp.result
    except rospy.ServiceException as e:
        #printLine('An error occured while trying to take an action ', e)
        return "failed"

home = os.environ['HOME']
csv_path = home+'/catkin_ws/src/action_handler/scripts/global_actions/mode/csv/modes.csv'
modes = {}
def process_csv():
    global modes
    modes = readCSV(csv_path)
    for mode in modes:
        temp = {}
        for flag in modes[mode]['mode_flag'].split('|'):
            flag = flag.split(':')
            temp[flag[0]] = flag[1]
        modes[mode]['mode_flag'] = temp
    printLine(modes)

        
process_csv()
mode = 'mnl'
premode = ''
default_retry_counter = 1
def trigger_actions():
    if modes[mode]['change_action'] != 'null':
        
        #printLine('taking aciton based on mode change', modes[mode]['change_action'])
        
        if(modes[mode]['action_retry_count'] == '0'):
            counter = default_retry_counter 
        else:
            try:
                counter = int(modes[mode]['action_retry_count'])
            except ValueError as e:
                #printLine('failed to convert the primary action retry counter for mode', mode,'with error', e)
                counter = default_retry_counter 
                
        for action in modes[mode]['change_action'].split('|'):
            for _ in range(counter):
                result = asq(action)
                if(result != "failed"):
                    break

def change_mode(inmode):
    global modes, mode, premode, default_retry_counter 
    if inmode != mode:
        if inmode == mode+'cancel':
            premode == mode 
            mode = modes[mode]['retract_mode']
            trigger_actions()
            return 'mode_changed'
        elif inmode in modes[mode]['mode_flag']:
            if (modes[mode]['mode_flag'][inmode] == '1'):
                premode = mode
                mode = inmode
                trigger_actions()
            else:
                return 'cannot_change_mode'
        else:
            return 'cannot_change_mode'
    else:
        return 'mode_not_found'

def get_mode():
    global mode
    return mode

def get_premode():
    global premode
    return premode


def get_is_running():
    global is_running
    return str(is_running)

is_running = False
def start():
    global is_running
    is_running = True
    thread = threading.Thread(target=run)
    # thread.daemon = True
    thread.start()
    
def stop():
    global is_running
    is_running = False

mode_topic_name = rospy.get_param('/mode/mode_topic', '/mode')
premode_topic_name = rospy.get_param('/mode/premode_topic', '/premode')
mode_pub = rospy.Publisher(mode_topic_name,String, queue_size=10)
premode_pub = rospy.Publisher(premode_topic_name,String, queue_size=10) 
publish_rate = rospy.get_param('/mode/mode_rate', "5")
rate = rospy.Rate(float(publish_rate))
msg = String()
def run():
    global is_running, rate, premode_pub, premode, mode, mode_pub, msg
    #printLine('Mode Controller is Running')
    while not rospy.is_shutdown() and is_running:            
        rate.sleep()
        msg.data = premode
        premode_pub.publish(msg)
        msg.data = mode 
        mode_pub.publish(msg)

change_mode_topic_name = rospy.get_param('/mode/change_mode_topic', '/change_mode')
def change_mode_cb(msg):
    change_mode(msg.data)
rospy.Subscriber(change_mode_topic_name,String, change_mode_cb)

start()