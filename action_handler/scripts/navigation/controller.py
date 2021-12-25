file_name = __file__.split('/')[-1][:-3]
if file_name == '__init__' or file_name == '__init__.':
    file_name = __file__.split('/')[-2]
def printLine(*args): 
    '''
        prints information on the console screen
    '''
    print(file_name+': '+'\n      - '+'\n      - '.join([str(arg) for arg in list(args)]))
    
import glob
import os
import rospy
import time
# import threading

from slamware_ros_sdk.srv import SyncSetStcmRequest, SyncSetStcm

from slamware_ros_sdk.msg import CancelActionRequest, MoveToRequest, GoHomeRequest, MoveByDirectionRequest, ActionDirection
from geometry_msgs.msg import Pose, Twist, PoseStamped

######################################## navigation control related #############################


################ Detach and Stop ###################


cmd_vel_pub = rospy.Publisher('/slamware_ros_sdk_server_node/cmd_vel_no_limit', Twist, queue_size=10)
cancel_action_pub = rospy.Publisher('/slamware_ros_sdk_server_node/cancel_action', CancelActionRequest, queue_size=10)
cancel_msg = CancelActionRequest()
twist_msg = Twist()
def stop():
    global twist_msg
    ##printLine('Stopping the Robot')
    twist_msg = Twist()
    # cancel_action_pub.publish(cancel_msg)
    cmd_vel_pub.publish(twist_msg)
    return 'stopped'

detach_flag = False
def detach(val):
    global detach_flag
    if val == '1':
        detach_flag = False
        return 'connected'
    else:
        detach_flag = True
        stop()
        return 'detached'

def toggle_detach():
    global detach_flag
    detach_flag = not detach_flag
    stop()
    return 'done'

def is_detached():
    global detach_flag
    if detach_flag:
        return '0'
    else: 
        return '1'
        

################ linear manual movement ###################
move_msg_publish_time = 0
def move(x,z):
    global twist_msg, move_msg_publish_time
    if not detach_flag:
        if not (float(x) == twist_msg.linear.x and float(z) == twist_msg.angular.z):
            move_by_direction_msg = MoveByDirectionRequest()
            move_by_direction_msg.direction.direction = -1
            move_by_direction_msg.options.speed_ratio.is_valid = True
            move_by_direction_msg.options.speed_ratio.value = -0.05
            move_by_direction_pub.publish(move_by_direction_msg)
            twist_msg = Twist()
            twist_msg.linear.x = float(x)
            twist_msg.angular.z = float(z)
            if(abs(twist_msg.linear.x )>0.3 or abs(twist_msg.angular.z )>0.7):
                return 'failed'
            cmd_vel_pub.publish(twist_msg)
            move_msg_publish_time = time.time()
        return 'moving'
    else:
        return 'Detached'

move_by_direction_msg = MoveByDirectionRequest()
move_by_direction_pub = rospy.Publisher('/slamware_ros_sdk_server_node/move_by_direction', MoveByDirectionRequest, queue_size=10)
move_by_direction_request = '0'
def move_by_direction(req):
    global move_by_direction_pub, twist_msg, move_msg_publish_time, move_by_direction_msg, move_by_direction_request
    if not detach_flag:
        move_by_direction_msg = MoveByDirectionRequest()
        move_by_direction_msg.options.speed_ratio.is_valid = True
        move_by_direction_msg.options.speed_ratio.value = 0.05
        if req != '-1':
            if move_by_direction_request != req:
                move_by_direction_request = req
                move_by_direction_msg.direction.direction = int(req)
                move_by_direction_pub.publish(move_by_direction_msg)
        else:
            if move_by_direction_request != '-1':
                move_by_direction_request = '-1'
                stop()
    else:
        return 'Detached'

# def threaded_move_terminater():
    # global move_msg_publish_time, twist_msg
    # while not rospy.is_shutdown():
        # time.sleep(0.2)
        # if (twist_msg.linear.x != 0 or twist_msg.angular.z != 0 ) and time.time() - move_msg_publish_time > 0.4:
        #     stop()
            
# thread = threading.Thread(target=threaded_move_terminater)
# thread.start()

################ autonomous angled goal ###################

    
angled_goal_pub = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=10)
def angled_goal(pose):
    global angled_goal_pub
    if not detach_flag:
        msg = PoseStamped()
        pose = [float(val) for val in pose.split('&')]
        msg.header.frame_id = 'slamware_map'
        msg.header.stamp = rospy.Time.now()
        msg.header.frame_id
        msg.pose.position.x = pose[0]
        msg.pose.position.y = pose[1]
        msg.pose.position.z = pose[2]
        msg.pose.orientation.x = pose[3]
        msg.pose.orientation.y = pose[4]
        msg.pose.orientation.z = pose[5]
        msg.pose.orientation.w = pose[6]
        angled_goal_pub.publish(msg)
        return 'Done'
    else:
        return 'Detached'
    
################ autonomous unangled goal ###################
unangled_goal_pub = rospy.Publisher('/slamware_ros_sdk_server_node/move_to', MoveToRequest, queue_size=1)
def unangled_goal(pose):
    global unangled_goal_pub
    if not detach_flag:
        msg = MoveToRequest()
        pose = [float(val) for val in pose.split('&')]
        msg.location.x = pose[0]
        msg.location.y = pose[1]
        msg.location.z = 0.0
        unangled_goal_pub.publish(msg)
        return 'Done'
    else:
        return "Detached"
    
################ Go Home Request ###################
go_home_pub = rospy.Publisher('/slamware_ros_sdk_server_node/go_home',GoHomeRequest, queue_size=10)    
def go_home():
    global go_home_pub
    if not detach_flag:
        msg = GoHomeRequest()
        go_home_pub.publish(msg)
        return "Done"
    else: 
        return "Detached"
    
    
######################################## maps related processing #############################

home= os.environ['HOME']
valid_files = ['map.pgm', 'goals.txt','map.stcm']
def list_maps():
    maps = glob.glob(home+'/catkin_ws/src/public/maps/*/')
    ###printLine('Attempting to list maps from',home+'/catkin_ws/src/public/maps/*/',*maps)
    valid_maps = {}
    for m in maps:
        ##printLine('checking the validity of ', m,type(m))
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
            ##printLine('map ', m + ' ' + str(type(m)), 'is valid')
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
    ##printLine('updating current map position', pose, current_map)
    map_list = list_maps()
    file = open(map_list[current_map]['pose'],'w+')
    file.write(pose)
    file.close()
    return 
    
    

def update_pose(pose):
    global current_map 
    if(current_map):
        set_current_pose(pose)
        # set_current_home_pose(pose)
        update_pose_file(pose)
        return 'Done'
    else:
        return 'failed'