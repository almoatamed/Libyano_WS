import os
import subprocess
home = os.environ['HOME']

if not os.path.exists('/opt/ros/melodic/bin/roscore') or os.path.exists('/opt/ros/noetic/bin/roscore'):
    os.chdir(home)
    try:
        code_name = subprocess.check_output(['lsb_release','-dc']).split('\n')[-2].split('\t')[-1]
    except TypeError:
        code_name = subprocess.check_output(['lsb_release','-dc']).decode().split('\n')[-2].split('\t')[-1]
    print('your Ubuntu Distro is ', code_name)
    if  'focal' in code_name:
        os.system("sh -c \'echo \"deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main\" > /etc/apt/sources.list.d/ros-latest.list\'")
        os.system('sudo apt install curl')
        os.system('curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -')
        os.system('sudo apt update')
        os.system('sudo apt install ros-noetic-desktop-full -y')
        os.system('echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc')
        os.system('sudo apt install python3-rosdep python3-rosinstall python3-rosinstall-generator python3-wstool build-essential -y')
        os.system('sudo apt install python3-rosdep -y')
        os.system('sudo rosdep init')
        os.system('rosdep update')
        os.system('apt install ros-noetic-rosbridge-server')
        os.system('apt install ros-noetic-rosserial-arduino')
        os.chdir(home+'/catkin_ws/')
        os.system('rosdep install --from-paths src --ignore-src -r -y')
        os.system('catkin_make -DPYTHON_EXECUTABLE=/usr/bin/python3')
    elif 'bionic' in code_name:
        os.system('sudo sh -c \'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main\" > /etc/apt/sources.list.d/ros-latest.list\'')
        os.system('sudo apt install curl')
        os.system('curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -')
        os.system('sudo apt update')
        os.system('sudo apt install ros-melodic-desktop-full -y')
        os.system('echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc')
        os.system('sudo apt install python-rosdep python-rosinstall python-rosinstall-generator python-wstool build-essential -y')
        os.system('sudo apt install python-rosdep -y')
        os.system('sudo rosdep init')
        os.system('rosdep update')
        os.system('apt install ros-melodic-rosbridge-server')
        os.system('apt install ros-melodic-rosserial-arduino')
        os.chdir(home+'/catkin_ws/')
        os.system('rosdep install --from-paths src --ignore-src -r -y')
        os.system('catkin_make -DPYTHON_EXECUTABLE=/usr/bin/python3')

