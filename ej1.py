from scipy.interpolate import interp1d
import numpy as np
import matplotlib.pyplot as plt
ts = [0.0, 0.22, 0.85, 1.0, 1.5, 1.6, 1.99]
vs = [0.0, 0.1, -0.15, -0.03, 0.75, -0.3, 0.01]
l_p = []
l_p.append(ts[0])

for j in range(len(ts)-1):
    l_p.append((ts[j]+ts[j+1])/2)
    l_p.append(ts[j+1])
f = interp1d(ts,vs, kind='cubic')
plt.plot(ts, vs, 'o', l_p, f(l_p), '-')
plt.legend(['data', 'cubic'], loc='best')
plt.show()

"""
def spline_velocidad(ts, vs):
    #l_p = [] 

    return None

def trapecio_adaptativo(p, v_p):
    return None

def posicion_particula():
    return None
    """