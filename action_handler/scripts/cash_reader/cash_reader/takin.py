from scripts.cash_reader.cash_reader.nv9biller import Biller
import time
import rospy
from status_msgs.msg import cash_reader_msg, cash_reader_channel_msg
from std_msgs.msg import String
import threading
import os

######################## logging functionality ########################################################################

file_name = __file__.split('/')[-1][:-3]
if file_name == '__init__' or file_name == '__init__.':
    file_name = __file__.split('/')[-2]
def printLine(*args):
    '''
        prints information on the console screen
    '''
    global name
    print(file_name+': '+'\n      - '+'\n      - '.join([str(arg) for arg in list(args)]))

######################## reaceiving the control signal as a topic########################################################################
def control_cb(msg):
    """
        takes one byte argument and check if it is a valid control command.
    """
    global flag
    int_flag = int(msg.data)
    if int_flag in flag_dict and global_ev not in ['Stacking', 'Rejecting']:
        printLine('cash reader control reaceived ', msg)
        flag = int_flag

######################## publish voucher out message ########################################################################
def voucher_out():
    '''
        requests the dispance of voucher card, with given value
    '''
    global channel_used
    printLine('publishing voucher out')
    file = open(os.environ['HOME'] + '/catkin_ws/src/public/voucher_system/voucher_request.txt','w+')
    file.write(str(channel_used))
    file.close()

######################## reading the state of the cash reader ########################################################################
def threaded_read():
    '''
        continues reading of the cash reader
    '''
    global biller
    printLine('starting threaded reading')
    while not rospy.is_shutdown():
        try:
            while not rospy.is_shutdown():
                time.sleep(rate)
                read()
        except Exception as e:
            printLine('reading error',e)
            while not reinit() and not rospy.is_shutdown():
                    time.sleep(2.5)
            continue
######################## reading the state of the cash reader ########################################################################
def read():
    """
        reads the current state of the cash_reader.
    """
    global biller, msg, pub, flag, global_ev
    counters = biller.counters
    msg.cash_reader_counters.dispensed = counters['dispensed']
    msg.cash_reader_counters.rejected = counters['rejected']
    msg.cash_reader_counters.stacked = counters['stacked']
    msg.cash_reader_counters.transferred = counters['transferred']
    msg.cash_reader_counters.stored = counters['stored']
    msg.events = list([str(event) for event in biller.poll()])
    for ev in msg.events:
        printLine('env', ev)
        global_ev = ev
        if ev == 'Stacked':
            printLine('stacked detected')
            voucher_out()
            flag = 2
    pub.publish(msg)

######################## checking the response of hte cash reader ########################################################################
def check():
    """
        checks if the counters and if the rejected or stacked elements increases it returns the final service response
    """
    printLine('cash reader checking started')
    global flag, msg, fail_counter, biller, t_start, time_out, rate, channel_used
    while not rospy.is_shutdown():
        
        if time.time() - t_start > time_out:
            flag = 1
            return 'timeout'
        elif flag == 1:
            return 'cancelled'
        
        time.sleep(rate)
        
        if msg.cash_reader_counters.rejected >0:
            printLine('returned rejected')
            return 'rejected'
        
        elif msg.cash_reader_counters.stacked >0 or flag == 2:
            printLine('returned stacked')
            return 'stacked'

######################## initiation variables and parameters ########################################################################
printLine('starting cash reader handler')
# port = rospy.get_param('/cash_reader/port_path', '/dev/serial/by-id/usb-FTDI_FT232R_USB_UART_AB0M7YO6-if00-port0')
port ='/dev/serial/by-id/usb-FTDI_FT232R_USB_UART_AB0M7YO6-if00-port0'

queue_size = int(rospy.get_param('/global/queue_size', '10'))
pub = rospy.Publisher('/cash_reader/status',cash_reader_msg, queue_size=queue_size)

time_out = 40
t_start = time.time()
rate = 1/float(rospy.get_param('/cash_reader/rate', str(1/1.2)))
biller = None
global_ev = None
msg = cash_reader_msg()
channels = []
channel_used = None

sub = rospy.Subscriber('/cash_reader/control',String, control_cb )

flag = 0
flag_dict = {
    1: 'stop',
    0: 'continue'
}


######################## initiate the biller and read its availabel channels ########################################################################
def init():
    '''
    initializing the biller from a given serial port, and readig the channels available on the cashreader provieded
    '''
    global biller, port, channels, msg

    while not rospy.is_shutdown():
        try:
            printLine('creating cash readre')
            biller = Biller(port)
            printLine('biller has been created')
            channels = []
            for ch in biller.channels:
                channel_msg = cash_reader_channel_msg()
                channel_msg.channel = ch.channel
                channel_msg.currency = ch.currency
                channel_msg.value = ch.value
                channels.append(channel_msg)
            msg.cash_reader_channel = channels
            printLine(channels)
            t = threading.Thread(target=threaded_read)
            t.start()
            break
        except Exception as e:
            time.sleep(2)
            # printLine('Error while trying to start Cash reader', e)
            continue
######################## try to start the biller on the start of the action server ########################################################################
def reinit():
    '''
        Reinitialize the cash reader and return either success as boolean True or failur as Falses
    '''
    printLine('reinitializing')
    global biller
    try: 
        biller.close()
        biller = Biller(port)
        printLine('biller has been created')
        channels = []
        for ch in biller.channels:
            channel_msg = cash_reader_channel_msg()
            channel_msg.channel = ch.channel
            channel_msg.currency = ch.currency
            channel_msg.value = ch.value
            channels.append(channel_msg)
        msg.cash_reader_channel = channels
        printLine('creation process succees')
        return True
    except Exception as error:
        printLine('reinit exception', error)
        return False
######################## try to start the biller on the start of the action server ########################################################################

t = threading.Thread(target=init)
t.start()
def takein(channel=1):
    '''
    main function, called to handle takin action for the cash reader.
    '''
    printLine('taking in')
    global t_start, time_out, biller, msg, channels, port ,queue_size,\
         pub,rate,flag,flag_dict,sub, channel_used
         
    flag = 0
    t_start = time.time()
    count = 0
    while count <5 :
        try:
            biller.counters_reset()
            biller.channels_set(tuple((int(channel),)))
            channel_used = int(channel)
            biller.counters_reset()
            printLine('starting cash_reader ')
            biller.enable()
            biller.display_enable()
            result = check()
            biller.disable()
            biller.display_disable()
            biller.counters_reset()
            return result
        except Exception as e:
            time.sleep(0.5)
            count += 1  
            printLine('error in cash reader', e)
    printLine('returning failed')
    return 'failed'
