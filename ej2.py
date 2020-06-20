import numpy as np
import scipy.linalg as splinalg

def soltrinf(A, b):
    n = A.shape[0]
    x = b

    for idx in range(n):
        for jdx in range(idx):
           x[idx] = x[idx] - A[idx, jdx] * x[jdx]
        x[idx] = x[idx] / A[idx, idx]

    return x

#Ejercicio 2a

def gseidel(A,b,mit,err):
    n = A.shape[0]
    k = 0
    x = np.zeros((n, 1))
    while k < mit:
        x_it = np.zeros((n, 1))
        for i in range(n):
            s = 0
            for j in range(i):
                s +=  A[i, j] * x_it[j]
            for j in range(i+1, n):
                s +=  A[i, j] * x[j]

            x_it[i] = (b[i] - s) / A[i, i]

        #Compruebo si se acerca al resultado, sino, sigo iterando
        norm = np.linalg.norm(x_it - x, np.inf)
        if norm <= err:
            #print("[ gseidel ]  x_it - x (inf) == {} <= {}\n".format(norm, err))
            return [x_it, k]
        x = x_it
        k += 1
    return [x, k]


A1 = np.array([
    [3., 1., 1.],
    [2., 6., 1.],
    [1., 1., 4.]
])

b1 = np.array([
    [5],
    [9],
    [6]
])

print(gseidel(A1,b1,30,1e-5))

#Ejercicio 2b

def sor(A,b,omega,err,mit):
    return None