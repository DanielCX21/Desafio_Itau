import dados
import numpy as np
from matplotlib.colors import BoundaryNorm
from matplotlib import cm
import matplotlib.pyplot as plt

tolerancia = 1
parametro = 9
medo_inicial = 0

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
def venda_short(situacao, patrimonio,preco):
    quantidade = patrimonio / preco
    situacao = True
    tupla = (situacao, quantidade)
    return tupla
def compra_short(situacao,quantidade,preco, patrimonio):
    patrimonio_final = (2 * patrimonio) - quantidade * preco
    situacao = False
    tupla = (situacao,patrimonio_final)
    return tupla
def backtest_sl(timeframe,situacao_long, situacao_short, angulo, datas, param1, param2, medo, patrimonio,preco):
    translacao = timeframe - 1
    for i in range(len(medo)):
        if not situacao_long and not situacao_short and angulo[i] < (90 * param1) and medo[i + translacao] <= 0:
            #compra long!
            situacao_long, quantidade = compras_long(situacao_long,patrimonio,preco[i + translacao])
            #print(f"LONG:Comprei dia {datas[i + translacao]} por {preco[i + translacao]}")
        if situacao_long and not situacao_short and angulo[i] < (90 * param2) and medo[i + translacao] > 0:
            #venda long!
            situacao_long, patrimonio = vendas_long(situacao_long,quantidade,preco[i + translacao])
            #print(f"LONG:Vendi dia {datas[i + translacao]} por {preco[i + translacao]}")
        if not situacao_long and not situacao_short and angulo[i] < (90 * param2) and medo[i + translacao] > 0:
            #venda short!
            situacao_short, quantidade = venda_short(situacao_short,patrimonio,preco[i + translacao]) 
            #print(f"SHORT:Vendi dia {datas[i + translacao]} por {preco[i + translacao]}")
        if not situacao_long and situacao_short and angulo[i] < (90 * param1) and medo[i + translacao] < 0:
            #compra short!
            situacao_short, patrimonio = compra_short(situacao_short,quantidade,preco[i + translacao],patrimonio)
            #print(f"SHORT:Comprei dia {datas[i + translacao]} por {preco[i + translacao]}")
    if situacao_long:
        patrimonio = quantidade * preco[-1]
        #print(f"terminei comprado e vendi no ultimo dia por {datas[i + translacao]}")
    if situacao_short:
        patrimonio = (2 * patrimonio) - quantidade * preco[-1]
        #print(f"terminei vendido e vendi no último dia por {datas[i + translacao]}")
    return patrimonio
def backtest(timeframe,situacao_long,angulo, param1, param2, medo, patrimonio,preco):
    contador = 0
    translacao = timeframe - 1
    patrimonios = [1,1]
    perdas = list()
    ganhos = list()
    for i in range(len(medo) - translacao):
        if not situacao_long and angulo[i] < (90 * param1) and medo[i + translacao] > medo_inicial:
            #compra long!
            situacao_long, quantidade = compras_long(situacao_long,patrimonio,preco[i + translacao])
            #print(f"LONG:Comprei dia {datas[i + translacao]} por {preco[i + translacao]}")
        if situacao_long and angulo[i] < (90 * param2) and medo[i + translacao] <  -medo_inicial:
            #venda long!
            situacao_long, patrimonio = vendas_long(situacao_long,quantidade,preco[i + translacao])
            contador += 1
            #print(f"LONG:Vendi dia {datas[i + translacao]} por {preco[i + translacao]}")
            patrimonios[0] = patrimonios[1]
            patrimonios[1] = patrimonio
            if patrimonios[1] < patrimonios[0]:
                perda_percentual = (patrimonios[0] - patrimonios[1]) / patrimonios[0]
                perdas.append(perda_percentual)
            if patrimonios[1] > patrimonios[0]:
                ganho_percentual = (patrimonios[1] - patrimonios[0]) / patrimonios[0]
                ganhos.append(ganho_percentual)
    if situacao_long:
        patrimonio = quantidade * preco[-1]
        contador += 1
        #print(f"terminei comprado e vendi no ultimo dia por {datas[i + translacao]}")
    if media(ganhos) == 0 or media(perdas) == 0:
        risco = False
    else:
        risco = media(ganhos) / media(perdas)
    perdas.clear() 
    return patrimonio, contador, risco

data_inicial = ["31/01/2018", "31/01/2018", "31/01/2019", "31/01/2020", "31/01/2021", "31/01/2022", "31/01/2019"]
data_final = ["11/09/2024", "31/01/2019","31/01/2020" ,"31/01/2021", "31/01/2022", "31/01/2023", "31/01/2023"]

y_interpolar = list()
coefs_angular = list()
estou_comprado = False
patrimonio = 1
nome_moeda = dados.nome_arquivo[19:22]
angulos = list()
possiveis_possiveis = list()
possiveis = list()


for i in range(len(data_inicial)):
    preco = dados.preco_close
    medo = dados.medo
    datas = dados.data
    inicio = datas.index(data_inicial[i])
    fim = datas.index(data_final[i]) + 1
    datas = datas[inicio:fim]
    preco = preco[inicio:fim]
    medo = medo[inicio:fim]

    x_interpolar = list(range(1,(parametro + 1)))
    x = np.linspace(0,1,100)
    y = np.linspace(0,1,100)
    X,Y = np.meshgrid(x,y)
    Z = np.zeros(X.shape)

    for i in range(len(medo) - parametro + 1):
        for j in range(parametro):
            y_interpolar.append(medo[i+j])
        angular = float(np.polyfit(x_interpolar,y_interpolar,1)[0])
        coefs_angular.append(angular)
        y_interpolar.clear()

    for coef in coefs_angular:
        informacao = float(np.fabs(np.degrees(np.arctan(coef))))
        angulos.append(informacao)
    #print(len(angulos))
    #print(len(datas))

    for a in range(X.shape[0]):
        for b in range(X.shape[1]):
            Z[a, b] = backtest(parametro,estou_comprado,angulos,X[a,b],Y[a,b],medo,1,preco)[0]
    
    submatriz = Z[tolerancia:,tolerancia:]

    indices = np.unravel_index(np.argmax(submatriz),submatriz.shape)
    primeiro = indices[0] + tolerancia
    segundo = indices[1] + tolerancia

    aceitavel = submatriz.max() * (0.65)
    #BTC - 0,65
    #ETH - 0,68
    #SOL - 0,8
    numero = 0

    for a in range(X.shape[0] - tolerancia):
        for b in range(X.shape[1] - tolerancia):
            if submatriz[a,b] >= aceitavel:
                first = a + tolerancia
                second = b + tolerancia
                #print((X[first,second],Y[first,second]))
                #numero += 1
                possiveis.append((X[first,second],Y[first,second]))
    possiveis_possiveis.append(possiveis.copy())
    possiveis.clear()
    angulos.clear()
    Z = np.zeros(X.shape)
    x_interpolar.clear()

tuplas_comuns = set(possiveis_possiveis[0]).intersection(*map(set, possiveis_possiveis[1:]))
tuplas_comuns = list(tuplas_comuns)
print(tuplas_comuns)

x, y = zip(*tuplas_comuns)

plt.scatter(x, y)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Gráfico de Dispersão dos Pontos")
plt.show()
