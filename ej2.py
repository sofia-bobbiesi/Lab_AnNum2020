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

def SOR(A,b,omega,err,mit):

#def SOR(A, b, x0, tol, max_iter, w): 
    if (omega<=1 or omega>2): 
        print('omega should be inside [1, 2)') 
        step = -1
        x = float('nan')
        return 
    n = b.shape 
    x0 = np.zeros(n)
    x = x0

    for step in range (1, mit): 
        for i in range(n[0]): 
            new_values_sum = np.dot(A[i, :i], x[:i])
            old_values_sum = np.dot(A[i, i+1 :], x0[ i+1: ]) 
            x[i] = (b[i] - (old_values_sum + new_values_sum)) / A[i, i] 
            x[i] = np.dot(x[i], omega) + np.dot(x0[i], (1 - omega))  

        if (np.linalg.norm(np.dot(A, x)-b ) < err):
            break 
        x0 = x

    #print("X = {}".format(x)) 
    #print("The number of iterations is: {}".format(step))
    return [x,step]
x = SOR(A1, b1, 1.6, 1e-1, 30)
print(x)
#print(np.dot(A1, x))