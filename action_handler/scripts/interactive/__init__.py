from scripts.interactive.speaking.speak import speak, push_to_queue as speak_push_to_queque, play_temp as speak_play_temp, set_stop as speak_set_stop
from scripts.interactive.speaking.sound_manager import del_sound
from scripts.interactive.speaking.sound_manager import play_saved_file
from scripts.interactive.speaking.sound_manager import play_temp
from scripts.interactive.speaking.sound_manager import sounds_list
from scripts.interactive.speaking.sound_manager import save_sound

from scripts.interactive.head.pixel_grid import set_eyes
from scripts.interactive.head.pixel_grid import set_brightness as set_eyes_brightness

# from scripts.interactive.head.movement import move as move_head, home as move_head_home, relative_move as move_head_relative
from scripts.interactive.head.head_motion import \
                                        add_motion as head_add_motion,  \
                                        clear_motions_queue as head_clear_motion_queue,\
                                        move_head_home as head_move_home,\
                                        push_angled_movement as head_push_angled_movement,\
                                        play_angled_movement as head_play_angled_movement,\
                                        play_motions_by_motion as head_play_motions_by_motion,\
                                        play_motions_by_name as head_play_motions_by_name, \
                                        push_motion_by_name as head_push_motion_by_name,\
                                        push_motions_by_motion as head_push_motions_by_motion,\
                                        relative_move as head_relative_move, \
                                        get_motions_names
                                        
                                        

from scripts.interactive.led.ring import set_brightness as set_ring_brightness, set_flow as set_ring_flow

from scripts.interactive.led.strip import set_color as set_strip_color 
#print('Importing Interactive Actions')


Actions = {
    ############ sound ###################3
    'speak': speak,
    'speak_push_to_queue': speak_push_to_queque,
    'del_sound': del_sound,
    'play_saved_file': play_saved_file,
    'play_temp': play_temp,
    'sounds_list': sounds_list, 
    'save_sound': save_sound,
    'speak_set_stop': speak_set_stop,
    'speak_play_temp': speak_play_temp,
    ########## Eyes ##################
    'set_eyes': set_eyes,
    'set_eyes_brightness':set_eyes_brightness,
    
    ########## HEAD ##################
    'head_add_motion': head_add_motion,  
    'head_clear_motion_queue': head_clear_motion_queue,
    'head_move_home': head_move_home,
    'head_push_angled_movement': head_push_angled_movement,
    'head_play_angled_movement': head_play_angled_movement,
    'head_play_motions_by_motion':head_play_motions_by_motion,
    'head_play_motions_by_name': head_play_motions_by_name, 
    'head_push_motion_by_name': head_push_motion_by_name,
    'head_push_motions_by_motion': head_push_motions_by_motion,
    'head_relative_move': head_relative_move,
    'head_get_motions_names':get_motions_names,
    ########## LED Ring ##################
    'set_ring_flow': set_ring_flow,
    'set_ring_brightness':set_ring_brightness,
    
    ########## LED strip ##################
    'set_strip_color': set_strip_color,
    
    
}