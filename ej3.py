from matplotlib import pyplot
from scipy.optimize import linprog
import numpy as np

"""
    Wish to resolve:
    minimize -500m - 300s
    subject to: 2m + s ≤ 40
                m + 2s ≤ 50
                m, s ≥ 0
"""

#Ejercicio 3a

def ex_3a():
    print('Respuesta al ejercicio 3a: \n')
    c = np.array([-500, -300])
    A_ub = np.array([
        [2, 1],
        [1, 2]
    ])
    b_ub = np.array([40, 50])
    bounds = [(0, None), (0, None)]
    
    res = linprog(
        c = c,
        A_ub = A_ub,
        b_ub = b_ub,
        bounds = bounds,
        method = "interior-point"
    )

    print("Éxito: {}\n".format(res.success))
    print("Iteraciones: {}\n".format(res.nit))
    print("Status: {}\n".format(res.status))
    #print(res.message + "\n")
    if res.success:
        print("El cliente necesita fabricar al menos:\n")
        print("Mesas: {} unidades\n".format(round(res.x[0])))
        print("Sillas: {} unidades\n".format(round(res.x[1])))
        print("Ingreso neto maximizado con los recursos disponibles: {}\n".format(500 * round(res.x[0]) + 300 * round(res.x[1])))

#Ejercicio 3b

def ex_3b():
    print('Respuesta al ejercicio 3b: \n')

#Ejercicio 3c
def ex_3c():
    print('Respuesta al ejercicio 3c: \n')

#Call the answers
ex_3a()
