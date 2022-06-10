import math
from math import sin, cos, sqrt, atan2, radians, pi
import pandas as pd
import csv
from math import pow
import numpy as np
import matplotlib.pyplot as plot
import matplotlib.pyplot as plt

call_data = pd.read_csv(r'C:\Users\koray\Dropbox\Koray GÜNAL\PC\Desktop\BEACON-DISTANCE/raspi1.csv').values.flatten()
call_data = np.flip(call_data)
i = np.arange(0, call_data.size, 1)
dist_arr_1  = np.genfromtxt(r'C:\Users\koray\Dropbox\Koray GÜNAL\PC\Desktop\BEACON-DISTANCE/raspi1.csv',delimiter='/n')
dist_arr_2 = np.genfromtxt(r'C:\Users\koray\Dropbox\Koray GÜNAL\PC\Desktop\BEACON-DISTANCE/raspi2.csv',delimiter='/n')
dist_arr_3 = np.genfromtxt(r'C:\Users\koray\Dropbox\Koray GÜNAL\PC\Desktop\BEACON-DISTANCE/raspi3.csv',delimiter='/n')

mean_1=np.nanmean(dist_arr_1)
mean_2=np.nanmean(dist_arr_2)
mean_3=np.nanmean(dist_arr_3)

print("distance of tag from reference point 1=",mean_1)
print("distance of tag from reference point 2=",mean_2)
print("distance of tag from reference point 3=",mean_3)

fig = plot.figure()
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)

ax1.plot(dist_arr_1)
ax1.axhline(y=mean_1, color='g', linestyle='-')

ax2.plot(dist_arr_2)
ax2.axhline(y=mean_2, color='g', linestyle='-')


ax3.plot(dist_arr_3)
ax3.axhline(y=mean_3, color='g', linestyle='-')

plot.show()
beaconx=list()
beacony=list()
r1=mean_1
r2=mean_2
r3=mean_3

def trilateration(x1,y1,r1,x2,y2,r2,x3,y3,r3):
    A = 2 * x2 - 2 * x1
    B = 2 * y2 - 2 * y1
    C = r1 ** 2 - r2 ** 2 - x1 ** 2 + x2 ** 2 - y1 ** 2 + y2 ** 2
    D = 2 * x3 - 2 * x2
    E = 2 * y3 - 2 * y2
    F = r2 ** 2 - r3 ** 2 - x2 ** 2 + x3 ** 2 - y2 ** 2 + y3 ** 2
    x = (C * E - F * B) / (E * A - B * D)
    y = (C * D - A * F) / (B * D - A * E)
    return x, y

x,y = trilateration(0,4,mean_1,4,0,mean_2,0,10,mean_3)

beaconx.append(x)
beacony.append(y)
print("beaconx={}".format(beaconx))
print("beacony={}".format(beacony))
print(mean_1,mean_2,mean_3)


def calculateDistance(x1,y1,x2,y2):
     dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
     return dist
print("distance between calculated and setup coordinates=", calculateDistance(1.5, 0, x, y) )

print("calculated cordinates of tag (x,y)=",x,y)

if x>0 and x<3.6 and y>5.16 and y<10:
    print("---------------1. Otopark alanı dolu------------------")
elif x<3.6 and x>6.6 and y>5.16 and y>10:
    print("2. Otopark alanı dolu")
elif x>6.9 and x<10 and y>5.16 and y<10:
    print("3. Otopark alanı dolu")
elif x>0 and x<3.6 and y<4.96 and y>0:
    print("4. Otopark alanı dolu")
elif x<3.6 and x>6.6 and y<4.96 and y>0:
    print("5. Otopark alanı dolu")
elif x>6.9 and x<10 and y<4.96 and y>0:
    print("6. Otopark alanı dolu")
else:
    print("Otopark alanı boş")

img = plt.imread(r'C:\Users\koray\Dropbox\Koray GÜNAL\PC\Desktop\BEACON-DISTANCE/tez.jpg')
fig, ax = plt.subplots()
x=range(15)
ax.imshow(img,extent=[-0.2,10.2,-0.2,10.2])

piCordinetesX=[0,4,0]
piCordinetesY=[4,0,10]
plt.scatter(piCordinetesX, piCordinetesY,c="yellow",
            linewidths=4,
            marker="^",
            edgecolor="red",
            s=400)
beaconCordinatex=[beaconx]
beaconCordinatey=[beacony]

plt.scatter(beaconCordinatex, beaconCordinatey,c="blue",
            linewidths=4,
            marker="o",
            edgecolor="red",
            s=400)

plt.show()
