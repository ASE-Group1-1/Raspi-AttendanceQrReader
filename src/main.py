#!/usr/bin/env python
#-*- coding: UTF-8 -*-
'''
Main application
'''

import qrcode
import requests

while (True):
    print "1: Scan qrcode and create attendance"
    print "2: exit"
    select=int(raw_input("Please select: "))
    if select == 1:
        result=qrcode.read().strip()
        print result
        r = requests.post("https://attendancetrackingdesktop.appspot.com/rest/attendance/create", data={'attendance': result})
        print r.status_code, r.reason
        print "DONE"
    elif select == 2:
        print "shutting down the application..."
        break
