from __future__ import print_function

print('starting story controller')
import json
import rospy 
import threading 
import time
import os
from action_handler_msgs.srv import action_srv
from std_msgs.msg import String


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
    # rospy.wait_for_service(action_service_name)
    try:
        take_action = rospy.ServiceProxy(action_service_name, action_srv)
        resp = take_action(action)
        return resp.result
    except rospy.ServiceException as e:
        printLine('error while taking action', e)
        return 'failed'


parent_obj  = {'status':'halt'}
def init(parent):
    global parent_obj 
    parent_obj = parent
    
home = os.environ["HOME"]
stories_json_path = home + "/catkin_ws/src/action_handler/scripts/operation/mode_controllers/ato/story_controller/stories.json"
stories = {}
#api
def load_stories_json():
    global stories_json_path, stories
    file = open(stories_json_path, 'r')
    stories = json.load(file)
    file.close()
load_stories_json()
def update_stories_json():
    global stories
    stories_json_obj = json.dumps(stories)
    file = open(stories_json_path, 'w+')
    file.write(stories_json_obj)
    file.close()

t_out = 2
t_start = 0
acts_names = []

def modify_and_validate_story(story):
    global t_out, t_start, acts_names
    printLine('validating and modifyging story ', story)
    if time.time() - t_start > t_out :
        printLine('loading acts from act manager')
        t_start = time.time()
        acts_names = asq('act/get_acts_names').split('|')
        if acts_names[0] == '':
            acts_names = []
        printLine('act fetched', acts_names)
    flag = 'valid'
    try:
        if 'acts' not in story:
            printLine('story object does not have act')
            return False
        for act in story['acts']:
            printLine('checking act '+ act )
            if act not in acts_names:
                printLine('act '+ act + ' is not found in acts names')
                story['acts'].pop(act)
                flag = 'modified'
        if len(story['acts']) == 0:
            printLine('story ' + story['name'] + ' has no acts')
            return False
        if 'name' not in story:
            printLine('story has no name')
            return False
        elif story["name"] == "":
            printLine('story name is not valid')
            return False
        elif 'count' not in story:
            printLine('story ' + story['name'] + ' has no valid count')
            return False
        else: 
            try:
                count  = int(story['count'])
                if count < 0 or count > 100:
                    return False
            except ValueError:
                 return False
        if 'end_action' not in story:
            return False
        else:
            if story['end_action'] not in stories['end_actions']:
                return False
        return flag
    except Exception as e:
        printLine('Error while validating story ', e)
        return False

def validate_story_by_name(story_name):
    global stories 
    if story_name not in stories['stories']:
        printLine('story vlidation by name failed, story not found')
        return False
    resp = modify_and_validate_story(stories['stories'][story_name])
    return resp 
        
def validate_all_stories():
    global stories
    if parent_obj['status'] == 'halt':
        printLine('validating all stories')
        load_stories_json()
        printLine('stories', stories)
        story_validation_list = []
        for story in stories['stories']:
            print('story', story)
            resp = validate_story_by_name(story)
            story_validation_list.append({story: resp})
        for validation in story_validation_list:
            if not validation.values()[0]:
                story_name = validation.keys()[0]
                printLine('attempting to remove story ', story_name)
                try:
                    stories['stories'].pop(story_name)
                    if stories['default_story'] == story_name:
                        stories['default_story'] = ''
                except KeyError:
                    printLine('key value error during the removal of story', validation.keys()[0])
                    pass
        update_stories_json()
    printLine('finished validating stories')

printLine('continuing')
#api
def get_stories():
    global stories
    # printLine('getting stories (before validation) ', stories)
    validate_all_stories()
    resp = json.dumps(stories)
    # printLine('getting stories ', resp, stories)
    return resp
#api
def set_default_story(story_name):
    global act_index, story_current_count
    if parent_obj['status'] == 'halt':
        validate_all_stories()
        if story_name in stories['stories']:
            stories['default_story'] = story_name
            act_index = 0
            story_current_count = 0
            try:
                pause_list.remove('story_ended')
            except ValueError:
                pass
            update_stories_json()
            return 'done'
        else:
            'story_not_found'
    else: 
        return 'story_controller_is_running'

def validate_story(story):
    global t_out, t_start, acts_names
    if time.time() - t_start > t_out :
        t_start = time.time()
        acts_names = asq('act/get_acts_names').split('|')
        if acts_names[0] == '':
            acts_names = []
    try:
        if 'acts' not in story:
            printLine('story has no acts')
            return False
        for act in story['acts']:
            if act not in acts_names:
                printLine('act '+act+' not found in valid acts', acts_names)
                return False
        if len(story['acts']) == 0:
            printLine('story has no acts', story['acts'])
            return False
        if 'name' not in story:
            printLine('story has no name property')
            return False
        elif story["name"] == "":
            printLine('story has empty name')
            return False
        if 'count' not in story:
            printLine('story has no count property')
            return False
        else: 
            try:
                count  = int(story['count'])
                if count < 0 or count > 100:
                    printLine('story count is not valid')
                    return False
            except ValueError:
                printLine('story count is not valid number')
                return False
        if 'end_action' not in story:
            printLine('story has no end_action property')
            return False
        elif story['end_action'] not in stories['end_actions']:
            printLine('story end_action is not valid', story['end_action'])
            return False
        return True    
    except Exception as e:
        printLine('Error while validating story ', e)
        return False
#api
def add_story(story_json):
    global stories
    printLine('adding new story', story_json)
    if parent_obj['status'] == 'halt':
        try:
            story = json.loads(story_json)
            printLine('story after being converted to object', story)
            if not validate_story(story):
                return 'failed'
            printLine('story is valid')
            stories['stories'][story['name']] = story
            update_stories_json()
            return 'done'
        except Exception as e:
            printLine('Error while adding new stroy ', e)
            return 'failed'
    else:
        return 'story_controller_is_running'
#api
def del_story(story_name_json):
    global stories
    if parent_obj['status'] == 'halt':
        try:
            story_name = json.loads(story_name_json)['name']
        except ValueError as e:
            printLine('could not load the story name ', e)
            return 'failed'
        if story_name not in stories['stories']:
            return 'not_found'
        try:
            stories['stories'].pop(story_name)
            if stories['default_story'] == story_name:
                stories['default_story'] = ''
            update_stories_json()
            return 'done'
        except Exception as e:
            printLine('Failed to delte story ', 'story name: ' + story_name, e)
            return 'failed'
    else:
        return 'story_controller_is_running'
    
is_running = False
is_running_thread_flag = False

pause_list = []
#api
def pause_story(reason):
    global pause_list
    printLine('attempting to add pausing reason ', reason)
    if reason == '':
        return 'not_valid_reason'
    if reason not in pause_list:
        if len(pause_list) == 0:
            asq('act/clear_queue')
            asq('navigation/stop')
        pause_list.append(reason)
        return 'paused'
    else:
        return 'reason_exists'
#api    
def stop():
    asq('act/clear_queue')
    asq('navigation/stop')
    
#api
def continue_story(reason):
    global pause_list
    printLine('attempting to remove pausing reason ', reason)
    if reason not in pause_list:
        return 'reason_not_found'
    else: 
        pause_list.remove(reason)
        return 'done'
    
pause_list_pub = rospy.Publisher('/story_controller/get_status_json', String, queue_size=2)
string_msg = String()
rate = rospy.Rate(5)
def pause_list_pub_thread():
    while not rospy.is_shutdown():
        rate.sleep()
        string_msg.data = json.dumps({
            'pause_list': pause_list,
            'story_current_count': story_current_count,
            'act_index': act_index,
            'length_of_act_queue': length_of_act_queue,
            'main_status': parent_obj['status'],
            'default_story': stories['default_story'],
            'running_action': running_action
        })
        pause_list_pub.publish(string_msg)
pause_list_thread = threading.Thread(target=pause_list_pub_thread)
pause_list_thread.start()

def push_act(act):
    printLine('pushing act to queue', act)
    asq('act/push_to_queue_by_name/'+act)
    while length_of_act_queue == 0:
        time.sleep(0.01)
    return 

length_of_act_queue = 0
def act_queue_len_cb(length):
    global length_of_act_queue
    length_of_act_queue = int(length.data)
rospy.Subscriber('/act/act_queue_length', String, act_queue_len_cb)

running_action = ''
def running_action_cb(action):
    global running_action
    running_action = action.data
rospy.Subscriber('/act/running_action', String, running_action_cb)


story_current_count = 0
act_index= 0
def run():
    global stories, pause_list, length_of_act_queue, parent_obj, story_current_count, is_running_thread_flag, act_index
    is_running_thread_flag = True
    while not rospy.is_shutdown():
        if parent_obj['status'] == 'halt':
            time.sleep(2)
            continue
        elif stories['default_story'] == '':
            asq('operation/main_switch/mnl')
            printLine('no default story',parent_obj)
            time.sleep(3)
            continue
        elif len(pause_list) == 0 and length_of_act_queue == 0 and running_action == '':
            if act_index == len(stories['stories'][stories['default_story']]['acts']):
                act_index = 0
                story_current_count +=1
                if stories['stories'][stories['default_story']]['count'] > 0:
                    printLine('increasing story count ' + str(story_current_count), 'current default story max cound' + str(stories['stories'][stories['default_story']]['count'])  )
                    if story_current_count >= int(stories['stories'][stories['default_story']]['count']):
                        end_story()
            else:
                printLine('pushing act ')
                push_act(stories['stories'][stories['default_story']]['acts'][act_index])
                act_index +=1
        else: 
            time.sleep(0.2)
    is_running_thread_flag = False
        
def go_home():
    asq('navigation/go_home')

def stay_put():
    pass

end_actions_performers = {
    'stay_put':stay_put,
    'go_home': go_home
}

def end_story():
    printLine('ending story', 'story count' + str(story_current_count), 'act index' + str(act_index))
    pause_story('story_ended')
    end_actions_performers[stories['stories'][stories['default_story']]['end_action']]()

#api    
def restart():
    global act_index, story_current_count, pause_list
    printLine('restarting story')
    asq('act/clear_queue')
    asq('navigation/stop')
    act_index = 0
    story_current_count = 0
    try:
        pause_list.remove('story_ended')
    except ValueError:
        pass
    return 'done'
    
    
    
def start():
    thread = threading.Thread(target=run)
    thread.start()
start()
    