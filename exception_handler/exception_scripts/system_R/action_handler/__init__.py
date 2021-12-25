import subprocess
import time
import os

file_name = __file__.split('/')[-1][:-3]
if file_name == '__init__' or file_name == '__init__.':
    file_name = __file__.split('/')[-2]
def printLine(*args):
    '''
        prints information on the console screen
    '''
    global name
    print(file_name+': '+'\n      - '+'\n      - '.join([str(arg) for arg in list(args)]))
    
try:
    system_type = os.environ['SYSTEM_TYPE']
    if system_type not in ['J', 'R']:
        raise KeyError
except KeyError:
    system_type = 'G'
    
t_start = time.time()
time_out = 21

##printLine('starting action_handler exception handler')

launch_file = {
    'G': 'action_server.launch',
    'R': 'action_server_R.launch'
}

def run(current_status):
    global t_start, time_out

    nodes_list = current_status.nodes_list  
    if '/action_handler_'+system_type not in nodes_list and time.time() -t_start > time_out: 
        t_start  = time.time()
        ##printLine('Action Handler is not Running')
        subprocess.Popen(['roslaunch', 'action_handler', launch_file[system_type]])