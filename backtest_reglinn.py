import numpy as np
import matplotlib.pyplot as plt
import dados
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt

medo = dados.medo
y_interpolar = list()
coefs_angular = list()
estou_comprado = False
patrimonio = 1
preco = dados.preco_close
datas = dados.data
timeframe = 50

def compras(situacao,patrimonio, preco):
    quantidade = patrimonio / preco
    situacao = True
    tupla = (situacao,quantidade)
    return tupla
def vendas(situacao,quantidade, preco):
    patrimonio_final = quantidade * preco
    situacao = False
    tupla = (situacao,patrimonio_final)
    return tupla

def backtest(datas, angulo, param1, param2, situacao, patrimonio):
    translacao = (parametro) - 1
    for i in range(len(datas) - translacao):
        if not situacao and angulo[i] < (90 * param1) and medo[i + translacao] <= 0:
            situacao, quantidade = compras(situacao,patrimonio,preco[i + translacao])
        if situacao and angulo[i] < (90 * param2) and medo[i + translacao] > 0:
            situacao, patrimonio = vendas(situacao,quantidade,preco[i + translacao])
    if situacao:
        patrimonio = quantidade * preco[-1]
    return patrimonio

x = np.linspace(0, 1, 100)  
y = np.linspace(0, 1, 100)
X, Y = np.meshgrid(x, y)
maximos = list()
angulos = list()
Z = np.zeros(X.shape)


for k in range(2,timeframe + 1):
    estou_comprado = False
    parametro = k
    x_interpolar = list(range(1,parametro + 1))

    for i in range(len(medo) - parametro + 1):
        for j in range(parametro):
            y_interpolar.append(medo[i+j])
        angular = float(np.polyfit(x_interpolar,y_interpolar,1)[0])
        coefs_angular.append(angular)
        y_interpolar.clear()

    for coef in coefs_angular:
        informacao = float(np.fabs(np.degrees(np.arctan(coef))))
        angulos.append(informacao)

    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            Z[i, j] = backtest(datas, angulos, X[i, j], Y[i, j], estou_comprado, 1)
    maximos.append(Z.max())
    print(Z.max())

    angulos.clear()
    x_interpolar.clear()
    coefs_angular.clear()
    Z = np.zeros(X.shape)
    
    
maximo_x = list(range(0,len(maximos)))

plt.plot(maximo_x,maximos)
plt.show()
