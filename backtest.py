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

patrimonio = float(1000)

patrimonio_inicial = patrimonio

comprado = False

contador = 0

sinal_compra = 0
sinal_venda = 0

quantidade = 0

compras = 0

vendas = 0

patrimonio_contabilizado = list()

for data, candle in reversed(list(dicionario_dados.items())):

    sinal_compra = funcoes.gerar_sinal_compra(candle) 
    sinal_venda = funcoes.gerar_sinal_venda(candle)

    patrimonio_contabilizado.append(patrimonio)

    if sinal_compra == 1 and not comprado:
        comprado = True
        compras += 1
        print(f"{data}: compra")
        quantidade = patrimonio / candle['close']

    if sinal_venda == -1 and comprado:
        comprado = False
        vendas += 1
        patrimonio = quantidade * candle['close']
        print(f"{data}: Vende: {patrimonio}") 

    if comprado:
        contador += 1

    if contador % 15 == 0 and contador > 14 and quantidade * candle['close'] > patrimonio and comprado:
        comprado = False
        vendas += 1
        patrimonio = quantidade * candle['close']
        print(f"{data}: Vende: {patrimonio} no lucro após 15 dias") 

    if contador % 30 == 0 and contador > 29 and comprado:
        comprado = False
        vendas += 1
        patrimonio = quantidade * candle['close']
        print(f"{data}: Vende: {patrimonio} no prejuizo após 30 dias") 

print(f"o patrimonio é {patrimonio}")

print(f"Foram feitas {compras + vendas} operações")
