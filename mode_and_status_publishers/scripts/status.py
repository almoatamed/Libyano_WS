#!/usr/bin/env python
from __future__ import print_function
import rospy
from status_msgs.msg import status
from status_msgs.msg import driver_msg
from std_msgs.msg import String
from slamware_ros_sdk.msg import RobotBasicState
import subprocess

###################
# this script receives the currenct robot statsu from different 
# parties and translate it into one status message
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
    

def platform_basic_state_cb(state_message):
    global current_status
    current_status.power.battery = state_message.battery_percentage
    current_status.power.cord = state_message.is_dc_in
    current_status.power.charging_status = state_message.is_charging

def interactive_mcu_cb(msg):
    global current_status
    current_status.sensors = msg.sensors
    current_status.controllers = msg.controllers
    current_status.mcu = [1]

# def driver_cb(msg):
#     global current_status
#     current_status.driver = msg

def mode_cb(mode):
    global current_status
    current_status.mode = mode.data

# def controlled_processes_cb(msg):
#     global current_status
#     current_status.system_controlled_processes = msg.data


if __name__ == "__main__":


    ###############################################
    #parameters#
    ###############################################
    
    current_status = status()
    
    node_name = "status_handler"
    anonymous_node = False
    rospy.init_node(node_name, anonymous=anonymous_node)

    status_topic = rospy.get_param('/status/status_topic', '/status')
    interactive_mcu_topic = rospy.get_param('/mcu/interactive/out_topic','/mcu/interactive/output')
    platform_basic_state  = rospy.get_param('/platform/basic_state', '/slamware_ros_sdk_server_node/robot_basic_state')
    # movement_driver_topic = rospy.get_param('/mcu/movement/driver/status_topic','/mcu/movement/driver/status')
    # controlled_processes_topic = rospy.get_param('/system/controlled_processes_topic','/system/controlled_processes')
    mode_topic = '/mode'
    
    publish_rate = rospy.get_param('/status/status_rate', '5')
    current_status.power.battery = 90
    current_status.power.charging_status = 0
    current_status.mcu = [0]
    node_list = [] 
    ###############################################

    status_pub = rospy.Publisher(status_topic,status, queue_size=10)

    rospy.Subscriber(interactive_mcu_topic, status, interactive_mcu_cb)
    rospy.Subscriber(platform_basic_state, RobotBasicState,platform_basic_state_cb)
    # rospy.Subscriber(movement_driver_topic, driver_msg, driver_cb )
    # rospy.Subscriber(controlled_processes_topic, String, controlled_processes_cb )
    rospy.Subscriber(mode_topic, String, mode_cb)

    rate = rospy.Rate(float(publish_rate))
    while not rospy.is_shutdown():
        rate.sleep()
        status_pub.publish(current_status)