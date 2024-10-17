import dados
import regressao_linear as regressao_linear
import numpy as np
import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D
from backtest_reglin import a,b

estou_comprado = False
patrimonio = 1
preco = dados.preco_close
medo = dados.medo
angulos = regressao_linear.angulos_data
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
    translacao = regressao_linear.parametro - 1
    for i in range(len(datas) - translacao):
        if not situacao and angulo[i] < (90 * param1) and medo[i + translacao] >= 0:
            situacao, quantidade = compras(situacao,patrimonio,dados.preco_close[i + translacao])
            #print(f"comprei: {datas[i + translacao]}")
        if situacao and angulo[i] < (90 * param2) and medo[i + translacao] < 0:
            situacao, patrimonio = vendas(situacao,quantidade,dados.preco_close[i + translacao])
            #print(f"vendi: {datas[i + translacao]}")
            #print(patrimonio)
    return patrimonio

print(backtest(dados.data,angulos,a,b,estou_comprado,1))
