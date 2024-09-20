import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
from analise_BTC import medo_BTC
from scipy.optimize import fsolve

x_pontos = np.arange(1,2002,dtype=int)
y_pontos = np.array(medo_BTC)
tamanho = len(medo_BTC)

#print(len(medo_BTC)) = 2001

cs_ex = CubicSpline(x_pontos,y_pontos)

x_suave = np.linspace(x_pontos[0],x_pontos[-1], tamanho * 100)
y_suave = cs_ex(x_suave)

cs_deriv = cs_ex.derivative()
cs_seg_deriv = cs_deriv.derivative()

y_deriv = cs_deriv(x_suave)
y_seg_deriv = cs_seg_deriv(x_suave)

pontos_criticos_x = fsolve(cs_deriv, x_suave)
pontos_criticos_y = cs_ex(pontos_criticos_x)

pontos_inflexao_x = fsolve(cs_seg_deriv, x_suave)
pontos_inflexao_y = cs_ex(pontos_inflexao_x)

#plt.subplot(1, 2, 1)
plt.plot(x_pontos, y_pontos, 'o', color='red', label='Pontos Originais')
plt.plot(x_suave, y_suave, color='blue', label='Cubic Spline')
plt.scatter(pontos_criticos_x, pontos_criticos_y, color='orange')
#plt.subplot(1, 2, 2)
plt.plot(x_suave, y_deriv, color='green', label='Derivada da Spline')
plt.scatter(pontos_inflexao_x, pontos_inflexao_y, color='purple')
plt.grid()
plt.tight_layout()
plt.show()

for i in range(len(x_pontos) - 1):
    print(f"Coefs {i}: {cs_ex.c[:,i]}")
