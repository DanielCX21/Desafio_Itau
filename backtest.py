import dados
import funcoes
import numpy as np

periodo = 14
rsi = funcoes.rsi(dados.preco_open,dados.preco_close,periodo)

#ajustar as ordens(logica), as variaveis(correcao macaco) e diminuir as linhas com as condições equivalentes!
def compra(data,data_inicial,preco_inicial,preco_abertura,preco_close,preco_maximo,preco_minimo,previsao_final,previsao_parcial,patrimonio,timeframe, parametro_teste):
    quantidade = patrimonio / preco_inicial
    index_data = data.index(data_inicial)
    patrimonio_final = patrimonio
    vendi_parcial = False
    for i in range(timeframe): #saida parcial
        if preco_maximo[index_data + i + 1] > previsao_parcial:
            patrimonio_final += (parametro_teste *previsao_parcial * quantidade) 
            vendi_parcial = True
            break
    for i in range(timeframe): #data e preço precisam estar em fase!
        if preco_maximo[index_data + i + 1] > previsao_final:
            patrimonio_final += ((1 - parametro_teste) * previsao_final * quantidade)
            return data[index_data + i + 1], patrimonio_final
            #saida total
    #agora vamos tratar da parte em que não foi atingido o preço final!
    if preco_abertura[index_data + timeframe] < previsao_parcial and preco_maximo[index_data + timeframe] > previsao_parcial and preco_close[index_data + timeframe] < previsao_final and vendi_parcial:
        #com certeza ja vendi parcial nesse caso!
        #somente essa possibilidade
        patrimonio_final += ((1 - parametro_teste) * previsao_parcial * quantidade)
        return data[index_data + timeframe], patrimonio_final
    ###########################################
    #começo o ultimo dia menor que prev parcial
    ###########################################
    if preco_abertura[index_data + timeframe] < previsao_parcial and preco_maximo[index_data + timeframe] > previsao_parcial and preco_minimo[index_data + timeframe] > previsao_parcial and vendi_parcial:
        #com certeza ja vendi parcial nesse caso!
        #subiu e continuou em cima
        #somente essa possibilidade
        patrimonio_final += ((1 - parametro_teste) * previsao_parcial * quantidade)
        return data[index_data + timeframe], patrimonio_final
    #nao chego a atingir a prev parcial no ultimo dia => saio perdendo ou ganhando(?) já atingi parcial ou não(?) => 4 possibilidades
    #detalhe para refatoração: reduzir os 4 casos em 2 (é possível!)
    if preco_abertura < previsao_parcial and preco_maximo < previsao_parcial and vendi_parcial and preco_close[index_data + timeframe] < preco_inicial[index_data + timeframe]:
    #vendi parcial e perdi
        patrimonio_final -= (1 - parametro_teste) * quantidade * np.fabs(preco_close[index_data + timeframe] - preco_inicial[index_data + timeframe])
        return data[index_data + timeframe], patrimonio_final
    if preco_abertura < previsao_parcial and preco_maximo < previsao_parcial and vendi_parcial and preco_close[index_data + timeframe] > preco_inicial[index_data + timeframe]:
    #vendi parcial e nao perdi
        patrimonio_final += (1 - parametro_teste) * quantidade * np.fabs(preco_close[index_data + timeframe] - preco_inicial[index_data + timeframe])
        return data[index_data + timeframe], patrimonio_final
    if preco_abertura < previsao_parcial and preco_maximo < previsao_parcial and not vendi_parcial and preco_close[index_data + timeframe] < preco_inicial[index_data + timeframe]:
    #nao vendi e nao perdi
        return data[index_data + timeframe], quantidade*preco_close[index_data + timeframe]
    if preco_abertura < previsao_parcial and preco_maximo < previsao_parcial and not vendi_parcial and preco_close[index_data + timeframe] > preco_inicial[index_data + timeframe]:
    #nao vendi e perdi
        return data[index_data + timeframe], quantidade*preco_close[index_data + timeframe]
    #subo e vou cair agora:
    if preco_abertura < previsao_parcial and preco_maximo > previsao_parcial and preco_minimo < previsao_parcial and vendi_parcial:
        patrimonio_final += ((1 - parametro_teste) * previsao_parcial * quantidade)
        return data[index_data + timeframe], patrimonio_final
#espelhar para o short e ajustar para inserção de parametros "aleatorios"!


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

