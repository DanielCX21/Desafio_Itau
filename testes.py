import funcoes
import dados

periodo = 14
rsi = funcoes.relativestr(dados.preco_open,dados.preco_close,periodo)
sinais = funcoes.sinal_compra_venda_rsi(rsi,dados.data,periodo)

compra = 0
venda = 0

for valor in sinais:
    if valor['sinal'] == 1:
        compra += 1
    else:
        if valor['sinal'] == 0:
            pass
        else:
            venda += 1

print(compra)
print(venda)
