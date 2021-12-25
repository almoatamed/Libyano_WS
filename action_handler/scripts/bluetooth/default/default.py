import os
import threading

file_name = __file__.split('/')[-1][:-3]
if file_name == '__init__' or file_name == '__init__.':
    file_name = __file__.split('/')[-2]
def printLine(*args):
    '''
        prints information on the console screen
    '''
    global name
    print(file_name+': '+'\n      - '+'\n      - '.join([str(arg) for arg in list(args)]))
    
home = os.environ['HOME']
os.chdir(home+'/catkin_ws/src/action_handler/scripts/bluetooth/default')

def clear():
    os.chdir(home+'/catkin_ws/src/action_handler/scripts/bluetooth/default')
    file = open('def','w+')
    file.write('')
    file.close()
    return 'done'

def set(uuid):
    os.chdir(home+'/catkin_ws/src/action_handler/scripts/bluetooth/default')
    file = open('def','w+')
    file.write(uuid)
    file.close()
    return 'done'

def get():
    os.chdir(home+'/catkin_ws/src/action_handler/scripts/bluetooth/default')
    file = open('def','r+')
    dev = file.read().strip()
    file.close()
    if dev:
        return dev
    else:
        return 'empty'
    
    
def run():
    dev = get()
    if dev !='empty':
        home = os.environ['HOME']
        os.system(home+'/catkin_ws/src/action_handler/scripts/bluetooth/connect.sh '+dev)
        return 'done'

def start():
    thread = threading.Thread(target=run)
    thread.start()

start()