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

home = os.environ['HOME']
user = home.split('/')[-1]    
ethname = 'enp2s0'

#printLine('User: ' + user, 'Ethernet Terminal '+ ethname)

os.chdir('/home/' + user + '/catkin_ws/src/networking/scripts/R/')

os.system('cp ./referances/initial/cloud.cfg  /media/' +user+ '/writable/etc/cloud/cloud.cfg')
os.system('cp ./referances/initial/50-cloud-init.yaml  /media/' +user+ '/writable/etc/netplan/50-cloud-init.yaml')

os.system('ip addr add 10.0.0.1/24 dev ' + ethname)
os.system('ssh-keygen -f "/home/salem/.ssh/known_hosts" -R "10.0.0.2"')

