import numpy as np
import dados
from scipy.interpolate import CubicSpline

parametro = 4

medo = dados.medo
datas = dados.data
y_interpolar = list()
x_interpolar = list(range(1,parametro + 1))
coefs_angular = list()

for i in range(len(medo) - parametro + 1):
    for j in range(parametro):
        y_interpolar.append(medo[i+j])
    angular = float(np.polyfit(x_interpolar,y_interpolar,1)[0])
    coefs_angular.append(angular)
    y_interpolar.clear()
#tenho os coefs angulares. Agora vamos colocar "em fase" com o medo.

inicio_index = int((parametro + 1) / 2) - 1
fim_index = int(((2 * len(datas)) - 1 - parametro) / 2) + 1

medo = medo[inicio_index:fim_index]

angulos = list()

for coef in coefs_angular:
    informacao = float(np.fabs(np.degrees(np.arctan(coef))))
    angulos.append(informacao)

print(angulos)

#print(len(angulos_data)) = len(data) - parametro + 1
#começo a iterar a partir do primeiro elemento e termino no ultimo - parametro
#qual é o range valido para fazer as análises?
#para 3 pontos vale dos indices 1 até (len(data) - 1 - 1)
#usando um timeframe qualquer: [1,2,3,4...1999,2000] => [1,2...n],[2,3...n + 1]... [2000-(n-1)...1999,2000] com 2001 - parametro + 1 elementos
#quando temos termo central, estamos pegando a melhor aproximação e ai a série valeria de (1 + n)/2 até (4001 - n)/2 para isso, n deve ser ímpar.
#para n par, basta pegar o elemento sucessor ou o antecessor. Não é relevante


'''
#dividino os intervalos para verificar o que ocorre

inicio = 0 #4 * (int)
fim = 1999 #4 * (int)

#primeiro ROSA
eixo_x_primeiro = list()
eixo_y_primeiro = list()
for i in range((int(inicio / 4)),(int(fim / 4))):
    for j in range(1,5):
        y = interpolador.reta(coefs_angular[i * 4],coefs_linear[i * 4],j)
        eixo_y_primeiro.append(y)
        eixo_x_primeiro.append(4 * i + j)
#plt.plot(eixo_x_primeiro,eixo_y_primeiro,color='pink')

#segundo ROXO
eixo_x_segundo = list()
eixo_y_segundo = list()
for i in range((int(inicio / 4)),(int(fim / 4))):
    for j in range(1,5):
        y = interpolador.reta(coefs_angular[i * 4 + 1],coefs_linear[i * 4 + 1],j)
        eixo_y_segundo.append(y)
        eixo_x_segundo.append(4 * i + j)
#plt.plot(eixo_x_segundo,eixo_y_segundo,color='purple')

#terceiro AZUL
eixo_x_terceiro = list()
eixo_y_terceiro = list()
for i in range((int(inicio / 4)),(int(fim / 4))):
    for j in range(1,5):
        y = interpolador.reta(coefs_angular[i * 4 + 2],coefs_linear[i * 4 + 2],j)
        eixo_y_terceiro.append(y)
        eixo_x_terceiro.append(4 * i + j)
#plt.plot(eixo_x_terceiro,eixo_y_terceiro,color='blue')

#quarto VERDE
eixo_x_quarto = list()
eixo_y_quarto = list()
for i in range((int(inicio / 4)),(int(fim / 4))):
    for j in range(1,5):
        y = interpolador.reta(coefs_angular[i * 4 + 3],coefs_linear[i * 4 + 3],j)
        eixo_y_quarto.append(y)
        eixo_x_quarto.append(4 * i + j)
#plt.plot(eixo_x_quarto,eixo_y_quarto,color='green')

#plotar o gráfic junto
eixo_x_medo = np.arange(0,2001,1)
eixo_x_suave = np.linspace(0,2001,len(eixo_x_medo) * 100)
cs = CubicSpline(eixo_x_medo, medo_BTC)
eixo_y_suave = cs(eixo_x_suave)
plt.plot(eixo_x_suave,eixo_y_suave,color='red')

plt.grid(True)
plt.show()
'''
