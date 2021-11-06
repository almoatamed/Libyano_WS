#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped, Pose
from move_base_msgs.msg import MoveBaseActionResult
from simple_goal_handler import transform_pose
from tf.transformations import euler_from_quaternion as e2q
from tf.transformations import quaternion_from_euler as q2e
from math import pi
from geometry_msgs.msg import Twist
from common import splitter

def status_cb(data):
    global status 
    status = splitter(data.data)

def mode_cb(data):
    global mode, cmd_vel_pub
    if data.data == 'chg':
        twist = Twist()
        cmd_vel_pub.publish(twist)
    mode = data.data

def go_home():
    global simple_goal_pub
    pose = PoseStamped()
    pose.header.stamp = rospy.Time(0)
    pose.header.frame_id = 'map'
    pose.pose.position.x = -2.7
    pose.pose.position.y = 1.5
    pose.pose.orientation.w = 1.0
    simple_goal_pub.publish(pose)

def result_cb(data):
    global status, cmd_vel_pub, home_modes
    if mode in home_modes:
        pose = Pose()
        pose.position.x = 0.0
        pose.position.y = 0.0
        pose.position.z = 0.0
        pose.orientation.x = 0.0
        pose.orientation.y = 0.0
        pose.orientation.z = 0.0
        pose.orientation.w = 1.0
        base_footprint_to_map = transform_pose(pose,'base_footprint','map')
        x = base_footprint_to_map.position.x
        y = base_footprint_to_map.position.y
        yaw = e2q([
            base_footprint_to_map.orientation.x,
            base_footprint_to_map.orientation.y,
            base_footprint_to_map.orientation.z,
            base_footprint_to_map.orientation.w,
        ])[2]
        yaw_angle = yaw*180/pi
        print(x,y,yaw_angle)

        if (-10<yaw_angle<10) and (x<-2.6) and (1.4<y<1.6) and mode != 'chg':
            twist = Twist()
            twist.linear.x = -0.24
            cmd_vel_pub.publish(twist)
        



if __name__ == '__main__':

    mode = ''
    home_modes = ['lbt','sth']

    simple_goal_pub = rospy.Publisher('/simple_goal', PoseStamped,queue_size=10)
    cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rospy.init_node('go_home')

    rospy.Subscriber('/status',String,status_cb)
    rospy.Subscriber('mode',String,mode_cb)
    rospy.Subscriber('/move_base/result', MoveBaseActionResult, result_cb)

    rate = rospy.Rate(0.05)
    while not rospy.is_shutdown():
        
        rate.sleep()
        if mode in home_modes and status['charging'] == '0':
            go_home()

