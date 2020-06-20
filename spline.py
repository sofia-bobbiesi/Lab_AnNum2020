from scipy.interpolate import interp1d
import numpy as np
import matplotlib.pyplot as plt

def spline_velocidad(ts, vs):
    prom = []
    if len(ts)>=0:
        prom.append(ts[0])

    for i in range(len(ts)-1):
        prom.append((ts[i]+ts[i+1])/2)
        prom.append(ts[i+1])
    
    spline_cb = interp1d(ts, vs, kind='cubic')
    interp = []
    for j in range(len(prom)):
        interp.append(spline_cb(prom[j]))

    return prom, interp

x = [0.0, 0.22, 0.85, 1.0, 1.5, 1.6, 1.99]
y = [0.0, 0.1, -0.15, -0.03, 0.75, -0.3, 0.01]
xgraph, ygraph = spline_velocidad(x, y)
plt.plot(x, y, 'o', xgraph, ygraph, '-')
plt.legend(['puntos', 'spline cubico'], loc='best')
plt.show()