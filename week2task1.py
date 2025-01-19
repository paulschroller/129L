import numpy as np
import matplotlib.pyplot as plt
from random import randint

data = np.loadtxt("/root/Desktop/host/mesh.dat", skiprows=1)
#plt.plot(data[:,0], data[:,1], linewidth=0,marker='o')
#plt.xlabel("X")
#plt.ylabel("Y")
#plt.show()

def grahamscan(points):
    startingpoint = points[0]
    startngpointindex = 0
    for i in range(len(points)):
        if startingpoint[1] > points[i][1]:
            startingpoint = points[i]
            startingpointindex = i
        elif startingpoint[1] == points[i][1]:
            if startingpoint[0] > points[i][0]:
                startingpoint = points[i]
                startingpointindex = i
    def sortbyangle(array):
        if len(array) < 2:
            return array
        low, same, high = [], [], []
        pivot = array[randint(0,len(array)-1)]
        pivotangle = (startingpoint[0]-pivot[0])/(((pivot[0]-startingpoint[0])**2+(pivot[1]-startingpoint[1])**2)**0.5)
        for item in array:
            itemangle = (startingpoint[0]-item[0])/(((item[0]-startingpoint[0])**2+(item[1]-startingpoint[1])**2)**0.5)
            if itemangle < pivotangle:
                low.append(item)
            elif itemangle == pivotangle:
                same.append(item)
            elif itemangle > pivotangle:
                high.append(item)
        if len(same) > 1:
            trimmedsame = same[0]
            for item in same:
                if (item[0]-startingpoint[0])**2+(item[1]-startingpoint[1])**2 > (trimmedsame[0]-startingpoint[0])**2+(trimmedsame[1]-startingpoint[1])**2:
                    trimmedsame = item
        return sortbyangle(low) + trimmedsame + sortbyangle(high)