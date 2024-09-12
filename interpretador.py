import json
import transform_data

#Carregar o arquivo JSON
with open('dados-BTC.json', 'r') as arquivo:
#Salva em dados
    dados = json.load(arquivo)

#Acessar a lista de dados no campo 'Data' do JSON
#Forma esquisita de armazenar, porem lista_dados
#é a lista de interesse que contém os valores que precisamos
lista_dados = dados['Data']['Data']

#exemplo


