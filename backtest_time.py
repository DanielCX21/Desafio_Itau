import dados
import backtest
import transform_data

data_inicial = "01/01/2020"
data_final = "01/01/2024"

preco = dados.preco_close
medo = dados.medo
datas = dados.data
y_interpolar = list()
coefs_angular = list()
estou_comprado = False
patrimonio = 1
nome_moeda = dados.nome_arquivo[19:22]
inicio = datas.index(data_inicial)
fim = datas.index(data_final) + 1

datas = datas[inicio:fim]
preco = preco[inicio:fim]
medo = medo[inicio:fim]


