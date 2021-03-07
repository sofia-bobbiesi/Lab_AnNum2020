from inspect    import signature
from matplotlib import pyplot as plt
from math       import *
import numpy as np
from sympy      import *
from warnings   import catch_warnings
from scipy.interpolate import CubicSpline

x = Symbol('x') # Para poder interpretar funciones

def ilagrange(xi=list, yi=list, zi=list):
    n = len(xi)
    #Construimos primero los polinomios Li(x):
    pn = 0
    w = []
    for i in range(n):
        li = 1
        f_xi = yi[i]
        for j in range(n):
            if i != j:
                li *= (x-xi[j])/(xi[i]-xi[j])
        # Hago sum f(xi)*Li(x)
        pn += li*f_xi

    pn = lambdify(x,pn)
    for i in zi:
        w.append(pn(i))
    return w

def inewton(xi=list, yi=list, zi=list):
    #n filas, 2n-1 columnas
    n = len(xi)
    f = np.zeros((n,n),float)
    for i in range(0,n):
        f[i][0] = yi[i]
    
    # Hago la tabla de diferencias divididas
    for i in range(1,n):
        for j in range(1,i+1):
            f[i][j] = (f[i][j-1]-f[i-1][j-1])/(xi[i]-xi[i-j])
    
    w = []
    pk = 0

    #Calculo el polinomio de la forma a0 + a1(x-x0)...
    for i in range(0,n):
        p_pol = 1
        for j in range(0,i):
            p_pol *= (x-xi[j])

        pk += f[i][i]*p_pol

    pk = lambdify(x,pk)

    for i in zi:
        w.append(pk(i))

    return w

def ej3():
    fun = lambda x: 1/x
    zj = lambda x: 24/25 + x/25

    xi = list(range(1,6))
    yi = [fun(i) for i in range(1,6)]
    
    zi = [zj(i) for i in range(1,102)]
    l_fun = [fun(i) for i in zi]
    
    plt.plot(zi,inewton(xi,yi,zi),label = 'p: polinomio interpolante',color='pink')
    plt.plot(zi,l_fun,label = 'f: 1/x',color='purple')
    plt.grid()
    plt.legend()
    plt.show()

def ej4(n=int):
    fun = lambda x: 1/(1+25*x**2)

    xi = [((2*(i-1))/(n-1)) for i in range(1,n+1)]
    f_xi = [fun(i) for i in xi]

    zi = np.linspace(-1, 1, 200) #crea puntos equisespaciados
    f_fun = [fun(i) for i in zi]
    
    plt.plot(zi,inewton(xi,f_xi,zi),label='Polinomio Interpolante de Newton')
    plt.plot(zi,f_fun,label='Función original')
    plt.title(f"n = {n}")
    plt.grid()
    plt.legend()
    plt.show()

def ej5():
    # Primero, debemos leer el archivo con los datos, generando una matriz.
    # La primer columna son los años, la segunda son las temperaturas que usaremos.
    datos = np.loadtxt("datos/datos_aeroCBA.dat")

    # El atributo "shape" de la matriz "datos" nos dice la forma de la matriz (una tupla).
    # La cantidad de filas de la matriz está en el primer elemento de shape.
    filas = datos.shape[0]

    # Generamos dos listas, donde vamos a colocar nuestros datos.
    años = []
    temps = []

    # Las funciones de interpolación, en algunos casos, sólo funcionan si no tenemos NaN's,
    # debemos filtrarlos usando la función de numpy "isnan".

    for fila in range(filas):
        # Para acceder al elemento i,j de la matriz, debemos hacer datos[i][j]
        temperatura = datos[fila][1]
        if not np.isnan(temperatura):
            años.append(datos[fila][0])
            temps.append(temperatura)

    # La función CubicSpline genera el polinomio que representa la interpolación por spline cubico.
    # Necesitaremos extrapolar, por lo que podemos usar la opción extrapolate (si no se rompe al evaluar).
    polinomio = CubicSpline(años, temps, extrapolate=True)

    # Vamos a generar la lista de años en los que vamos a evaluar nuestro polinomio, 1957-2017.
    puntos = list(range(1957, 2018))

    # Evaluamos el polinomio en los puntos generados.
    final = polinomio(puntos)

    # Vamos a dibujar nuestro gráfico
    plt.plot(puntos, final)
    plt.title("Temperaturas promedio en Córdoba, 1957-2017")
    plt.xlabel("Años")
    plt.ylabel("Temperaturas [°C]")
    plt.grid()
    plt.show()