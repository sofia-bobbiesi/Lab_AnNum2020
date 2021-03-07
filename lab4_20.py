from inspect    import signature
from matplotlib import pyplot as plt
import numpy as np
import sympy as sp
from warnings   import catch_warnings
from scipy.interpolate import CubicSpline


def ej1a():
    datos = np.loadtxt("datos/datos1a.dat")

    # Los datos tendrán los "x" en el primer elemento y los "y" en el segundo del arreglo
    x_dat = datos[0]
    y_dat = datos[1]

    # np.polyfit devuelve el polinomio de grado k que cumpla el ajuste por cuadrados mínimos
    # Realizar el ajuste con una recta implica buscar el polinomio de grado 1
    polinomio = np.polyfit(x_dat, y_dat, deg=1)

    plt.plot(x_dat, y_dat, '.', label="datos")

    # Evaluar usando np.polyval
    plt.plot(x_dat, np.polyval(polinomio, x_dat), label="ajuste")
    plt.legend()
    plt.show()
   

#    (b)  Dada  la  rectay=3/4x−12,  generar  un  conjunto  de  pares  (xi,yi), i=  1,...,20,en  el  intervalo  [0,10],  con  dispersi ́on  normal  en  el  eje  y.   Realizar  un  ajuste  lineala  los  datos,  obtener  los  coeficientes  y  dibujar  el  ajuste.   Investigar  los  comandos:linspace, randm, polyvalypolyfit, de la librer ́ıa numpy

def ej1b():
    # Recta
    recta = lambda x: (3/4)*x - (1/2)
    # Generar 20 puntos equiespaciados en [0, 10]
    x_dat = np.linspace(0, 10, 20)
    # Generar 20 puntos con dispersión normal en el eje y
    disp = np.random.normal(size=20)
    # Sumarlos a los puntos de la recta
    y_dat = recta(x_dat) + disp

    # Ajustar por una recta los nuevos puntos
    polinomio = np.polyfit(x_dat, y_dat, deg=1)

    # Graficar la recta
    plt.plot(x_dat, np.polyval(polinomio, x_dat), label="ajuste")
    # Graficar datos
    plt.plot(x_dat, y_dat, '.', label="datos")
    # Graficar recta original
    plt.plot(x_dat, recta(x_dat), label="original")
    plt.legend()
    # Mostrar gráfico
    plt.show()