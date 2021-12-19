from __future__ import print_function
print('starting mnl script')
is_running = False 
status = 'stopped'
def start():
    global is_running, status
    is_running = True
    status = 'running'
    return 'done'
    
def stop():
    global status, is_running
    is_running = False
    status = 'halt' 
    return True

def get_status():
    global status
    return status
    
obj = {
    "start": start,
    "stop": stop,
    "status": get_status
}
    