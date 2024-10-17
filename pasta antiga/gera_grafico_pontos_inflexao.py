import numpy as np
from analise_BTC import medo_BTC
import programas_apoio_reglin.interpolador as interpolador
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

precisao = 100
x_pontos = np.arange(2,2000,dtype=int)
y_pontos = np.array(medo_BTC)
tamanho = len(medo_BTC)
ponto_inflexao_x = list()
y_inflexao = list()
x_suave = np.linspace(x_pontos[0], x_pontos[-1], len(x_pontos) * precisao)
y_suave = list()
sol = [0,0,0]

for i in range(2,len(medo_BTC) - 1):
    sol_antiga = sol
    pontos = [[1,medo_BTC[i - 1]],[2,medo_BTC[i]],[3,medo_BTC[i + 1]]]
    ponto_inflexao_candidato = interpolador.pontos_inflexao(pontos)
    sol = interpolador.resolve_sistema(pontos)
    for j in range(precisao):
        fator = j / precisao
        y_suave_ponto = interpolador.pol(sol,2 + fator)
        y_suave.append(y_suave_ponto)
        y_suave_ponto

    if ponto_inflexao_candidato != -1:
        translacao = i - 2
        ponto_inflexao_x.append(ponto_inflexao_candidato + translacao)
        y_inflexao.append(interpolador.pol(sol,ponto_inflexao_candidato))

'''
Para o curto prazo, arrumar os gráficos e deixar os pontos de inflexão 
na curva principal sempre
'''

plt.plot(x_suave,y_suave,color='blue')
plt.scatter(ponto_inflexao_x,y_inflexao,color='red')
plt.grid(True)

'''
eixo_x_medo = np.arange(0,2001,1)
eixo_x_suave = np.linspace(0,2001,len(eixo_x_medo) * 100)
cs = CubicSpline(eixo_x_medo, medo_BTC)
plt.scatter(eixo_x_medo,medo_BTC,color='yellow')
eixo_y_suave = cs(eixo_x_suave)
plt.plot(eixo_x_suave,eixo_y_suave,color='red')
'''

plt.show()

'''
Vamos pegar a cada 3 pontos e interpolar o polinomio cubico para 
cada intervalo por ex:
pontos: [1,2,3]:
pol: y = ax3 + bx2 + cx + d
seg_der: y = 6ax + b
pontos de inflexão: x = -3a / b
Marcar no grafico do preço e no medo
Estratégia simétrica!
Teste:
1) Mudança na concavidade
2) Período sem variação brusca no índice
3) Verificar quantos dias passamos longe do neutro
4) Juntar os dois primeiros
'''
