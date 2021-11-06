import os
home = os.environ['HOME']

os.chdir(home+'/catkin_ws/src/bootup_loading_interface/app')
os.system('npm start')