import numpy as np
import matplotlib.pyplot as plt
import json
import transform_data

nome_arquivo = 'dados_moedas\dados-BTC.json'

with open(nome_arquivo, 'r') as arquivo:
    dados = json.load(arquivo)

lista_dados = dados['Data']['Data']

#print(len(lista_dados))

x = 50

#for i in range(x,x + 50):
    #print(i)
    #print(lista_dados[i]['fear_greed_value'])

print(lista_dados[72]['time'])
