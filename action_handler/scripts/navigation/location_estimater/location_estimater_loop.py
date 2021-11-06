
import rospy
from geometry_msgs.msg import Pose
import tf 
import time
rospy.init_node('location_estimater_loop')


file_name = __file__.split('/')[-1][:-3]
if file_name == '__init__' or file_name == '__init__.':
    file_name = __file__.split('/')[-2]
def printLine(*args):
    '''
        prints information on the console screen
    '''
    global name
    print(file_name+': '+'\n      - '+'\n      - '.join([str(arg) for arg in list(args)]))


listener = tf.TransformListener()
to_frame = '/slamware_map'
from_frame = '/base_link'
def transform_pose():
    global to_frame, from_frame
    try:
        (trans,rot) = listener.lookupTransform(to_frame, from_frame, rospy.Time(0))
        return trans,rot
    except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
        return False, False
    
    
rate = rospy.Rate(8)
pub = rospy.Publisher('/current_pose', Pose, queue_size=1)
pose = Pose()
def run():
    global pub, rate
    printLine('Running Location Estimater')
    while not rospy.is_shutdown():
        time.sleep(0.125)
        trans,rot = transform_pose()
        if trans:
            pose.position.x = trans[0]
            pose.position.y = trans[1]
            pose.position.z = trans[2]
            pose.orientation.x = rot[0]
            pose.orientation.y = rot[1]
            pose.orientation.z = rot[2]
            pose.orientation.w = rot[3]
            pub.publish(pose)

run()