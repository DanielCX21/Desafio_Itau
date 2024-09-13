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

medo_BTC_norm = list()
volume_BTC = list()
preco_open_BTC = list()
preco_close_BTC = list()
data_BTC = list()
media = 0

for valor in lista_dados:
    media += valor['fear_greed_value']

media = media
media = media / len(lista_dados)
media = int(media)

for valor in lista_dados:
    medo_BTC_norm.append(valor['fear_greed_value'] - media)

#ou...
"""
for valor in lista_dados:
    medo_BTC_norm.append(valor['fear_greed_value'])
"""

for valor in lista_dados:
    volume_BTC.append(valor['volumeto'] - media)

for valor in lista_dados:
    preco_open_BTC.append(valor['fear_greed_value'])

for valor in lista_dados:
    preco_close_BTC.append(valor['fear_greed_value'])

for valor in lista_dados:
    data_BTC.append(transform_data.unix_dh(valor['fear_greed_value']))

def der(medo):
    der_medos = list()
    for i in range(len(medo) - 1):
        der_medos.append(medo[i + 1] - medo[i])
    return der_medos

def seg_der(der_medo):
    seg_der_medos = list()
    for i in range(len(der_medo) - 1):
        seg_der_medos.append(der_medo[i + 1] - der_medo[i])
    return seg_der_medos

print(media)
print(medo_BTC_norm)

def sinal_compra(mas1, mas2, vel1, vel2):
    if vel1 > 0 and vel2 > 0:
        if (mas1 * vel1 - mas2 * vel2) == 0:
            return 1
    else:
        return 0

def sinal_venda(mas1, mas2, vel1, vel2):
    if vel1 < 0 and vel2 < 0:
        if (mas1 * vel1 - mas2 * vel2) == 0:
            return -1
    else:
        return 0

