from inspect    import signature
from matplotlib import pyplot as plt
import math
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

def ej2():
    fx = lambda x: math.asin(x)
    gx = lambda x: math.cos(x)

    #Creo los 50 puntos equisespaciados para los intervalos dados
    fxi = np.linspace(0, 1, 50)
    gxi = np.linspace(0,4*math.pi,50)

    #Evalua los polinomios en cada punto del intervalo
    fyi = [fx(i) for i in fxi]
    gyi = [gx(i) for i in gxi]

    print('Para la función arcsen(x) los restos son:')
    for i in range(0,6):
        _,resto, _, _, _ = np.polyfit(fxi,fyi, deg=i, full=True)
        print(f'Para n ={i} el resto es: {resto}')

    print('\nPara la función cos(x) los restos son:')
    for i in range(0,6):
        _,resto, _, _, _ = np.polyfit(gxi,gyi, deg=i, full=True)
        print(f'Para n ={i} el resto es: {resto}')

def ej3a():
    datos = np.loadtxt("datos3a.dat")

    x = datos[0]
    y = datos[1]

    # aplico ln en ambos miembros para simplificar la ecuacion
    y_hat = np.log(y)
    x_hat = np.log(x)

    p = np.polyfit(x_hat,y_hat,1)

    A = p[0]
    c_hat = p[1]
    C = np.exp(c_hat)
    
    return A,C


def ej3b():
    datos = np.loadtxt("datos3a.dat")

    x = datos[0]
    y = datos[1]

    y_hat = np.log(y)
    x_hat = np.log(x)

    p = np.polyfit(x_hat,y_hat,deg=1)

    A = p[0]
    c_hat = p[1]
    C = np.exp(c_hat)
    
    return A,C

def ej4():
    datos = np.genfromtxt('datos/covid_italia.csv', delimiter=',')
    x = datos[:,0] #Lee toda la matriz, la columna 0
    y = datos[:,1]
    
    #y(x) = ae**bx => ln(y) = ln(a) + b*x
    y_hat = np.log(y) #Reajusto los datos de y

    ajuste = np.polyfit(x, y_hat,deg=1) # Devuelve los coefs de an,..,a0

    b = ajuste[0]
    a_hat = ajuste[1]
    a = np.exp(a_hat)

    modelo = lambda x: a*np.exp(b*x)

    plt.plot(x,modelo(x),label='Función aproximada')
    plt.plot(x,y_hat,label='Datos de ajuste')
    plt.plot(x,y,label="Datos")
    plt.legend()
    plt.show()

ej4()