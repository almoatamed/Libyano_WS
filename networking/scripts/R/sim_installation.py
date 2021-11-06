import os
import time

os.system('apt update')
os.system('pip3 install pyserial')
os.system('mkdir -p ~/Documents/SIM7600X_4G_for_JETSON_NANO')
os.system('wget -P ~/Documents/SIM7600X_4G_for_JETSON_NANO/ https://www.waveshare.com/w/upload/6/64/SIM7600X_4G_for_JETSON_NANO.tar.gz')

home = os.environ['HOME']

os.chdir(home+'/Documents/SIM7600X_4G_for_JETSON_NANO/')
os.system('tar -xvf SIM7600X_4G_for_JETSON_NANO.tar.gz')
os.system('sudo groupadd -f -r gpio')
os.system('sudo usermod -a -G gpio your_user_name')
os.system('sudo udevadm control --reload-rules && sudo udevadm trigger')
os.system('sudo apt-get install minicom')
os.system('apt-get install udhcpc')

home= os.environ['HOME']
os.chdir(home)
os.system('wget https://www.waveshare.com/w/upload/4/46/Simcom_wwan.zip')
os.system('unzip Simcom_wwan.zip')
os.chdir(home+'/simcom_wwan')
os.system('make')

os.system('mkdir /usr/sbin/sim_startup')
os.system('cp '+home+'/catkin_ws/src/networking/scripts/R/referances/startup/sim_start.py /usr/sbin/sim_startup/start.py')
os.system('cp '+home+'/catkin_ws/src/networking/scripts/R/referances/startup/sim_commander.py /usr/sbin/sim_startup/sim_commander.py')
file = open('/etc/systemd/system/sim_startup.service', 'w+')
file.write('''[Unit]
Description=SIM Connection control
After=wpa_supplicant@wlan0.service network.target accesspoint@wlan0.service syslog.target

[Service]
ExecStart=/usr/bin/python3 /usr/sbin/sim_startup/start.py
ExecStop=echo "Done!"

[Install]
WantedBy=multi-user.target
''')
file.close()
os.system('systemctl daemon-reload')
time.sleep(3)
os.system('systemctl start sim_startup.service')
time.sleep(3)
os.system('systemctl enable sim_startup.service')