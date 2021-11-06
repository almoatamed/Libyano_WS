#!/usr/bin/env python
import os
import subprocess
import rospy

file_name = __file__.split('/')[-1][:-3]
if file_name == '__init__' or file_name == '__init__.':
    file_name = __file__.split('/')[-2]
def printLine(*args):
    '''
        prints information on the console screen
    '''
    global name
    print(file_name+': '+'\n      - '+'\n      - '.join([str(arg) for arg in list(args)]))
    
rospy.init_node('interface_process_monitor')

printLine('starting interface')

home = os.environ['HOME']
os.chdir(home+'/catkin_ws/src/third_party/web_server/interface_app')
command = r'/usr/bin/npm start'
p = subprocess.Popen(command.split(' '))
printLine('started interface')
rate = rospy.Rate(0.5)
while not rospy.is_shutdown() and not p.poll():
    rate.sleep()
try:
    p.terminate()
except:
    pass
printLine('interface process died')

