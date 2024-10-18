data = [9,8,7,6,5,4,3,2,1]

vetor = [1,2,3,4,5,6,7,8,9]

parametro = 5

inicio_index = int((parametro + 1) / 2) - 1
fim_index = int(((2 * len(data)) - 1 - parametro) / 2) + 1

#ja sei q é inteiro

print(vetor)

vetor = vetor[inicio_index:fim_index]

print(vetor)
