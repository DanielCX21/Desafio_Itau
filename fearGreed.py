import requests

feraAndgreed = requests.get('https://api.coin-stats.com/v2/fear-greed?type=all')

if (feraAndgreed.status_code == 200):
    print('aberta com sucesso!')
    feraGreed = feraAndgreed.json()