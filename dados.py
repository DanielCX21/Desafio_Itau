import json
import transform_data

nome_arquivo = 'dados_moedas/dados-SOL.json'

nome_arquivo_apoio = 'dados_moedas/dados-BTC.json'

if nome_arquivo == 'dados_moedas/dados-BTC.json':
    with open(nome_arquivo, 'r') as arquivo:
        dados = json.load(arquivo)
else:
    with open(nome_arquivo, 'r') as arquivo:
        dados = json.load(arquivo)
    with open(nome_arquivo_apoio, 'r') as arquivo_apoio:
        dados_apoio = json.load(arquivo_apoio)
        lista_dados_apoio = dados_apoio['Data']['Data']

lista_dados = dados['Data']['Data']
medo = list()
volume_to= list()
volume_from = list()
preco_open = list()
preco_close = list()
preco_high = list()
preco_low = list()
data = list()

data_inicio = lista_dados[0]['time']
data_final = lista_dados[-1]['time']


for i, valor in enumerate(lista_dados):
    if "fear_greed_value" in valor:
        medo.append(valor["fear_greed_value"] - 50)
    else:
        medo.append(lista_dados_apoio[i]["fear_greed_value"] - 50)

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
