
view_sets = [
    'main', 'bootup'
]

route = ''
def set_current_route_name(route_name):
    global route 
    route = route_name

current_set = 'main'
def change_set(set_name):
    global current_set
    if set_name in view_sets:
        current_set = set_name
        return 'changed'
    else:
        return 'not_found'
    
def change_view_set(set_name):
    global route, current_set
    if current_set == 'main':
        if route == 'slide-show':
            return change_set(set_name)
        else:
            return 'current_set_is_serving'
    else:
        return change_set(set_name)
    
def force_change_view_set(set_name):
    return change_set(set_name)

def get_set():
    global current_set
    return current_set

def get_route():
    global route
    return route

def get_sets():
    global view_sets
    return '|'.join(view_sets)


def get_current_route_name():
    global route
    return route