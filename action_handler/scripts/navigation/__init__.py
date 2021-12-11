from scripts.navigation.controller import move, move_by_direction
from scripts.navigation.controller import angled_goal, unangled_goal
from scripts.navigation.controller import stop
from scripts.navigation.controller import go_home
from scripts.navigation.controller import detach, is_detached, toggle_detach
from scripts.navigation.controller import get_maps_names, get_maps, get_current_map
from scripts.navigation.controller import set_map
from scripts.navigation.controller import set_current_pose, set_current_home_pose, update_pose

from scripts.navigation.points_manager.point_manager import add_point, del_point, fetch_points


from scripts.navigation.location_estimater.location_estimater import start as le_start, stop as le_stop, is_running as le_is_running, get_current_pose
from scripts.navigation.goal_monitor.goal_monitor import start as gm_start, cancel as gm_stop, is_running as gm_is_running, get_current_goal_state as gm_last_state
Actions = {
############################# navigation controller  #####################################
    
    ########### Map Related Actions ##############
    'get_maps': get_maps,
    'get_maps_names': get_maps_names,
    'get_current_map': get_current_map,
    
    'set_map': set_map,
    
    'set_pose': set_current_pose,
    'set_home_pose': set_current_home_pose,
    'update_pose':update_pose,
    
    ########### Movement Related Actions ##############
    'stop': stop,
    
    'go_home': go_home,
    
    'detach': detach,
    'toggle_detach': toggle_detach,
    'is_detached': is_detached,
    
    'unangled_goal':unangled_goal,
    'angled_goal': angled_goal, 
    
    'move': move,
    'move_by_direction': move_by_direction,
    
############################# location estimater  #####################################
    'location_estimater_start': le_start,
    'location_estimater_stop': le_stop,
    
    'location_estimater_is_running': le_is_running,
    
    'get_current_pose': get_current_pose,

############################# point_manager  #####################################
    'add_point': add_point, 
    'del_point': del_point,
    'fetch_points': fetch_points,

############################# goal_monitor  #####################################
    'goal_monitor_start': gm_start,
    'goal_monitor_stop': gm_stop,
    
    'goal_monitor_is_running': gm_is_running,
    
    'goal_monitor_get_last_state': gm_last_state,
}
