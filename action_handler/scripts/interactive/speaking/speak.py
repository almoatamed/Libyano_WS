#!/usr/bin/env python
import threading 
import rospy
import os
import time
# import pygame
from playsound import playsound


file_name = __file__.split('/')[-1][:-3]
if file_name == '__init__' or file_name == '__init__.':
    file_name = __file__.split('/')[-2]
def printLine(*args):
    '''
        prints information on the console screen
    '''
    global name
    print(file_name+': '+'\n      - '+'\n      - '.join([str(arg) for arg in list(args)]))


# pygame.mixer.init()
queue = []
isSpeaking = False
rate = rospy.Rate(2)
def start():
    while not rospy.is_shutdown():
        if len(queue) > 0:
            file = queue.pop(0)
            # pygame.mixer.music.load(file)
            # pygame.mixer.music.play()
            playsound(file)
            # while pygame.mixer.music.get_busy() and isSpeaking:
            #     time.sleep(0.1)
            # pygame.mixer.music.stop()
            print('Done')
        else:
            rate.sleep()
        

t = threading.Thread(target=start)
t.start()

def speak(file):
    global queue
    file = os.getenv('HOME')+'/catkin_ws/src/action_handler/scripts/interactive/speaking/sounds/'+file
    if not isSpeaking:
        queue.append(file)
        return "running"
    else:
        return "speaking"


def push_to_queue(file):
    global queue
    file = os.getenv('HOME')+'/catkin_ws/src/action_handler/scripts/interactive/speaking/sounds/'+file
    queue.append(file)
    return "running"

def set_stop():
    global isSpeaking
    isSpeaking = False
    return 'Done'

def generate(phrase, lang,name):
    os.chdir( os.getenv('HOME') + '/catkin_ws/src/action_handler/scripts/interactive/speaking/generaters')
    os.system('/usr/bin/python3 generate_'+lang+'.py "' + phrase + '"' + ' "' + name + '"' )

home = os.environ['HOME']
sounds_path = home + '/catkin_ws/src/action_handler/scripts/interactive/speaking/sounds/'
def save_sound(phrase,lang,name):
    try:
        generate(phrase,lang,name)
        file = open(sounds_path+name+'_content.txt','w+')
        file.write(phrase)
        file.close()
        return 'done'
    except Exception as e:
        return 'failed'


def play_temp(lang,phrase):
    save_sound(phrase,lang,'temp')   
    file = os.getenv('HOME')+'/catkin_ws/src/action_handler/scripts/interactive/speaking/sounds/temp.mp3'
    queue.append(file)
    return "running"
    