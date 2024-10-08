import funcoes
import dados
import numpy as np
import matplotlib.pyplot as plt

periodo = 14
rsi = funcoes.relativestr(dados.preco_open,dados.preco_close,periodo)

#print(len(rsi)) = 1988
#print(len(dados.data[periodo - 1:])) = 1988

estou_comprado = False
patrimonio_inicial = 1000
patrimonio = patrimonio_inicial
parametro1 = 0.1

for i, data in enumerate(dados.data[(periodo - 1):]):
    if rsi[i] > 70 and not estou_comprado:
        #força compradora -> compro LONG!
        estou_comprado = True
        quantidade = patrimonio / dados.preco_close[i]
        previsao = dados.preco_close[i] * np.exp(parametro1 / (dados.medo[i] + 50))

