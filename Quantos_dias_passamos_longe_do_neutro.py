from analise_BTC import medo_BTC
from math import fabs

quantidade = len(medo_BTC)
ganancia = 0
medos = 0
neutro = 0
extremo_medo = 0
extrema_ganancia = 0

for medo in medo_BTC:
    if medo > 0:
        if medo > 20:
            extrema_ganancia += 1
        if medo > 5:
            ganancia += 1
    if medo < 0:
        if medo < -25:
            extremo_medo += 1
        if medo < -5:
            medos += 1
    if medo == 0:
        neutro += 1

print("Passamos {} dias, cerca de {:.2f} % do tempo fora da neutralidade, sendo {} dias na ganancia e {} dias no medo".format(quantidade,(quantidade/2001)*100,ganancia,medos))
print("Passamos {} dias em neutro: (50) -> {:.2f}% do tempo!".format(neutro, ((neutro/len(medo_BTC)*100))))
print("Passamos {} dias em extremo medo".format(extremo_medo))
print("Passamos {} dias em extrema ganancia".format(extrema_ganancia))
