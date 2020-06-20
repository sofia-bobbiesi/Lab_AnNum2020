import scipy.linalg
import numpy as np

def soltrinf(A, b):
    n = A.shape[0]
    x = b

    for i in range(n):
        for j in range(i):
           x[i] = x[i] - A[i, j] * x[j]
        x[i] = x[i] / A[i, i]
    return x


def gseidel(A, b, err, mit):
    n = A.shape[0]
    k = 0
    x  = np.zeros((n, 1))
    while k < mit:
        x_it = np.zeros((n, 1))
        for i in range(n):
            s = 0
            for j in range(i):
                s = s + A[i, j] * x_it[j]
            for j in range(i+1, n):
                s = s + A[i, j] * x[j]

            x_it[i] = (b[i] - s) / A[i, i]

        #Ver si se acerca o no
        norm = np.linalg.norm(x_it - x, np.inf)
        if norm <= err:
            print("[ gseidel ]  x_it - x (inf) == {} <= {}\n".format(norm, err))
            return [x_it, k]
        #No se acerca, sigo iterando
        x = x_it
        k += 1

    return [x, k]



#[x,k] = gseidel(A, [1,2,3], 1e-2, 100)
#print([x,k])

import numpy as np 
import math 

#A = np.array([[3.0, 1.0, 0., 0., 0., 0., 0., 0., 0., 0.],[1.0, 3.0, 1.0, 0., 0., 0., 0., 0., 0., 0.], [0., 1.0, 3.0, 1.0, 0., 0., 0., 0., 0., 0.], [0., 0, 1.0, 3.0, 1.0, 0., 0., 0., 0., 0.], [0., 0., 0., 1.0, 3.0, 1.0, 0., 0., 0., 0.], [0., 0., 0., 0., 1.0, 3.0, 1.0, 0., 0., 0.], [0., 0., 0., 0., 0., 1.0, 3.0, 1.0, 0., 0.], [0., 0., 0., 0., 0., 0., 1.0, 3.0, 1.0, 0.], [0., 0., 0., 0., 0., 0., 0., 1.0, 3.0, 1.0], [0., 0., 0., 0., 0., 0., 0., 0., 1.0, 3.0]])
b = np.array([1.0, 2.0, 3.0])
tol =  10 ** (-15)
max_iter = 20
#w = 1.5

def sor(A, b, tol, max_iter, w): 
    if (w<=1 or w>2): 
        print('w should be inside [1, 2)')
        step = -1
        x = float('nan') 
        return x
    n = b.shape 
    x0 = np.zeros(n)
    x = x0 

    for step in range (1, max_iter): 
        for i in range(n[0]): 
            new_values_sum = np.dot(A[i, :i], x[:i])
            old_values_sum = np.dot(A[i, i+1 :], x0[ i+1: ]) 
            x[i] = (b[i] - (old_values_sum + new_values_sum)) / A[i, i] 
            x[i] = np.dot(x[i], w) + np.dot(x0[i], (1 - w))  
        #if (np.linalg.norm(x - x0) < tol): 
        if (np.linalg.norm(np.dot(A, x)-b ) < tol):
            print(step) 
            break 
        x0 = x

    print("X = {}".format(x)) 
    print("The number of iterations is: {}".format(step))
    return x


A = np.array([[3.,1.,1.],[0.,1.,0.],[0.,0.,1.]])
x = sor(A, b, tol, max_iter, 1.5)
print(np.dot(A, x))