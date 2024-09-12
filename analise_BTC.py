import json
import transform_data

with open('dados-BTC.json', 'r') as arquivo:
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
volume_BTC = list()
preco_open_BTC = list()
preco_close_BTC = list()
data_BTC = list()

for valor in lista_dados:
    medo_BTC.append(valor['fear_greed_value'])

for valor in lista_dados:
    volume_BTC.append(valor['volumeto'])

for valor in lista_dados:
    preco_open_BTC.append(valor['fear_greed_value'])

for valor in lista_dados:
    preco_close_BTC.append(valor['fear_greed_value'])

for valor in lista_dados:
    data_BTC.append(transform_data.unix_dh(valor['fear_greed_value']))


