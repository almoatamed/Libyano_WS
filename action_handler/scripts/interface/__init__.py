from scripts.interface.interface import set_current_route_name, get_current_route_name, change_view_set, get_set, get_sets, force_change_view_set, get_route, _get_set, change_route, get_interface_config_json,  change_interface_config_json,_get_config


Actions = {
    'set_current_route_name':set_current_route_name,
    '_get_set': _get_set,
    '_get_config': _get_config,

    
    'change_view_set':change_view_set, 
    'force_change_view_set':force_change_view_set, 
    
    'change_route': change_route,
    
    'get_current_route_name': get_current_route_name, 
    'get_route': get_route,
    
    'get_sets': get_sets,
    'get_set': get_set,
    
    'get_interface_config_json':get_interface_config_json,
    'change_interface_config_json':change_interface_config_json,
}
