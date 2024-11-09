import dados
import numpy as np
from matplotlib.colors import BoundaryNorm
import matplotlib.pyplot as plt
from funcoes import backtest

tolerancia = 2
parametro = 9

data_inicial = ["31/01/2018", "31/12/2019"]
data_final = ["31/12/2023", "31/12/2023"]

y_interpolar = list()
coefs_angular = list()
estou_comprado = False
patrimonio = 1
nome_moeda = dados.nome_arquivo[19:22]
angulos = list()
possiveis_possiveis = list()
possiveis = list()

for i in range(len(data_inicial)):
    preco = dados.preco_close.copy()
    medo = dados.medo.copy()
    datas = dados.data.copy()
    inicio = datas.index(data_inicial[i])
    fim = datas.index(data_final[i]) + 1
    datas = datas[inicio:fim]
    preco = preco[inicio:fim]
    medo = medo[inicio:fim]
    comparacao = preco[-1] / preco[0]

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

    for a in range(X.shape[0]):
        for b in range(X.shape[1]):
            Z[a, b] = backtest(parametro,estou_comprado,angulos,X[a,b],Y[a,b],medo,1,preco)[0]
    
    submatriz = Z[tolerancia:,tolerancia:]

    aceitavel = comparacao
    #BTC - 0,65
    #ETH - 0,68
    #SOL - 0,8

    for a in range(X.shape[0] - tolerancia):
        for b in range(X.shape[1] - tolerancia):
            if submatriz[a,b] >= aceitavel:
                first = a + tolerancia
                second = b + tolerancia
                possiveis.append((first,second))
    possiveis_possiveis.append(possiveis.copy())
    possiveis.clear()
    angulos.clear()
    Z = np.zeros(X.shape)
    x_interpolar.clear()
    preco.clear()
    datas.clear()
    medo.clear()
    print("1")

tuplas_comuns = set(possiveis_possiveis[0]).intersection(*map(set, possiveis_possiveis[1:]))
tuplas_comuns = list(tuplas_comuns)
print(tuplas_comuns)
print(len(tuplas_comuns))

x, y = zip(*tuplas_comuns)

plt.scatter(x, y)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Gráfico de Dispersão dos Pontos")
plt.show()

