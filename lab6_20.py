import numpy as np
import scipy.integrate as integrate
from math import ceil, cos, sin, tan, e, pi, sqrt, inf,log
from matplotlib import pyplot
from scipy.linalg import lu

def soltrsup(A,b):
    #si no es invertible, cortar
    try:
        np.linalg.inv(A)
    except Exception as e:
        print("El sistema no tiene solución")
        return e

    n = A.shape[0]
    x = b.copy()

    for i in range(n - 1, -1 , -1):
        for j in range(i + 1, n):
            x[i] = x[i] - A[i][j] * x[j]
        x[i] = x[i] / A[i][i]

    return x

def soltrinf(A,b):
    #si no es invertible, cortar
    try:
        np.linalg.inv(A)
    except Exception as e:
        print("El sistema no tiene solución")
        return e

    n = A.shape[0]
    x = b.copy()

    #Si es invertible, tiene solución
    for i in range(n):
        for j in range(i):
            x[i] = x[i] - A[i][j] * x[j]
        x[i] = x[i] / A[i][i]

    return x

# Notar que ambos métodos no dan resultados fraccionarios,
# usar print(scipy.linalg.solve_triangular(A,b)) en cambio
R = np.array([
        [2, 7, 1, 8, 2],
        [0, 8, 1, 8, 2],
        [0, 0, 8, 4, 5],
        [0, 0, 0, 9, 0],
        [0, 0, 0, 0, 4],
    ],float)
b = np.array([3, 1, 4, 1, 5])


def egauss(A,b):
    # A es una matriz R^(n*n)
    # b es un vector de R^n
    # retorna el par (U, y), donde
    # U es una matriz triangular R^(n*n)
    # y es un vector de R^n, la solución
    n = A.shape[0]
    U = A.copy()
    y = b.copy()
    for k in range(n - 1):
        for i in range(k + 1, n):
            if U[k,k] == 0:
                print("No se puede seguir la eliminación gaussiana: U[{}, {}] == 0\n".format(k, k))
                raise ValueError(f"U[{k}, {k}] == 0\n")
            m = U[i, k] / U[k, k]
            for j in range(k + 1, n):
                U[i, j] = U[i, j] - m * U[k, j]
            y[i] = y[i] - m * y[k]
    U = np.triu(U)
    return U, y

# A = np.array([[2,-2,1],[1,1,3],[0,4,1]])
# b = np.array([-1,6,9])

# print(egauss(A,b))

def soleg(A,b):
    try:
        U, y = egauss(A, b)
        x = soltrsup(U, y)
        return x
    except Exception as e:
        print("No se pudo realizar la eliminación gaussiana...\n")
        return e

def sollu(A,b):
    P,L,U = lu(A)
    y = soltrinf(L,P.T @ b)
    x = soltrsup(U,y)
    return x

def ej4():

    A = np.array([
            [4,-1,0,-1,0,0],
            [-1,4,-1,0,-1,0],
            [0,-1,4,0,0,-1],
            [-1,0,0,4,-1,0],
            [0,-1,0,-1,4,-1],
            [0,0,-1,0,-1,4]
        ],float)

    b1 = np.array([1,1,1,0,0,0],float)
    b2 = np.array([1,1,1,1,1,1],float)

    print(f"Resultado por método LU para A y b1 {sollu(A,b1)}")
    print(f"Resultado por método LU para A y b2 {sollu(A,b2)}")
    print(f"Resultado por método de Gauss para A y b1 {soleg(A,b1)}")
    print(f"Resultado por método Gauss para A y b2 {soleg(A,b2)}")
    #Si no se la define como float, al hacer soleg no admite
    # division fraccionaria y el resultado es [0,0,0,0], lo cual
    # es incorrecto. El método LU es preciso.

def jacobi(A,b,err,mit):
    # x sol aprox
    # k catidad de it
    n = A.shape[0] #número de ecuaciones del sistema
    xo = np.zeros(n) #elijo el conjunto x(0) como (0,0,..,0)
    x = np.zeros(n)

    k = 0
    while k < mit:
        for i in range(n):
            sumatoria = 0
            for j in range(n):
                if i != j:
                    sumatoria += A[i][j]*xo[j]
            x[i] = (b[i]-sumatoria)/A[i][i]
    
        if np.linalg.norm(x - xo, np.inf) <= err:
            print('El procedimiento fue exitoso')
            return [x, k]
        k += 1
        xo = x.copy() #Redifino todos los xo

    return [x,k]

def gseidel(A,b,err,mit):
    # x sol aprox
    # k catidad de it
    n = A.shape[0] #número de ecuaciones del sistema
    xo = np.zeros(n) #elijo el conjunto x(0) como (0,0,..,0)
    #x = np.zeros(n)
    
    k = 0
    while k < mit:
        x = np.zeros(n)
        for i in range(n):
            sumatoria = 0
            for j in range(i):
                sumatoria += A[i][j]*x[j]
            for j in range(i+1,n):
                sumatoria += A[i][j]*xo[j]
            x[i] = (b[i]-sumatoria)/A[i][i]
    
        if np.linalg.norm(x - xo, np.inf) <= err:
            print('El procedimiento fue exitoso')
            return [x, k]
        k += 1
        xo = x.copy() #Redifino todos los xo
        
    return [x,k]

def ej6():
    A1 = np.array([[3,2,1],[1,6,1],[1,1,4]],float)
    b1 = np.array([5,9,6],float)
    A2 = np.array([[5,7,6,5],[7,10,8,7],[6,8,10,9],[5,7,9,10]],float)
    b2 = np.array([23,32,33,31],float)


    _, j = jacobi(A1,b1,10e-11,100)
    _, g = gseidel(A1,b1,10e-11,100)
    
    print(f"Para el 1) se necesitan {j} con el método de Jacobi") #41 
    print(f"Para el 1) se necesitan {g} con el método de Gauss-Seidel") #14

    
    _, j = jacobi(A2,b2,10e-4,500)
    _, g = gseidel(A2,b2,10e-4,1000)
    print(f"Para el 2) se necesitan {j} con el método de Jacobi") #500
    print(f"Para el 2) se necesitan {g} con el método de Gauss-Seidel") #474
