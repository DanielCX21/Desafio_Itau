import numpy as np
import dados

def compras_long(situacao, patrimonio, preco):
    quantidade = patrimonio / preco
    situacao = True
    tupla = (situacao, quantidade)
    return tupla
def vendas_long(situacao, quantidade, preco):
    patrimonio_final = quantidade * preco
    situacao = False
    tupla = (situacao,patrimonio_final)
    return tupla

def backtest(timeframe,situacao_long,angulo, param1, param2, medo, patrimonio,preco):
    contador = 0
    translacao = timeframe - 1
    for i in range(len(medo) - translacao):
        if not situacao_long and angulo[i] < (90 * param1) and medo[i + translacao] >= 0:
            #compra long!
            situacao_long, quantidade = compras_long(situacao_long,patrimonio,preco[i + translacao])
            #print(f"LONG:Comprei dia {datas[i + translacao]} por {preco[i + translacao]}")
        if situacao_long and angulo[i] < (90 * param2) and medo[i + translacao] < 0:
            #venda long!
            situacao_long, patrimonio = vendas_long(situacao_long,quantidade,preco[i + translacao])
            contador += 1
            #print(f"LONG:Vendi dia {datas[i + translacao]} por {preco[i + translacao]}")
    if situacao_long:
        patrimonio = quantidade * preco[-1]
        contador += 1
        #print(f"terminei comprado e vendi no ultimo dia por {datas[i + translacao]}")
    return patrimonio, contador

preco = dados.preco_close
medo = dados.medo
datas = dados.data
y_interpolar = list()
coefs_angular = list()
estou_comprado = False
estou_vendido = False
patrimonio = 1
parametro = 3
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

angulos = list()

for coef in coefs_angular:
    informacao = float(np.fabs(np.degrees(np.arctan(coef))))
    angulos.append(informacao)


print(X[1,93])
print(Y[1,93])

print(backtest(parametro,estou_comprado,angulos,X[20,93],Y[20,93],medo,1,preco)[0])
