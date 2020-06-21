import matplotlib.pyplot as plt
from scipy.optimize import linprog
import numpy as np

"""
    Wish to resolve:
    maximize -500m - 300s
    subject to: 2m + s ≤ 40
                m + 2s ≤ 50
                m, s ≥ 0
"""

#Ejercicio 3a

def ex_3a():
    print('\33[1mRespuesta al ejercicio 3a: \33[0m \n')
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
        print("El carpintero necesita fabricar al menos:\n")
        print("{} mesas\n".format(round(res.x[0])))
        print("{} sillas\n".format(round(res.x[1])))
        print("Ingreso neto maximizado con los recursos disponibles: {}\n".format(500 * round(res.x[0]) + 300 * round(res.x[1])))

#Ejercicio 3b

def ex_3b():
    print('\33[1mRespuesta al ejercicio 3b: (ver Figura 1)\33[0m\n')
    m = np.linspace(0, 20, 100)
    s_1 = -2 * m + 40
    s_2 = (1/2) * (-m + 50)
    
    plt.plot(m, s_1, label = "$s = -2 m + 40$")
    plt.plot(m, s_2, label = "$s = (1/2) * (-m + 50)$")

    plt.title('Maximizar -500m - 300s')
    plt.legend(loc = "upper right")
    plt.ylim(0, 40)
    plt.xlim(0, 20)
    plt.ylabel("$s$")
    plt.xlabel("$m$")
    plt.fill_between(m, 0, np.minimum(s_1, s_2), alpha = 0.75)

    plt.grid()
    plt.show()

#Ejercicio 3c
def ex_3c():
    print('\33[1mRespuesta al ejercicio 3c:\33[0m \n')
    c = np.array([-500, -500, -300, -300])
    A_ub = np.array([
        [2, 2, 1, 1],
        [1, 1, 2, 2]
    ])
    b_ub = np.array([40, 50])
    bounds = [(0, None), (0, None), (0, None), (0, None)]
    
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
    print(res.message + "\n")
    if res.success:
        """ mc: res.x[0]
            ma: res.x[1]
            sc: res.x[2]
            sa: res.x[3]
        """
        horas_ayudante = 2 * round(res.x[1]) + round(res.x[3]) 
        neto = 500 * round(res.x[0]) + 500 * round(res.x[1]) + 300 * round(res.x[2]) + 300 * round(res.x[3])
        paga_ayudante = 200 * horas_ayudante
        porcentaje_ingreso = round(100 - 100 * (paga_ayudante / neto))
        print("Ingreso neto por el trabajo: {}\n".format(neto))
        print("Paga correspondiente al ayudante: {}\n".format(paga_ayudante))
        print("Ingreso del carpintero: {}\n".format(neto - paga_ayudante))
        print("Porcentaje de ingreso del carpintero ≈ {} %\n".format(porcentaje_ingreso))
        print("Como el porcentaje es del ≈ {}, deja un pequeño margen para contratar al ayudante.".format(porcentaje_ingreso), "Luego, este trabajaría {} hs aproximadamente.\n".format(horas_ayudante))

#Call the answers
ex_3a()
ex_3b()
ex_3c()