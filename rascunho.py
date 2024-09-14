import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

x = np.array([1, 2, 3])
y = np.array([6, 2, 5.5])

cs = CubicSpline(x, y)

cs_deriv = cs.derivative()

x_plot = np.linspace(0, 2, 100)
y_plot = cs(x_plot)
y_deriv_plot = cs_deriv(x_plot)

plt.plot(x_plot, y_plot, label='Spline Cúbico')
plt.plot(x_plot, y_deriv_plot, label='Derivada do Spline', linestyle='--')
plt.scatter(x, y, color='red', label='Pontos Dados')

plt.legend()
plt.grid(True)
plt.title("Interpolação e Derivada do Spline Cúbico")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
