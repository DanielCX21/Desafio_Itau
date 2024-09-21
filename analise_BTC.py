import json
from dados import transform_data
import numpy as np
from scipy.interpolate import lagrange
import matplotlib.pyplot as plt

with open('dados/dados-BTC.json', 'r') as arquivo:
    dados = json.load(arquivo)

lista_dados = dados['Data']['Data']
#para criar algo sobre o momento da curva, vamos interpolar
#com os pontos pontos (x,y) conforme a curva for "se revelando"
#na troca de concavidade possivelmente será um ponto a ser 
#estudado
medo_BTC = list()
volume_to_BTC= list()
volume_from_BTC = list()
preco_open_BTC = list()
preco_close_BTC = list()
data_BTC = list()

for valor in lista_dados:
    medo_BTC.append(valor['fear_greed_value'] - 50)

for valor in lista_dados:
    volume_to_BTC.append(valor['volumeto'])

for valor in lista_dados:
    volume_from_BTC.append(valor['volumefrom'])

for valor in lista_dados:
    preco_open_BTC.append(valor['open'])

for valor in lista_dados:
    preco_close_BTC.append(valor['close'])

for valor in lista_dados:
    data = transform_data.unix_dh(valor['time'])
    data = data[:-9] 
    data_BTC.append(data)
