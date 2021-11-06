#from __future__ import print_function
import os
import time
import subprocess


default_dev = ''


home = '/home/ubuntu'

def log(*args):
    file = open(home+'/log.txt','a+')
    file.write('\n- '.join([str(arg) for arg in list(args)])+'\n')
#    time.sleep(0.1)
    file.close()
os.environ['DISPLAY']=":0"


log('starting to check bluetooth default connecter')

#os.system('pulseaudio -k')
os.system('pulseaudio -k')
time.sleep(2)
os.system("pulseaudio --start")
time.sleep(2)
#os.system('screen -d -m')
while True:
    os.chdir(home+'/catkin_ws/src/action_handler/scripts/bluetooth/default')
    log('attempting to check default')
    file = open('def', 'r')
    dev = file.read()
    file.close()
    if(dev):
        con = subprocess.check_output('hcitool con'.split(' ')).decode().split('\n')
        log('checked connected devices', con)
        if len(con)<3:
            try:
                os.system('pkill pulseaudio')
#                time.sleep(1)
                os.system("pulseaudio -k")
#                time.sleep(2)
#                os.system('runuser -u ubuntu -- pulseaudio --start')
                os.system("pulseaudio --start")
#                time.sleep(2)
                os.system("bluetoothctl disconnect" + dev)
                log('connecting to '+dev)
#                x = subprocess.check_output(['runuser', '-l', 'ubuntu', '-c','"bluetoothctl connect ' +dev + '"'])
                x = "bluetoothctl connect " +dev
#                time.sleep(1)
                os.system(x)
                log(str(x))
#                log('runuser -l ubuntu -c "bluetooth connect ' +dev + '"')
#                subprocess.check_output(['bluetoothctl','connect',dev])
            except Exception as err:
                os.system('pkill pulseaudio')
#                time.sleep(1)
                os.system("pulseaudio -k")
#                time.sleep(2)
#                os.system('runuser -u ubuntu -- pulseaudio --start')
                os.system("pulseaudio --start")
#                time.sleep(2)
                os.system("bluetoothctl disconnect" + dev)
                log(err)
    time.sleep(1)


