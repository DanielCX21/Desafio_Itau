import json
from dados import transform_data
import numpy as np
from scipy.interpolate import lagrange
#import matplotlib.pyplot as plt

with open('dados/dados-BTC.json', 'r') as arquivo:
    dados = json.load(arquivo)

#Acessar a lista de dados no campo 'Data' do JSON
#Forma esquisita de armazenar, porem lista_dados
#é a lista de interesse que contém os valores que precisamos
lista_dados = dados['Data']['Data']
#vamos criar um vetor com as datas
#preciso somente desse arquivo para 
#me dar as informações nescessarias

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
media = 0

for valor in lista_dados:
    media += valor['fear_greed_value']

media = media
media = media / len(lista_dados)
media = int(media)

#for valor in lista_dados:
#    medo_BTC.append(valor['fear_greed_value'] - media)

#ou...

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

der_seg_preco = list()

for i in range(1, len(medo_BTC) - 1):
    x = np.array([i - 1,i,i + 1])
    y = np.array([preco_close_BTC[i - 1],
                  preco_close_BTC[i],
                  preco_close_BTC[i + 1]])
    interpol = lagrange(x, y)
    interpol = interpol.deriv()
    #interpol = interpol.deriv()
    der_seg_preco.append(int(interpol(i)))
#tenho uma lista com todas as segundas derivadas do preco

eixo_x = list()

for i in range(len(medo_BTC) - 2):
    eixo_x.append(i)

'''
plt.plot(eixo_x,der_seg_preco,color='blue')
plt.plot(data_BTC,medo_BTC,color='red')
primeira_data = data_BTC[0]
ultima_data = data_BTC[-1]
plt.gca().set_xticks([primeira_data, ultima_data])
plt.show() 
'''