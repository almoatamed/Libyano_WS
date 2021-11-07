import subprocess
import rospy
from std_msgs.msg import String

file_name = __file__.split('/')[-1][:-3]
if file_name == '__init__' or file_name == '__init__.':
    file_name = __file__.split('/')[-2]
def printLine(*args):
    '''
        prints information on the console screen
    '''
    global name
    print(file_name+': '+'\n      - '+'\n      - '.join([str(arg) for arg in list(args)]))
    
pub = rospy.Publisher('/system/controlled_processes', String, queue_size=10)
msg = String()

controlled_processes ={}

def start_controlled_process(command,name):
    #printLine('starting controlled process', name, command)
    try:
        controlled_processes[name] = subprocess.Popen(command.replace('&', '/').split('%'))
        msg.data = '/'.join(controlled_processes.keys())
        pub.publish(msg)
        return 'done'
    except Exception as e:
        #printLine('Exception while starting Controlled process ', e)
        return 'failed'
    
    
def kill_process(name):
    #printLine('killing controlled process ', name)
    try:
        if name not in controlled_processes:
            return 'not_found'
        controlled_processes[name].kill()
        controlled_processes.pop(name)
        msg.data = '/'.join(controlled_processes.keys())
        pub.publish(msg)
        return 'done'
    except Exception as e:
        #printLine('error while killing controlled process', name)
        return 'failed'
    
    