import subprocess
import time

file_name = __file__.split('/')[-1].strip()[:-3]
if file_name == '__init__' or file_name == '__init__.':
    file_name = __file__.split('/')[-2]
def printLine(*args):
    '''
        prints information on the console screen
    '''
    global name
    print(file_name+': '+'\n      - '+'\n      - '.join([str(arg) for arg in list(args)]))

t_start = time.time()
time_out = 21

def run(current_status):
    global t_start, time_out

    nodes_list = current_status.nodes_list
        
    if '/serial_starter_movement' not in nodes_list and time.time() - t_start > time_out:
        t_start  = time.time()
        ##printLine('Movement Mcu is not Running')
        subprocess.Popen(['roslaunch', 'serial_starter', 'serial_starter_movement.launch'])