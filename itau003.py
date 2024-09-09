import requests
import json

class CANDLES_DATA:
    def __init__(self, data, open, high, low, close, volume):
        self.data = str(data)
        self.open = float(open)
        self.high = float(high)
        self.low = float(low)
        self.close = float(close)
        self.volume = float(volume)

    def trans_json(self):
            return {
                'data': self.data,
                'open': self.open,
                'high': self.high,
                'low': self.low,
                'close': self.close,
                'volume': self.volume
            }

Lista_Dados = []

function = 'TIME_SERIES_DAILY'
symbol = input('Digite o simbolo da ação: ')
outputsize = input('Digite compact ou full: ')
apikey ='TJ9ACZBIZCVZPLZT'
urlMatriz = 'https://www.alphavantage.co/query?'

link = urlMatriz + 'function=' + function + "&symbol=" + symbol + '&outputsize=' + outputsize + '&apikey=' + apikey

web = requests.get(link)

#print(link,"\n")

if (web.status_code == 200):
    dados = web.json()

    if 'Time Series (Daily)' in dados:
        for chaves, valores in dados["Time Series (Daily)"].items():
            candle = CANDLES_DATA(
                data=chaves, 
                open=valores['1. open'], 
                high=valores['2. high'], 
                low=valores['3. low'], 
                close=valores['4. close'], 
                volume=valores['5. volume']
            )
            Lista_Dados.append(candle)
    else:
        print('ERRO AO ACESSAR TIME SERIES')
else:
    print('ERRO AO ACESSAR A API: ', web.status_code)

# Convertendo a lista de objetos para uma lista de dicionários
lista_dados_dict = [candle.trans_json() for candle in Lista_Dados]

with open('dados_candles.json', 'w') as json_file:
    json.dump(lista_dados_dict, json_file, indent=4)

print("Dados salvos em 'dados_candles.json'.")

#for o in Lista_Dados:
#    print('data: ', o.data, 'open: ', o.open, 'low: ', o.low, 'high: ', o.high , 'close: ', o.close)