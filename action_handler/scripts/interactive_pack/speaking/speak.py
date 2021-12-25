#!/usr/bin/env python3
import threading 
import rospy
import os
import time


def playsound(path):
    os.system('mpg123 '+path)


def printLine(*args):
    global name
    print(__file__.split('/')[-1][:-3]+': '+'\n      - '+'\n      - '.join([str(arg) for arg in list(args)]))

isSpeaking = False 
def playfile(file):
    global isSpeaking
    isSpeaking = True
    playsound(file)
    isSpeaking = False

queue = []
def start():
    global isSpeaking
    while not rospy.is_shutdown():
        time.sleep(0.5)
        if len(queue) > 0:
            isSpeaking = True    
            file = queue.pop(0)
            playfile(file)
        else:
            isSpeaking = False
        

t = threading.Thread(target=start)
t.start()
def speak(file):
    global queue
    file = os.getenv('HOME')+'/catkin_ws/src/action_handler/scripts/interactive/speaking/sounds/'+file
    #printLine(file)
    if not isSpeaking:
        queue.append(file)
        return "running"
    else:
        return "speaking"


def push_to_queue(file):
    global queue
    file = os.getenv('HOME')+'/catkin_ws/src/action_handler/scripts/interactive/speaking/sounds/'+file
    #printLine(file)
    queue.append(file)
    return "running"


