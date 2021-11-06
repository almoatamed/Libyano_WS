#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import Pose
from move_base_msgs.msg import MoveBaseActionResult
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import face_recognition
import numpy as np
import time
from tf import transformations
import math

def mode_cb(data):
    global mode
    mode = data.data

def get_yaw(pose):
    return transformations.euler_from_quaternion([pose.orientation.x,pose.orientation.y,pose.orientation.z,pose.orientation.w])[2]

def track_encoding_cb(data):
    global track_encoding, track_image_location, track_initial_robot_pose, track_string
    track_string = data.data
    parameters = data.data.split('&')
    track_encoding = np.array([float(i) for i in parameters[1].split('/')])
    track_image_location = [float(i) for i in parameters[0].split('/')]
    track_initial_robot_pose = Pose()
    track_initial_robot_pose.position.x = float(parameters[2])
    track_initial_robot_pose.position.y = float(parameters[3])
    track_initial_robot_pose.position.z = 0.0
    track_initial_robot_pose.orientation.x = float(parameters[4])
    track_initial_robot_pose.orientation.y = float(parameters[5])
    track_initial_robot_pose.orientation.z = float(parameters[6])
    track_initial_robot_pose.orientation.w = float(parameters[7])
    print(track_image_location)

def mb_result_cb(data):
    global mode, flag, pre_flag
    print('move base result callbase status text\n',data.status.text)
    if flag == 'trn':
        turn()

def turn():
    global goal_publisher, base_frame, turn_counter, turn_limit, turn_divider, flag,flags,pre_flag
   
    required_yaw = math.pi/turn_divider
    
    if turn_counter ==0 and flag != flags['turn']:
        pre_flag = flag
        flag = flags['turn']
        turn_counter +=1
    elif turn_counter>=turn_limit:
        turn_counter =0
        flag = pre_flag
        pre_flag = flags['turn']
    else:
        turn_counter+=1
    
    required_q = transformations.quaternion_from_euler(0,0,required_yaw)
    pose = PoseStamped()
    pose.pose.orientation.x = required_q[0]
    pose.pose.orientation.y = required_q[1]
    pose.pose.orientation.z = required_q[2]
    pose.pose.orientation.w = required_q[3]
    pose.header.frame_id = base_frame
    pose.header.stamp = rospy.Time.now()
    goal_publisher.publish(pose)
    

def estimate_location():
    global track_initial_robot_pose, track_image_location, track_center
    right = track_image_location[1]
    left = track_image_location[3]

    track_center = (right+left)/2



if __name__ == "__main__":

    # parameters
    mode = 'nav'
    flag = 'nav'
    flags = {
        'turn':'trn', # it means the robot is turning around
        'track':'trk'
    }
    pre_flag = 'nav'

    base_frame = 'base_footprint'
    main_frame = 'map'

    turn_counter = 0
    turn_limit = 3 
    turn_divider = 2

    track_string = ''
    track_encoding = ''
    track_initial_robot_pose = ''
    track_image_location = ''
    track_center

    mb_result_topic = '/move_base/result'

    goal_publisher = rospy.Publisher('/simple_goal',PoseStamped,queue_size=10)

    rospy.init_node('tracker')

    rospy.Subscriber('/track_encoding', String, track_encoding_cb)
    rospy.Subscriber('/mode', String, mode_cb)
    rospy.Subscriber(mb_result_topic, MoveBaseActionResult, mb_result_cb)
    turn()
    rospy.spin()