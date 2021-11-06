import subprocess
import rospy

file_name = __file__.split('/')[-1][:-3]
if file_name == '__init__' or file_name == '__init__.':
    file_name = __file__.split('/')[-2]
def printLine(*args):
    '''
        prints information on the console screen
    '''
    global name
    print(file_name+': '+'\n      - '+'\n      - '.join([str(arg) for arg in list(args)]))
    
def kill_node(node_name):
    nodes = [node for node in subprocess.check_output('rosnode list', shell=True).split('\n') if node]
    if node_name in nodes:
        subprocess.call('ros')
        return 'done'
    else:
        return 'failed'