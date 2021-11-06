import threading
import rospy
import time
from std_msgs.msg import String
from action_handler_msgs.srv import action_srv

from scripts.startup.stages import power_stage
from scripts.startup.stages import sync
from scripts.startup.stages import choice_stage
from scripts.startup.stages import slam
stages = {
    'slam':slam,
    'power_stage':power_stage,
    'chose_existing_map':sync,
    'choices_stage':choice_stage
    }
current_stage = None



file_name = __file__.split('/')[-1][:-3]
if file_name == '__init__' or file_name == '__init__.':
    file_name = __file__.split('/')[-2]
def printLine(*args):
    '''
        prints information on the console screen
    '''
    global name
    print(file_name+': '+'\n      - '+'\n      - '.join([str(arg) for arg in list(args)]))
    
def threaded_check():
    global stages, current_stage
    current_stage  = 'power_stage'
    printLine('Beginning Threaded Check')
    while not rospy.is_shutdown() and current_stage:
        printLine('starting stage', current_stage)
        stages[current_stage].run()
        time.sleep(1)
        while not rospy.is_shutdown() and stages[current_stage].is_running():
            time.sleep(1)
        current_stage = stages[current_stage].get_next_stage()
        if current_stage == 'end' or not current_stage:
            break
    end()


def begin():
    global current_stage, mode
    printLine('begenning the startup stages with ',current_stage)
    if not current_stage:
        thread = threading.Thread(target=threaded_check)
        thread.start()
        return 'Began'        

def remote_interface():
    if not current_stage:
        return 'str_not_running'
    #printLine('Attempting to get the remote interface on from the current stage ', current_stage)
    try:
        return stages[current_stage].get_remote_interface()
    except:
        return 'failed'

def main_interface():
    if not current_stage:
        return 'str_not_running'
    #printLine('Attempting to get the remote interface on from the current stage ', current_stage)
    try:
        return stages[current_stage].get_main_interface()
    except:
        return 'failed'

def perform(stage, method, *args):
    global current_stage, stages
    printLine('performing Method on the current stage', 'current stage: '+current_stage, 'required stage: '+stage, 'method: '+method, 'Arguments: '+ str(args))
    if stage == current_stage:
        try:
            if args:
                return stages[current_stage].obj[method](*args)
            else:
                return stages[current_stage].obj[method]()
        except Exception as err:
            printLine('Error while performing method', err)
            return 'failed'
    else:
        return 'umatching_stages'

def get_performables():
    global current_stage
    if not current_stage:
        return 'not_running'
    try:
        return '|'.join(stages[current_stage].obj.keys())
    except Exception as e:
        printLine('Error while getting performables on stage', current_stage, 'with error',e)
        return 'failed'

def get_current_stage():
    #printLine('Attempting to get the current stage', current_stage)
    return current_stage

def get_manual_controls():
    global stages, current_stage
    try:
        return stages[current_stage].get_manual_controls()
    except Exception as e:
        printLine('no manual controls at this stage' , e)
        return "cmd_vel|arrow_goal|point_goal"

def asq(action):
    action_service_name = rospy.get_param('/action/action_service_name','/action')
    # rospy.wait_for_service(action_service_name)
    try: 
        take_action = rospy.ServiceProxy(action_service_name,action_srv)
        resp = take_action(action)
        return resp.result
    except rospy.ServiceException as e:
        printLine('An error occured while trying to take an action ', e)
        return "failed"

def end():
    printLine('ending the startup staging process')
    global current_stage
    current_stage = None
    asq('global_actions/switch_mode/strcancel')
    return 'done'
    
def init_run():
    mode = asq('global_actions/get_current_mode')
    if mode == 'str':
        begin()
        
def init():
    thread = threading.Thread(target=init_run)
    thread.start()

init()