import numpy as np
import dados
from funcoes import backtest, backtest_date

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

print(f"Patrimonio: {backtest_date(timeframe,estou_comprado,angulos,X[a,b],Y[a,b],medo,1,preco, datas)[0]}")
#print(f"Numero de trades: {backtest_date(timeframe,estou_comprado,angulos,X[a,b],Y[a,b],medo,1,preco, datas)[1]}")
#print(f"Vitorias: {backtest_date(timeframe,estou_comprado,angulos,X[a,b],Y[a,b],medo,1,preco, datas)[3]}")
#print(f"Aproveitamento: {backtest_date(timeframe,estou_comprado,angulos,X[a,b],Y[a,b],medo,1,preco, datas)[0] / (preco[-1]/preco[0])}")
#print(f"Risco: {backtest_date(timeframe,estou_comprado,angulos,X[a,b],Y[a,b],medo,1,preco, datas)[2]}")
