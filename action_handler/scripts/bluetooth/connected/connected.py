import subprocess
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
    
def connected():
    try:
        devs = subprocess.check_output(['hcitool','con']).decode().strip()
        print(devs)
        devs = devs.split('\n')[1:]
        print(devs)
        if devs:
            id =  devs[0].strip().split(' ')[2]
            name = subprocess.check_output(['hcitool','name',id]).decode().strip()
            return '/'.join([id,name])
        else:
            return 'not_connected'
    except subprocess.CalledProcessError:
        return 'no_connection'  
    
def reset_volume(volume):
    connection  = connected()
    if connection == 'not_connected':
        return 'not_connection'
    id = connection.split('/')[0]
    home = os.environ['HOME']
    print(id)
    os.chdir(home+'/catkin_ws/src/action_handler/scripts/bluetooth/')
    os.system('. '+home+'/catkin_ws/src/action_handler/scripts/bluetooth/connected/pactl_devs.sh')
    # os.system('. /home/libyano/pactl_test.sh')
    sinks_file = open('sinks.txt','r')
    pactl_devs = sinks_file.read().strip().replace('\n', ' ').split(' ')
    sinks_file.close()
    for dev in pactl_devs:
        dev = dev.replace('.monitor','')
        if id.replace(':','_') in dev:
            print('found',dev)
            os.system('pactl set-default-sink '+dev)
            print('pactl set-default-sink '+dev)
            os.system('pactl set-sink-volume '+dev+' ' +volume+'%')
            print('pactl set-sink-volume '+dev+' ' +volume+'%')
            return 'done'
    return 'not_found'