import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3])  # Valores x dos pontos
y = np.array([2, 3, 5])  # Valores y correspondentes

polinomio = np.polyfit(x, y, 2)

x_novo = np.linspace(min(x), max(x), 100)
y_novo = np.polyval(polinomio, x_novo)

derivada = np.polyder(polinomio)

y_derivada = np.polyval(derivada, x_novo)

print(f'Coeficientes do polinômio: {polinomio}')
print(f'Coeficientes da derivada: {derivada}')
