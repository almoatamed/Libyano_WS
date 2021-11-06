import os

home = os.environ['HOME']
os.system('python ' +home + '/catkin_ws/src/third_party/web_server/install_nginx.py')
os.system('python ' +home + '/catkin_ws/src/third_party/web_server/install_mongodb.py')
os.system('python ' +home + '/catkin_ws/src/third_party/web_server/install_npm.py')