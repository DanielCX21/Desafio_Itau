import numpy as np
from analise_BTC import volume_from_BTC, volume_to_BTC, data_BTC
import matplotlib.pyplot as plt

dias = 0
media_from_dado = list()
media_to_dado = list()
media_to = 0
media_from = 0
contador_to = 0
contador_from = 0

periodo = 20

for i, data in enumerate(data_BTC):
    dias += 1
    if dias < periodo:
        pass
    else:
        for j in range(periodo):
            media_from += volume_from_BTC[i - j]
            media_to += volume_to_BTC[i - j]
        media_to = media_to / 20
        media_from = media_from / 20
        media_from_dado.append(media_from)
        media_to_dado.append(media_to)
        media_to = 0
        media_from = 0
        
'''
        if volume_from_BTC[i] > media_from_dado[i-20] * 1.25:
            print(f"Em {data} o volume_from foi maior 25% que a média")
            contador_from += 1
        if volume_to_BTC[i] > media_to_dado[i-20] * 1.25:
            print(f"Em {data} o volume_to foi 25% maior que a média")
            contador_to += 1

print(f"Dias que o volume from ficou 25% acima: {contador_from}")
print(f"Dias que o volume to ficou 25% acima: {contador_to}")
'''

'''
#plotando o gráfico para volume from
x_media = list(range(20,len(volume_from_BTC) + 1))
y_media = media_from_dado
x = list(range(len(data_BTC)))
y = volume_from_BTC
plt.plot(x,y,color='red')
plt.plot(x_media,y_media,color='blue')
plt.show()
'''

'''
#plotando o gráfico para volume to
x_media = list(range(50,len(volume_to_BTC) + 1))
y_media = media_to_dado
x = list(range(len(data_BTC)))
y = volume_to_BTC
plt.plot(x,y,color='red')
plt.plot(x_media,y_media,color='blue')
plt.show()
'''