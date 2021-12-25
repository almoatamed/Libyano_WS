import rospy
# import os
import time
from geometry_msgs.msg import PoseStamped
import threading 



file_name = __file__.split('/')[-1][:-3]
if file_name == '__init__' or file_name == '__init__.':
    file_name = __file__.split('/')[-2]
def printLine(*args):
    '''
        prints information on the console screen
    '''
    global name
    print(file_name+': '+'\n      - '+'\n      - '.join([str(arg) for arg in list(args)]))
    
goals = []
def goal_scrapper(goals_file):
    global goal_index,goals
    goal_index = 0
    file = open(goals_file, 'r')
    lines = file.readlines()
    goals = []
    goal = {}
    for line, i in zip(lines, range(len(lines))):
        if line.strip() == '---':
            goals.append(goal)
            goal = {}
        elif line.strip() == 'position:':
            goal['position'] = {
                'x':lines[i+1].strip().split(' ')[1],
                'y':lines[i+2].strip().split(' ')[1],
                'z':lines[i+3].strip().split(' ')[1],
            }
            goal['orientation'] = {
                'x':lines[i+5].strip().split(' ')[1],
                'y':lines[i+6].strip().split(' ')[1],
                'z':lines[i+7].strip().split(' ')[1],
                'w':lines[i+8].strip().split(' ')[1],
            }
    #printLine(*goals)

referance_frame = 'map'
def set_goal(goal_point):
    global referance_frame 
    goal = PoseStamped()
    goal.header.frame_id = referance_frame
    goal.header.stamp = rospy.Time.now()
    goal.pose.position.x = float(goal_point['position']['x'])
    goal.pose.position.y = float(goal_point['position']['y'])
    goal.pose.position.z = float(goal_point['position']['z'])
    goal.pose.orientation.x = float(goal_point['orientation']['x'])
    goal.pose.orientation.y = float(goal_point['orientation']['y'])
    goal.pose.orientation.z = float(goal_point['orientation']['z'])
    goal.pose.orientation.w = float(goal_point['orientation']['w'])
    return goal

# home = os.environ['HOME']
# # os.chdir(home+'/catkin_ws/src/navigation/goals')
# # goal_scrapper()
# def reload_goals():
#     global home
#     os.chdir(home+'/catkin_ws/src/navigation/goals')
#     goal_scrapper()
    
status = 'cancelled'
def result_cb(data):
    print(data.status.text, data.status.status,'status')
    if (data.status.text != 'This goal was canceled because another goal was recieved by the simple action server') and status == 'running' and data.status.text != '':
        pub_goal()
        
move_base_simple_topic = '/move_base_simple/goal'
pub = rospy.Publisher(move_base_simple_topic, PoseStamped,queue_size=10)
goal_index = 1    
def pub_goal():
    global status, goal_index, pub, goals
    if status == 'running':
        pub.publish(set_goal(goals[goal_index]))
        if goal_index == (len(goals) - 1):
            goal_index = 0
        else:
            goal_index +=1

sub = None
move_base_result_topic = '/move_base/result'
def start():
    global move_base_result_topic, sub, goals
    if goals:
        sub = rospy.Subscriber(move_base_result_topic, MoveBaseActionResult, result_cb)
        pub_goal()
        thread = threading.Thread(target=run)
        thread.start()
        return 'running'
    else:
        return 'failed'

timeout =20
rate = rospy.Rate(0.2)
def run():
    global status, rate, timeout
    status = 'running'
    timer = time.time()
    while not rospy.is_shutdown() and status == 'running':
        rate.sleep()
        if time.time() - timer > timeout and status == 'running':
            timer = time.time()
            pub_goal()


def cancel():
    global sub, status
    sub.unregister()
    status = 'cancelled'
    
