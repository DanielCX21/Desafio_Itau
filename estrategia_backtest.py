import modulacao
import matplotlib.pyplot as plt

valores_feg = list()

for medo in modulacao.lista_dados:
    valores_feg.append(medo['fear_greed_value'])

'''
def der(y1, y2):
    return (y1 - y2)

#armazenar as derivadas de forma
#a verificar uma "aceleração"

def seg_der(y1, y2, y3, y4):
    return (der(y1,y2) - der(y3,y4))

derivadas = list()
segunda_derivada = list()

eixo_x = list()
eixo_x_nov = list()

for i in range(len(valores_feg) - 1):
    derivadas.append(der(valores_feg[i + 1],valores_feg[i]))
    eixo_x.append(i + 1)

for i in range(len(valores_feg) - 4):
    segunda_derivada.append(seg_der(valores_feg[i + 3],valores_feg[i + 2],valores_feg[i + 1],valores_feg[i]))
    eixo_x_nov.append(i + 1)

plt.figure(figsize=(12, 6))
plt.plot(eixo_x, derivadas, marker='', linestyle='-', color='red')
plt.plot(eixo_x_nov, segunda_derivada, marker='', linestyle='-', color='blue')
plt.show()
'''
