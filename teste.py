import dados
import regressao_linear as regressao_linear

estou_comprado = False
estou_vendido = False
patrimonio = 1
preco = dados.preco_close
medo = dados.medo
angulos = regressao_linear.angulos_data
datas = dados.data

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
def vendas_short(situacao, patrimonio, preco):
    quantidade = patrimonio / preco
    situacao = True
    tupla = (situacao, quantidade)
    return tupla
def compras_short(situacao, quantidade, preco):
    patrimonio_final = (2 * patrimonio) - quantidade * preco
    situacao = False
    tupla = (situacao, patrimonio_final)
    return tupla
#em long uso a situacao_long e em short situacao_short = estou_comprado e estou vendido

def backtest(datas, angulo, param1, param2, situacao_long,situacao_short, patrimonio, contador,preco):
    translacao = regressao_linear.parametro - 1
    for i in range(len(datas) - translacao):
        if not situacao_long and not situacao_short and angulo[i] < (90 * param1) and medo[i + translacao] < 0:
            #compra long
            situacao_long, quantidade = compras_long(situacao_long,patrimonio,preco[i + translacao])
            print(f"inicio do long {datas[i + translacao]}")
            
        if situacao and angulo[i] < (90 * param2) and medo[i + translacao] < 0:
            situacao, patrimonio = vendas_long(situacao,quantidade,dados.preco_close[i + translacao])
            print(f"vendi: {datas[i + translacao]}")
            contador += 1
            print(patrimonio)
        if not situacao and angulo[i] < (90 * param2) and medo[i + translacao] > 0:
            
    if situacao:
        patrimonio = quantidade * preco[-1]
        contador += 1
        print(patrimonio)
    return patrimonio, contador

a = 0.8181818181818182 
b = 0.5050505050505051

print(backtest(dados.data,angulos,a,b,estou_comprado,1,0)[0])
print(backtest(dados.data,angulos,a,b,estou_comprado,1,0)[1])
