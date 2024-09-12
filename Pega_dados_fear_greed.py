import requests
import json
from datetime import datetime, timezone
import transform_data

lista = []
linkMatriz = "https://min-api.cryptocompare.com/data/v2/histoday?"
fsym = "BTC"
tsym = "USD"
limit = 2000
toTs_unix = transform_data.dh_unix("11/09/2024")
link = linkMatriz + "fsym=" + fsym + "&" + "tsym=" + tsym + "&" + "limit=" + str(limit) + "&" + "toTs=" + str(toTs_unix)
#print(link)

web = requests.get(link)

fearAndgreed = requests.get('https://api.coin-stats.com/v2/fear-greed?type=all')

if fearAndgreed.status_code == 200:
    print('Fear and Greed data aberta com sucesso!')
    fearGreed = fearAndgreed.json()
else:
    print('Erro ao abrir Fear and Greed')

if web.status_code == 200:
    print('API de preços aberta com sucesso!')
    dados = web.json()  

    menor_timestamp = min([item['time'] for item in dados['Data']['Data']])
    menor_data = datetime.fromtimestamp(menor_timestamp, tz=timezone.utc).strftime('%Y-%m-%d')

    print(f'Usando a menor data encontrada: {menor_data}')
    timestamp_inicio = menor_timestamp

    for index in dados['Data']['Data']:
        unix_time = index['time']
        
        if unix_time >= timestamp_inicio:
            
            for fg in fearGreed['data']:
                if int(fg['timestamp']) == unix_time:
                    index['fear_greed_value'] = int(fg['value'])  
                    index['fear_greed_classification'] = fg['value_classification'] 
                    break
        
        lista.append(index)
    
    with open(f'dados-{fsym}.json', 'w') as json_file:
        json.dump(dados, json_file, indent=4)

    print(f'Dados filtrados e salvos em dados-{fsym}.json.')
else:
    print('Erro ao abrir API de preços')
