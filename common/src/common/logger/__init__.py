import sys
import os

file_name = __file__.split('/')[-1][:-3]
if file_name == '__init__' or file_name == '__init__.':
    file_name = __file__.split('/')[-2]
def printLine(*args):
    '''
        prints information on the console screen
    '''
    global name
    print(file_name+': '+'\n      - '+'\n      - '.join([str(arg) for arg in list(args)]))
    
logging_dir = 'catkin_ws/src/.log'

name = ''

def startLogging(file_name):
    global log_file, old_std, logging_flag
    log_file = open(os.path.join(os.getenv('HOME'),logging_dir,file_name+'.txt'),'w+')
    old_std = sys.stdout
    sys.stdout = log_file
    logging_flag = True

def stopLogging():
    global logging_flag
    if logging_flag:
        log_file.close()
        sys.stdout = old_std

def set_name(script_name):
    global name 
    name = script_name
    

