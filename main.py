import os 
import time
import threading 
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

if ( os.path.isdir(serialDevDir) ):
    serialDevices = os.listdir(serialDevDir) 

    if ( len(serialDevices) > 0 ):

        serialDevicePath = os.path.join(serialDevDir, serialDevices[0])
        print(serialDevicePath)

        serial = Serial(port=serialDevicePath, baudrate=19200, timeout=None) 

        while( True ):
            bytesToRead = serial.inWaiting()
            receivedMsg = serial.read(bytesToRead)
            if (receivedMsg):
                string += "".join(str(receivedMsg.decode()))
                if (";" in string):
                    print("received a message")
                    msgType = string.split(": ")[0].strip()
                    msgData = "".join(string.split(": ")[1:])
                    print(msgType)
                    if (msgType.lstrip() == "DRONE"):
                        msg = msgData.strip() #Ik ben er klaar mee, dit ga ik als bodge gebruiken, fuck dit
                        print(msg)
                        sock.sendto(b"command", tello_address)
                        sent = sock.sendto(msg.replace(";", "").encode(), tello_address)
                        print("sent message to drone")
                    string = ""
    else:

        print('No serial devices connected') 

else:

    print(serialDevDir + ' does not exist') 
