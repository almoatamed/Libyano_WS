#!/usr/bin/env python
import rospy
import os
import time
from geometry_msgs.msg import PoseStamped
from move_base_msgs.msg import MoveBaseActionResult
from std_msgs.msg import String

print(os.getcwd())
os.chdir(os.getenv("HOME"))
os.chdir('./catkin_ws/src/sim2/goals/')
print(os.getcwd())

def gaol_scrapper(file_name):
    file = open(file_name, mode='r')
    lines = file.readlines()
    goals = []
    goal = {}
    for line,i  in zip(lines,range(len(lines))):
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
            print(goal)
    return goals

def result_cb(data):
    global pub, goals, goal_index, mode, timer
    timeer = time.time()
    print(data.status.text, data.status.status,'status')
    if (data.status.text != 'This goal was canceled because another goal was recieved by the simple action server') and mode == 'nav' and data.status.text != '':
            pub.publish(set_goal(goals[goal_index]))
            if goal_index == (len(goals) - 1):
                goal_index = 0
            else:
                goal_index +=1



def set_goal(goal_point):
    goal = PoseStamped()
    global frame_id 
    goal.header.frame_id = frame_id
    goal.header.stamp = rospy.Time.now()
    goal.pose.position.x = float(goal_point['position']['x'])
    goal.pose.position.y = float(goal_point['position']['y'])
    goal.pose.position.z = float(goal_point['position']['z'])
    goal.pose.orientation.x = float(goal_point['orientation']['x'])
    goal.pose.orientation.y = float(goal_point['orientation']['y'])
    goal.pose.orientation.z = float(goal_point['orientation']['z'])
    goal.pose.orientation.w = float(goal_point['orientation']['w'])
    print('set goal function: goal: ',goal)
    return goal

def mode_cb(data):
    global mode, goal_index, goals, pub
    if mode != 'nav' and data.data=='nav':
        print('continuing')
        pub.publish(set_goal(goals[goal_index]))
        if goal_index == (len(goals) - 1):
            goal_index = 0
        else:
            goal_index +=1
    mode = data.data


if __name__ == "__main__":
    print('creating parameters\n')
    GoaLFile =          'house_goals.txt'
    frame_id =          'map'
    mode =              'nav'
    sleep_period =      1.0
    move_base_simple =  '/move_base_simple/goal'
    node_name =         'auto_move'
    move_base_result =  '/move_base/result'
    mode_topic =        'mode'
    print('creating goals\n')
    goals = gaol_scrapper(GoaLFile)

    print('creating goal index\n')
    goal_index = 1

    print('sleeping\n')
    time.sleep(sleep_period)

    print('creating publisher\n')
    pub = rospy.Publisher(move_base_simple, PoseStamped,queue_size=10)

    print('initiating node\n')
    rospy.init_node(node_name)
    
    time.sleep(sleep_period)
    time.sleep(sleep_period)
    print('publishing the first node \n')
    pub.publish(set_goal(goals[1]))
    print('subscribing to the move_base/resutl topic\n')
    rospy.Subscriber(move_base_result, MoveBaseActionResult, result_cb)
    rospy.Subscriber(mode_topic,String,mode_cb)

    timer = time.time()
    rate = rospy.Rate(0.2)
    while not rospy.is_shutdown():
        rate.sleep()
        if time.time() - timer >20  and mode=='nav':
            timer = time.time()            
            pub.publish(set_goal(goals[goal_index]))
            if goal_index == (len(goals) - 1):
                goal_index = 0
            else:
                goal_index +=1