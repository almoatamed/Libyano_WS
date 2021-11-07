#!/usr/bin/env python
import threading 
import rospy
import os
import time
import pygame


file_name = __file__.split('/')[-1][:-3]
if file_name == '__init__' or file_name == '__init__.':
    file_name = __file__.split('/')[-2]
def printLine(*args):
    '''
        prints information on the console screen
    '''
    global name
    print(file_name+': '+'\n      - '+'\n      - '.join([str(arg) for arg in list(args)]))


pygame.mixer.init()
queue = []
isSpeaking = False
def start():
    global isSpeaking
    while not rospy.is_shutdown():
        time.sleep(0.5)
        if len(queue) > 0:
            isSpeaking = True    
            file = queue.pop(0)
            pygame.mixer.music.load(file)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy() and isSpeaking:
                time.sleep(0.1)
            pygame.mixer.music.stop()
            print('Done')
        else:
            time.sleep(0.2)
            isSpeaking = False
        

t = threading.Thread(target=start)
t.start()

def speak(file):
    global queue
    file = os.getenv('HOME')+'/catkin_ws/src/action_handler/scripts/interactive/speaking/sounds/'+file
    printLine(file)
    if not isSpeaking:
        queue.append(file)
        return "running"
    else:
        return "speaking"


def push_to_queue(file):
    global queue
    file = os.getenv('HOME')+'/catkin_ws/src/action_handler/scripts/interactive/speaking/sounds/'+file
    printLine(file)
    queue.append(file)
    return "running"

def set_stop():
    global isSpeaking
    isSpeaking = False
    return 'Done'

def generate(phrase, lang,name):
    printLine('generating sound', phrase, name)
    os.chdir( os.getenv('HOME') + '/catkin_ws/src/action_handler/scripts/interactive/speaking/generaters')
    os.system('/usr/bin/python3 generate_'+lang+'.py "' + phrase + '"' + ' "' + name + '"' )

home = os.environ['HOME']
sounds_path = home + '/catkin_ws/src/action_handler/scripts/interactive/speaking/sounds/'
def save_sound(phrase,lang,name):
    printLine('saving sound', phrase)
    try:
        generate(phrase,lang,name)
        file = open(sounds_path+name+'_content.txt','w+')
        file.write(phrase)
        file.close()
        return 'done'
    except Exception as e:
        printLine('error while saving sound',e)
        return 'failed'


def play_temp(lang,phrase):
    save_sound(phrase,lang,'temp')   
    file = os.getenv('HOME')+'/catkin_ws/src/action_handler/scripts/interactive/speaking/sounds/temp.mp3'
    queue.append(file)
    return "running"
    