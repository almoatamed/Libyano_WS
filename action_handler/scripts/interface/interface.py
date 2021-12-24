import threading
import time 
import rospy
from std_msgs.msg import String
from action_handler_msgs.srv import action_srv
import os 
import json


##############################################Logging###############################################
file_name = __file__.split('/')[-1][:-3]
if file_name == '__init__' or file_name == '__init__.':
    file_name = __file__.split('/')[-2]
def printLine(*args):
    '''
        prints information on the console screen
    '''
    global name
    print(file_name+': '+'\n      - '+'\n      - '.join([str(arg) for arg in list(args)]))
    
########################################action server proxy#########################################
def asq(action):
    action_service_name = '/action'
    # rospy.wait_for_service(action_service_name)
    try:
        take_action = rospy.ServiceProxy(action_service_name, action_srv)
        resp = take_action(action)
        return resp.result
    except rospy.ServiceException as e:
        printLine('error while taking action', e)
        return 'failed'
    
    

##################################interface configuration actions###################################
acts_names = []
def get_acts_names():
    global acts_names
    acts_names = asq('act/get_acts_names').split('|')


home = os.environ["HOME"]
interface_json_file_path = home + '/catkin_ws/src/action_handler/scripts/interface/interface.json'
interface = {}
def load_interface_config_json():
    global interface, interface_json_file_path
    file = open(interface_json_file_path, 'r')
    interface = json.load(file)
    file.close()
load_interface_config_json()

def update_interface_config_json():
    global interface 
    interface_json_string = json.dumps(interface)
    file = open(interface_json_file_path, 'w+')
    file.write(interface_json_string)
    file.close()
    

def validate_acts():
    global interface 
    get_acts_names()
    if acts_names:
        for route in interface['routes']:
            for act in interface['routes'][route]['mounted_acts']:
                if act not in acts_names:
                    interface['routes'][route]['mounted_acts'] = [valid_act for valid_act in interface['routes'][route]['mounted_acts'] if valid_act != act]
            for act in interface['routes'][route]['destroy_acts']:
                if act not in acts_names:
                    interface['routes'][route]['destroy_acts'] = [valid_act for valid_act in interface['routes'][route]['destroy_acts'] if valid_act != act]
        for special_event in interface['special_events']:
            for act in interface['special_events'][special_event]:
                if act not in acts_names:
                    interface['special_events'][special_event] = [valid_act for valid_act in interface['special_events'][special_event] if valid_act != act]
        update_interface_config_json()

def validate_acts_thread():
    thread = threading.Thread(target=validate_acts)
    thread.start()

validate_acts_thread()


def validate_acts_from_temp(interface):
    get_acts_names()
    try:
        for route in interface['routes']:
            for act in interface['routes'][route]['mounted_acts']:
                if act not in acts_names:
                    interface['routes'][route]['mounted_acts'] = [valid_act for valid_act in interface['routes'][route]['mounted_acts'] if valid_act != act]
            for act in interface['routes'][route]['destroy_acts']:
                if act not in acts_names:
                    interface['routes'][route]['destroy_acts'] = [valid_act for valid_act in interface['routes'][route]['destroy_acts'] if valid_act != act]
        for special_event in interface['special_events']:
            for act in interface['special_events'][special_event]:
                if act not in acts_names:
                    interface['special_events'][special_event] = [valid_act for valid_act in interface['special_events'][special_event] if valid_act != act]
        return interface 
    except Exception as e: 
        printLine('Error occured while validating incoming json for inteface config', e)
        return False

#api
def get_interface_config_json():
    global interface
    validate_acts()
    return json.dumps(interface)

#api
def change_interface_config_json(json_string):
    global interface
    printLine('changing interface config', json_string)
    try:
        interface_temp = json.loads(json_string)
    except json.decoder.JSONDecodeError:
        return 'failed'
    interface_temp = validate_acts_from_temp(interface_temp)
    if interface_temp:
        interface = interface_temp
        update_interface_config_json()
        return 'Done'
    else:
        return 'failed'

#####################################Interface related actions######################################
route = 'slide-show'
def set_current_route_name(route_name):
    global route 
    route = route_name

def _get_set():
    global current_set, change_route_holder
    if change_route_holder:
        printLine('route change request is fetched', change_route_holder)
        ret =  '/'.join([current_set, change_route_holder])
        printLine('route change request is fetched', ret)
        change_route_holder = ''
        return ret
    return current_set

#api (internface_only)
def _get_config():
    return json.dumps({
        "interface": interface, 
        'current_set': _get_set()
    })

##################################### api/server related actions #####################################

current_set = 'main'
def change_set(set_name):
    global current_set
    printLine('changing set to ', set_name)
    if set_name in interface['sets']:
        current_set = set_name
        return 'changed'
    else:
        return 'not_found'

#api
def change_view_set(set_name):
    global route, current_set
    printLine('attempting to changing view set contitionally to ', set_name)
    if current_set == 'main':
        if route == 'slide-show':
            return change_set(set_name)
        else:
            printLine('failed to cange set, serving')
            return 'current_set_is_serving'
    else:
        return change_set(set_name)
    
#api
def force_change_view_set(set_name):
    printLine('forcing to changing view set to ', set_name)
    return change_set(set_name)

#api
change_route_holder = ''
def change_route(route_name):
    global change_route_holder
    printLine('changing route to ', route_name)
    change_route_holder =  route_name
    
#api    
def get_set():
    global current_set
    return current_set

#api
def get_route():
    global route
    return route

#api
def get_sets():
    global view_sets
    return '|'.join(interface['sets'])

#api
def get_current_route_name():
    global route
    return route


#####################################topic set/route publisher######################################
string_msg = String()
set_slash_route_pub = rospy.Publisher("/interface/set_slash_route", String, queue_size=10)
def set_slash_route_pub_thread_function():
    while not rospy.is_shutdown():
        time.sleep(0.25)
        string_msg.data = current_set + '/' + route
        set_slash_route_pub.publish(string_msg)    
        
set_slash_route_pub_thread = threading.Thread(target=set_slash_route_pub_thread_function)
set_slash_route_pub_thread.start()
