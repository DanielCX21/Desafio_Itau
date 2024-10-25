import dados
import backtest
import transform_data
import matplotlib.pyplot as plt
import numpy as np
from backtest import backtest
from matplotlib.colors import BoundaryNorm
from matplotlib import cm

tolerancia = 3

parametro = 9

#primeiro com BTC
data_inicial = ["31/01/2018", "31/01/2018", "31/01/2019", "31/01/2020", "31/01/2021", "31/01/2022", "31/01/2019"]
data_final = ["11/09/2024", "31/01/2019","31/01/2020" ,"31/01/2021", "31/01/2022", "31/01/2023", "31/01/2023"]

y_interpolar = list()
coefs_angular = list()
estou_comprado = False
patrimonio = 1
nome_moeda = dados.nome_arquivo[19:22]

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
    x = np.linspace(0,1,200)
    y = np.linspace(0,1,200)
    X,Y = np.meshgrid(x,y)
    Z = np.zeros(X.shape)

    for i in range(len(medo) - parametro + 1):
        for j in range(parametro):
            y_interpolar.append(medo[i+j])
        angular = float(np.polyfit(x_interpolar,y_interpolar,1)[0])
        coefs_angular.append(angular)
        y_interpolar.clear()

    angulos = list()

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
    print(f"Indices: {(primeiro,segundo)}. Parametros: {X[primeiro,segundo],Y[primeiro,segundo]}")
    print(f"Maximo: {submatriz.max()}. Confirmacao: {Z[primeiro,segundo]}. Confirmacao: {backtest(parametro,estou_comprado,angulos,X[primeiro,segundo],Y[primeiro,segundo],medo,1,preco)}")
    print(f"Numero de trades:{backtest(parametro,estou_comprado,angulos,X[primeiro,segundo],Y[primeiro,segundo],medo,1,preco)[1]}")
    print(f"(Retorno x risco) do parametro: {backtest(parametro,estou_comprado,angulos,X[primeiro,segundo],Y[primeiro,segundo],medo,1,preco)[2]}")

    aceitavel = submatriz.max() * (3 / 4)
    numero = 0

    for a in range(X.shape[0] - tolerancia):
        for b in range(X.shape[1] - tolerancia):
            if submatriz[a,b] >= aceitavel:
                first = a + tolerancia
                second = b + tolerancia
                #print((X[first,second],Y[first,second]))
                numero += 1

    angulos.clear()
    Z = np.zeros(X.shape)
    x_interpolar.clear()
