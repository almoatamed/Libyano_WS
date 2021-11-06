import os
import subprocess

x = subprocess.check_output('sudo lshw'.split(' ')).decode().split('\n')
p = []
for i,index in zip(x,range(len(x))):
    if 'product' in i:
        p.append(i.split(':'))

system_type = p[0][1].split(' ')[1][0]
if system_type == 'N':
    system_type = 'J'
if system_type not in ['R', 'J']:
    system_type = 'G'
    
home = os.environ['HOME']

os.chdir(home+'/catkin_ws/src/networking/scripts/')
if system_type in ['G','R']:
    print('installing Raspian Networking')
    os.system('python3 '+home+'/catkin_ws/src/networking/scripts/R/access_point_installation.py')
elif system_type == 'J':
    print('installing Jetson Networking')
    os.system('python3 '+home+'/catkin_ws/src/networking/scripts/J/installation.py')
    