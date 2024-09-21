import numpy as np
from scipy.interpolate import CubicSpline
from analise_BTC import medo_BTC

x_pontos = np.arange(1,2002,dtype=int)
y_pontos = np.array(medo_BTC)
tamanho = len(medo_BTC)
#print(len(medo_BTC)) = 2001

cs_ex = CubicSpline(x_pontos,y_pontos)
x_suave = np.linspace(x_pontos[0],x_pontos[-1], tamanho * 100)
cs_deriv = cs_ex.derivative()
cs_seg_deriv = cs_deriv.derivative()
y_seg_deriv = cs_seg_deriv(x_suave)

coeficientes_seg_deriv = cs_seg_deriv.c

pontos_inflexao_x = list()

#y = b + a(x - (i + 1))
#y = (b - a) + ax
#x = (a - b) / a
for i in range(coeficientes_seg_deriv.shape[1] - 1950):
    print(f"Intervalo [{i},{i + 1}]")
    print(f"Coeficiente de x: {coeficientes_seg_deriv[0, i]}") #a
    print(f"Coeficiente independente: {coeficientes_seg_deriv[1, i]}") #b  
    print(y_seg_deriv[i * 100])
