import numpy as np
import scipy.integrate as integrate
from math import pi,sqrt,e
from matplotlib import pyplot

# Ejercicio 1
fun = lambda t: (2/sqrt(pi))*(e**(-t**2))

def simpson(fun,a,b,N):
    if N%2 != 0:
        N+=1
    h = (b-a)/N
    xi0 = fun(a) + fun(b)
    xi1 = 0 #Suma de f(x2i-1)
    xi2 = 0 #Suma de f(x2i)
    for i in range(1,N): # i = 1,...,n-1
        x = a + i*h
        if i%2 == 0:
            xi2 += fun(x)
        else:
            xi1 += fun(x)
    return (h*(xi0 + 2*xi2 + 4*xi1))/3

#a = 0
#b = 10
#N = 51
puntos = np.linspace(0,10,11)
f_puntos = [simpson(fun,0,i,51) for i in puntos]
polinomios = [np.polyfit(puntos,f_puntos, deg=i) for i in range(2,11)]
poli_val = [np.polyval(polinomios[i],puntos[0]) for i in range(len(polinomios))]

# Ejercicio 2

for i in puntos:
    sum_poli = []
    for j in range(len(polinomios)):
        sum_poli.append(np.polyval(polinomios[j],i))
    
    prom = (sum(sum_poli)/len(polinomios[j]))
    print(f"Para el punto {i} el error por aproximación es {abs(f_puntos[int(i)]-prom)}")

#Calculas el promedio del error de cada punto

# Version del José
x_dat = np.linspace(0, 10, 11)
fun = lambda x: e**(-x**2)
y_dat = [simpson(fun,0,i,51) for i in puntos]

polinomios = [np.polyfit(puntos,f_puntos, deg=i) for i in range(2,11)]

for i in range(len(polinomios)):
    polinomios[j]=np.polyval(polinomios[j], x_dat)
    residuo=abs(polinomios[j] - y_dat[j])
    print("el error correspondiente a la valuacion es:\n", residuo)