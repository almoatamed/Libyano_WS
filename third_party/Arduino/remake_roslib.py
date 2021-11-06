import os

home = os.environ['HOME']
os.chdir(home+'/catkin_ws/src/third_party/Arduino')
os.system('rm -rf ./libraries/ros_lib')
packages = [
    'status_msgs','mcu_msgs'
]
os.system('rosrun rosserial_arduino make_libraries.py ./libraries/ '+ ' '.join(packages))
os.system('cp ./backup/ros_lib/ros.h ./libraries/ros_lib/ros.h')
os.system('cp ./backup/ros_lib/ArduinoHardware.h ./libraries/ros_lib/ArduinoHardware.h')
os.system('cp ./backup/ros_lib/ros/node_handle.h ./libraries/ros_lib/ros/node_handle.h')

