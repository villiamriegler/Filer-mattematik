import matplotlib.pyplot as plt
import numpy as np
from NumericDerivative import *


y = input('Ange en funktion: ')
f = lambda x: eval(y)

xpoints = np.array([])
ypoints = np.array([])
dfpoints = np.array([])
for x in range(-50,50):
    xpoints = np.append(xpoints,x)
    ypoints = np.append(ypoints,f(x))
    dfpoints = np.append(dfpoints, derivative(f,x)) 




plt.plot(xpoints, ypoints)
plt.plot(xpoints, dfpoints)
plt.grid()
plt.show()
