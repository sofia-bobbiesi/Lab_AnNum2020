import numpy as np
import scipy.integrate as integrate
from math import ceil, cos, sin, tan, e, pi, sqrt, inf,log
import matplotlib.pyplot as plt
from scipy.optimize import linprog

# cantidad_P >= 3
# cantidad_N >= 1.5
# cantidad_K >= 4

#		P	N	K	$
# T1	3	1	8	10
# T2	2	3	2	8

# x : Kg de fertilizante T1 en 1 Kg de fertilizante Nuevo
# y : Kg de fertilizante T2 en 1 Kg de fertilizante Nuevo

# x + y = 1

# minimizar el costo total cubriendo requerimientos del suelo

# Costo total de 1 Kg de fertilizante Nuevo: x*10 + y*8

# Requerimientos:
# x*3 + y*2 >= 3
# x + 3*y >= 1.5
# x*8 + y*2 >= 4

# min 10*x+8*y
# s.a
#	 x*3 + y*2 >= 3
#	 x + 3*y >= 1.5
#	 x*8 + y*2 >= 4

# y >= (3 - 3*x)*(1/2)
# y >= (1.5 - x)*(1/3)
# y >= (4 - 8*x)*(1/2)


def ej1():
    x = np.arange(0,1.01,0.01)

    y1 = (3 - 3*x)*(1/2)
    y2 = (1.5 - x)*(1/3)
    y3 = (4 - 8*x)*(1/2)

    y4 = np.maximum(y1,np.maximum(y2,y3))

    plt.plot(x,y1)
    plt.plot(x,y2)
    plt.plot(x,y3)

    plt.fill_between(x,y4,2.5,alpha=0.5)

    #plt.fill_between(x,y1,2.5,alpha=0.,hatch='/')
    #plt.fill_between(x,y2,2.5,alpha=0.,hatch='|')
    #plt.fill_between(x,y3,2.5,alpha=0.,hatch='-')

    plt.ylim(0,2.5)
    plt.xlim(0,1)

    plt.grid()
    plt.show()

def ej2():
    # max z = x + y 
    # 50*x + 24*y <= 2400
    # 30*x + 33*y <= 2100

    x = np.arange(0, 50, 1.)
    y1 = (1/24)*(-50*x + 2400)
    y2 = (1/33)*(-30*x + 2100)
    # Cuando maximizas se minimiza para la forma estandar
    y3 = np.minimum(y1,y2)
  
    plt.plot(x,y1)
    plt.plot(x,y2)
    plt.plot(x,y3)
    #Curvas de nivel 
    y4 = 60-x
    y5 = 65-x
    y6 = 70-x
    plt.plot(x,y4,".",color='black')
    plt.plot(x,y5,".",color='black')
    plt.plot(x,y6,".",color='black')
    plt.fill_between(x,y3,0,color='purple',alpha=0.4,hatch='*')
    plt.grid()
    plt.show()


#                   A       B       curar
#medicamento 1      3       2       25

#medicamento 2      4      1       20

#total              25      10

#a) x: unidad de medicina 1
# y: unidad de medicina 2

#funcion objetivo f = 25 * x + 20 * y 

# 3 * x + 4 * y <=25
# 2 * x + y <= 10
# x,y >= 0

def ej3():
    x = np.arange(0, 5, 0.1)
    y1 = (25 - 3*x)/4
    y2 = 10 - 2* x
    y3 = np.minimum(y1,y2)

    plt.plot(x,y1)
    plt.plot(x,y2)
    plt.plot(x,y3)
    plt.fill_between(x,y3,0,color='pink',alpha=0.4,hatch='*')
    plt.grid()
    plt.show()
    #Como debo maximizar -> encuentro el minimo entre las rectas
    c = np.array([-25, -20])
    A = np.array([ [3,4], [2,1] ])
    b = np.array([25,10])
    x0_bounds = (0, None)
    x1_bounds = (0, None)

    res = linprog(c, A_ub = A, b_ub = b, bounds=[x0_bounds, x1_bounds])
    print(res)
    return res

def ej4():
    # max z = 7*x + 4*y + 3*z
    # sujeto a:
    #          x + 2*y + 2*z <=30
    #          2*x + y + 2*z <=45

    z = np.array([-7,-4,-3])
    A = np.array([[1,2,2],[2,1,2]],float)
    b = np.array([30,45])
    
    x_bounds = (0, None)
    y_bounds = (0, None)
    z_bounds = (0,None)

    res = linprog(z, A_ub = A, b_ub = b, bounds=[x_bounds, y_bounds,z_bounds])
    print(res)


def ej5b():
    # Costo total = Costo_1 + Costo_2 + Costo_3 + Costo_4

# Costo total = Horas_1 * 68.3 + Horas_2 * 69.5 + Horas_3 * 71 + Horas_4 * 71.2

# Completar la Tarea M
# M_1 / 52 + M_2 / 57 + M_3 / 51 + M_4 / 56 >= 1

# Completar la Tarea N
# N_1 / 212 + N_2 / 218 + N_3 / 201 + N_4 / 223 >= 1

# Horas_1 = M_1 + N_1 + P_1 + Q_1

# Costo total = (M_1 + N_1 + P_1 + Q_1) * 68.3 + Horas_2 * 69.5 + Horas_3 * 71 + Horas_4 * 71.2

# Horas disponibles
# M_1 + N_1 + P_1 + Q_1 <= 220

##############

# Función objetivo: Costo total
# Restricciones:
#	Completar las tareas (4 restricciones)
#	Horas disponibles (4 restricciones)
# M_1 M_2 M_3 M_4 N_1 N_2 N_3 N_4 ... Q_4

    c = np.tile(np.array([68.3, 69.5, 71, 71.2]), 4)

    # Tareas

    tabla = np.array([52,57,51,56,212,218,201,223,25,23,26,21,60,57,54,55])
    tabla = 1/tabla

    A1 = np.zeros((4,16))
    I = np.repeat(np.arange(4),4)
    J = np.arange(16)
    A1[I,J] = -tabla

    b1 = -np.ones(4)

    # Horas disponibles

    A2 = np.tile(np.eye(4),4)
    b2 = np.array([220,300,245,190])

    A_ub = np.vstack([A1,A2])
    b_ub = np.hstack([b1,b2])

    res = linprog(c,A_ub=A_ub,b_ub=b_ub)

    # M_1 M_2 M_3 M_4 N_1 N_2 N_3 N_4 ... Q_4

    x = np.round(res.x)

    for i in range(4):
        print("el equipo {} debe ocupar: {}".format(i+1,x[np.arange(4)*4+i]))


def ej6():
    costos  = np.loadtxt("datos/costos.dat", dtype = "float")
    stock   = np.loadtxt("datos/stock.dat", dtype = "float")
    demanda = np.loadtxt("datos/demanda.dat", dtype = "float")

        # Dimensión (10000,)
    c = costos.flatten()
    # Dimensión (200,)
    b_ub = np.hstack((stock, (-1)*demanda))
    # Dimensión (200, 10000)
    A_ub = np.vstack(
        ( np.kron(np.eye(100), np.ones(100)), np.kron(np.ones(100), -np.eye(100)) )
    )
    # Dimensión (10000,)
    bounds = 10000 * [(0, None)]

    res = linprog(
        c = c,
        A_ub = A_ub,
        b_ub = b_ub,
        bounds = bounds,
    )


    print(f"Éxito: {res.success}\n")
    print(f"Iteraciones: {res.nit}\n")
    print(res.message + "\n")
    #Quizás hubiera sido más sano hacer un reshape de res.x y printear como matriz
    if res.success:
        print("Solución:\n")
        for i in range(100):
            for j in range(100):
                if round(res.x[100 * i + j]) > 0:
                    print(f"Del depósito {i + 1} se transporta al cliente {j + 1} aprox. {round(res.x[100 * i + j])} unidades")
        print("\n")
        print(f"Valor de la función objetivo: {res.fun}\n")