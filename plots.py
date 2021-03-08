import matplotlib.pyplot as plt
import numpy as np


f = input('Ange en funktion: ')
y = lambda x: eval(f)

xpoints = np.array([])
ypoints = np.array([])
for x in range(-500,500):
    xpoints = np.append(xpoints,x)
    ypoints = np.append(ypoints,y(x))




plt.plot(xpoints, ypoints)
plt.grid()
plt.show()