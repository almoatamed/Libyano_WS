#!/usr/bin/env python
import rospy
from sensor_msgs.msg import CompressedImage
import face_recognition
import cv2
from cv_bridge import CvBridge
import numpy as np
import time 


# Initialize some variables
def image_cb(data):
    print('cb')
    global breaker, face_locations, cv_bridge, start
    # if time.time() - start > 0.2:
    start= time.time()
    frame = cv_bridge.compressed_imgmsg_to_cv2(data)
    frame = np.array(frame)[:,:,::-1]
    face_locations = face_recognition.face_locations(frame)
    
    # Display the results
    for top, right, bottom, left in face_locations:
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        face_distance_const = 1.0 
        width_px_const = 75
        font = cv2.FONT_HERSHEY_DUPLEX
        width = right - left
        height = abs(top - bottom)
        avg = (width+height)/2
        distance = (-0.0217*width + 2.6275)
        print(distance,avg,height,width,left,top,right,bottom)
        cv2.putText(frame, str(distance), (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        # Display the resulting image
        cv2.imshow('Video', frame)



if __name__ == "__main__":

    start = time.time()

    face_locations = []
    cv_bridge = CvBridge()
    rospy.init_node('face_recognizer_test')

    rospy.Subscriber('camera/image_raw/compressed',CompressedImage,image_cb)

    rospy.spin()
    video_capture.release()
    cv2.destroyAllWindows()