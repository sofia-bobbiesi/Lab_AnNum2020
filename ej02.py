import scipy.linalg
import numpy as np
import math

def soltrinf(A, b):
    n = A.shape[0]
    x = b

    for i in range(n):
        for j in range(i):
           x[i] = x[i] - A[i, j] * x[j]
        x[i] = x[i] / A[i, i]
    return x

def gseidel(A,b,err,mit):
    n = A.shape[0]
    x = np.zeros(n)
    k = 0 

    LD = np.tril(A)     #Triangular inferior de A
    U = np.triu(A,1)    #Triangular superior de A

    while k < mit:
        x_it = soltrinf(LD, b - (U @ x))
        norma = np.linalg.norm(x_it - x, np.inf)
        if norma <= err:
            print("[gseidel] || x_it - x || (inf)=={} <= {}\n".format(norma,err))
            return [x_it, k]
        x = x_it
        k =+ 1

    return [x,k]


def sor(A, b, omega, err, mit): 
    if (omega<=1): 
        print('Omega debe ser mayor a 1 \n') 
        k = -1
        x = float('nan')
        return 

    n = A.shape[0]
    k = 0
    x = np.zeros((n,1))

    L = np.tril(A, -1)
    D = np.diag(np.diag(A))
    U = np.triu(A, 1)

    izq  = D + omega * L
    der = omega * U + (omega - 1) * D

    while k < mit:

        x_it = soltrinf(izq , omega * b - (der @ x))
        
        norm = np.linalg.norm(x_it - x, np.inf)
        if norm <= err:
            print("[ sor ] || x_it - x ||(inf) == {} <= {}\n".format(norm, err))
            return [x_it, k]
        x = x_it
        k += 1
    
    return [x, k]


A = np.array([
    [3.,1.,1.],
    [2.,6.,1.],
    [1.,1.,4.]])

b = np.array([5.0, 9.0, 6.0])
tol =  1e-5
mit = 30
x = sor(A, b, 1.5, tol, mit)
y = gseidel(A,b,tol,mit)
print(x)
print(y)
