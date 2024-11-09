import numpy as np
import dados
from funcoes import backtest

medo_inicial = 0

preco = dados.preco_close
medo = dados.medo
datas = dados.data
y_interpolar = list()
coefs_angular = list()
estou_comprado = False
estou_vendido = False
patrimonio = 1

escolha_data_inicial = "31/12/2019" #str(input("Digite a data de inicio até 31/01/2018: "))

inicio = datas.index(escolha_data_inicial)

escolha_data_final = "31/12/2023" #str(input("Digite a data final até 11/09/2024: "))

fim = datas.index(escolha_data_final) + 1

datas = datas[inicio:fim]
preco = preco[inicio:fim]
medo = medo[inicio:fim]

a = 21
b = 9
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

print(f"Patrimonio: {backtest(timeframe,estou_comprado,angulos,X[a,b],Y[a,b],medo,1,preco)[0]}")
print(f"Numero de trades: {backtest(timeframe,estou_comprado,angulos,X[a,b],Y[a,b],medo,1,preco)[1]}")
print(f"Vitorias: {backtest(timeframe,estou_comprado,angulos,X[a,b],Y[a,b],medo,1,preco)[3]}")
print(f"Aproveitamento: {backtest(timeframe,estou_comprado,angulos,X[a,b],Y[a,b],medo,1,preco)[0] / (preco[-1]/preco[0])}")
#print(f"Risco: {backtest(timeframe,estou_comprado,angulos,X[a,b],Y[a,b],medo,1,preco)[2]}")
