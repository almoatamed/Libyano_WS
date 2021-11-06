#!/usr/bin/env python
import rospy
from sensor_msgs.msg import CompressedImage as Image
from cv_bridge import CvBridge
import cv2


def gstreamer_pipeline():
    return (
        "nvarguscamerasrc ! "
        "video/x-raw(memory:NVMM), "
        "width=(int)%d, height=(int)%d, "
        "format=(string)NV12, framerate=(fraction)%d/1 ! "
        "nvvidconv flip-method=%d ! "
        "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
        "videoconvert ! "
        "video/x-raw, format=(string)BGR ! appsink"
        % (
            capture_width,
            capture_height,
            framerate,
            flip_method,
            display_width,
            display_height,
        )
    )

def pub_image_msg():
    global cap, pub, cv_bridge
    ret, img = cap.read()
    if ret:
        img_msg = cv_bridge.cv2_to_compressed_imgmsg(img)
        img_msg.header.stamp = rospy.Time.now()
        img_msg.header.frame_id = 'base_link'
        # print('\n')
            # print(rospy.Time.now())
        pub.publish(img_msg)


if __name__ == '__main__':

    # parameters 
    capture_width=1280
    capture_height=720
    display_width=1280
    display_height=720 
    framerate=10
    flip_method=0

    pub = rospy.Publisher('camera/image_raw/compressed',Image, queue_size=0)

    rospy.init_node('pi_camera')

    rate = rospy.Rate(framerate+1)

    print(gstreamer_pipeline())
    cap = cv2.VideoCapture(gstreamer_pipeline(), cv2.CAP_GSTREAMER)
    cv_bridge = CvBridge()

    if cap.isOpened():
        while not rospy.is_shutdown():
            rate.sleep()
            pub_image_msg()
    else:
        print('Could not open camera')
