import dados
import regressao_linear as regressao_linear
import numpy as np
import matplotlib.pyplot as plt

estou_comprado = False
preco = dados.preco_close
medo = dados.medo
angulos = regressao_linear.angulos
datas = dados.data

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
    translacao = (regressao_linear.parametro) - 1
    for i in range(len(datas) - translacao):
        if not situacao and angulo[i] < (90 * param1) and medo[i + translacao] >= 0:
            situacao, quantidade = compras(situacao,patrimonio,dados.preco_close[i + translacao])
            #print(f"compra:{preco[i + translacao]}")
        if situacao and angulo[i] < (90 * param2) and medo[i + translacao] < 0:
            situacao, patrimonio = vendas(situacao,quantidade,dados.preco_close[i + translacao])
            #print(f"Venda:{preco[i + translacao]}")
        if situacao:
            patrimonio = quantidade * preco[-1]
    return patrimonio

x = np.linspace(0, 1, 100)  
y = np.linspace(0, 1, 100)
X, Y = np.meshgrid(x, y)
Z = np.zeros(X.shape)


for i in range(X.shape[0]):
    for j in range(X.shape[1]):
        Z[i, j] = backtest(datas, angulos, X[i, j], Y[i, j], estou_comprado, 1)

print(Z.max())

indice_maior_valor = np.unravel_index(np.argmax(Z), Z.shape)

print(indice_maior_valor)

print(X[50,81])
print(Y[50,81])

estou_comprado = False


print(backtest(datas, angulos, X[50,81], Y[50,81], estou_comprado, 1))


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_xlabel('param1')
ax.set_ylabel('param2')
ax.set_zlabel('Patrimônio final')
plt.show()
