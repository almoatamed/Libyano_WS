import subprocess
import time

time_out = 20
t_start = time.time()

def reset_entwork():
    subprocess.call('ip link set eth0 down'.split(' '))
    subprocess.call('ip link set eth0 up'.split(' '))
    subprocess.call('ip addr add 10.0.0.1/24 dev eth0'.split(' '))
    subprocess.call('ip route del default dev eth0'.split(' '))
    subprocess.call('ip route add default via 10.0.0.13'.split(' '))

def check():
    try: 
        ip = subprocess.check_output('ip -4 addr show eth0').split('\n')[1].strip().split(' ')[1].split('/')[0]
    except subprocess.CalledProcessError:
        ip  = '' 
    if ip != '10.0.0.1':
        reset_entwork()

def run(current_status):
    global t_start
    if time.time() - t_start > time_out:
        t_start = time.time()
        check()