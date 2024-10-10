import json
import transform_data

nome_arquivo = 'dados_moedas/dados-BTC.json'

with open(nome_arquivo, 'r') as arquivo:
    dados = json.load(arquivo)

lista_dados = dados['Data']['Data']
medo = list()
volume_to= list()
volume_from = list()
preco_open = list()
preco_close = list()
preco_high = list()
preco_low = list()
data = list()

for valor in lista_dados:
    medo.append(valor['fear_greed_value'] - 50)

for valor in lista_dados:
    volume_to.append(valor['volumeto'])

for valor in lista_dados:
    volume_from.append(valor['volumefrom'])

for valor in lista_dados:
    preco_open.append(valor['open'])

for valor in lista_dados:
    preco_close.append(valor['close'])

for valor in lista_dados:
    preco_high.append(valor['high'])

for valor in lista_dados:
    preco_low.append(valor['low'])

for valor in lista_dados:
    dat = transform_data.unix_dh(valor['time'])
    dat = dat[:-9] 
    data.append(dat)

#Quantos dias passamos longe do neutro?
#Todas as listas tem 2001 elementos