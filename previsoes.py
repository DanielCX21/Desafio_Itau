import matplotlib.pyplot as plt
import analise_BTC
import numpy as np

periodo = 14

def rsi(abertura,fechamento,periodo):
    R_S_I = list()
    dias = 0
    for i in range(len(analise_BTC.data_BTC)):
        ganhos = 0
        perdas = 0
        dias += 1
        if dias < periodo:
            pass
        else:
            for j in range(periodo):
                if fechamento[i - j] > abertura[i - j]:
                    ganhos += np.fabs(fechamento[i - j] - abertura[i - j])
                else:
                    perdas += np.fabs(abertura[i - j] - fechamento[i - j]) 
            R_S = ganhos / perdas
            RSI_1 = (100 * R_S) / (1 + R_S)
            R_S_I.append(RSI_1) 
    return R_S_I
#len(R_S_I) = len(abertura) - periodo + 1

def sinal_compra_venda(RSI,data, periodo):
    #gera sinal de compra ou venda
    datas = data[periodo:]
    registros = []
    for i, dat in enumerate(datas):
        if RSI[i] > 70:
            registro = {"data" : dat, "sinal" : -1}
        if RSI[i] < 30:
            registro = {"data" : dat, "sinal" : 1}
        if RSI[i] >= 30 and RSI[i] <= 70:
            registro = {"data" : dat, "sinal" : 0}
        registros.append(registro)
    return registros

def previsao(inicio, timeframe, a, b, f, g, sinal):
    #ao ser acionado um inicio, devolvo a previsão do preço após
    #um "timeframe" específico
    #g - f será sempre menor que 1 e maior que -1
    #alfa e beta devem ser pequenos de modo que o preço não varie tanto
    if sinal == 0:
        pass
    else: 
        b = - b
        final = np.exp(b * timeframe)
        final = final * (g - f) * (a)
        final = 1 + final
        final = inicio * final
        return final



'''
RSI = rsi(analise_BTC.preco_open_BTC,analise_BTC.preco_close_BTC,periodo)
registros = sinal_compra_venda(RSI,analise_BTC.data_BTC,periodo)
for i in range(len(RSI)):
    print(registros[i])
    print(RSI[i])
'''

'''

RSI = rsi(analise_BTC.preco_open_BTC,analise_BTC.preco_close_BTC,periodo)

eixo_x = np.arange(0, 2002 - periodo)

plt.plot(eixo_x,RSI,color='red')
plt.grid(True)
plt.show()
'''