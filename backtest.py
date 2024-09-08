#pega uma base de dados e testa algo
import json

with open('dados_candles.json', 'r') as json_file:
    lista_dados = json.load(json_file)

dicionario_dados = {}

for candle in lista_dados:
    dicionario_dados[candle['data']] = {
        'open': candle['open'],
        'high': candle['high'],
        'low': candle['low'],
        'close': candle['close'],
        'volume': candle['volume']
    }
#esta armazenado em dicionario_dados
#testando algo simples

#iterando sobre o dicionário e calculando a diferença entre 'close' e 'open' 
#para ver se é maior que 10%
for data, candle in dicionario_dados.items():
    if candle['close'] > candle['open'] * 1.1:
        print(f"Data: {data}, o preço aumentou mais de 10%")

    if candle['close'] < candle['open'] * 0.9:
        print(f"Data: {data}, o preço caiu mais de 10%")
        