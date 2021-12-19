from scripts.interface.interface import set_current_route_name, get_current_route_name, change_view_set, get_set, get_sets, force_change_view_set, get_route, _get_set, change_route


Actions = {
    'set_current_route_name':set_current_route_name,
    '_get_set': _get_set,

    
    'change_view_set':change_view_set, 
    'force_change_view_set':force_change_view_set, 
    
    'change_route': change_route,
    
    'get_current_route_name': get_current_route_name, 
    'get_route': get_route,
    
    'get_sets': get_sets,
    'get_set': get_set,
}
