#!/usr/bin/env python
import rospy 

from sensor_msgs.msg import CompressedImage
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import Pose
from actionlib_msgs.msg import GoalID
from geometry_msgs.msg import Twist


import cv_bridge
import cv2
import numpy as np
import face_recognition

from datetime import datetime
# import threading
import time

from simple_goal_handler import transform_pose




#############S####################################
# functions
#################################################

def log(data):
    now = datetime.now().strftime('%H:%M:%S')
    print(now + ': ' + str(data))

def analyze_frame(frame):
    start = time.time()
    # log('analyzing')
    global  mode, track_encoding , change_mode_pub,\
            track_location, bridge, faceCascade, unknown_face_track_count, \
            known_face_encodings, unknown_face_encodings,unknown_face_counts,\
            unknown_face_counts_increased, goal_cancel_publisher, track_string, cmd_vel_pub
    
    scale_percent = 40

    frame = bridge.compressed_imgmsg_to_cv2(frame,'bgr8')

    width = int(frame.shape[1] * scale_percent / 100)
    height = int(frame.shape[0] * scale_percent / 100)

    gray = cv2.cvtColor(cv2.resize(frame, (width, height)), cv2.COLOR_BGR2GRAY)
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_locations = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    if len(face_locations) >0:
        print(face_locations)
        face_encodings = face_recognition.face_encodings(frame, face_locations)
        for face,i in zip(face_encodings,range(len(face_encodings))):
            matches = face_recognition.compare_faces(known_face_encodings, face)
            if not any(matches):
                matches = face_recognition.compare_faces(unknown_face_encodings, face)
                if any(matches):
                    index = matches.index(True)
                    unknown_face_counts[index]+=1
                    unknown_face_counts_increased[index] = True 
                else:
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
            change_mode_pub.publish('trk')
            goal_id= GoalID()
            goal_cancel_publisher.publish(goal_id)
            twist = Twist()
            cmd_vel_pub.publish(twist)

            track_encoding = track_encodings[0]
            track_location = track_locations[0]
            known_face_encodings.append(track_encoding)

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
            log('Tracking an encoding located at' + str(track_location))            
        elif len(track_encodings) > 1:
            change_mode_pub.publish('trk')
            goal_id= GoalID()
            goal_cancel_publisher.publish(goal_id)
            twist = Twist()
            cmd_vel_pub.publish(twist)

            index = track_locations.index(max([abs(i[0]-i[2]) for i in face_locations]))
            track_encoding = track_encodings[index]
            track_location = track_locations[index]
            known_face_encodings.append(track_encoding)
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
            log('Tracking an encoding located at' + str(track_location))
   
    log('Finished at: ' + str(time.time() - start))
##################################################





#################################################
# publisher
#################################################

def track_encoding_pub():
    global mode
    if mode == 'trk' and track_string:
            track_publisher.publish(track_string)

##################################################



#################################################
# callbacks
#################################################

def mode_cb(data):
    global mode, premode
    premode = mode
    mode = data.data

##################################################






#################################################
# main
#################################################

def main():
    global  mode, track_encoding , change_mode_pub, unknown_face_locations, \
            track_location, bridge, track_publisher, cmd_vel_pub, faceCascade, \
            known_face_encodings, unknown_face_encodings,unknown_face_counts,\
            unknown_face_counts_increased, goal_cancel_publisher, track_string, \
            unknown_face_track_count
            
    # parameters 
    mode = 'nav'
    premode = ''


    track_encoding = []
    track_location = []
    known_face_encodings = []
    unknown_face_encodings = []
    unknown_face_counts = []
    unknown_face_counts_increased = []
    unknown_face_locations = []
    track_string = ''
    unknown_face_track_count = 3

    # loading cascade model
    bridge = cv_bridge.CvBridge()
    faceCascade = cv2.CascadeClassifier('/usr/share/opencv4/haarcascades/haarcascade_frontalface_default.xml')


    # publishers
    # this topic publisher is for changing the robot mode 
    change_mode_pub = rospy.Publisher("/change_mode",String,queue_size=10)
    # this topic is for publishing the face encoding of the person being tracked 
    track_publisher = rospy.Publisher('/track_encoding', String, queue_size=10)
    # for cancelling goals of move base
    goal_cancel_publisher = rospy.Publisher('/move_base/cancel',GoalID,queue_size=10)
    # (command volecity) manual control of robot movement
    cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)


    # initializing node
    log('initializing node')
    rospy.init_node('threaded_face')

    # subscriptions
    log('subscribing to topics ...')
    mode_sub = rospy.Subscriber('/mode', String, mode_cb)

    # main loop
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        if mode == 'nav':
            frame = rospy.wait_for_message('/usb_cam/image_raw/compressed', CompressedImage)
            analyze_frame(frame)
            # x = threading.Thread(target=analyze_frame, args=(frame,))
            # x.setDaemon(True)
            # x.start()
            # log(str(imgmsg.header.stamp), str(face_encodings))
            # log('new image is received ')
        else:
            rate.sleep
            track_encoding_pub()

    log('Exiting threaded face detection and recognition node')


##################################################





##################################################
# main call 
##################################################
if __name__ == '__main__':
    main()
##################################################
