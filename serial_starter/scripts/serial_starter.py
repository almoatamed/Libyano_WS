#!/usr/bin/env python
import os
import subprocess
import rospy
from rospy.timer import sleep

file_name = __file__.split('/')[-1][:-3]
if file_name == '__init__' or file_name == '__init__.':
    file_name = __file__.split('/')[-2]
def printLine(*args):
    '''
        prints information on the console screen
    '''
    global name
    print(file_name+': '+'\n      - '+'\n      - '.join([str(arg) for arg in list(args)]))
    
if __name__ == "__main__":


    rospy.init_node('serial_mcu_handler')

    ##printLine('starting serial mcu handler')

    ###############################################
    #parameters#
    ###############################################

    keyword_param = rospy.get_param('~keyword_serial','rduino')
    specific_port = rospy.get_param('~specific_port', "no").lower()
    specific_port_name = rospy.get_param('~specific_port_name', '/dev/ttySHT0')
    node_name = rospy.get_param('~node_name')

    
    serial_id_paths = rospy.get_param('/serial/serial_path', '/dev/serial/by-id/')
    publish_rate = rospy.get_param('/serial/serial_starter_rate', '0.5')

    if specific_port == 'no':
        printLine('serial keyword: '+keyword_param)
    else:
        printLine('specific  port named ', specific_port_name)




    ###############################################
    rate = rospy.Rate(float(publish_rate))
    
    while not rospy.is_shutdown():
        rate.sleep()
        serial_ports = []
        if specific_port != 'yes':
            ##printLine('Trying to detect the port automatically')
            try:
                for port in os.listdir(serial_id_paths):
                    if not os.path.isdir(os.path.join(serial_id_paths, port)) and keyword_param in port:
                        serial_ports.append(os.path.join(serial_id_paths,port))
                        ##printLine('suitable serial port found: ', port)
            except OSError:
                pass
                ##printLine('No serials detected!!')
            
        else:
            ##printLine('A specfic port is chosen: ', specific_port_name)
            serial_ports = [specific_port_name]
        
        if not serial_ports :
            printLine('\nNo Microcontrollers Detected!\n')
        else:
            ##printLine('starting connection on port ' + serial_ports[0])
            # command = ['roslaunch','serial_starter','serial_node.launch','name:='+node_name,'port:='+serial_ports[0]]
            command = str('rosrun rosserial_arduino serial_node.py '+serial_ports[0]+' __name:='+node_name).split(' ')
            try:
                p = subprocess.Popen(command,
                                    cwd="/",
                                    universal_newlines=True)
                ##printLine('Serial Controller Started')
                rate = rospy.Rate(2)
                while not rospy.is_shutdown() and not p.poll():
                    rate.sleep()
                try:
                    p.terminate()
                except:
                    pass
                ##printLine('process ended')
            except Exception as e:
                printLine("Error", e)
                pass