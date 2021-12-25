#!/usr/bin/env python 
from __future__ import print_function
import rospy
from common.action_server import action_service_query
from common.csv import readCSV

from std_msgs.msg import String
from status_msgs.msg import status
###################
# modes are included in the CSV fiel modes.csv at the CSV directory!
# for any farther questions contacyt the manager of the Agile system ;)
#
# By: Salem Elmotamed
###################


file_name = __file__.split('/')[-1][:-3]
if file_name == '__init__' or file_name == '__init__.':
    file_name = __file__.split('/')[-2]
def printLine(*args):
    '''
        prints information on the console screen
    '''
    global name
    print(file_name+': '+'\n      - '+'\n      - '.join([str(arg) for arg in list(args)]))
    
def trigger_actions():
    if modes[mode]['change_action'] != 'null':
        ##printLine('taking aciton based on mode change', modes[mode]['change_action'])
        if(modes[mode]['action_retry_count'] == '0'):
            counter = action_retry_counter
        else:
            try:
                counter = int(modes[mode]['action_retry_count'])
            except ValueError as e:
                ##printLine('failed to convert the primary action retry counter for mode', mode,'with error', e)
                counter = action_retry_counter
        for action in modes[mode]['change_action'].split('|'):
            for _ in range(counter):
                result = action_service_query(action)
                if(result != "failed"):
                    break

def change_mode_cb(inmode):
    global modes, mode, premode, action_retry_counter
    inmode = inmode.data
    if inmode != mode:
        if inmode == mode+'cancel':
            premode == mode 
            mode = modes[mode]['retract_mode']
            trigger_actions()
        elif inmode in modes[mode]['mode_flag']:
            if (modes[mode]['mode_flag'][inmode] == '1'):
                premode = mode
                mode = inmode
                trigger_actions()
        
def status_cb(msg):
    global current_status
    current_status = msg


if __name__ == '__main__':

    # startLogging('mode-handler')

    ##printLine('Starting mode publisher')

    ###############################################
    #parameters#
    ###############################################


    node_name = "mode_handler"
    anonymous_node = False
    rospy.init_node(node_name,anonymous=anonymous_node)

    # mode dictionary
    csv_path = rospy.get_param('/mode/csv_path', '../csv/modes.csv')
    modes = readCSV(csv_path)
    for mode in modes:
        temp = {}
        for flag in modes[mode]['mode_flag'].split('/'):
            flag = flag.split(':')
            temp[flag[0]] = flag[1]
        modes[mode]['mode_flag'] = temp
    print(modes)
    action_retry_counter = int(rospy.get_param('/mode/action_retry_counter', '1'))

    # topic names
    mode_topic_name = rospy.get_param('/mode/mode_topic', '/mode')
    premode_topic_name = rospy.get_param('/mode/premode_topic', '/premode')
    change_mode_topic_name = rospy.get_param('/mode/change_mode_topic', '/change_mode')
    status_topic_name = rospy.get_param('/status/status_topic', '/status')
    
    publish_rate = rospy.get_param('/mode/mode_rate', "5")

    # dynamic variables
    current_status = status()
    
    mode = 'str'
    premode = ''
    ###############################################

    # creating publishers
    mode_pub = rospy.Publisher(mode_topic_name,String, queue_size=10)
    premode_pub = rospy.Publisher(premode_topic_name,String, queue_size=10) 
    

    # subscribing to topics
    rospy.Subscriber(change_mode_topic_name,String, change_mode_cb)
    rospy.Subscriber(status_topic_name,status, status_cb)

    rate = rospy.Rate(float(publish_rate))
    while not rospy.is_shutdown():
        rate.sleep()
        mode_pub.publish(mode)
        premode_pub.publish(premode)

    # stopLogging()



