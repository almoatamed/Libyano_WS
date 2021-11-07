#!/usr/bin/env python

import rospy
from status_msgs.msg import status
import subprocess
import time

import sys
import os
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

# from movement import run as movement_run
from exception_scripts.power import run as power_run
from exception_scripts.web_server import run as web_server_run
from exception_scripts.interactive import run as interactive_run
from exception_scripts.system_J import run as system_J_run
from exception_scripts.system_R import run as system_R_run
# from hardware import run as hardware_run


x = subprocess.check_output('sudo lshw'.split(' ')).decode().split('\n')
p = []
for i,index in zip(x,range(len(x))):
    if 'product' in i:
        p.append(i.split(':'))

system_type = p[0][1].split(' ')[1][0]
if system_type == 'N':
    system_type = 'J'
if system_type not in ['R', 'J']:
    system_type = 'G'
    
file_name = __file__.split('/')[-1][:-3]
if file_name == '__init__' or file_name == '__init__.':
    file_name = __file__.split('/')[-2]
def printLine(*args):
    '''
        prints information on the console screen
    '''
    global name
    print(file_name+': '+'\n      - '+'\n      - '.join([str(arg) for arg in list(args)]))

#printLine('Starting Exception Handler',system_type)

R_exception_hanlders = {
    # 'interactive': interactive_run,
    # 'system_R_run': system_R_run,
    'power': power_run,
    }

J_exception_hanlders = {
    # 'movement': movement_run,
    # 'webserver': web_server_run,
    # 'power': power_run,
    # 'hardware' : hardware_run
    # 'system_J_run': system_J_run,
    }

G_exception_hanlders = {
    # 'movement': movement_run,
    # 'interactive': interactive_run,
    'power': power_run,
    # 'webserver': web_server_run,
    #'hardware' : hardware_run
    # 'system_R_run': system_R_run
    }

exception_hanlders = {
    'R': R_exception_hanlders,
    'G': G_exception_hanlders,
    'J': J_exception_hanlders
}

current_status = None 

def status_cb(msg):
    global current_status, current_nodes_list
    current_status = msg
    current_status.nodes_list = current_nodes_list

def run():
    global exception_hanlders, current_status
    for category in exception_hanlders[system_type]:
        exception_hanlders[system_type][category](current_status)
        
def check_nodes_list():
    global current_nodes_list
    try:
        current_nodes_list= [node for node in subprocess.check_output('rosnode list', shell=True).split('\n') if node]
    except TypeError: 
        current_nodes_list = [node for node in subprocess.check_output('rosnode list', shell=True).decode().split('\n') if node]
      
printLine(system_type)

if __name__ == "__main__":
    rospy.init_node('exceptiun_server')
    rospy.Subscriber(rospy.get_param('/status/topic_name','/status'),status,status_cb)
    rate = rospy.Rate(2)
    current_status = status()
    current_nodes_list =[] 
    period= 3
    count = 0
    time.sleep(30)
    check_nodes_list()
    while not rospy.is_shutdown():
        if count>period:
            check_nodes_list()
            count = 0
        else:
            count+=1
        current_status.nodes_list = current_nodes_list
        rate.sleep()
        # if current_status:
        run()
        