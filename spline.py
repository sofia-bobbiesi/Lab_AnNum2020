from scipy.interpolate import interp1d
import numpy as np
import matplotlib.pyplot as plt
x = [0.0, 0.22, 0.85, 1.0, 1.5, 1.6, 1.99]
y = [0.0, 0.1, -0.15, -0.03, 0.75, -0.3, 0.01]
xnew = np.linspace(0, 1.99, num=40, endpoint=True)
f = interp1d(x,y, kind='cubic')
plt.plot(x, y, 'o', xnew, f(xnew), '-')
plt.legend(['data', 'cubic'], loc='best')
plt.show()


def spline_velocidad():
    
    return None