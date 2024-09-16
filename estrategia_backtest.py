import analise_BTC
from math import fabs
from collections import Counter

patrimonio = 10000

patrimonios = list()
#teste de qual é a melhor massa

data = analise_BTC.data_BTC[1:-1]
vel = analise_BTC.der_seg_preco
medo = analise_BTC.medo_BTC[1:-1]

dados = analise_BTC.lista_dados

massas = list()

media = 0

for velw in vel:
    media += velw

media = int(media / len(vel))

for i in range(2,3):
    for j in range(len(data)):
        if fabs((i * medo[j]) - vel[j]) < media and medo[j] != 0:
            if medo[j] > 0:
                print(f"Venda: {data[j]}")
            else:
                print(f"Compra: {data[j]}")
