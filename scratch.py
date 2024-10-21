import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import BoundaryNorm
from matplotlib import cm

# Gerar a grade
x = np.linspace(0, 1, 100)
y = np.linspace(0, 1, 100)
X, Y = np.meshgrid(x, y)

# Ajustar Z para ser uma célula menor
Z = np.sin(2 * np.pi * X[:-1, :-1]) * np.sin(2 * np.pi * Y[:-1, :-1])

# Definir os limites dos intervalos e as cores associadas
intervals = [-1, -0.5, 0, 0.5, 1]  # Intervalos de valores
colors = ['blue', 'green', 'yellow', 'red']  # Cores para cada intervalo

# Criar o colormap e normalizador para mudanças bruscas
cmap = cm.get_cmap('RdYlBu', len(colors))  # Colormap com o número de cores desejado
norm = BoundaryNorm(intervals, cmap.N)  # Normalizador com limites bruscos

# Plotar o gráfico com mudanças bruscas de cor
plt.pcolormesh(X, Y, Z, cmap=cmap, norm=norm, shading='flat')

# Adicionar barra de cores com os intervalos
plt.colorbar(boundaries=intervals, ticks=[-1, -0.5, 0, 0.5, 1])

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Gráfico com Mudanças Bruscas de Cor')
plt.show()
