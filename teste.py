import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definindo a função f(x, y)
def f(x, y):
    return np.sin(np.sqrt(x**2 + y**2))

# Criando a grade de pontos (x, y)
x = np.linspace(-5, 5, 100)  # 100 pontos no intervalo [-5, 5]
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)      # Criar a malha de coordenadas
Z = f(X, Y)                   # Avaliar a função em cada ponto da malha

# Criando a figura e o eixo 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plotar a superfície 3D
ax.plot_surface(X, Y, Z, cmap='viridis')

# Adicionando rótulos aos eixos
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('f(X, Y)')

# Exibir o gráfico
plt.show()
