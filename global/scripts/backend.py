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
    
rospy.init_node('backend')

#printLine('starting backend')

home = os.environ['HOME']
command = r'/usr/bin/node '+home+'/catkin_ws/src/backend/index.js'
p = subprocess.Popen(command.split(' '))
#printLine('started backend')
rate = rospy.Rate(0.5)
while not rospy.is_shutdown() and not p.poll():
    rate.sleep()
try:
    p.terminate()
except:
    pass
#printLine('backend process died')
