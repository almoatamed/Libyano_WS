# import subprocess


# file_name = __file__.split('/')[-1][:-3]
# if file_name == '__init__' or file_name == '__init__.':
#     file_name = __file__.split('/')[-2]
# def printLine(*args):
#     '''
#         prints information on the console screen
#     '''
#     global name
#     print(file_name+': '+'\n      - '+'\n      - '.join([str(arg) for arg in list(args)]))

# def disconnect():
#     try:
#         subprocess.check_output(['bluetoothctl','disconnect'])
#         return 'Done'
#     except subprocess.CalledProcessError:
#         return 'not_connected'
    
    # import subprocess
import os
main_device  = '17:00:26:2B:0F:1D'
def disconnect():
    # try:
    #     subprocess.check_output(['hci','connect',main_device])
    #     return 'Done'
    # except subprocess.CalledProcessError:
    #     return 'failed'
    home = os.environ['HOME']
    os.system(home+'/catkin_ws/src/action_handler/scripts/bluetooth/disconnect.sh')
    
    return 'done'