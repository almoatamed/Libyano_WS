#!/usr/bin/env python

import sys
import os
import subprocess
import rospy
from logger import startLogging, stopLogging
if __name__ == "__main__":
    rospy.init_node('Serial Starter')

    keyword_param = rospy.get_param('Serial_keyword','rduino')

    # startLogging('serial_starter')

    serial_ports = []
    serial_id_paths = '/dev/serial/by-id/'
    for port in os.listdir(serial_id_paths):
        if not os.path.isdir(os.path.join(serial_id_paths, port)) and keyword_param in port:
            serial_ports.append(os.path.join(serial_id_paths,port))
    if not serial_ports :
        print('\nNo Arduino Microcontroller Detected!\n')
    else:
        command = ['rosrun','rosserial_arduino','serial_node.py',serial_ports[0]]
        log_file = open(os.path.join(os.getenv('HOME'),'.log','rosserial-'+keyword_param+'.txt'),'w+')
        p = subprocess.Popen(command,
                            cwd="/",
                            stdout=log_file,
                            stderr=log_file,
                            universal_newlines=True)
    # stopLogging()
    exit()