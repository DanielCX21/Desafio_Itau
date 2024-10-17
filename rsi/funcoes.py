import numpy as np

def relativestr(abertura,fechamento,periodo):
    R_S_I = list()
    dias = 0
    for i in range(len(abertura)):
        ganhos = 0
        perdas = 0
        dias += 1
        if dias < periodo:
            continue
        else:
            for j in range(periodo):
                dif = fechamento[i - j] - abertura[i - j]
                if dif > 0:
                    ganhos += np.fabs(dif)
                else:
                    perdas += np.fabs(dif) 
            R_S = ganhos / perdas
            RSI_1 = 100 - (100 / (1 + R_S))
            RSI_1 = float(RSI_1)
            R_S_I.append(RSI_1) 
    return R_S_I
#len(R_S_I) = len(abertura) - periodo + 1

def stochastic_rsi(rsi,periodo):
    rsi_stochastic = list()
    for i in range(len(rsi) - periodo):
        base = rsi[i:i + periodo]
        maximo = max(base)
        minimo = min(base)
        param = (base[-1] - minimo) / (maximo - minimo)
        param = param * 100
        rsi_stochastic.append(param)
    return rsi_stochastic
#len(rsi_stochastic) = len(rsi) - 14

def sinal_compra_venda_rsi(RSI,data,periodo):
    datas = data[periodo:]
    registros = []
    for i, dat in enumerate(datas):
        if float(RSI[i]) > 70:
            dicionario = {"data": dat, "sinal": 1}
        else:
            if float(RSI[i]) < 30:
                dicionario = {"data" : dat, "sinal" : -1}
            else:
                dicionario = {"data" : dat, "sinal" : 0}
        registros.append(dicionario)
    return registros
#len(registros) = 1987

def previsao_primeira(inicio, timeframe, a, b, f, g, sinal):
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

def previsao_segunda(inicio, timeframe, indice, parametro, parametro_segundo):
    indice += 50
    preco_final = inicio * np.exp(parametro * timeframe / indice)
    margem = (preco_final - inicio) * parametro_segundo
    return (preco_final,margem)
