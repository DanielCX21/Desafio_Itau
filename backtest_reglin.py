import dados
import regressao_linear
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

estou_comprado = False
patrimonio = 1000
preco = dados.preco_close
medo = dados.medo
angulos = regressao_linear.angulos_data
datas = dados.data

def compras(situacao,patrimonio, preco):
    quantidade = patrimonio / preco
    situacao = True
    return (situacao,quantidade)
def vendas(situacao,quantidade, preco):
    patrimonio_final = quantidade * preco
    situacao = False
    return (situacao,patrimonio_final)

def backtest(datas, angulo, param1, param2, situacao, patrimonio):
    translacao = regressao_linear.parametro - 1
    for i in range(len(datas) - translacao):
        if not situacao and angulo[i] < 90*param1 and medo[i + translacao] > 0:
            compra = compras(situacao,patrimonio,dados.preco_close[i + translacao])
            situacao = compra[0]
            quantidade = compra[1]
        if situacao and angulo[i] < 90*param2 and medo[i + translacao] < 0:
            venda = vendas(situacao,quantidade,dados.preco_close[i + translacao])
            situacao = venda[0]
            patrimonio = venda[1]
    return patrimonio

x = np.linspace(0, 1, 100)  
y = np.linspace(0, 1, 100)
X, Y = np.meshgrid(x, y)

Z = np.zeros(X.shape)

for i in range(X.shape[0]):
    for j in range(X.shape[1]):
        Z[i, j] = backtest(datas, angulos, X[i, j], Y[i, j], estou_comprado, patrimonio)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_xlabel('X (param1)')
ax.set_ylabel('Y (param2)')
ax.set_zlabel('Patrimônio final')
plt.show()
