import requests
import json

lista = []
linkMatriz = "https://min-api.cryptocompare.com/data/v2/histoday?"

#parametros

fsym = input('Simbolo da criptomoeda. Exemplo: BTC: ') 
tsym = input('Moeda de conversão. Exemplo: USD: ') 
limit = input('Número de dias/candles que você deseja. Exemplo: 2000: ')
toTs = input('Unix timestamp para limitar até uma data específica. Exemplo: 1609459200 (que representa 1º de janeiro de 2021): ')

#link concatenado

link = linkMatriz + "fsym=" + fsym + "&" + "tsym=" + tsym + "&" + "limit=" + limit + "&" + "toTs=" + toTs

print(link)

web = requests.get(link)

#tratamento de erros

if (web.status_code == 200):
    print('aberta com sucesso!')
    dados = web.json()
    #SALVA EM UM ARQUIVO
    with open(f'dados-{fsym}.json', 'w') as json_file:
        json.dump(dados, json_file, indent=4)

    for index in dados['Data']['Data']:
        lista.append(index)
else:
    print('erro ao abrir ')
import requests
import json

lista = []
linkMatriz = "https://min-api.cryptocompare.com/data/v2/histoday?"

#parametros


fsym = input('Simbolo da criptomoeda. Exemplo: BTC: ') 
tsym = input('Moeda de conversão. Exemplo: USD: ') 
limit = input('Número de dias/candles que você deseja. Exemplo: 2000: ')
toTs = input('Unix timestamp para limitar até uma data específica. Exemplo: 1609459200 (que representa 1º de janeiro de 2021): ')

#link concatenado

link = linkMatriz + "fsym=" + fsym + "&" + "tsym=" + tsym + "&" + "limit=" + limit + "&" + "toTs=" + toTs

print(link)

web = requests.get(link)



#tratamento de erros

if (web.status_code == 200):
    print('aberta com sucesso!')
    dados = web.json()
    #SALVA EM UM ARQUIVO
    with open(f'dados-{fsym}.json', 'w') as json_file:
        json.dump(dados, json_file, indent=4)

    for index in dados['Data']['Data']:
        lista.append(index)
else:
    print('erro ao abrir ')


