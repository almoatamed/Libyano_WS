import os
import subprocess


home = os.environ['HOME']
os.system('rm -rf ' + home + '/catkin_ws/src/sketches/*')
os.chdir(home+'/catkin_ws/src')        
os.system('python3 third_party/hardware/install_hardware_detection.py')
os.chdir(home+'/catkin_ws/src/global/scripts/')
os.system('python3 system_type_detecter.py')
os.system('source $HOME/.bashrc')

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
    
if system_type == 'R':
    os.system('python3 ' + home+ '/catkin_ws/src/third_party/python/install.py')
    os.system('python3 ' + home+ '/catkin_ws/src/third_party/ros/install.py')
    os.system('python3 ' + home+ '/catkin_ws/src/third_party/hardware/install_sound.py')
    os.system('python3 ' + home+ '/catkin_ws/src/networking/scripts/install.py')
    os.system('echo \"export token=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\" >> $HOME/.bashrc')
    os.system('echo \"10.0.0.13    Libyano_R\" >> /etc/hosts')
    os.system('echo \"10.0.0.1    Libyano_J\" >> /etc/hosts')
    os.system('echo \"export ROS_MASTER_URI=http://Libyano_R:11311\" >> $HOME/.bashrc')
    os.system('echo \"export ROS_HOSTNAME=Libyano_R\" >> $HOME/.bashrc')
    os.system('echo \"export DISPLAY=:0\" >> $HOME/.bashrc')
    os.system('echo \"source $HOME/catkin_ws/devel/setup.bash\" >> $HOME/.bashrc')
elif system_type == 'J':
    os.chdir(home+'/catkin_ws/src')        
    os.system('python3 ' + home+ '/catkin_ws/src/networking/scripts/install.py')
    os.system('python3 ' + home+ '/catkin_ws/src/third_party/python/install.py')
    os.system('python3 ' + home+ '/catkin_ws/src/third_party/ros/install.py')
    os.system('python3 ' + home+ '/catkin_ws/src/third_party/web_server/install.py')
    os.system('python3 ' + home+ '/catkin_ws/src/third_party/web_server/build.py')
    os.system('echo \"export token=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\" >> $HOME/.bashrc')
    os.system('echo \"10.0.0.13    Libyano_R\" >> /etc/hosts')
    os.system('echo \"10.0.0.1    Libyano_J\" >> /etc/hosts')
    os.system('echo \"export ROS_MASTER_URI=http://Libyano_R:11311\" >> $HOME/.bashrc')
    os.system('echo \"export ROS_HOSTNAME=Libyano_J\" >> $HOME/.bashrc')
    os.system('echo \"export DISPLAY=:0\" >> $HOME/.bashrc')
    os.system('echo \"source $HOME/catkin_ws/devel/setup.bash\" >> $HOME/.bashrc')
    

