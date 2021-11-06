import os

home  = os.environ["HOME"]
# os.system('python ' + home + '/catkin_ws/src/third_party/web_server/install.py')

path1 = home + '/catkin_ws/src/third_party/web_server/interface_app_template'
path2 = home + '/catkin_ws/src/third_party/web_server'
interface_path = home+'/catkin_ws/src/interface4'

os.chdir(interface_path)
os.system('npm install')
os.system('npm run build')
os.system('rm -rf ' + path2 + '/interface_app')
os.system('mkdir ' + path2 + '/interface_app')
os.system('cp -R ' + path1 + '/*  ' + path2 + '/interface_app')
os.chdir(path2+'/interface_app')
os.system('npm install')
os.system('cp -R ' + interface_path +'/dist/* ' + path2 + '/interface_app/.'  )

os.chdir(home+'/catkin_ws/src/remote')
os.system('npm install')
os.system('npm run build')

os.chdir(home+'/catkin_ws/src/backend')
os.system('npm install')