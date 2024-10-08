import dados
import funcoes

periodo = 14
rsi = funcoes.rsi(dados.preco_open,dados.preco_close,periodo)

def compra(data,data_inicial,preco_inicial,preco_maximo,previsao_final,previsao_parcial,patrimonio,timeframe):
    quantidade = patrimonio / preco_inicial
    for i in range(timeframe):
        if preco_maximo[i] > previsao_final:
            return data[i], quantidade*previsao_final
    

    return data_final, patrimonio

def backtest(timeframe, sinal, rsi):
#type(sinal) = list of dict
    patrimonio = 1000
    estou_comprado = False
    #manipular dentro da funcao
    for i, dicionario in sinal:
        if dicionario['sinal'] == 1 and not estou_comprado:
            estou_comprado = True
            #compra
        else:
            if dicionario['sinal'] == -1 and estou_comprado:
                pass
                #venda
            else:
                pass
                #passa
    return (primeiro_k,segundo_k,patrimonio)

#testar os 3 parametros:
#primeiro k (1e5)
#segundo k (1e5)
#timeframe (2 até 5)

for i in range(100000):
    #ajustar casas decimais dos k's
    i = i / 10000
    for j in range(100000):
        j = j / 10000
        for k in range(2,6):
            info = backtest(k,,rsi)

