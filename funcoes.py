import numpy as np

def media(vetor):
    if len(vetor) == 0:
        return 0
    else:
        med = 0
        for valor in vetor:
            med += valor
        return (med / (len(vetor)))
def compras_long(situacao,patrimonio, preco):
    quantidade = patrimonio / preco
    situacao = True
    tupla = (situacao,quantidade)
    return tupla
def vendas_long(situacao,quantidade, preco):
    patrimonio_final = quantidade * preco
    situacao = False
    tupla = (situacao,patrimonio_final)
    return tupla
def backtest(timeframe,situacao_long,angulo, param1, param2, medo, patrimonio,preco):
    medo_inicial = 0
    contador = 0
    ganhei = 0
    perdi = 0
    translacao = timeframe - 1
    patrimonios = [1,1]
    perdas = list()
    ganhos = list()
    for i in range(len(medo) - translacao):
        if not situacao_long and angulo[i] < (90 * param1) and medo[i + translacao] > medo_inicial:
            #compra long!
            situacao_long, quantidade = compras_long(situacao_long,patrimonio,preco[i + translacao])
            #print(f"LONG:Comprei por {preco[i + translacao]}")
        if situacao_long and angulo[i] < (90 * param2) and medo[i + translacao] <  -medo_inicial:
            #venda long!
            situacao_long, patrimonio = vendas_long(situacao_long,quantidade,preco[i + translacao])
            contador += 1
            #print(f"LONG:Vendi por {preco[i + translacao]}")
            patrimonios[0] = patrimonios[1]
            patrimonios[1] = patrimonio
            if patrimonios[1] < patrimonios[0]:
                perda_percentual = (patrimonios[0] - patrimonios[1]) / patrimonios[0]
                perdas.append(perda_percentual)
                ganhei += 1
            if patrimonios[1] > patrimonios[0]:
                ganho_percentual = (patrimonios[1] - patrimonios[0]) / patrimonios[0]
                ganhos.append(ganho_percentual)
                perdi += 1
    if situacao_long:
        patrimonio = quantidade * preco[-1]
        contador += 1
        patrimonios[0] = patrimonios[1]
        patrimonios[1] = patrimonio
        if patrimonios[1] < patrimonios[0]:
            perda_percentual = (patrimonios[0] - patrimonios[1]) / patrimonios[0]
            perdas.append(perda_percentual)
            ganhei += 1
        if patrimonios[1] > patrimonios[0]:
            ganho_percentual = (patrimonios[1] - patrimonios[0]) / patrimonios[0]
            ganhos.append(ganho_percentual)
            perdi += 1
        #print(f"terminei comprado e vendi no ultimo dia por {preco[-1]}")
    if media(ganhos) == 0 or media(perdas) == 0:
        risco = False
    else:
        risco = media(ganhos) / media(perdas)
    perdas.clear()
    vitorias = ganhei
    return patrimonio, contador, risco, vitorias
def backtest_date(timeframe,situacao_long,angulo, param1, param2, medo, patrimonio,preco, data):
    medo_inicial = 0
    contador = 0
    ganhei = 0
    perdi = 0
    translacao = timeframe - 1
    patrimonios = [1,1]
    perdas = list()
    ganhos = list()
    for i in range(len(medo) - translacao):
        if not situacao_long and angulo[i] < (90 * param1) and medo[i + translacao] > medo_inicial:
            #compra long!
            situacao_long, quantidade = compras_long(situacao_long,patrimonio,preco[i + translacao])
            print(f"LONG:Comprei por {preco[i + translacao]} no dia {data[i + translacao]}")
        if situacao_long and angulo[i] < (90 * param2) and medo[i + translacao] <  -medo_inicial:
            #venda long!
            situacao_long, patrimonio = vendas_long(situacao_long,quantidade,preco[i + translacao])
            contador += 1
            print(f"LONG:Vendi por {preco[i + translacao]} no dia {data[i + translacao]}")
            print(f"O patrimonio após isso é de {patrimonio}")
            patrimonios[0] = patrimonios[1]
            patrimonios[1] = patrimonio
            if patrimonios[1] < patrimonios[0]:
                perda_percentual = (patrimonios[0] - patrimonios[1]) / patrimonios[0]
                perdas.append(perda_percentual)
                ganhei += 1
            if patrimonios[1] > patrimonios[0]:
                ganho_percentual = (patrimonios[1] - patrimonios[0]) / patrimonios[0]
                ganhos.append(ganho_percentual)
                perdi += 1
    if situacao_long:
        patrimonio = quantidade * preco[-1]
        contador += 1
        patrimonios[0] = patrimonios[1]
        patrimonios[1] = patrimonio
        if patrimonios[1] < patrimonios[0]:
            perda_percentual = (patrimonios[0] - patrimonios[1]) / patrimonios[0]
            perdas.append(perda_percentual)
            ganhei += 1
        if patrimonios[1] > patrimonios[0]:
            ganho_percentual = (patrimonios[1] - patrimonios[0]) / patrimonios[0]
            ganhos.append(ganho_percentual)
            perdi += 1
        print(f"terminei comprado e vendi no ultimo dia por {preco[-1]} no dia {data[i + translacao]}")
    if media(ganhos) == 0 or media(perdas) == 0:
        risco = False
    else:
        risco = media(ganhos) / media(perdas)
    perdas.clear()
    vitorias = ganhei
    return patrimonio, contador, risco, vitorias
def escolhedor(maximos):
    tamanho = len(maximos)
    media_trades = 0
    media_patrimonio = 0
    media_risco = 0
    media_possibilidades = 0
    for item in maximos:
        media_patrimonio += item['maximo']
        media_possibilidades += item['Pares possíveis']
        media_trades += item['número de trades']
        media_risco += item['retorno x risco']
    media_patrimonio /= tamanho
    media_risco /= tamanho
    media_possibilidades /= tamanho
    media_trades /= tamanho
    apoio = list()
    for item in maximos:
        produto = (item['Pares possíveis'] - media_possibilidades) * (item['número de trades'] - media_trades) * (item['número de trades'] - media_trades) * (item['retorno x risco'] - media_risco)
        produto = np.fabs(produto)
        apoio.append(produto)
    maximo = max(apoio)
    indices = apoio.index(maximo)
    return indices
