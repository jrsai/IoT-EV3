#! /usr/bin/env python3
import serial
import time
import EV3BT

EV3 = serial.Serial('/dev/rfcomm0')
s = EV3BT.encodeMessage(EV3BT.MessageType.Text, 'Internet of Things', 'IoT A2 Message Sent')
print(EV3BT.printMessage(s))
EV3.write(s)
time.sleep(1)
EV3.close()
