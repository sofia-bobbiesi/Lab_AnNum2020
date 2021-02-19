import numpy as np
import math
# Ejercicio 1
def ej1():
    x = float(input('Ingrese un numero x: '))
    y = float(input('Ingrese un numero y: '))
    z = float(input('Ingrese un numero z: '))

    print("x/y+z = ", x/y+z)
    print("x/(y+z) = ", x/(y+z))
    print('x/y*z', x/y*z)
    print('x/(y*z)', x/(y*z))


#Ejercicio 2
def ej2():
    a = 1 + 2**(-53)
    print(a)
    b = a-1
    print(b)

    a = 1 + 2**(-52)
    print(a)
    b = a-1
    print(b)

#Ejercicio 3
def ej3(print_all = True):
    a = 2.
    b = 2.
    if print_all:
        while not np.isinf(a):
            print(f"a = {a}")
            a *= 2.
        print("Overflow!")

        while b > 0.:
            print(f"b = {b}")
            b /= 2.
        print("Underflow!")
    else:
        while not np.isinf(2. * a):
            a *= 2.
        print(f"a = {a}")
        print("El próximo causa Overflow!")

        while (b / 2.) > 0.:
            b /= 2.
        print(f"b = {b}")
        print("El próximo causa Underflow!")

# Ejercicio 4
def ej4a():
    x = 0
    while x != 10:
        x = x + 0.1
# Nunca llega a ser 10 :(
def ej4b():
    x = 0
    while x != 10:
        x = x + 0.5

# Ejercicio 5
def ej5(n=int):
    for i in range(n):
        i *= i
    return f"El factorial de {n} es {i}"

def ej5b(n=int):
    return math.factorial(n)

""" Probar con
1)
1.0000000000000003                                                                                                                         
1.0000000000000002
Debe dar "Iguales"
2)
1.0000000000000003
1.0000000000000004
Debe dar "Iguales", pero con tol_rel = 10e-17 debe dar "Distintos"
Después tratar on tol_rel = 0.0, tol_abs = 10e-17
"""
# Ejercicio 6
def ej6(tol_rel, tol_abs):
    a = float(input("Dar un real: "))
    b = float(input("Dar otro real: "))

    print("Sin tolerancia")
    if abs(a-b) > 0:
        print(f"{a} y {b} son iguales")
    else:
        print(f"{a} y {b} son distintos")

    """
    tol_abs = Tolerancia absoluta, mientras la diferencia no sea menor se consideran distintos
    tol_rel = Tolerancia relativa, a medida que los valores se vuelven más grandes, se vuelve más
              grande la diferencia permitida mientras que aún se les permitir considerarse iguales
    """
    print("Con tolerancia")
    if abs(a-b) > max(tol_rel * max(a, b), tol_abs):
        print(f"{a} y {b} son iguales")
    else:
        print(f"{a} y {b} son distintos")

# Ejercicio 7
def ej7(x=int, n=int):
    return pow(x, n)

def potencias(n=int):
    for i in range(6):
        print(f"La potencia {i} de {n} es {ej7(n,i)}")

# Ejercicio 8
def baskhara_mala(a,b,c):
    dis = (b**2) - (4*a*c)
    if dis < 0:
        return "No tiene solución real"
    elif dis == 0:
        x1 = (-b + math.sqrt(dis))/2*a
        return x1, x1
    else:
        print(dis)
        x1, x2  = (-b + math.sqrt(dis))/(2*a),(-b - math.sqrt(dis))/(2*a)
        return x1, x2

def baskhara_buena(a,b,c):
    # Definicion del libro
    dis = (b**2) - (4*a*c)
    x1 = (-2*c)/(b+math.sqrt(dis))
    x2 = (-2*c)/(b-math.sqrt(dis))
    return x1,x2

def buena(a, b, c):
    """ Enviada por el profesor """
    """ Vemos cuál b resulta más lejos de 0 """
    if b >= 0:
        x_1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    else:
        x_1 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    """ Una vez obtenida la primera raíz, recordemos que x_1*x_2 = c/a y usamos eso para obtener x_2 """
    x_2 = c / (a * x_1)
    return x_1, x_2

# Ejercicio 9
def horn(pol,x):
    b = pol[0]
    for i in range(1,len(pol)):
        b = pol[i] + x*b
    return b

coef_input = input("Ingresar los n coeficientes del polinomio, de mayor a menor grado: ")   
coefs = list(map(float,coef_input.split(' ')))
x = float(input("Evaluar P en x = "))
p = horn(coefs, x)
print("Polinomio P evaluado en x =",x, "resulta:",p)

