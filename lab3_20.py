from inspect    import signature
from matplotlib import pyplot as plt
from math       import *
import numpy as np
from sympy      import *
from warnings   import catch_warnings


x = Symbol('x')
# .  Programar una funcion en pytho que evalue el polinomio interpolante p usando la formade Lagrange.  La funcion debe llamarse “ilagrange” y tener como entrada (x, y, z) donde x, y ∈Rn son las coordenadas de los pares a interpolar (o seap(xi) =yi,i= 1, . . . , n)yz∈Rm son  valores  para  evaluar p.   La  salida debe  ser w ∈Rm tal  que wj=p(zj),j= 1, . . . , m.  La sintaxis a utilizar debe ser:python> w = ilagrange(x, y, z)

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

xi = [2,2.5,4]
yi = [1/2,2/5,1/4]
zi = [0,1,3]
print(ilagrange(xi,yi,zi))

# Realizar una funcion en python an ́aloga a la del ejercicio 1 pero utilizando la forma de New-ton del polinomio interpolante, calculando los coeficientes mediantediferencias divididas.La funci ́on debe llamarse “inewton”.

def inewton(xi=list, yi=list, zi=list):
    #n filas, 2n-1 columnas
    n = len(xi)
    f = np.zeros((n,n),float)
    for i in range(0,n):
        f[i][0] = yi[i]
    
    for i in range(1,n):
        for j in range(1,i+1):
            f[i][j] = (f[i][j-1]-f[i-1][j-1])/(xi[i]-xi[i-j])
    
    w = []
    pk = 0

    for i in range(0,n):
        p_pol = 1
        for j in range(0,i):
            p_pol *= (x-xi[j])

        pk += f[i][i]*p_pol

    pk = lambdify(x,pk)

    for i in zi:
        w.append(pk(i))

    return w

print(inewton(xi,yi,zi))

#  Considerar  la  funci ́onftal  quef(x)  =  1/x.   Utilizando  el  ejercicio  anterior,  graficaren  una  misma  figurafypque  interpole{(i, f(i))}5i=1,  usando  para  ambas  los  puntosequiespaciadoszj= 24/25 +j/25,j= 1, . . . ,101

def ej3():
    fun = lambda x: 1/x
    zj = lambda x: 24/25 + x/25

    xi = [1,2,3,4,5]
    yi = [fun(1),fun(2),fun(3),fun(4),fun(5)]
    zi = []
    l_fun = []

    for i in range(1,102):
        zi.append(zj(i))
    
    for i in zi:
        l_fun.append(fun(i))

    plt.plot(zi,inewton(xi,yi,zi),label = 'p: polinomio interpolante',color='pink')
    plt.plot(zi,l_fun,label = 'f: 1/x',color='purple')
    plt.grid()
    plt.legend()
    plt.show()

