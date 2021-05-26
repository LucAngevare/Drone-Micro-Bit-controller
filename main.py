import subprocess
import os
import time
import threading
import shutil
import socket
import sys
import time
import chardet
from datetime import datetime
from serial import Serial

host = ''
port = 9000
locaddr = (host,port)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
tello_address = ('192.168.10.1', 8889)
sock.bind(locaddr)
nextCompassPoll = 0.0 ;
serialDevDir='/dev/serial/by-id'
string = ""
doneMoveFile = False

src = r"/home/pi/Desktop/Drone/micro:bit_hex.hex"
destination = r"/media/pi/MICROBIT/code.hex"

while (not os.path.isdir(serialDevDir)):
    print("replug the micro:bit")
    time.sleep(5)

while (not doneMoveFile):
    if (not os.path.isdir("/media/pi/MICROBIT")):
        print("please replug the micro:bit hh")
        time.sleep(5)
    try:
        shutil.copyfile(src, destination)
        print("done the movement")
        doneMoveFile = True
    except:
        print("Please replug the micro:bit h")
        time.sleep(5)

if ( os.path.isdir(serialDevDir) ):
    serialDevices = os.listdir(serialDevDir)

    if ( len(serialDevices) > 0 ):

        serialDevicePath = os.path.join(serialDevDir, serialDevices[0])
        print(serialDevicePath)

        serial = Serial(port=serialDevicePath, baudrate=19200, timeout=None)

        while( True ):
            try:
                helpme = subprocess.check_output(["iwgetid", "-r"]).strip()
                if (not helpme == b"TELLO-59FB9E"):
                    time.sleep(10)
                    print("not yet connected to wifi")
                else:
                    bytesToRead = serial.inWaiting()
                    receivedMsg = serial.read(bytesToRead)
                    if (receivedMsg):
                        string += "".join(str(receivedMsg.decode(chardet.detect(receivedMsg).get("encoding"))))
                        print(string)
                        print(receivedMsg)
                        if (";" in string):
                            print("received a message")
                            msgType = string.split(": ")[0].strip()
                            msgData = "".join(string.split(": ")[1:])
                            print(msgType)
                            if (msgType.lstrip() == "DRONE"):
                                msg = msgData.split(";")[0].strip()
                                print(msg)
                                sock.sendto(b"command", tello_address)
                                sent = sock.sendto(msg.encode(), tello_address)
                                print("sent message to drone")
                            string = ""
            except:
                print("not yet connected to wifi")
                time.sleep(10)
    else:

        print('No serial devices connected')
