import numpy as np

def soltrinf(A, b):
    n = A.shape[0]
    x = b

    for i in range(n):
        for j in range(i):
           x[i] = x[i] - A[i, j] * x[j]
        x[i] = x[i] / A[i, i]

    return x

#Ejercicio 2a

def gseidel(A,b,mit,err):
    n = A.shape[0]
    k = 0
    x = np.zeros((n, 1))
    
    A_LD = np.tril(A)
    A_U  = np.triu(A, 1)

    while k < mit:

        x_it = soltrinf(A_LD, b - (A_U @ x))
        #Check if it comes close to the result, otherwise, keep iterating
        norm = np.linalg.norm(x_it - x, np.inf)
        if norm <= err:
            print("[ gseidel ] || x_it - x ||(inf) == {} <= {}\n".format(norm, err))
            return [x_it, k]
        x = x_it
        k += 1
    
    return [x, k]

#Ejercicio 2b

def SOR(A,b,omega,err,mit):
    if (omega<=1): 
        print('omega must be greater than 1 \n') 
        k = -1
        x = float('nan')
        return 

    n = A.shape[0]
    k = 0
    x = np.zeros((n,1))

    A_L = np.tril(A, -1)
    A_D = np.diag(np.diag(A))
    A_U = np.triu(A, 1)

    left  = A_D + omega * A_L
    right = omega * A_U + (omega - 1) * A_D

    while k < mit:

        x_it = soltrinf(left , omega * b - (right @ x))
        #Check if it comes close to the result, otherwise, keep iterating
        norm = np.linalg.norm(x_it - x, np.inf)
        if norm <= err:
            print("[ sor ] || x_it - x ||(inf) == {} <= {}\n".format(norm, err))
            return [x_it, k]
        x = x_it
        k += 1
    
    return [x, k]