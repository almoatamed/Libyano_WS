import subprocess
import time
import os

try:
    system_type = os.environ['SYSTEM_TYPE']
    if system_type not in ['J', 'R']:
        raise KeyError
except KeyError:
    system_type = 'G'

print(system_type)

if  system_type == 'J':
    print('pausing to give Raspberry the ahead start')
    time.sleep(20)
while True:
    try:
        out = subprocess.call(str('roslaunch global bringup_'+system_type + '.launch').split(' '))
    except KeyboardInterrupt:
        os.system('killall node')
        exit()
    except subprocess.CalledProcessError:
        os.system('killall node')
        continue
    except Exception as e:
        print('Error while running globa script',e)
        os.system('killall node')
        exit()