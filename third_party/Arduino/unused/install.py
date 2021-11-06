import platform 
import os

home = os.environ['HOME']

if not os.path.exists(home+'/Arduino/'):
    os.chdir(home+'/Downloads')
    arch = platform.uname()[-1]
    link = ''
    if(arch == 'aarch64'):
        link = 'https://downloads.arduino.cc/arduino-1.8.15-linuxaarch64.tar.xz'
    elif arch == 'x86_64':
        link = 'https://downloads.arduino.cc/arduino-1.8.15-linux64.tar.xz'
    elif arch == 'aarch32':
        link = 'https://downloads.arduino.cc/arduino-1.8.15-linuxarm.tar.xz'

    if link:
        os.mkdir('arduino')
        os.chdir('arduino')
        os.system('wget '+link)
        os.system('tar -xvf '+link.split('/')[-1])
        os.chdir(link.split('/')[-1][:-7])
        os.system('./install.sh')
    else:
        print('no link found')

os.chdir(home +'/Arduino')
os.system('rm -rf libraries')
os.system('ln -s $HOME/catkin_ws/src/third_party/Arduino/libraries')
