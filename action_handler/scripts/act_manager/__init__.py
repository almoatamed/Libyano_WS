from act_manager import get_acts_names
from scripts.act_manager.act_manager import add_act, clear_queue, get_acts, del_act, is_paused, play_new_act_by_act, play_new_act_by_name, push_to_queue_by_act, push_to_queue_by_name, stop, toggle_pause, stop_and_clear, get_acts_names, get_queue_length
Actions = {
    'clear_queue': clear_queue, 
    
    'stop': stop, 
    'stop_and_clear': stop_and_clear, 

    'toggle_pause': toggle_pause,
    'is_paused': is_paused,
    
    'del_act': del_act, 
    'add_act': add_act, 
    
    'get_acts': get_acts,
    'get_acts_names':get_acts_names,
    
    'play_new_act_by_act': play_new_act_by_act,
    'play_new_act_by_name': play_new_act_by_name, 
    
    'push_to_queue_by_act': push_to_queue_by_act,
    'push_to_queue_by_name': push_to_queue_by_name, 
    
    'get_queue_length': get_queue_length
}