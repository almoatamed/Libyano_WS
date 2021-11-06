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

os.system('apt install hostapd -y')
os.system('apt install unzip -y')    
file = open(r'/etc/hostapd/hostapd.conf','w+')
file.write(
    '''driver=nl80211
ssid=Libyano
country_code=DE
hw_mode=g
channel=1
auth_algs=1
wpa=2
wpa_passphrase=password
wpa_key_mgmt=WPA-PSK
wpa_pairwise=TKIP
rsn_pairwise=CCMP
''')
file.close()
os.system('chmod 600 /etc/hostapd/hostapd.conf')
file = open(r'/etc/systemd/system/accesspoint@.service','w+')
file.write(
    '''[Unit]
Description=accesspoint with hostapd (interface-specific version)
Wants=wpa_supplicant@%i.service

[Service]
ExecStartPre=/sbin/iw dev %i interface add ap@%i type __ap
ExecStart=/usr/sbin/hostapd -i ap@%i /etc/hostapd/hostapd.conf
ExecStopPost=-/sbin/iw dev ap@%i del

[Install]
WantedBy=sys-subsystem-net-devices-%i.device
''')
file.close()
os.system('systemctl daemon-reload')
os.system('systemctl enable accesspoint@wlan0.service')


file = open(r'/etc/wpa_supplicant/wpa_supplicant-wlan0.conf', 'w+')
file.write('''country=DE
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
    ssid="Streamers"
    psk="Join@stream2021"
    key_mgmt=WPA-PSK   # see ref (4)
}
''')
file.close()
os.system('chmod 600 /etc/wpa_supplicant/wpa_supplicant-wlan0.conf')    
os.system('systemctl disable wpa_supplicant.service')

file = open(r'/etc/systemd/system/wpa_supplicant@wlan0.service', 'w+')
file.write('''[Unit]
BindsTo=accesspoint@%i.service
After=accesspoint@%i.service


[Service]
ExecStartPost=/lib/systemd/systemd-networkd-wait-online --interface=%i --timeout=60 --quiet
ExecStartPost=/bin/ip link set ap@%i up
ExecStopPost=-/bin/ip link set ap@%i up
''')
file.close()

file = open(r'/etc/systemd/network/08-wifi.network','w+')
file.write('''[Match]
Name=wl*
[Network]
LLMNR=no
MulticastDNS=yes
# If you need a static ip address, then toggle commenting next four lines (example)
DHCP=yes
#Address=192.168.50.60/24
#Gateway=192.168.50.1
#DNS=84.200.69.80 1.1.1.1
# ''')
file.close()

os.system('echo \'bridge=br0\' >> /etc/hostapd/hostapd.conf')

file = open('/etc/systemd/network/02-br0.netdev', 'w+')
file.write('''[NetDev]
Name=br0
Kind=bridge
''')
file.close()

file = open('/etc/systemd/network/04-eth0.network', 'w+')
file.write('''[Match]
Name=eth0
[Network]
Bridge=br0
''')
file.close()

file = open('/etc/systemd/network/16-br0_up.network', 'w+')
file.write('''[Match]
Name=br0
[Network]
IPMasquerade=yes
Address=10.0.0.13/24
DHCPServer=yes
[DHCPServer]
DNS=84.200.69.80 1.1.1.1
''')
file.close()
os.system('mkdir /usr/sbin/wlan_connection')
os.system('cp '+home+'/catkin_ws/src/networking/scripts/R/referances/maintainer/start.py /usr/sbin/wlan_connection/start.py')
file = open('/etc/systemd/system/wlan_connection.service','w+')
file.write('''[Unit]
Description=Wlan Connection control
After=wpa_supplicant@wlan0.service network.target accesspoint@wlan0.service syslog.target

[Service]
ExecStart=/usr/bin/python3 /usr/sbin/wlan_connection/start.py
ExecStop=echo "Done!"

[Install]
WantedBy=multi-user.target
''')
os.system('systemctl daemon-reload')
time.sleep(3)
os.system('systemctl start wlan_connection.service')
os.system('systemctl enable wlan_connection.service')