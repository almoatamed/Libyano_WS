import os

home  = os.environ["HOME"]
interface_path = home+'/catkin_ws/src/bootup_loading_interface'
template_path = home + '/catkin_ws/src/third_party/web_server/interface_app_template'

os.chdir(interface_path)
os.system('npm install')
os.system('npm run build')
os.system('rm -rf ' + interface_path + '/app')
os.system('mkdir ' + interface_path + '/app')
os.system('cp -R ' + template_path + '/*  ' + interface_path + '/app')
os.chdir(interface_path+'/app')
os.system('npm install')
os.system('cp -R ' + interface_path +'/dist/* ' + interface_path + '/app/.'  )
