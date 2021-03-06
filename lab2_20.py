
from inspect    import signature
from matplotlib import pyplot
from math       import *
from numpy      import *
from sympy      import *
from warnings   import catch_warnings

import matplotlib.pyplot as plt

x = Symbol('x')

# Ejercicio 1
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
    
    # Iniciamos nuestras listas de puntos y evaluaciones
    hx = []
    hf = []
    
    if sign(u) != sign(v):
        # Si el signo de a y b son diferentes, podemos comenzar
        # Hacemos nuestra primera iteracion antes del bucle
        c = (a + b) / 2.0
        w = fun(c)
        hx.append(c)
        hf.append(w)
        while abs(w) > err and kit < mit:
            kit = kit + 1
            # Aqui elegimos a quien reemplazara nuestro punto medio
            # Sera el que mantenga la condicion inicial de a y b
            if sign(w) != sign(u):
                b = c
            else:
                a = c
            c = (a + b) / 2.0
            w = fun(c)
            hx.append(c)
            hf.append(w)            
    else:
        print("Elegir otro intervalo")
            
    return hx, hf

fun_lab2ej2a = lambda x : tan(x) - 2*x

fun_lab2ej2b = lambda x : x**2 - 3

# Ejercicio 2
def ej2():
    """ Intervalos para fun_lab2ej2a """
    ia1 = [0.8 , 1.4]
    ia2 = [-1 , 0.5]

    hx_ej2a_ia1, hf_ej2a_ia1 = rbisec(fun_lab2ej2a, ia1, 1e-5, 100)
    hx_ej2a_ia2, hf_ej2a_ia2 = rbisec(fun_lab2ej2a, ia2, 1e-5, 100)

    """ Intervalos para fun_lab2ej2b """
    ib1 = [0.0 , 3.0]
    ib2 = [-4.0 , 0.0]
    
    hx_ej2b_ib1, hf_ej2b_ib1 = rbisec(fun_lab2ej2b, ib1, 1e-5, 100)
    hx_ej2b_ib2, hf_ej2b_ib2 = rbisec(fun_lab2ej2b, ib2, 1e-5, 100)

    l_space = linspace(-5, 5, 600)

    fun_lab2ej2a_completa = list(map(fun_lab2ej2a, l_space))
    fun_lab2ej2b_completa = list(map(fun_lab2ej2b, l_space))
    
    pyplot.plot(l_space, fun_lab2ej2a_completa, 'g', label = "fun_lab2ej2a")
    pyplot.plot(l_space, fun_lab2ej2b_completa, 'r', label = "fun_lab2ej2b")

    pyplot.plot(hx_ej2a_ia1, hf_ej2a_ia1, '.--b', \
                label = "rbisec fun_lab2ej2a [{} , {}]".format(*ia1))
    pyplot.plot(hx_ej2a_ia2, hf_ej2a_ia2, '.--b', \
                label = "rbisec fun_lab2ej2a [{} , {}]".format(*ia2))

    pyplot.plot(hx_ej2b_ib1, hf_ej2b_ib1, '.:k', \
                label = "rbisec fun_lab2ej2b [{} , {}]".format(*ib1))
    pyplot.plot(hx_ej2b_ib2, hf_ej2b_ib2, '.:k', \
                label = "rbisec fun_lab2ej2b [{} , {}]".format(*ib2))

    x1, x2, _, _ = pyplot.axis()
    pyplot.axis((x1, x2, -1, 1))
    pyplot.axhline(0, color='black')
    pyplot.axvline(0, color='black')
    pyplot.legend(loc="upper left")

    pyplot.show()

# Ejercicio 3
def  rnewton(fun, x0, err, mit):
    f = lambdify(x,fun)
    df = lambdify(x,fun.diff(x))
    
    hx, hf = [x0], [f(x0)]

    if df(x0) == 0:
	    print(f'La derivada es nula en el punto {x0}')
	    return hx, hf

    k = 0
    while (abs(f(x0)) >=err) and (k < mit):
	
	    xn = x0 - f(x0)/df(x0)
	
	    if abs((xn - x0)/xn) < err:
		    print('El paso es muy pequeño/el procedimiento fue exitoso')
		    return hx, hf

	    x0 = xn
	    hx.append(x0)
	    hf.append(f(x0))

    k +=1
    return hx, hf

# NO USAR NUNCA JAMÁS PI DE SYMPY. NUNCA!!! >:(

# Ejercicio 4
def ej4(a,x0,mit):
    if a > 0:
        fun = lambda x : x**3 - a
        return rnewton(fun,x0,1e-6,mit)
    else:
        print("a debe ser mayor a 0")

# Ejercicio 5
def ripf(fun, x0, err, mit):
    #g_p = lambdify(x,fun)
    hx = [x0]
    
    k = 0
    while k < mit:
        p = fun(x0) #g_p(x0)
        if abs(p-x0) < err:
            print('El paso es pequeño/procedimiento fue exitoso')
            return hx

        x0 = p 
        hx.append(x0)

        k+=1
    return hx

# Ejercicio 6
def ej6():
    funcion = lambda x : 2**(x-1)
    hx  = ripf(funcion, 1.5, 1e-5, 100)
    print(hx)

# Ejercicio 7
def ej7():
    lista_x = []
    n, h = 100, 1.5
    for i in range(n+1):
        lista_x.append(i*h/n)

    lista_y = []
    for x in lista_x:
        fun_ = lambda y : ( y - exp( -(1 - x*y)**2 ), 1 - 2*x*exp(- (1-x*y))* (1-x*y) )
        hy, _ = rnewton(fun_ , 1.2, 1e-8, 100)
        lista_y.append(hy[-1])

    plt.plot(lista_x , lista_y)
    plt.show()