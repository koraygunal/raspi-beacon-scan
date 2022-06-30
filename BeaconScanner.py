import math
from math import sin, cos, sqrt, atan2, radians, pi
import pandas as pd
import csv
from math import pow
import numpy as np
import matplotlib.pyplot as plot
import matplotlib.pyplot as plt
import ScanUtility
import bluetooth._bluetooth as bluez
from filterpy.kalman import KalmanFilter
from filterpy.common import Q_discrete_white_noise
import os

import math
import time

os.remove("rss_filter_beacon1.txt")
os.remove("rss_filter_beacon2.txt")
f=open("rss_filter_beacon1.txt","a")
f=open("rss_filter_beacon2.txt","a")

#Set bluetooth device. Default 0.
dev_id = 0
try:
    sock = bluez.hci_open_dev(dev_id)
    print ("\n *** Looking for BLE Beacons ***\n")
    print ("\n *** CTRL-C to Cancel ***\n")
except:
    print ("Error accessing bluetooth")

ScanUtility.hci_enable_le_scan(sock)
#Scans for iBeacons
m_power = -69
distance = 0

liste=list()
n=2
a=-69
dist_arr_1=list()
dist_arr_2=list()
dist_arr_3=[]
rssi_var1=list()
rssi_var2=list()
rssi_var3=[]
x_vals=[]
y_vals=[]

def calc_rss(n,d,a):
   cal_rss= (-10*n*(math.log(d,10)))+a
   print(cal_rss)

def calc_dist(rss,a,n):
    cal_d= pow(10,((rss-a)/(-10*n)))
    return cal_d

def animate(i):
    x_vals.append(next(index))
    y_vals.append(random.randint(0,5))

try:
    while True:
        returnedList = ScanUtility.parse_events(sock, 1)
        for item in returnedList:
            
            print('id:',item['macAddress'],'rssi:',item['rssi'],)
            #print(type(item)) #= dict
            print('XXXXXXXXXXXXXX')
            
            if item['macAddress']=="ac:23:3f:6f:98:28":
            
                rss=(1*item['rssi'])
                distance=calc_dist(item['rssi'],a,n)
            
            
                rssi_var1.append(rss)
                dist_arr_1.append(distance)
                
            #print(dist_arr_1)
                print(distance)
                print(rssi_var1)
            
                f=open("rss_filter_beacon1.txt","a")
            #f.seek(0)
            
            
                f.write(str(rss))
                f.write(str("\n"))
            
                f.close()
            if item['macAddress']=="ac:23:3f:6f:98:27":
            
                rss2=(1*item['rssi'])
                distance=calc_dist(item['rssi'],a,n)
            
            
                rssi_var2.append(rss)
                dist_arr_2.append(distance)
                
            #print(dist_arr_1)
                print(distance)
                print(rssi_var2)
            
                f=open("rss_filter_beacon2.txt","a")
            #f.seek(0)
            
            
                f.write(str(rss2))
                f.write(str("\n"))
            
                f.close()
            
            
            
            
            
                
                
                
            
            
            
except:
    #If items cannot return except block will be active
    #and pass this block
    pass			
