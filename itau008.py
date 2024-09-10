import requests
import json
from datetime import datetime, timezone

lista = []
linkMatriz = "https://min-api.cryptocompare.com/data/v2/histoday?"

# Parâmetros
fsym = input('Símbolo da criptomoeda. Exemplo: BTC: ') 
tsym = input('Moeda de conversão. Exemplo: USD: ') 
limit = input('Número de dias/candles que você deseja. Exemplo: 2000: ')

# Receber a data no formato AAAA-MM-DD e convertê-la para Unix timestamp
toTs_str = input('Data final (toTs) no formato AAAA-MM-DD: ')
toTs_dt = datetime.strptime(toTs_str, '%Y-%m-%d')
toTs_unix = int(toTs_dt.replace(tzinfo=timezone.utc).timestamp())  # Converter para Unix timestamp

# Link concatenado
link = linkMatriz + "fsym=" + fsym + "&" + "tsym=" + tsym + "&" + "limit=" + limit + "&" + "toTs=" + str(toTs_unix)

print(link)

# Solicitação de dados de preço
web = requests.get(link)

# Solicitação de dados Fear and Greed
feraAndgreed = requests.get('https://api.coin-stats.com/v2/fear-greed?type=all')

# Tratamento de erros para feraAndgreed
if feraAndgreed.status_code == 200:
    print('Fear and Greed data aberta com sucesso!')
    feraGreed = feraAndgreed.json()
else:
    print('Erro ao abrir Fear and Greed')

# Tratamento de erros para web
if web.status_code == 200:
    print('API de preços aberta com sucesso!')
    dados = web.json()
    
    # Encontrar a menor data (timestamp) em dados
    menor_timestamp = min([item['time'] for item in dados['Data']['Data']])
    
    # Exibir a data correspondente ao menor timestamp (com fuso horário UTC)
    menor_data = datetime.fromtimestamp(menor_timestamp, tz=timezone.utc).strftime('%Y-%m-%d')
    print(f'Usando a menor data encontrada: {menor_data}')
    
    # Utilizar a menor data como timestamp de início
    timestamp_inicio = menor_timestamp
    
    # Iterar sobre os dados de preços e adicionar Fear and Greed
    for index in dados['Data']['Data']:
        unix_time = index['time']
        
        # Verificar se o timestamp é maior ou igual ao timestamp de início
        if unix_time >= timestamp_inicio:
            
            # Verificar se a data em unix bate com as chaves de feraGreed
            for fg in feraGreed['data']:
                if int(fg['timestamp']) == unix_time:
                    index['fear_greed_value'] = int(fg['value'])  # Transformar o valor do índice de Fear and Greed em inteiro
                    index['fear_greed_classification'] = fg['value_classification']  # Adiciona a classificação (Fear, Extreme Fear, etc.)
                    break
        
        lista.append(index)
    
    # SALVA EM UM ARQUIVO
    with open(f'dados-{fsym}.json', 'w') as json_file:
        json.dump(dados, json_file, indent=4)

    print(f'Dados filtrados e salvos em dados-{fsym}.json.')
else:
    print('Erro ao abrir API de preços')
