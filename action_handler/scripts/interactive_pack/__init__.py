from scripts.interactive.speaking.speak import speak, push_to_queue as speak_push_to_queque
from scripts.interactive.speaking.sound_manager import del_sound
from scripts.interactive.speaking.sound_manager import play_saved_file
from scripts.interactive.speaking.sound_manager import play_temp
from scripts.interactive.speaking.sound_manager import sounds_list
from scripts.interactive.speaking.sound_manager import save_sound

from scripts.interactive.head.pixel_grid import set_eyes
from scripts.interactive.head.pixel_grid import set_brightness as set_eyes_brightness
from scripts.interactive.head.movement import move as move_head, home as move_head_home

from scripts.interactive.led.ring import set_brightness as set_ring_brightness, set_flow as set_ring_flow

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
    
    ########## Head ##################
    'set_eyes': set_eyes,
    'set_eyes_brightness':set_eyes_brightness,
    'move_head':move_head,
    'move_head_home': move_head_home,
    
    ########## LED Ring ##################
    'set_ring_flow': set_ring_flow,
    'set_ring_brightness':set_ring_brightness,
}