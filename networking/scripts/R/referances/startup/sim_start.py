import sim_commander
import os
import time
os.system('killall ModeManager')

sim_commander.checkStart()
print('started sim minicom successfully')
print('executing AT+CNMP=38')
print(sim_commander.execute('AT+CNMP=38'))

print('executing AT+CSQ')
print(sim_commander.execute('AT+CSQ'))

print('executing AT+CREG?')
print(sim_commander.execute('AT+CREG?'))

print('executing AT+COPS?')
print(sim_commander.execute('AT+COPS?'))

print('executing AT+CPSI?')
print(sim_commander.execute('AT+CPSI?'))

home= '/home/salem'
os.chdir(home+'/simcom_wwan')
os.system('insmod simcom_wwan.ko')
os.system('lsmod')
time.sleep(0.1)
os.system('dmesg')
time.sleep(0.1)
os.system('ip link set wwan0 up')
print(sim_commander.execute('AT$QCRMCALL=1,1'))
os.system('udhcpc -i wwan0')
os.system('ip route add default dev wwan0')
sim_commander.close()
