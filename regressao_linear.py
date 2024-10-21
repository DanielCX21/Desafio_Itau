import numpy as np
import matplotlib.pyplot as plt
import dados
import interpolador

colors = [
    "red", "blue", "green", "yellow", "purple", "orange", "pink", "brown", "black", "white",
    "gray", "cyan", "magenta", "lime", "maroon", "navy", "olive", "teal", "violet", "indigo",
    "gold", "silver", "beige", "coral", "crimson", "darkblue", "darkgreen", "darkred", "lightblue", "lightgreen"
]

medo = dados.medo
datas = dados.data

timeframe = int(input("Qual será o timeframe: "))

if timeframe < 3:
    print("Não")

else:
    y_interpolar = list()
    x_interpolar = list(range(1,timeframe + 1))
    coefs_angular = list()
    coefs_linear = list()

    for i in range(len(datas) - timeframe + 1):
        for j in range(timeframe):
            y_interpolar.append(medo[i+j])
        angular = float(np.polyfit(x_interpolar,y_interpolar,1)[0])
        linear = float(np.polyfit(x_interpolar,y_interpolar,1)[1])
        coefs_linear.append(linear)
        coefs_angular.append(angular)
        y_interpolar.clear()

    angulos = list()

    for coef in coefs_angular:
        informacao = float(np.fabs(np.degrees(np.arctan(coef))))
        angulos.append(informacao)

    eixo_x = list()
    eixo_y = list()

    print(angulos)

    for a in range(timeframe):
        for i in range(int((len(datas) - timeframe) / 4)):
            for j in range(1,(timeframe + 1)):
                y = interpolador.reta(coefs_angular[i * 4 + a],coefs_linear[i * 4 + a],j)
                eixo_y.append(y)
                eixo_x.append(4 * i + j)
        plt.plot(eixo_x,eixo_y,color=colors[a])
        eixo_y.clear()
        eixo_x.clear()

    plt.grid(True)
    plt.show()
