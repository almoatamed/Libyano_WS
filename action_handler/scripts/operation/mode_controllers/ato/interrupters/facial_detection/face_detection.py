from __future__ import print_function

import threading 
import time

import rospy 
from  action_handler_msgs.srv import action_srv
from std_msgs.msg import String

import jetson.inference
import jetson.utils

import argparse
import sys



file_name = __file__.split('/')[-1][:-3]
if file_name == '__init__' or file_name == '__init__.':
    file_name = __file__.split('/')[-2]
def printLine(*args):
    '''
        prints information on the console screen
    '''
    global name
    print(file_name+': '+'\n      - '+'\n      - '.join([str(arg) for arg in list(args)]))



def asq(action):
    action_service_name = '/action'
    rospy.wait_for_service(action_service_name)
    try:
        take_action = rospy.ServiceProxy(action_service_name, action_srv)
        resp = take_action(action)
        return resp.result
    except rospy.ServiceException as e:
        #printLine('error while taking action', e)
        return 'failed'


parent = {
    'status': 'halt'
}
def init(obj):
    global parent 
    #printLine('initializing parent on facial detection interrupter')
    parent = obj


    
running  = False
def start():
    global running 
    if not running: 
        running = True
        thread = threading.Thread(target = run)
        thread.start()

def validate_interrupt():
    return True

request = {
    'interrupter': 'facial_detection',
    'handler': 'serve', 
    'args':{
    }
}

parser = argparse.ArgumentParser(description="Classify a live camera stream using an image recognition DNN.")

parser.add_argument("input_URI", type=str, default="", nargs='?', help="URI of the input stream")
parser.add_argument("output_URI", type=str, default="", nargs='?', help="URI of the output stream")
parser.add_argument("--network", type=str, default="googlenet", help="pre-trained model to load (see below for options)")
parser.add_argument("--camera", type=str, default="0", help="index of the MIPI CSI camera to use (e.g. CSI camera 0)\nor for VL42 cameras, the /dev/video device to use.\nby default, MIPI CSI camera 0 will be used.")
parser.add_argument("--width", type=int, default=1280, help="desired width of camera stream (default is 1280 pixels)")
parser.add_argument("--height", type=int, default=720, help="desired height of camera stream (default is 720 pixels)")
parser.add_argument('--headless', action='store_true', default=(), help="run without display")

# is_headless = ["--headless"] if sys.argv[0].find('console.py') != -1 else [""]
argv = ['', '--input-width=640', '--input-height=480', '/dev/video0', 'rtp://192.168.31.51:1234', '--headless']

try:
	opt = parser.parse_known_args(args =argv[1:])
	#printLine('parsed options', opt)
	opt = opt[0]
	#printLine(sys.argv)
except:
	#printLine("Error on parsing args on the facial detection interrupter")
	parser.print_help()
	sys.exit(0)

output_frames = False


print('starting loading models'.center(80,'#'))
input_vid = jetson.utils.videoSource(opt.input_URI, argv=argv)
output_vid = None
if output_frames:
	output_vid = jetson.utils.videoOutput(opt.output_URI, argv=argv)


object_net = jetson.inference.detectNet("ssd-mobilenet-v2", threshold=0.5)
face_net = jetson.inference.detectNet("facenet", threshold=0.5)
print('finished loading models'.center(80,'#'))

def interrupt():
    #printLine('interrupting based on valid facial detection')
    parent['interrupt_request'](request)
    
valid_detect_count = 0
interrupt_detect_count = 1
def run():
    global parent, running, valid_detect_count, interrupt_detect_count
    while not rospy.is_shutdown() and running:
        try:
            if  parent['status'] == 'halt' or not parent['interrupt_config']['facial_detection']['enabled']:
                time.sleep(5)
            else:
                time.sleep(0.25)
                img = input_vid.Capture()
                detections = object_net.Detect(img,overlay='none')
                valid_person = None
                for detection in detections:
                    if detection.ClassID == 1 and detection.Width > 500:
                        if not valid_person:
                            valid_person = detection
                        else: 
                            if detection.Width > valid_person.Width: 
                                valid_person = detection
                if not valid_person:
                    valid_detect_count = 0
                else: 
                    faces = face_net.Detect(img,overlay='none')
                    if faces:
                        valid_detect_count+=1
                        if valid_detect_count >= interrupt_detect_count:
                            valid_detect_count = 0
                            interrupt()
                    else: 
                        valid_detect_count = 0
                if output_vid:
                    output_vid.Render(img)
        except KeyError:
            time.sleep(1)
            #printLine('key error on facial detection')


def stop():
    global running
    running = False
    
    