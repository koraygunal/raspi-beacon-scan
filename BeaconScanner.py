#This is a working prototype. DO NOT USE IT IN LIVE PROJECTS

import ScanUtility
import bluetooth._bluetooth as bluez
import math
import time
import math
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
araislem=0
n = 2
try:
	while True:
		returnedList = ScanUtility.parse_events(sock, 10)
		for item in returnedList:
			print(item)

			print('XXXXXXXXXXXXXX')
			liste=list()
			while len(liste)<10:

			araislem = 10**(m_power - (item['rssi'])/(10*n))
			append.araislem(liste)
		toplam=sum(liste)
		uzunluk=len(liste)
		ortalama=toplam/uzunluk
		print(ortalama)
			time.sleep(1)
			
		    

			
           

except:

    pass


