from analise_BTC import preco_close_BTC, preco_open_BTC, data_BTC
import numpy as np
import matplotlib.pyplot as plt
import previsoes

rsi_indice = previsoes.rsi(preco_open_BTC,preco_close_BTC,14)
#o rsi começa após 13 dias

preco_abertura = preco_open_BTC[13:] 
preco_fechamento = preco_close_BTC[13:] 

tempo = 1

bom_long = 0
ruim_long = 0
bom_short = 0
ruim_short = 0

patrimonio = 1000

for i in range(len(rsi_indice)):
    if rsi_indice[i] < 30:
        #short
        if preco_close_BTC[i + tempo] - preco_close_BTC[i] < 0:
            bom_short += 1
            #print(data_BTC[i], "bom")
            patrimonio = (patrimonio * preco_close_BTC[i + tempo]) / preco_close_BTC[i]
            #caiu, ganhei
        else:
            ruim_short += 1
            #print(data_BTC[i], "ruim")
            patrimonio = (patrimonio * preco_close_BTC[i + tempo]) / preco_close_BTC[i]
            #subiu, perdi
    if rsi_indice[i] > 70:
        #long
        if preco_close_BTC[i + tempo] - preco_close_BTC[i] > 0:
            bom_long += 1
            #print(data_BTC[i], "bom")
            patrimonio = (patrimonio * preco_close_BTC[i + tempo]) / preco_close_BTC[i]
            #subiu, ganhei
        else:
            ruim_long += 1
            #print(data_BTC[i], "ruim") 
            patrimonio = (patrimonio * preco_close_BTC[i + tempo]) / preco_close_BTC[i]
            #caiu, perdi

total_short = bom_short + ruim_short
total_long = bom_long + ruim_long

print(f"Bom long: {bom_long}")
print(f"Ruim long: {ruim_long}")
print(f"Bom short: {bom_short}")
print(f"Ruim short: {ruim_short}")

print(patrimonio)
