import numpy as np
from analise_BTC import medo_BTC
import interpolador
import matplotlib.pyplot as plt

x_pontos = np.arange(2,2000,dtype=int)
y_pontos = np.array(medo_BTC)
tamanho = len(medo_BTC)
ponto_inflexao = list()
y_inflexao = list()
x_suave = np.linspace(x_pontos[0], x_pontos[-1], len(x_pontos) * 100)
y_suave = list()

for i in range(2,len(medo_BTC) - 1):
    pontos = [[1,medo_BTC[i - 1]],[2,medo_BTC[i]],[3,medo_BTC[i + 1]]]
    ponto_inflexao_candidato = interpolador.pontos_inflexao(pontos)
    sol = interpolador.resolve_sistema(pontos)

    for j in range(100):
        fator = j / 100
        y_suave_ponto = interpolador.pol(sol,2 + fator)
        y_suave.append(y_suave_ponto)
        y_suave_ponto

    if ponto_inflexao_candidato != -1:
        translacao = i - 2
        ponto_inflexao.append(ponto_inflexao_candidato + translacao)
        y_inflexao.append(interpolador.pol(sol,ponto_inflexao_candidato))

'''
Para o curto prazo, arrumar os gráficos e deixar os pontos de inflexão 
na curva principal sempre
'''

plt.plot(x_suave,y_suave,color='blue')
plt.scatter(ponto_inflexao,y_inflexao,color='red')
plt.grid(True)
plt.show()

'''
Vamos pegar a cada 3 pontos e interpolar o polinomio cubico para 
cada intervalo por ex:
pontos: [1,2,3]:
pol: y = ax3 + bx2 + cx + d
seg_der: y = 6ax + 2b
pontos de inflexão: x = -a / 3b
Marcar no grafico do preço e no medo
Estratégia simétrica!
Teste:
1) Mudança na concavidade
2) Período sem variação brusca no índice
3) Verificar quantos dias passamos longe do neutro
4) Juntar os dois primeiros
'''
