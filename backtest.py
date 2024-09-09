#pega uma base de dados e testa algo
import json
import funcoes

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

patrimonio = float(1000)

comprado = False

contador = 0

sinal_compra = 0
sinal_venda = 0

quantidade = 0

for data, candle in dicionario_dados.items():

    sinal_compra = funcoes.gerar_sinal_compra(candle) 
    sinal_venda = funcoes.gerar_sinal_venda(candle)

    if sinal_compra == 1 and not comprado:
        comprado = True
        print(f"{data}: compra")
        quantidade = patrimonio / candle['close']

    if sinal_venda == -1 and comprado:
        comprado = False
        print(f"{data}: Vende") 
        patrimonio = quantidade * candle['close']

    if comprado:
        contador += 1

    if contador % 15 == 0 and contador > 14 and quantidade * candle['close'] > patrimonio:
        comprado = False
        patrimonio = quantidade * candle['close']

    if contador % 30 == 0 and contador > 29:
        comprado = False
        patrimonio = quantidade * candle['close']

print(f"o patrimonio é {patrimonio}")
