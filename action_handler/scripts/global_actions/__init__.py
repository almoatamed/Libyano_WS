print('Importing Global Actions')

from scripts.global_actions.mode.mode import change_mode, get_is_running as get_mode_controller_running_state,get_mode,get_premode,start as start_mode_controller,stop as stop_mode_controller, process_csv


Actions = {
    # mode related
    'switch_mode': change_mode,
    'get_current_mode': get_mode,
    'get_previous_mode': get_premode,
    'get_mode_controller_running_state':get_mode_controller_running_state,
    'start_mode_controller': start_mode_controller,
    'stop_mode_controller': stop_mode_controller,
    'process_modes_csv': process_csv
}
