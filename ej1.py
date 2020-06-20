from scipy.interpolate import interp1d
import numpy as np
import matplotlib.pyplot as plt

#Ejercicio 1a

def spline_velocidad(ts, vs):
    l_p = []
    if len(ts)>=0:
        l_p.append(ts[0])

    for j in range(len(ts)-1):
        l_p.append((ts[j]+ts[j+1])/2)
        l_p.append(ts[j+1])

    spline_c = interp1d(ts,vs, kind ='cubic')
    i_p = []
    for j in range(len(l_p)):
        i_p.append(spline_c(l_p[j]))

    return l_p,i_p
"""
x = [0.0, 0.22, 0.85, 1.0, 1.5, 1.6, 1.99]
y = [0.0, 0.1, -0.15, -0.03, 0.75, -0.3, 0.01]
xgraph, ygraph = spline_velocidad(x, y)
plt.plot(x, y, 'o', xgraph, ygraph, '-')
plt.legend(['puntos', 'spline cubico'], loc='best')
plt.show() """

#Ejercicio 1b

def trapecio_adaptativo(p, v_p):
    return None

def posicion_particula():
    return None
