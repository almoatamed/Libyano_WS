import os

home  = os.environ["HOME"]
# os.system('python ' + home + '/catkin_ws/src/third_party/web_server/install.py')

electron_template_path = home + '/catkin_ws/src/third_party/web_server/interface_app_template'
web_server_path = home + '/catkin_ws/src/third_party/web_server'
interface_path = home+'/catkin_ws/src/interface4'

os.chdir(interface_path)
os.system('npm install')
os.system('npm run build')
os.system('rm -rf ' + web_server_path + '/interface_app')
os.system('mkdir ' + web_server_path + '/interface_app')
os.system('cp -R ' + electron_template_path + '/*  ' + web_server_path + '/interface_app')
os.chdir(web_server_path+'/interface_app')
os.system('npm install')
os.system('cp -R ' + interface_path +'/dist/* ' + web_server_path + '/interface_app/.'  )

os.chdir(home+'/catkin_ws/src/remote')
os.system('npm install')
os.system('npm run build')

os.chdir(home+'/catkin_ws/src/backend')
os.system('npm install')