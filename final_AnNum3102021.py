# Sofía Bobbiesi Bender, DNI = 43135851
from math import cos, sqrt
import numpy as np
# Ejercicio 1:

def rbisec(fun, I, err, mit):
    """
    Funcion para aplicar algoritmo de biseccion, dando como salida
    dos listas: historial de puntos medios e historial de evaluaciones
    """
    # I = [a, b]
    a = I[0]
    b = I[1]

    u = fun(a)
    v = fun(b)

    # Iniciamos nuestro contador de iteraciones
    kit = 0
    
    if np.sign(u) != np.sign(v):
        # Si el signo de a y b son diferentes, podemos comenzar
        # Hacemos nuestra primera iteracion antes del bucle
        c = (a + b) / 2.0
        w = fun(c)
        while abs(w) > err and kit < mit:
            kit += 1
            # Aqui elegimos a quien reemplazara nuestro punto medio
            # Sera el que mantenga la condicion inicial de a y b
            if np.sign(w) != np.sign(u):
                b = c
            else:
                a = c
            c = (a + b) / 2.0
            w = fun(c)         
    else:
        print("Elegir otro intervalo")
            
    return c

def ej1():
    fun_ej1 = lambda x: cos(x)
    I = [0,3]
    res = rbisec(fun_ej1,I,1e-10,10)
    print(f"La aproximación por el método de bisección es: {res}") # res = 1.57177734375
    return res


def trapecio(fun,a,b,N):
    # I = [a,b] 
    # N cantidad de sub intervalos 
    h = (b-a)/N
    suma_parcial = [ fun(a + j*h) for j in range(1, N)] #Evaluo en los puntos iterativos xj
    return h/2 * (fun(a) + fun(b) + 2 * sum(suma_parcial)) #Termino de evaluar en la funcion

def ej2():
    fun_ej2 = lambda x: sqrt(1-x**2)
    # I = [-1,1]
    # N = 10
    res = trapecio(fun_ej2,-1,1,10)
    print(f"La aproximación por el método del trapecio compuesto es: {res}") # res = 1.5185244144417753
    return res

def aprox_pi():
    aprox_ej1 = abs(np.pi/2-ej1())
    aprox_ej2 = abs(np.pi/2-ej2())

    if aprox_ej1 > aprox_ej2:
        print(f"La regla del trapecio tiene un error más chico de {aprox_ej2} al aproximar pi/2")
    elif aprox_ej1 < aprox_ej2:
        print(f"El método de bisección tiene un error más chico de {aprox_ej1} al aproximar pi/2")
    elif aprox_ej1 == aprox_ej2:
        print(f"El método de bisección tiene el mismo error que la regla del trapecio, de {aprox_ej1}")
    return
# Bisección aproxima mejor con 0.000981016955103442 de error
aprox_pi()