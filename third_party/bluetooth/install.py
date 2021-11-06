import os 
import time
home = os.environ['HOME']

os.system('apt install bluez -y')
os.system('mkdir /usr/sbin/bluetooth_default_connecter')
os.system('cp '+home+'/catkin_ws/src/third_party/bluetooth/referances/start.py /usr/sbin/bluetooth_default_connecter/start.py')
file = open('/etc/systemd/system/bluetooth_default_connecter.service','w+')
file.write('''[Unit]
Description=bluetooth default connecter
After=network.target bluetooth.target syslog.target

[Service]
ExecStart=/usr/bin/python /usr/sbin/bluetooth_default_connecter/start.py
ExecStop=echo "Done!"

[Install]
WantedBy=multi-user.target
''')
os.system('systemctl daemon-reload')
time.sleep(3)
os.system('systemctl start bluetooth_default_connecter.service')
os.system('systemctl enable bluetooth_default_connecter.service')