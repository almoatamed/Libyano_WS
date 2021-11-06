import os

home = os.environ['HOME']

os.chdir(home)
try:
    os.mkdir('Arduino')
except OSError:
    pass
os.chdir(home +'/Arduino')
os.system('rm -rf libraries')
os.system('ln -s $HOME/catkin_ws/src/third_party/Arduino/libraries')
os.chdir(home+'/catkin_ws/src/third_party/Arduino')
os.system('gunzip < $HOME/catkin_ws/src/third_party/Arduino/arduino-cli_0.19.3_Linux_ARM64.tar.gz | tar xvf -')
os.system('chmod +x  $HOME/catkin_ws/src/third_party/Arduino/arduino-cli ')
os.system('./arduino-cli core install arduino:sam')
os.system('echo "alias arduino-cli=$HOME/catkin_ws/src/third_party/Arduino/arduino-cli" >> $HOME/.bashrc')
os.system('python ./modify_ros_serial.py')