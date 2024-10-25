listas = [
    [(1, 2), (3, 4), (5, 6)],
    [(3, 4), (5, 6), (7, 8)],
    [(1, 2), (3, 4), (5, 6)]
]

# Converte as listas internas para conjuntos e faz a interseção entre eles
tuplas_comuns = set(listas[0]).intersection(*map(set, listas[1:]))

# Resultado como uma lista (opcional)
tuplas_comuns = list(tuplas_comuns)
print(tuplas_comuns)

