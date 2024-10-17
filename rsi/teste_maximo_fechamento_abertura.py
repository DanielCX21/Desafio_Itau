import dados
from numpy import fabs
import transform_data

#ajuste o parametro para sabermos em quais são os dias que fazemos más vendas 
#em caso de long e más compras em caso de short!

parametro = 0

for i in range(len(dados.lista_dados)):
    if fabs(dados.preco_close[i] - dados.preco_high[i]) <= dados.preco_high[i] * parametro:
        print(f"{transform_data.dh_unix(dados.data[i])} ruim.")
    if fabs(dados.preco_open[i] - dados.preco_high[i]) <= dados.preco_high[i] * parametro:
        print(f"{transform_data.dh_unix(dados.data[i])} ruim.")
    if fabs(dados.preco_close[i] - dados.preco_low[i]) <= dados.preco_low[i] * parametro:
        print(f"{transform_data.dh_unix(dados.data[i])} ruim.")
    if fabs(dados.preco_open[i] - dados.preco_low[i]) <= dados.preco_low[i] * parametro:
        print(f"{transform_data.dh_unix(dados.data[i])} ruim.")
    
