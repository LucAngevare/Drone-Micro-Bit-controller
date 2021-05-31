# DJI Tello Micro:Bit controller

Yeah I don't know why I even bothered writing a README.md file for this honestly

## Description

For computer science we were told to just do whatever with a micro:bit, the micro:bit was a damn pain in the backside to work with, for all the same reasons as other things made/owned by Microsoft. The radio channels were totally not configurable, so I was unable to communicate with the drone directly with the micro:bit via WiFi (which theoretically works via 2,4GHz up to 5GHz). The thing had Bluetooth that was only able to communicate with other micro:bits or mobile (you can pair with the thing via laptop but connecting to it is very much a different question) so I couldn't connect with the Bluetooth.

I was left with the only option of connecting my Raspberry Pi to the Micro:Bit with USB so I can have communication via serial. This gave me a ton of issues because for some reason writeline for the micro:bit didn't work and readline for the Serial module on the Raspberry Pi was just slow and cut it on the wrong places. I was forced to make my own delimiter code that waits until a semi-colon is in the input and retrieves only everything before it. This worked well.

After having tested the code and it working really well, for some reason my Raspberry Pi thought it would be an amazingly helpful idea to go ahead and forget it has any WiFi access. It wasn't able to find any network adapters, via `raspi-config` nothing worked, via `nmcli` nothing worked, the GUI didn't allow me to do anything. As of yet I have no idea what it was and it really set me back tons, I have 2 Raspberry Pis but I lent out my 4B because that one generated too much heat to hold and was too big, so I used my 0W. I had a really old Raspberry Pi Model B but that obviously doesn't have any network and is even slower than the 0W.

## Usage

Either use crontab with

```
@reboot sh /home/pi/path/to/installed/directory/startup.sh >/home/pi/logs/cronlog 2>&1
```

to start the Python script on boot, or just run startup.sh or main.py to run the script. Connect to the drone's WiFi (note: this only works with the DJI Tello, thus the repository's name) before or after launching the script and make sure that if you had the micro:bit connected before boot, you need to unplug and replug the micro:bit. If all goes well you should now be able to control the drone with the micro:bit! To make sure they are connected, press any button on the micro:bit or tilt it some, if the drone starts blinking green, they're connected, if it doesn't, something went wrong. The left button on the micro:bit makes it take off and go up, the right button makes it go down, the logo makes it land. Tilting it backward or forward makes the drone go back or forward respectively, tilting it left or right makes the drone rotate left or right.
