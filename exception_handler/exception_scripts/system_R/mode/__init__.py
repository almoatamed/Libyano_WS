import subprocess
import time

file_name = __file__.split('/')[-1][:-3]
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

printLine('starting mode exception handler')

def run(current_status):
    global t_start, time_out

    nodes_list = current_status.nodes_list
    # printLine(*nodes_list)
    if '/mode_handler' not in nodes_list and time.time() -t_start > time_out:
        t_start  = time.time()
        printLine('mode Handler is not Running')
        subprocess.Popen(['roslaunch', 'mode_and_status_publishers', 'mode.launch'])