

file_name = __file__.split('/')[-1][:-3]
if file_name == '__init__' or file_name == '__init__.':
    file_name = __file__.split('/')[-2]
def printLine(*args): 
    '''
        prints information on the console screen
    '''
    print(file_name+': '+'\n      - '+'\n      - '.join([str(arg) for arg in list(args)]))
    
import rospy
from geometry_msgs.msg import Twist
from slamware_ros_sdk.msg import CancelActionRequest
from slamware_ros_sdk.srv import SyncSetStcm
from slamware_ros_sdk.srv import SyncSetStcmRequest
import time
import glob
import os
from geometry_msgs.msg import Pose
printLine('Imported General requirents')

from scripts.navigation.actions import go_home_platform as go_home_action
from scripts.navigation.actions import manual as manual_action
from  scripts.navigation.actions import pass_action as pass_action

printLine('Imported Actions')

navigation_actions = {
    'go_home': go_home_action, 
    'manual': manual_action,
    'pass': pass_action,
}


cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
cancel_action_pub = rospy.Publisher('/slamware_ros_sdk_server_node/cancel_action', CancelActionRequest, queue_size=10)
printLine('Publishers have been created')
cancel_msg = CancelActionRequest()
twist_msg = Twist()
def stop():
    printLine('Stopping the Robot')
    twist_msg = Twist()
    cancel_action_pub.publish(cancel_msg)
    cmd_vel_pub.publish(twist_msg)


navigation_mode = 'pass'
navigation_actions[navigation_mode].start()
switch_timeout = 5
t_start= 0
def switch(nav_mode):
    global navigation_mode, t_start
    if time.time() - t_start > switch_timeout:
        if navigation_mode != nav_mode:
            if nav_mode in navigation_actions:
                t_start = time.time()
                navigation_actions[navigation_mode].cancel()
                navigation_mode = nav_mode
                stop()
                time.sleep(3)
                resp = navigation_actions[nav_mode].start()
                if resp ==  'failed':
                    printLine('Failed to Start Navigation mode')
                    navigation_actions['pass'].start()
                    return 'failed'
                printLine('Started navigation mode successfully')
                return 'running'
            else:
                printLine('Required Navigation mode is not found')
                return 'not_found'
        else:
            printLine('Navigation mode requested is already running')
            return 'already_running'
    else:
        printLine('Too rapid changing in naviagion mode')
        return 'too_rapid'
            
    
    
def get_navigation_mode():
    global navigation_mode
    return navigation_mode




######################################## maps related processing #############################

home= os.environ['HOME']
valid_files = ['map.pgm', 'goals.txt','map.stcm']
def list_maps():
    maps = glob.glob(home+'/catkin_ws/src/public/maps/*/')
    #printLine('Attempting to list maps from',home+'/catkin_ws/src/public/maps/*/',*maps)
    valid_maps = {}
    for m in maps:
        printLine('checking the validity of ', m,type(m))
        def delete_map(map_dir):
            os.system('rm -rf '+map_dir)
        files = os.listdir(m)
        delete_flag = False
        if len(files) < 2:
            delete_flag = True
        if not delete_flag:
            if 'pose.txt' not in files:
                delete_flag = True
        map_type = None
        if not delete_flag:
            if 'map.pgm' in files:
                map_type = 'map.pgm'
            elif 'map.stcm' in files:
                map_type = 'map.stcm'
            else:
                delete_flag = True
        if delete_flag:
            delete_map(m)
            continue
        else:
            printLine('map ', m + ' ' + str(type(m)), 'is valid')
            valid_maps[m.split('/')[-2]] = {
                'map': m+map_type,
                'pose': m+'pose.txt',
                'name': m.split('/')[-2]
            }
    return valid_maps        
    
def get_maps():
    maps = list_maps()
    if not maps:
        return 'no_maps'
    else:
        return '|'.join(['&'.join([m,maps[m]['map'],maps[m]['pose']]) for m in maps])

def maps_names():
    return [m.split('/')[-2] for m in glob.glob(home+'/catkin_ws/src/public/maps/*/')]

def get_maps_names():
    map_names_list = maps_names()
    if not map_names_list:
        return 'no_maps'
    else: 
        return '|'.join(map_names_list)

def sync_map(map_path, pose_path):
    file = open(map_path, 'rb')
    data = file.read()
    file.close()
    file = open(pose_path, 'r')
    pose = file.read()
    pose = pose.split('&')
    pose = [float(val) for val in pose]
    rospy.wait_for_service('slamware_ros_sdk_server_node/sync_set_stcm')
    req = SyncSetStcmRequest()
    req.raw_stcm = data
    req.robot_pose.position.x=pose[0]
    req.robot_pose.position.y=pose[1]
    req.robot_pose.position.z=pose[2]
    req.robot_pose.orientation.x=pose[3]
    req.robot_pose.orientation.y=pose[4]
    req.robot_pose.orientation.z=pose[5]
    req.robot_pose.orientation.w=pose[6]
    service = rospy.ServiceProxy('slamware_ros_sdk_server_node/sync_set_stcm',SyncSetStcm)
    service(req)

def set_map(map_name):
    global current_map
    maps = list_maps()
    if map_name not in maps:
        return 'not_found'
    sync_map(maps[map_name]['map'],maps[map_name]['pose'])
    current_map = map_name
    return 'Done'

current_map = None
def get_current_map():
    global current_map
    return current_map

set_pose_pub = rospy.Publisher('/slamware_ros_sdk_server_node/set_pose', Pose, queue_size=1)
def set_current_pose(pose):
    global set_pose_pub
    msg = Pose()
    pose = [float(val) for val in pose.split('&')]
    msg.position.x = pose[0]
    msg.position.y = pose[1]
    msg.position.z = pose[2]
    msg.orientation.x = pose[3]
    msg.orientation.y = pose[4]
    msg.orientation.z = pose[5]
    msg.orientation.w = pose[6]
    set_pose_pub.publish(msg)
    return 'Done'

set_home_pub = rospy.Publisher('/slamware_ros_sdk_server_node/set_home_pose', Pose, queue_size=1)
def set_current_home_pose(pose):
    global set_home_pub
    msg = Pose()
    pose = [float(val) for val in pose.split('&')]
    msg.position.x = pose[0]
    msg.position.y = pose[1]
    msg.position.z = pose[2]
    msg.orientation.x = pose[3]
    msg.orientation.y = pose[4]
    msg.orientation.z = pose[5]
    msg.orientation.w = pose[6]
    set_pose_pub.publish(msg)
    return 'Done'

def update_pose_file(pose):
    global current_map
    printLine('updating current map position', pose, current_map)
    map_list = list_maps()
    file = open(map_list[current_map]['pose'],'w+')
    file.write(pose)
    file.close()
    return 
    
    

def update_pose(pose):
    global current_map 
    if(current_map):
        set_current_pose(pose)
        set_current_home_pose(pose)
        update_pose_file(pose)
        return 'Done'
    else:
        return 'failed'