
import serial
import time
import sys


def checkStart():
        global ser 
        ser = serial.Serial("/dev/ttyUSB2",115200)
        ser.flushInput()
        while True:
            ser.write( ('AT\r\n').encode() )
            time.sleep(0.1);
            if ser.inWaiting():
                time.sleep(0.01)
                recBuff = ser.read(ser.inWaiting())
                print( 'try to start\r\n' + recBuff.decode() )
                if 'OK' in recBuff.decode():
                    recBuff = ''
                    return

def execute(command):
    ser.write((command + '\r\n').encode())
    t_start = time.time()
    recBuff = ''
    while time.time() - t_start < 2:
        time.sleep(0.1)
        if ser.inWaiting():
            time.sleep(0.01)
            recBuff = ser.read(ser.inWaiting())
        if recBuff != '':
            return recBuff.decode()
        else:
            return None
        
def close():
    global ser
    if ser != None:
        ser.close()

if __name__ == '__main__':
    try:
        checkStart()
        if len(sys.argv) <2:
            print('command is not provieded')
            exit()
        else:    
            commandInput = sys.argv[1]
            print('executing command ', commandInput)    
            ser.write((commandInput + '\r\n').encode())
            time.sleep(0.1)
            if ser.inWaiting():
                    time.sleep(0.01)
                    recBuff = ser.read(ser.inWaiting())
            if recBuff != '':
                    print(recBuff.decode())
                    recBuff = ''
    except:
        if ser != None:
            ser.close()
