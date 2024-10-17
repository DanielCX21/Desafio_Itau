import numpy as np

# Exemplo de matriz
matriz = np.array([[1, 5, 3], [8, 2, 6], [4, 7, 9]])

# Encontrar o valor máximo
max_valor = np.max(matriz)

# Encontrar o índice do valor máximo
indice_max = np.unravel_index(np.argmax(matriz), matriz.shape)

print(f"Valor máximo: {max_valor}")
print(f"Índice do valor máximo: {indice_max}")
