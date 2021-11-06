import time
import subprocess
import threading 

file_name = __file__.split('/')[-1][:-3]
if file_name == '__init__' or file_name == '__init__.':
    file_name = __file__.split('/')[-2]
def printLine(*args):
    '''
        prints information on the console screen
    '''
    global name
    print(file_name+': '+'\n      - '+'\n      - '.join([str(arg) for arg in list(args)]))
    
scan_data = ''

# def threaded_scanner():
#     global scan_data
#     scan_data = ''
#     data = subprocess.check_output('bluetoothctl scan on'.split(' ')).decode()
#     print(data)
#     scan_data = data
    
    
# def scan():
#     global scan_data
#     thread = threading.Thread(target=threaded_scanner)
#     thread.start()
#     time.sleep(10)
#     subprocess.check_output('pkill bluetoothctl'.split(' '))
#     time.sleep(1)
#     devs = scan_data.split('Device')
#     print(scan_data)
#     print(devs)
#     if len(devs) <2:
#         devs = 'no_scan'
#     else: 
#         devs = devs[1:]
#         devs_result = []
#         for dev in devs:
#             dev = dev.strip().split(' ')
#             dev = '/'.join([dev[0],' '.join(dev[1:])])
#             devs_result.append(dev)    
#         devs = '|'.join(devs_result)
#     return devs


def scan():
    scans = subprocess.check_output(['hcitool', '-i','hci0', 'scan' ]).decode().strip().split('\n')
    if len(scans) > 1:
        devs = []
        for dev in scans[1:]:
            if '\tn' in dev:
                dev = dev[:dev.index('\tn')].strip()
            dev = dev+'/no_name'
            devs.append(dev)
        return '|'.join(devs)
    else:
        return 'no_scan' 
    