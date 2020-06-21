import numpy as np
import scipy.linalg as splinalg

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
    n, _ = A.shape
    bb = b.copy()
    if bb.shape == (n,1):
        bb = bb.reshape(n)

    k = 0
    x = np.zeros((n, 1))
    
    A_LD = np.tril(A)
    A_U  = np.triu(A, 1)

    while k < mit:

        x_it = soltrinf(A_LD, bb - (A_U @ x))
        #Compruebo si se acerca al resultado, sino, sigo iterando
        norm = np.linalg.norm(x_it - x, np.inf)
        if norm <= err:
            #print("[ gseidel ] || x_it - x ||(inf) == {} <= {}\n".format(norm, err))
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
    [5.],
    [9.],
    [6.]
])

print("gseideal solution:")
print(gseidel(A1,b1,30,1e-5),"\n")


#Ejercicio 2b

def SOR(A,b,omega,err,mit):
    if (omega<=1 or omega>=2): 
        print('omega should be inside (1, 2)') 
        k = -1
        x = float('nan')
        return 
    n = b.shape 
    x0 = np.zeros(n)
    x = x0

    for k in range (1, mit): 
        for i in range(n[0]): 
            new_values_sum = np.dot(A[i, :i], x[:i])
            old_values_sum = np.dot(A[i, i+1 :], x0[ i+1: ]) 
            x[i] = (b[i] - (old_values_sum + new_values_sum)) / A[i, i] 
            x[i] = np.dot(x[i], omega) + np.dot(x0[i], (1 - omega))  

        if (np.linalg.norm(np.dot(A, x)-b ) < err):
            break 
        x0 = x
    return [x,k]

print("SOR solution:")
x = SOR(A1, b1, 2, 1, 30)
print(x)