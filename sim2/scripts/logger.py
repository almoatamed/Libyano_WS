import sys

logging_dir = '.log'
logging_flag = False

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