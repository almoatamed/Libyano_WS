import time
import os
import requests as r

old_ssid = ""
current_ssid = ""
password = ""

def reconnect():    
    os.system('/usr/bin/pkill wpa_supplicant')
    os.system('/sbin/ip link set ap@wlan0 down')
    os.system('/sbin/ip link set ap@wlan0 up')
#    os.system('/usr/bin/pkill dhclient')
    os.system('wpa_supplicant -B -iwlan0 -c /etc/wpa_supplicant/wpa_supplicant-wlan0.conf -Dnl80211,wext')
#    os.system('dhclient wlan0')
    print('connecting')



def check():
    global old_ssid, current_ssid, password
    f = open('/etc/wpa_supplicant/wpa_supplicant-wlan0.conf')
    lines = f.readlines()
    for line in lines:
        # line = line.replace("\t","").replace(" ","")
        if "ssid" in line:
            start = line.index('"')+1
            end = start+line[start:].index('"')-1
#            print("indices for ssid", start,end)
#            print("ssid", line[start:end])
            current_ssid = line[start:end]
        elif "psk" in line:
            start = line.index('"')+1
            end = start+line[start:].index('"')-1
            password = line[start: end]
    f.close()

while True:
    time.sleep(15)
    try:
        check()
        if current_ssid != old_ssid and current_ssid !="":
            print('new ssid', current_ssid)
            reconnect()
            old_ssid = current_ssid
            time.sleep(10)
        try:
            r.get('http://google.com')
        except Exception as e:
            print('error while trying to ping', e)
            if current_ssid !="":
                reconnect()
                time.sleep(10)
    except Exception as e:
        print('error', e)
        break

