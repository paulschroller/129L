import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("/root/Desktop/host/mesh.dat", skiprows=1)
plt.plot(data[:,0], data[:,1], linewidth=0,marker='o')
plt.xlabel("X")
plt.ylabel("Y")
plt.show()