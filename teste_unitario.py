import numpy as np
import dados
from funcoes import backtest, backtest_date
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

a = 76
b = 62
timeframe = 9
x = np.linspace(0,1,100)

x_interpolar = list(range(1,(timeframe + 1)))
x = np.linspace(0,1,100)
y = np.linspace(0,1,100)
X,Y = np.meshgrid(x,y)
Z = np.zeros(X.shape)

for i in range(len(medo) - timeframe + 1):
    for j in range(timeframe):
        y_interpolar.append(medo[i+j])
    angular = float(np.polyfit(x_interpolar,y_interpolar,1)[0])
    coefs_angular.append(angular)
    y_interpolar.clear()

angulos = list()

for coef in coefs_angular:
    informacao = float(np.fabs(np.degrees(np.arctan(coef))))
    angulos.append(informacao)

ASD = 1


datas_especificas = [
    datas[0],   datas[335] , datas[700],  datas[1066],  datas[1431],  datas[1796],  datas[2160]
    #31/01/2018 #01/01/2019  #01/01/2020, #01/01/2021   #01/01/2022   #01/01/2023   #31/12/2023
]


datas_especifica = [
    datas[0],   datas[267] , datas[632],  datas[997],  datas[1361]
]
    #09/04/2020 #01/01/2021  #01/01/2022, #01/01/2023   #01/01/2022


if ASD == 1:
    print(f"Patrimonio: {backtest_date(timeframe,estou_comprado,angulos,X[a,b],Y[a,b],medo,1,preco, datas)[0]}")
    plt.plot(datas,backtest_date(timeframe,estou_comprado,angulos,X[a,b],Y[a,b],medo,1,preco, datas)[4],color="lightgreen", linewidth=3)
    plt.xticks(datas_especificas, rotation=45)
    plt.ylabel('SOL/USD', fontsize=16)
    plt.show()

else:
    print(f"Patrimonio: {backtest(timeframe,estou_comprado,angulos,X[a,b],Y[a,b],medo,1,preco)[0]}")
    print(f"Numero de trades: {backtest(timeframe,estou_comprado,angulos,X[a,b],Y[a,b],medo,1,preco)[1]}")
    print(f"Vitorias: {backtest(timeframe,estou_comprado,angulos,X[a,b],Y[a,b],medo,1,preco)[3]}")
    print(f"Aproveitamento: {backtest(timeframe,estou_comprado,angulos,X[a,b],Y[a,b],medo,1,preco)[0] / (preco[-1]/preco[0])}")
    print(f"Risco: {backtest(timeframe,estou_comprado,angulos,X[a,b],Y[a,b],medo,1,preco)[2]}")

