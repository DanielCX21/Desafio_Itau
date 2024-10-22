import numpy as np
import matplotlib.pyplot as plt
import dados
import transform_data

medo_inicial = 0

def media(vetor):
    med = 0
    for valor in vetor:
        med += valor
    return (med / (len(vetor)))
def compras_long(situacao,patrimonio, preco):
    quantidade = patrimonio / preco
    situacao = True
    tupla = (situacao,quantidade)
    return tupla
def vendas_long(situacao,quantidade, preco):
    patrimonio_final = quantidade * preco
    situacao = False
    tupla = (situacao,patrimonio_final)
    return tupla
def venda_short(situacao, patrimonio,preco):
    quantidade = patrimonio / preco
    situacao = True
    tupla = (situacao, quantidade)
    return tupla
def compra_short(situacao,quantidade,preco, patrimonio):
    patrimonio_final = (2 * patrimonio) - quantidade * preco
    situacao = False
    tupla = (situacao,patrimonio_final)
    return tupla
def backtest_sl(timeframe,situacao_long, situacao_short, angulo, datas, param1, param2, medo, patrimonio,preco):
    translacao = timeframe - 1
    for i in range(len(medo)):
        if not situacao_long and not situacao_short and angulo[i] < (90 * param1) and medo[i + translacao] <= 0:
            #compra long!
            situacao_long, quantidade = compras_long(situacao_long,patrimonio,preco[i + translacao])
            #print(f"LONG:Comprei dia {datas[i + translacao]} por {preco[i + translacao]}")
        if situacao_long and not situacao_short and angulo[i] < (90 * param2) and medo[i + translacao] > 0:
            #venda long!
            situacao_long, patrimonio = vendas_long(situacao_long,quantidade,preco[i + translacao])
            #print(f"LONG:Vendi dia {datas[i + translacao]} por {preco[i + translacao]}")
        if not situacao_long and not situacao_short and angulo[i] < (90 * param2) and medo[i + translacao] > 0:
            #venda short!
            situacao_short, quantidade = venda_short(situacao_short,patrimonio,preco[i + translacao]) 
            #print(f"SHORT:Vendi dia {datas[i + translacao]} por {preco[i + translacao]}")
        if not situacao_long and situacao_short and angulo[i] < (90 * param1) and medo[i + translacao] < 0:
            #compra short!
            situacao_short, patrimonio = compra_short(situacao_short,quantidade,preco[i + translacao],patrimonio)
            #print(f"SHORT:Comprei dia {datas[i + translacao]} por {preco[i + translacao]}")
    if situacao_long:
        patrimonio = quantidade * preco[-1]
        #print(f"terminei comprado e vendi no ultimo dia por {datas[i + translacao]}")
    if situacao_short:
        patrimonio = (2 * patrimonio) - quantidade * preco[-1]
        #print(f"terminei vendido e vendi no último dia por {datas[i + translacao]}")
    return patrimonio
def backtest(timeframe,situacao_long,angulo, param1, param2, medo, patrimonio,preco):
    contador = 0
    translacao = timeframe - 1
    patrimonios = [1,1]
    perdas = list()
    for i in range(len(medo) - translacao):
        if not situacao_long and angulo[i] < (90 * param1) and medo[i + translacao] > medo_inicial:
            #compra long!
            situacao_long, quantidade = compras_long(situacao_long,patrimonio,preco[i + translacao])
            print(f"LONG:Comprei dia {datas[i + translacao]} por {preco[i + translacao]}")
        if situacao_long and angulo[i] < (90 * param2) and medo[i + translacao] < -medo_inicial:
            #venda long!
            situacao_long, patrimonio = vendas_long(situacao_long,quantidade,preco[i + translacao])
            contador += 1
            print(f"LONG:Vendi dia {datas[i + translacao]} por {preco[i + translacao]}")
            patrimonios[0] = patrimonios[1]
            patrimonios[1] = patrimonio
            if patrimonios[1] < patrimonios[0]:
                perda_percentual = (patrimonios[0] - patrimonios[1]) / patrimonios[0]
                perdas.append(perda_percentual)
    if situacao_long:
        patrimonio = quantidade * preco[-1]
        contador += 1
        #print(f"terminei comprado e vendi no ultimo dia por {datas[i + translacao]}")
    risco = media(perdas)
    perdas.clear() 
    return patrimonio, contador, risco

preco = dados.preco_close
medo = dados.medo
datas = dados.data
y_interpolar = list()
coefs_angular = list()
estou_comprado = False
estou_vendido = False
patrimonio = 1

escolha_data_inicial = "01/01/2019" #str(input("Digite a data de inicio até 31/01/2018: "))


inicio = datas.index(escolha_data_inicial)

escolha_data_final = "01/01/2023" #str(input("Digite a data final até 11/09/2024: "))


fim = datas.index(escolha_data_final) + 1

datas = datas[inicio:fim]
preco = preco[inicio:fim]
medo = medo[inicio:fim]

a = 62
b = 70
timeframe = 3
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

print(backtest(timeframe,estou_comprado,angulos,0.035,0.0315,medo,1,preco))
