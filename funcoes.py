import numpy as np

YELLOW = "\033[93m"
RESET = "\033[0m"
RED = "\033[31m"

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
    return situacao,quantidade
def vendas_long(situacao,quantidade, preco):
    patrimonio_final = quantidade * preco
    situacao = False
    return situacao, patrimonio_final
def backtest(timeframe,angulo, param1, param2, medo, patrimonio,preco):
    medo_inicial = 0
    contador = 0
    ganhei = 0
    perdi = 0
    translacao = timeframe - 1
    patrimonios = [1,1]
    perdas = list()
    ganhos = list()
    situacao_long = False
    for i in range(len(medo) - translacao):
        if not situacao_long and angulo[i] < (90 * param1) and medo[i + translacao] > medo_inicial:
            #compra long!
            situacao_long, quantidade = compras_long(situacao_long,patrimonio,preco[i + translacao])
        if situacao_long and angulo[i] < (90 * param2) and medo[i + translacao] <  -medo_inicial:
            #venda long!
            situacao_long, patrimonio = vendas_long(situacao_long,quantidade,preco[i + translacao])
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
    if media(ganhos) == 0 or media(perdas) == 0:
        risco = False
    else:
        risco = media(ganhos) / media(perdas)
    perdas.clear()
    vitorias = ganhei
    return patrimonio, contador, risco, vitorias
def backtest_date(timeframe,situacao_long,angulo, param1, param2, medo, patrimonio,preco, data):
    
    datas_especificas = [
    data[0],   data[335] , data[700],  data[1066],  data[1431],  data[1796],  data[2160]
    #31/01/2018 #01/01/2019  #01/01/2020, #01/01/2021   #01/01/2022   #01/01/2023   #31/12/2023
]
    
    datas_especifica = [
    data[0],   data[267] , data[632],  data[997],  data[1361]
]
  
    medo_inicial = 0
    contador = 0
    ganhei = 0
    perdi = 0
    translacao = timeframe - 1
    patrimonios = [1,1]
    perdas = list()
    ganhos = list()
    eixo_y = [1] * translacao
    eixo_y_marcador = [1]
    for i in range(len(medo) - translacao):
        if data[i + translacao] in datas_especificas and situacao_long:
            print(f"{RED}O Patrimonio na virada do ano: {data[i + translacao]} é {vendas_long(True, quantidade,preco[i + translacao])[1]}{RESET}")
            eixo_y_marcador.append(vendas_long(True, quantidade,preco[i + translacao])[1])
        if data[i + translacao] in datas_especificas and not situacao_long:
            print(f"{RED}O Patrimonio na virada do ano: {data[i + translacao]} é {patrimonios[1]}{RESET}")
            eixo_y_marcador.append(patrimonios[1])
        if not situacao_long and angulo[i] < (90 * param1) and medo[i + translacao] > medo_inicial:
            #compra long!
            situacao_long, quantidade = compras_long(situacao_long,patrimonio,preco[i + translacao])
            print(f"LONG:Comprei por {preco[i + translacao]} no dia {data[i + translacao]}")
        if situacao_long and angulo[i] < (90 * param2) and medo[i + translacao] <  -medo_inicial:
            #venda long!
            situacao_long, patrimonio = vendas_long(situacao_long,quantidade,preco[i + translacao])
            contador += 1
            print(f"LONG:Vendi por {preco[i + translacao]} no dia {data[i + translacao]}")
            print(f"{YELLOW}O patrimonio após isso é de {patrimonio}{RESET}")
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
            eixo_y.append(vendas_long(True, quantidade,preco[i + translacao])[1])
        if not situacao_long:
            eixo_y.append(patrimonio)
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
    return patrimonio, contador, risco, vitorias, eixo_y, eixo_y_marcador
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
    print(media_trades)
    print(media_patrimonio)
    for item in maximos:
        if item['número de trades'] >= media_trades and item['maximo'] >= media_patrimonio and item['Trades certos'] >= (item['número de trades'] - item['Trades certos']):
            produto = ((item['número de trades'] - media_trades) ** (2)) * (item['maximo'] - media_patrimonio) 
            produto = np.fabs(produto)
            apoio.append(produto)
        else:
            apoio.append(0)
    maximo = max(apoio)
    indices = apoio.index(maximo)
    return indices
