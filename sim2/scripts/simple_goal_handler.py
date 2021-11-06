#!/usr/bin/env python

import rospy
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import Pose

import tf2_ros
import tf2_geometry_msgs  # **Do not use geometry_msgs. Use this instead for PoseStamped


def transform_pose(input_pose, from_frame, to_frame):
    # **Assuming /tf2 topic is being broadcasted
    tf_buffer = tf2_ros.Buffer()
    listener = tf2_ros.TransformListener(tf_buffer)

    pose_stamped = tf2_geometry_msgs.PoseStamped()
    pose_stamped.pose = input_pose
    pose_stamped.header.frame_id = from_frame
    pose_stamped.header.stamp = rospy.Time(0)

    try:
        # ** It is important to wait for the listener to start listening. Hence the rospy.Duration(1)
        output_pose_stamped = tf_buffer.transform(pose_stamped, to_frame, rospy.Duration(1))
        return output_pose_stamped.pose

    except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException) as e:
        print('error',e)
        return transform_pose(input_pose, from_frame, to_frame)
        
def handle(data):
    global x_lower,x_upper,y_lower,y_upper, pub,main_frame
    pose = Pose()
    pose.position.x = data.pose.position.x
    pose.position.y = data.pose.position.y
    pose.position.z = data.pose.position.z
    pose.orientation.x = data.pose.orientation.x
    pose.orientation.y = data.pose.orientation.y
    pose.orientation.z = data.pose.orientation.z
    pose.orientation.w = data.pose.orientation.w
    pose_translated = transform_pose(pose,  data.header.frame_id,  main_frame)
    if (x_lower<pose_translated.position.x<x_upper) and (y_lower<pose_translated.position.y<y_upper):
        pose_stamped = PoseStamped()
        pose_stamped.pose = pose_translated
        pose_stamped.header.stamp = rospy.Time.now()
        pose_stamped.header.frame_id = main_frame
        pub.publish(pose_stamped)



if __name__ =="__main__":
    main_frame = 'map'
    x_upper = 8.0
    x_lower = -5.0
    y_upper = 4.0
    y_lower = -4.0
    pub_topic = '/move_base_simple/goal'
    simple_goal_topic = '/simple_goal'

    pub = rospy.Publisher(pub_topic,PoseStamped,queue_size=10)
    rospy.init_node("simple_goal_handler")
    sub_simple_goal  = rospy.Subscriber(simple_goal_topic,PoseStamped,handle)
    rospy.spin()