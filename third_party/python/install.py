import os

os.system('sudo apt update')
os.system('sudo apt install python2.7 -y')
os.system('sudo apt install python3.6 -y')
os.system('sudo apt install python-pip -y')
os.system('sudo apt install python2-pip -y')
os.system('sudo apt install python3-pip -y')
os.system('sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 2')
os.system('sudo update-alternatives --install /usr/bin/python python /usr/bin/python2.7 2')
os.system('pip install pyserial')
os.system('pip3 install pyserial')
os.system('pip install playsound')
os.system('pip3 install playsound')
os.system('pip install crcmod')
os.system('pip3 install crcmod')
os.system('pip install requests')
os.system('pip3 install requests')
