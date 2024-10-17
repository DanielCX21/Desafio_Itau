import numpy as np
import dados
from scipy.interpolate import CubicSpline

parametro = 4

medo_BTC = dados.medo
y_interpolar = list()
x_interpolar = list(range(1,parametro + 1))
coefs_angular = list()

for i in range(len(medo_BTC) - parametro + 1):
    for j in range(parametro):
        y_interpolar.append(medo_BTC[i+j])
    angular = float(np.polyfit(x_interpolar,y_interpolar,1)[0])
    coefs_angular.append(angular)
    y_interpolar.clear()

angulos_data = list()

for coef in coefs_angular:
    informacao = float(np.fabs(np.degrees(np.arctan(coef))))
    angulos_data.append(informacao)

#print(len(angulos_data)) = 1999 = 2001 - 2

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
