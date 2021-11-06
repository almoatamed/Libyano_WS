#!/usr/bin/env python

# this node will subscribe to the compressed camera image and perform face recognition on it, 
# if there is a face that we newly recognize and if that face existed in the range of the robot 
# also that face exists continuesly for defined amound of frames then we will start traking the person


# rospy used to initialize, subscribe, and publish
import rospy

# used to publish the chamge mode topic
from std_msgs.msg import String

# used to subscribe to the camera
from sensor_msgs.msg import Image
# from sensor_msgs.msg import CompressedImage

# used to publish the simple goal of tracking mode on the person track topic 
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import Pose

# used to convert Image message to cv mat image 
from cv_bridge import CvBridge
import face_recognition
import numpy as np
import time
# import cv2
from actionlib_msgs.msg import GoalID
from geometry_msgs.msg import Twist
from simple_goal_handler import transform_pose
import tf
from geometry_msgs.msg import Twist
def analyze_frame(data):
    global mode, track_encoding, change_mode_pub, pause, base_footprint_to_map, track_encodings, track_locations, track_location, old, cv_bridge, known_face_encodings, unknown_face_encodings,unknown_face_counts,unknown_face_counts_increased, goal_cancel_publisher, track_string, cmd_vel_pub
    # print('current mode',mode)
    if mode == 'nav' and not pause: # ignore pause its certainly useless
        # if time.time()>= old+0.2:
        print('analyzing')
        old = time.time()
        print(data.header.stamp)
        frame = cv_bridge.imgmsg_to_cv2(data,'bgr8')
        # frame = cv_bridge.compressed_imgmsg_to_cv2(data,)
        frame = np.array(frame)[:,:,::-1]
        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)
        for face,i in zip(face_encodings,range(len(face_encodings))):
            matches = face_recognition.compare_faces(known_face_encodings, face)
            if any(matches):
                print('i know you')
                continue
            else:
                matches = face_recognition.compare_faces(unknown_face_encodings, face)
                if(any(matches)):
                    index = matches.index(True)
                    unknown_face_counts[index]+=1
                    unknown_face_counts_increased[index] = True 
                else:
                    print('new face')
                    unknown_face_encodings.append(face)
                    unknown_face_counts.append(0)
                    unknown_face_counts_increased.append(False)
                    unknown_face_locations.append(face_locations[i])
        
        track_encodings = []
        track_locations = []
        for i in range(len(unknown_face_encodings)):
            if not unknown_face_counts_increased[i]:
                unknown_face_counts[i] = 0
            if unknown_face_counts[i] >= unknown_face_track_count:
                track_encodings.append(unknown_face_encodings[i])
                track_locations.append(unknown_face_locations[i])
        
        unknown_face_counts_increased = [False for _ in range(len(unknown_face_counts_increased))]
        
        if len(track_encodings) == 1:
            change_mode_pub.publish(track_mode_name)
            goal_id= GoalID()
            goal_cancel_publisher.publish(goal_id)
            twist = Twist()
            cmd_vel_pub.publish(twist)
            pause = True

            track_encoding = track_encodings[0]
            track_location = track_locations[0]

            pose = Pose()
            pose.position.x = 0.0
            pose.position.y = 0.0
            pose.position.z = 0.0
            pose.orientation.x = 0.0
            pose.orientation.y = 0.0
            pose.orientation.z = 0.0
            pose.orientation.w = 1.0

            base_footprint_to_map = transform_pose(pose,'base_footprint','map')

            track_encoding_string = '/'.join([str(float(i)) for i in list(track_encoding)])
            track_location_string = '/'.join(str(float(i)) for i in track_location)
            track_string = '&'.join([
                track_location_string,
                track_encoding_string,
                str(base_footprint_to_map.position.x),
                str(base_footprint_to_map.position.y),
                str(base_footprint_to_map.orientation.x),
                str(base_footprint_to_map.orientation.y),
                str(base_footprint_to_map.orientation.z),
                str(base_footprint_to_map.orientation.w),
                ])

            print(track_encoding_string)
            print(track_location_string)
            print(track_string)

        elif len(track_encodings)>1:
            change_mode_pub.publish('trk')
            goal_id= GoalID()
            goal_cancel_publisher.publish(goal_id)
            twist = Twist()
            cmd_vel_pub.publish(twist)
            pause = True

            index = track_locations.index(max([abs(i[0]-i[2]) for i in face_locations]))
            track_encoding = track_encodings[index]
            track_location = track_locations[index]

            pose = Pose()
            pose.position.x = 0.0
            pose.position.y = 0.0
            pose.position.z = 0.0
            pose.orientation.x = 0.0
            pose.orientation.y = 0.0
            pose.orientation.z = 0.0
            pose.orientation.w = 1.0

            base_footprint_to_map = transform_pose(pose,'base_footprint','map')

            track_encoding_string = '/'.join([str(float(i)) for i in list(track_encoding)])
            track_location_string = '/'.join(str(float(i)) for i in track_location)
            track_string = '&'.join([
                track_location_string,
                track_encoding_string,
                str(base_footprint_to_map.position.x),
                str(base_footprint_to_map.position.y),
                str(base_footprint_to_map.orientation.x),
                str(base_footprint_to_map.orientation.y),
                str(base_footprint_to_map.orientation.z),
                str(base_footprint_to_map.orientation.w),
                ])

            print(track_encoding_string)
            print(track_location_string)
            print(track_string)

        # print(track_encoding)

def change_mode(data):
    global mode, track_encoding_string, track_encoding, track_location, track_location_string, track_string, pause
    if data.data!='trk':
        pause = False
    mode = data.data

def publish_tracked_face_encoding():
    global track_encoding

def track_encoding_pub():
    global mode, track_publisher, track_encoding, track_location
    if mode == track_mode_name and track_string:
            track_publisher.publish(track_string)

            

if __name__ == "__main__":
    # starting main program
    print('starting face recognition ...')
    
    # parameters
    mode = 'nav' # modes are nav for navigation, chg for charging, trk for tracking , grt for greeting

    track_encoding = []
    track_encodings = []
    track_location = []
    track_locations = []
    track_encoding_string = ''
    track_location_string = ''
    track_string = ''
    base_footprint_to_map = Pose()

    node_name = "face_recognizer"
    track_mode_name = 'trk'

    change_mode_topic = "/change_mode"
    person_track_topic = "/person_track"
    camera_topic = '/camera/image_raw'
    # camera_topic = '/usb_cam/image_raw/compressed'
    mode_topic = '/mode'
    track_encoding_topic = '/track_encoding'
    goal_cancel_topic = '/move_base/cancel'
    vel_topic = '/cmd_vel'

    known_face_encodings = []

    unknown_face_locations = []
    unknown_face_encodings = []
    unknown_face_counts = []
    unknown_face_counts_increased = []
    unknown_face_track_count = 5
    pause = False

    # covnersino bridge 
    cv_bridge = CvBridge()

    # timers
    old = time.time()
    
    # publishers
    # this topic publisher is for changing the robot mode 
    change_mode_pub = rospy.Publisher(change_mode_topic,String,queue_size=10)
    # this topic is for publishing the face encoding of the person being tracked 
    track_publisher = rospy.Publisher(track_encoding_topic, String, queue_size=10)
    goal_cancel_publisher = rospy.Publisher(goal_cancel_topic,GoalID,queue_size=10)
    cmd_vel_pub = rospy.Publisher(vel_topic, Twist, queue_size=10)
    # initializing node
    rospy.init_node(node_name)

    # subscribers 
    # image source, the main camera
    sub_camera = rospy.Subscriber(camera_topic,Image,analyze_frame)
    # sub_camera = rospy.Subscriber(camera_topic,CompressedImage,analyze_frame)
    # mode tracker
    sub_mode = rospy.Subscriber(mode_topic, String, change_mode) 

    rate = rospy.Rate(1)
    rate.sleep()
    while not rospy.is_shutdown():
        track_encoding_pub()
        rate.sleep()







