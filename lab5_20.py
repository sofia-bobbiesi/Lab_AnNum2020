import numpy as np
import scipy.integrate as integrate
from math import ceil, cos, sin, tan, e, pi, sqrt, inf,log
from matplotlib import pyplot

def intenumcomp(fun,a,b,N,regla=str):
    # I = [a,b] 
    # N cantidad de sub intervalos 
    # integrar usando las reglas
    S = 0.
    #puntos = np.linspace(a,b,N+1)
    if str.lower(regla) == 'trapecio':
        h = (b-a)/N
        suma_parcial = [ fun(a + j*h) for j in range(1, N)] #Evaluo en los puntos iterativos xj
        S = h/2 * (fun(a) + fun(b) + 2 * sum(suma_parcial)) #Termino de evaluar en la funcion
        
    elif str.lower(regla) == 'pm':
        if N%2 != 0:
            N+=1
        h = (b-a)/(N+2)
        suma_parcial = [fun(a+(2*j+1)*h) for j in range(0,N//2 + 1)]
        S = 2*h*sum(suma_parcial)

    elif str.lower(regla) == 'simpson':
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
        S = (h*(xi0 + 2*xi2 + 4*xi1))/3
    else:
        print(f"La regla {regla} ingresada no es válida")
    # Notar que no se incluye el cálculo del error para las reglas compuestas
    #la salida debe ser un real
    return S

# tiempo = [0,6,12,18,24]
# velocidad = [38,41,46,48,45]
# N = len(tiempo)
# fun = lambda x: 9.64506173e-05*x**4 -7.33024691e-03*x**3 + 1.35416667e-01*x**2 -6.94444444e-02*x + 3.80000000e+01
# print(intenumcomp(fun,0,24,6,'pm')) # -> 1059.95 con trapecio, buena aproximación

def ej2():
    fun = lambda x: e**-x
    fun_aprox, _ = integrate.quad(fun,0,1)

    for i in [4,10,20]:
        print(f"Para N = {i}")
        print(f"El error por método del trapecio es {abs(fun_aprox-intenumcomp(fun,0,1,i,'trapecio'))}")
        print(f"El error por método de simpson es {abs(fun_aprox-intenumcomp(fun,0,1,i,'simpson'))}")
        print(f"El error por método de punto medio es {abs(fun_aprox-intenumcomp(fun,0,1,i,'pm'))}\n")

#Concluimos en que el método de simpson está re bueno, aproxima joya con errores re chiquitos

def senint(x):
    N = ceil(x / 0.01) + 1
    return intenumcomp(cos, 0, x, N, "trapecio")

def ej3():
    xi = np.linspace(0,2*pi,13)
    yi = [sin(i) for i in xi]
    zi = [senint(i) for i in xi]

    pyplot.plot(xi, yi, label="sin(x)")
    pyplot.plot(xi, zi, label="senint(x)")
    pyplot.legend(loc="upper left")
    pyplot.grid()
    pyplot.axhline(0, color="black")
    pyplot.show()

def ej4():
    #4a
    a = lambda x: x*e**-x
    a_aprox, _ = integrate.quad(a,0,1)
    error = inf
    n = 1
    while error > 10e-5:
        error = abs(a_aprox - intenumcomp(a,0,1,n,'trapecio'))
        n +=1
    print(f"La función x*e**-x tiene un error < 10e-5 para n = {n} con la regla del trapecio")

    n = 1
    error = inf
    while error > 10e-5:
        error = abs(a_aprox - intenumcomp(a,0,1,n,'simpson'))
        n +=1
    print(f"La función x*e**-x tiene un error < 10e-5 para n = {n} con la regla de simpson\n")

    #4b
    b = lambda x: x*sin(x)
    b_aprox, _ = integrate.quad(b,0,1)

    n = 1
    error = inf
    while error > 10e-5:
        error = abs(b_aprox - intenumcomp(b,0,1,n,'trapecio'))
        n +=1
    print(f"La función x*sin(x) tiene un error < 10e-5 para n = {n} con la regla del trapecio")

    n = 1
    error = inf
    while error > 10e-5:
        error = abs(b_aprox - intenumcomp(b,0,1,n,'simpson'))
        n +=1
    print(f"La función x*sin(x) tiene un error < 10e-5 para n = {n} con la regla de simpson\n")

    # #4c 
    c = lambda x: (1+x**2)**(3/2)
    c_aprox, _ = integrate.quad(c,0,1)

    n = 1
    error = inf
    while error > 10e-5:
        error = abs(c_aprox - intenumcomp(c,0,1,n,'trapecio'))
        n +=1
    print(f"La función (1+x**2)**(3/2) tiene un error < 10e-5 para n = {n} con la regla del trapecio")

    n = 1
    error = inf
    while error > 10e-5:
        error = abs(c_aprox - intenumcomp(c,0,1,n,'simpson'))
        n +=1
    print(f"La función (1+x**2)**(3/2) tiene un error < 10e-5 para n = {n} con la regla de simpson\n")

    # #4d
    #d = lambda x: 1/sqrt(1-sin(x)**2)/2)
    d = lambda x: sqrt(2)/sqrt(2-sin(x)**2) #es equivalente y más visible uwu
    d_aprox, _ = integrate.quad(d,0,pi/2)

    n = 1
    error = inf
    while error > 10e-5:
        error = abs(d_aprox - intenumcomp(d,0,pi/2,n,'trapecio'))
        n +=1
    print(f"La función 1/sqrt((1-sin(x)**2)/2) tiene un error < 10e-5 para n = {n} con la regla del trapecio")

    n = 1
    error = inf
    while error > 10e-5:
        error = abs(d_aprox - intenumcomp(d,0,pi/2,n,'simpson'))
        n +=1
    print(f"La función 1/sqrt((1-sin(x)**2)/2) tiene un error < 10e-5 para n = {n} con la regla de simpson\n")

def ej5a():
    """
    f(x) = exp(-x**2) , f(-x) = exp(-(-x)**2) = f(x) => exp es par
    Una forma de integrar sería:
    integral(-inf,+inf) f(x)dx = 2 * integral(0,+inf) f(x)dx
    También tenemos que 
    u ->  pi/2 <=> tan(u) -> +inf
    u -> -pi/2 <=> tan(u) -> -inf
    Si x = tan(u), u -> +pi/2, x -> +inf
                   u -> -pi/2, x -> -inf
    -x**2 = -tan(u)**2
    dx = sec(u)**2 * du = cos(u)**(-2) du
    """
    fun = np.vectorize(lambda u: np.exp(-tan(u)**2) * cos(u)**(-2))
    u = np.linspace(-pi/2, pi/2, 100)
    trapecio = integrate.trapz(fun(u), u)
    simpson  = integrate.simps(fun(u), u, even="avg")
    print("Integral por regla del Trapecio (integrate.trapz): %s\n"%trapecio)
    print("Integral por regla de Simpson (integrate.simps): %s\n"%simpson)
    return trapecio, simpson

def ej5b():
    fun = np.vectorize(lambda x : (x**2) * log(x + (x**2 + 1)**(1/2)))
    x = np.linspace(0, 2, 100)
    trapecio = integrate.trapz(fun(x), x)
    simpson  = integrate.simps(fun(x), x, even="avg")
    print("Integral por regla del Trapecio (integrate.trapz): %s\n"%trapecio)
    print("Integral por regla de Simpson (integrate.simps): %s\n"%simpson)
    return trapecio, simpson

def pendulo(l=int,alfa=int,N=int,regla=str):
    #alfa entre [0,90] en grados
    g = 9.8
    r_alfa = np.deg2rad(alfa)
    fun = lambda x : 1/sqrt(((1-sin(r_alfa/2)**2)*sin(x)**2))
    T = 4*(sqrt(l)/g) * intenumcomp(fun,0,pi/2,N,regla)
    return T