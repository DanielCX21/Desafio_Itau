import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
from analise_BTC import lista_dados
import transform_data

def plotar_grafico(datas, valores, preco):
    # Converter datas para objetos datetime se necessário
    if isinstance(datas[0], str):
        datas = [datetime.datetime.strptime(data, '%d/%m/%Y %H:%M:%S') for data in datas]

    # Criar o gráfico
    plt.figure(figsize=(12, 6))
    plt.plot(datas, valores, marker='', linestyle='-', color='red')
    #plt.plot(datas, preco, marker='', linestyle='-', color='green')


    # Adicionar título e rótulos
    plt.title('Gráfico de medo e ganância')
    plt.xlabel('Data')
    plt.ylabel('Valor')

    # Definir formato do eixo x
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))

    # Marcar apenas a primeira e a última data
    primeira_data = datas[0]
    ultima_data = datas[-1]
    plt.gca().set_xticks([primeira_data, ultima_data])

    # Adicionar uma grade e mostrar o gráfico
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Exemplo de uso com vetores específicos:

datas_graf = list()
medo_graf = list()
preco_fec = list()
vol = list()

for BTC in lista_dados:
    datas_graf.append(transform_data.unix_dh(BTC['time']))
    medo_graf.append(BTC['fear_greed_value'])
    preco_fec.append(BTC['close'])

plotar_grafico(datas_graf, medo_graf, preco_fec)
