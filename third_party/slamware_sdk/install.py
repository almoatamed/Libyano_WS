import os
home = os.environ["HOME"]
os.chdir(home+'/catkin_ws/src')
os.system('rm -rf ../slamware_sdk ../slamware_ros_sdk')
os.system('mv $HOME/catkin_ws/src/slamware_sdk $HOME/catkin_ws')
os.system('mv $HOME/catkin_ws/src/slamware_ros_sdk $HOME/catkin_ws')
os.chdir(home+'/catkin_ws/src/third_party/slamware_sdk')
os.system('gunzip < $HOME/catkin_ws/src/third_party/slamware_sdk/slamware_ros_sdk_linux-aarch64-gcc7.tar.gz | tar xvf -')
os.system('mv $HOME/catkin_ws/src/third_party/slamware_sdk/slamware_ros_sdk_linux-aarch64-gcc7/src/slamware_sdk $HOME/catkin_ws/src/.')
os.system('mv $HOME/catkin_ws/src/third_party/slamware_sdk/slamware_ros_sdk_linux-aarch64-gcc7/src/slamware_ros_sdk $HOME/catkin_ws/src/.')
os.system('mv $HOME/catkin_ws/src/slamware_sdk/lib/linux-aarch64 $HOME/catkin_ws/src/slamware_sdk/lib/linux-x86_64')
os.system('cp $HOME/catkin_ws/src/third_party/slamware_sdk/src/server/slamware_ros_sdk_server.cpp $HOME/catkin_ws/src/slamware_ros_sdk/src/server/slamware_ros_sdk_server.cpp')
os.system('cp $HOME/catkin_ws/src/third_party/slamware_sdk/src/server/slamware_ros_sdk_server.h $HOME/catkin_ws/src/slamware_ros_sdk/src/server/slamware_ros_sdk_server.h')
