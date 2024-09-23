from analise_BTC import medo_BTC
from math import fabs

quantidade = 0
ganancia = 0
medos = 0
neutro = 0

for medo in medo_BTC:
    if fabs(medo) > 5:
        quantidade += 1
        if medo > 0:
            ganancia += 1
        else:
            medos += 1
    else:
        if medo == 0:
            neutro += 1

print("Passamos {} dias, cerca de {:.2f} % do tempo fora da neutralidade, sendo {} dias na ganancia e {} dias no medo".format(quantidade,(quantidade/2001)*100,ganancia,medos))
print("Passamos {} dias em neutro: (50) -> {:.2f}% do tempo!".format(neutro, ((neutro/len(medo_BTC)*100))))
