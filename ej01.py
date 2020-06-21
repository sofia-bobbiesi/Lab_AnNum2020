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
    
    spline_cb = interp1d(ts,vs, kind='cubic')
    interp = []
    interp = spline_cb(prom)
    return prom, interp


def trapecio_adaptativo(x, y):
    n = len(x)
    a = x[0]
    b = x[n-1]
    if (n == 1):
        h = (b-a)
    else: 
        #Si hay n puntos entonces hay n-1 subintervalos
        h = (b-a)/(n-1)

    y_left = y[:-1]
    y_right = y[1:]
    res = (h/2) * np.sum(y_right+y_left)

    return res

def posicion_particula(ts, vs):
    ppos = []
    for j in range(len(ts)):
        ts_aux = ts[:j+1]
        vs_aux = vs[:j+1]
        ppos.append(trapecio_adaptativo(ts_aux, vs_aux))
    return ppos


x = [0.0, 0.22, 0.85, 1.0, 1.5, 1.6, 1.99]
y = [0.0, 0.1, -0.15, -0.03, 0.75, -0.3, 0.01]
xnew, ynew = spline_velocidad(x,y)
pos = posicion_particula(xnew, ynew)

plt.plot(xnew,pos,'-')
plt.title("Posición de la partícula")
plt.show()