#!/usr/bin/env python
#-*- coding: UTF-8 -*-
'''
Main application
'''

import qrcode
import requests
import pifacecad
import os

def print_instructions():
    print "Switch 0: Scan qrcode and create attendance"
    print "Switch 2: exit"
 
def finish_aplication(event):
    cad.lcd.clear()
    cad.lcd.set_cursor(0, 0)
    cad.lcd.write("Shutting down\n the application...")
    print "shutting down the application..."
    os.kill(os.getppid(),9)

def read_qrcode(event):
    cad.lcd.clear()
    cad.lcd.set_cursor(0, 0)
    result=qrcode.read().strip()
    print result
    r = requests.post("https://attendancetrackingdesktop.appspot.com/rest/attendance/create", data={'attendance': result})
    print r.status_code, r.reason
    print "DONE"
    cad.lcd.write(str(r.status_code))
    cad.lcd.write("\nDONE")
    print_instructions()
  
    
cad = pifacecad.PiFaceCAD()# get an object for the display
cad.lcd.backlight_on() # turns the backlight on
cad.lcd.set_cursor(0, 0)  # set the cursor to the initial position
listener = pifacecad.SwitchEventListener(chip=cad)
listener.register(0, pifacecad.IODIR_FALLING_EDGE, read_qrcode)
listener.register(2, pifacecad.IODIR_FALLING_EDGE, finish_aplication)
listener.activate()

print_instructions()
#    if cad.switches[0].value == 1:
#    elif cad.switches[2].value == 1:

