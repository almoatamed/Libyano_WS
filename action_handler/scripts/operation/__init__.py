from scripts.operation.main import get_is_running as main_get_is_running, get_running_mode as main_get_running_mode, get_status as main_get_status, load_modes_config, switch as main_switch
print('improted main operation script')
from scripts.operation.mode_controllers.ato.controller import get_interrupt_queue, change_interrupt_config_json, get_interrupt_config
from scripts.operation.mode_controllers.ato.story_controller.controller import add_story, del_story, pause_story, continue_story, get_stories, load_stories_json, restart, stop, set_default_story

print('all packages has been imported on operation controller   ')

Actions = {
 ####################################### Main ############################################
 'main_get_is_running': main_get_is_running, 
 'main_get_running_mode': main_get_running_mode, 
 'main_get_status': main_get_status, 
 
 'load_modes_config': load_modes_config, 
 
 'main_switch': main_switch, 
 
 #################################### ATO Controller #####################################
 'ato_get_interrupt_queue': get_interrupt_queue,
 'ato_get_interrupt_config': get_interrupt_config,
 'ato_change_interrupt_config': change_interrupt_config_json,
    
 #################################### Story Controller #####################################
'stop': stop, 
'restart': restart, 
'pause': pause_story, 
'continue': continue_story, 

'add_story': add_story, 
'del_story': del_story, 
'set_default_story':set_default_story,
'load_stories_json': load_stories_json, 

'get_stories': get_stories, 


}