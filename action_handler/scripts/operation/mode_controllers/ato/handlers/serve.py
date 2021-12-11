import rospy
import threading
import time 

parent = {}
def init(obj):
    global parent 
    parent = obj
    
current_request = None
running = False
def handle(request):
    global current_request 
    current_request = request
    if not running:
        thread = threading.Thread(target=run)
        thread.start()
        
def run():
    global current_request, running
    parent['pause']('serving')
    running = True
    while not rospy.is_shutdown():
        time.sleep(1)
        if parent['status'] == 'halt':
            break
        elif not (current_request['args']['route'] != 'slide-show' and current_request['args']['set'] == 'main'):
            break
    running = False
    parent['remove_interrupt'](current_request)
    parent['continue']('serving')