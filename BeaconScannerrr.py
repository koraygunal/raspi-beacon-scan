#This is a working prototype. DO NOT USE IT IN LIVE PROJECTS

import ScanUtility
import bluetooth._bluetooth as bluez
import math
import time

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
n = 4
try:
	while True:
		returnedList = ScanUtility.parse_events(sock, 10)
		for item in returnedList:
			print(item)
			#print(type(item)) #= dict
			print('XXXXXXXXXXXXXX')
			araislem = 10**(m_power - (item['rssi'])/(10*n))
			#print(araislem)
			#print('araislem(m)',+round(araislem,3))
			print(araislem)
			time.sleep(5)
			#araislem = (m_power - (item['rssi'])/(10*n))
			
			#distance = pow(araislem,10)
			#distance = float(distance)*100
			#print('Distance(m)',+round(distance,3))
			
			
           

except:
    #If items cannot return except block will be active
    #and pass this block
    pass

