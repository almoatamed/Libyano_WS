import os
import time
home = os.environ['HOME']


os.system('systemctl daemon-reload')
os.system('systemctl disable --now ifupdown dhcpcd dhcpcd5 isc-dhcp-client isc-dhcp-common rsyslog')
os.system('apt --autoremove purge ifupdown dhcpcd dhcpcd5 isc-dhcp-client isc-dhcp-common rsyslog')
os.system('rm -r /etc/network /etc/dhcp')
os.system('systemctl disable --now avahi-daemon libnss-mdns')
os.system('apt --autoremove purge avahi-daemon')
os.system('apt install libnss-resolve -y')
os.system('ln -sf /run/systemd/resolve/stub-resolv.conf /etc/resolv.conf')
os.system('apt-mark hold avahi-daemon dhcpcd dhcpcd5 ifupdown isc-dhcp-client isc-dhcp-common libnss-mdns openresolv raspberrypi-net-mods rsyslog')
os.system('systemctl enable systemd-networkd.service systemd-resolved.service')

file = open('/etc/systemd/network/02_eth_connection.network','w+')
file.write('''[Match]
# You can also use wildcards. Maybe you want enable dhcp
# an all eth* NICs
Name=eth0
[Network]
#DHCP=v4
# static IP
# 192.168.100.2 netmask 255.255.255.0
Address=10.0.0.1
Gateway=10.0.0.13
DNS=8.8.8.8 8.8.4.4 10.0.0.13 192.168.1.1 172.16.1.254
''')
file.close()
os.system('systemctl daemon-reload')
time.sleep(3)
os.system('systemctl enable systemd-networkd.service')
time.sleep(3)
os.system('systemctl start systemd-networkd.service')
time.sleep(3)
os.system('systemctl restart systemd-networkd.service')
time.sleep(3)
os.system('systemctl start system-resolved')
time.sleep(3)
os.system('systemctl restart system-resolved')
time.sleep(3)


os.system('echo \"10.0.0.3    Libyano_R\" >> /etc/hosts') #-- 
os.system('echo \"10.0.0.1    Libyano_J\" >> /etc/hosts') #-- 
os.system('echo \"export ROS_MASTER_URI=http://Libyano_R:11311\" >> $HOME/.bashrc') #-- 
os.system('echo \"export ROS_HOSTNAME=Libyano_J\" >> $HOME/.bashrc') #-- 
os.system('echo \"export DISPLAY=:0\" >> $HOME/.bashrc') #-- - 
os.system('echo \"source $HOME/catkin_ws/devel/setup.bash\" >> $HOME/.bashrc') #-- 
