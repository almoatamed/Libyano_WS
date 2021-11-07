

file_name = __file__.split('/')[-1][:-3]
if file_name == '__init__' or file_name == '__init__.':
    file_name = __file__.split('/')[-2]
def printLine(*args):
    '''
        prints information on the console screen
    '''
    global name
    print(file_name+': '+'\n      - '+'\n      - '.join([str(arg) for arg in list(args)]))

import subprocess
import os 
import rospy
from geometry_msgs.msg import Pose

home = os.environ['HOME']

running_state = False
proc = False
def start():
    global running_state, proc
    if not running_state:
        running_state = True
        try:
            #printLine('About to start the loop')
            proc = subprocess.Popen(str('/usr/bin/python '+home+'/catkin_ws/src/action_handler/scripts/navigation/location_estimater/location_estimater_loop.py').split(b' '))
            #printLine('started the loop')
        except Exception as e:
            #printLine('failed to start',e)
            return 'failed'
    return 'Done'
    
def stop():
    global running_state, proc
    if running_state:
        running_state = False
        try:
            os.system('rosnode kill /location_estimater_loop')
        except Exception as e:
            pass
            #printLine('Error while terminating proc', e)
        try:
            proc.terminate()
        except Exception as e:
            #printLine('Error while terminating proc', e)
        proc = False
    return "Done"

def is_running():
    global running_state
    if running_state:
        return 'yes'
    else:
        return 'no'

start()

current_pose = Pose()
def current_pose_cb(msg):
    global current_pose 
    current_pose = msg
rospy.Subscriber("/current_pose", Pose, current_pose_cb)
def get_current_pose():
    return '&'.join([
        str(current_pose.position.x),
        str(current_pose.position.y),
        str(current_pose.position.z),
        str(current_pose.orientation.x),
        str(current_pose.orientation.y),
        str(current_pose.orientation.z),
        str(current_pose.orientation.w),
        ])