import threading
import time 
import rospy
from std_msgs.msg import String

view_sets = [
    'main', 'bootup'
]



route = 'slide-show'
def set_current_route_name(route_name):
    global route 
    route = route_name

current_set = 'main'
def change_set(set_name):
    global current_set
    if set_name in view_sets:
        current_set = set_name
        return 'changed'
    else:
        return 'not_found'
    
def change_view_set(set_name):
    global route, current_set
    if current_set == 'main':
        if route == 'slide-show':
            return change_set(set_name)
        else:
            return 'current_set_is_serving'
    else:
        return change_set(set_name)
    
def force_change_view_set(set_name):
    return change_set(set_name)

change_route_holder = ''
def change_route(route_name):
    global change_route_holder
    change_route_holder =  route_name


def get_set():
    global current_set
    return current_set

def _get_set():
    global current_set, change_route_holder
    if change_route_holder:
        ret =  '/'.join([current_set, change_route_holder])
        change_route_holder = ''
        return ret
    return current_set

def get_route():
    global route
    return route

def get_sets():
    global view_sets
    return '|'.join(view_sets)


def get_current_route_name():
    global route
    return route

string_msg = String()
set_slash_route_pub = rospy.Publisher("/interface/set_slash_route", String, queue_size=10)
def set_slash_route_pub_thread_function():
    while not rospy.is_shutdown():
        time.sleep(0.25)
        string_msg.data = current_set + '/' + route
        set_slash_route_pub.publish(string_msg)    
        
set_slash_route_pub_thread = threading.Thread(target=set_slash_route_pub_thread_function)
set_slash_route_pub_thread.start()
