from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

x = [0.0, 0.22, 0.85, 1.0, 1.5, 1.6, 1.99]
y = [0.0, 0.1, -0.15, -0.03, 0.75, -0.3, 0.01]
f = interp1d(x,y, kind='cubic')
plt.plot(x, y, 'o', x, f(x), '-')
plt.legend(['data', 'cubic'], loc='best')
plt.show()

def spline_velocidad(ts,vs):
    return None
