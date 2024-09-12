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
