from scipy.interpolate import interp1d
from scipy.interpolate import CubicSpline
import numpy as np
import matplotlib.pyplot as plt

#Ejercicio 1a
x = [0.0, 0.22, 0.85, 1.0, 1.5, 1.6, 1.99]
y = [0.0, 0.1, -0.15, -0.03, 0.75, -0.3, 0.01]

def spline_velocidad(ts, vs):
    l_p = []
    if len(ts)>=0:
        l_p.append(ts[0])

    for j in range(len(ts)-1):
        l_p.append((ts[j]+ts[j+1])/2)
        l_p.append(ts[j+1])

    spline_c = CubicSpline(ts,vs, extrapolate=True)
    i_p = []
    i_p = spline_c(l_p)

    return l_p,i_p

"""
plt.plot(x, y, 'o', xgraph, ygraph, '-')
plt.legend(['puntos', 'spline cubico'], loc='best')
plt.show() """

#Ejercicio 1b

def trapecio_adaptativo(p, pv):
    n = len(p)
    a = p[0]
    b = p[n-1]
    if(n == 1): h = (b-a)
    else: h = (b-a)/(n-1)

    pv_r = pv[1:] # right endpoints
    pv_l = pv[:-1] # left endpoints
    return (h/2) * np.sum(pv_r + pv_l)


#Ejercicio 1c
xt, yt = spline_velocidad(x, y)

def posicion_particula(xp,yp):
    pp = []
    for i in range(len(xp)):
        pp.append(trapecio_adaptativo(xp[:i+1],yp[:i+1]))
    
    return pp

res = posicion_particula(xt,yt)

plt.plot(xt, res, '-')
plt.color()
plt.title('Posicion de la particula')
plt.show()
