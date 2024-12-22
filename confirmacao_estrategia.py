import numpy as np
import dados
from funcoes import *
import matplotlib.pyplot as plt

preco = dados.preco_close
medo = dados.medo
datas = dados.data
y_interpolar = list()
coefs_angular = list()
estou_comprado = False
patrimonio = 1
escolha_data_final = "31/12/2023"
fim = datas.index(escolha_data_final) + 1
datas = datas[:fim]
preco = preco[:fim]
medo = medo[:fim]

<<<<<<< HEAD:teste_unitario.py
a = 60
b = 67
timeframe = 15
x = np.linspace(0,1,100)
=======
a = 76
b = 62
timeframe = 9
>>>>>>> 673c816bc0e40e9f3f1ab49831cc87d8772440a3:confirmacao_estrategia.py

x = np.linspace(0,1,100)
y = np.linspace(0,1,100)
X,Y = np.meshgrid(x,y)
Z = np.zeros(X.shape)

angulos = criar_angulos(medo, timeframe)

ASD = 1

<<<<<<< HEAD:teste_unitario.py
'''
datas_especifica = [
=======
datas_especificas = [
>>>>>>> 673c816bc0e40e9f3f1ab49831cc87d8772440a3:confirmacao_estrategia.py
    datas[0],   datas[335] , datas[700],  datas[1066],  datas[1431],  datas[1796],  datas[2160]
    #31/01/2018 #01/01/2019  #01/01/2020, #01/01/2021   #01/01/2022   #01/01/2023   #31/12/2023
]
'''

<<<<<<< HEAD:teste_unitario.py
datas_especificas = [
=======
datas_especifica = [
>>>>>>> 673c816bc0e40e9f3f1ab49831cc87d8772440a3:confirmacao_estrategia.py
    datas[0],   datas[267] , datas[632],  datas[997],  datas[1361]
]
    #09/04/2020 #01/01/2021  #01/01/2022, #01/01/2023   #01/01/2022

if ASD == 1:
    print(f"Patrimonio: {backtest_date(timeframe,estou_comprado,angulos,X[a,b],Y[a,b],medo,1,preco, datas)[0]}")
    plt.plot(datas,backtest_date(timeframe,estou_comprado,angulos,X[a,b],Y[a,b],medo,1,preco, datas)[4],color="green", linewidth=4)
    plt.xticks(datas_especificas, rotation=35, fontsize=12)
    aparecer = backtest_date(timeframe,estou_comprado,angulos,X[a,b],Y[a,b],medo,1,preco, datas)[5].copy()
    del aparecer[0]
    del aparecer[1]
    plt.yticks(aparecer, fontsize=12)
    plt.ylabel('SOL/USD', fontsize=16)
    for data in datas_especificas:
        if data in datas[1:]:
            idx = datas.index(data)
            y_value = backtest_date(timeframe,estou_comprado,angulos,X[a,b],Y[a,b],medo,1,preco, datas)[4][idx]
            plt.plot([data, data], [0, y_value], color="red", linestyle="--", linewidth=1.5)
            plt.plot([datas_especificas[0],data], [y_value, y_value], color="red", linestyle="--", linewidth=1.5) 
            plt.scatter(data, y_value, color="black", zorder=5)

    plt.show()

else:
    print(f"Patrimonio: {backtest(timeframe,estou_comprado,angulos,X[a,b],Y[a,b],medo,1,preco)[0]}")
    print(f"Numero de trades: {backtest(timeframe,estou_comprado,angulos,X[a,b],Y[a,b],medo,1,preco)[1]}")
    print(f"Vitorias: {backtest(timeframe,estou_comprado,angulos,X[a,b],Y[a,b],medo,1,preco)[3]}")
    print(f"Aproveitamento: {backtest(timeframe,estou_comprado,angulos,X[a,b],Y[a,b],medo,1,preco)[0] / (preco[-1]/preco[0])}")
    print(f"Risco: {backtest(timeframe,estou_comprado,angulos,X[a,b],Y[a,b],medo,1,preco)[2]}")
