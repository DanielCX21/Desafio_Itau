from random import randint
import dados

preco_open = dados.preco_open
preco_close = dados.preco_close
datas = dados.data

tentativas = int(1e2)

patrimonio = 1

patrimonios = list()

translacao = 40

for _ in range(tentativas):
    patrimonio = 1
    i = 0
    while i < len(datas) - translacao:
        numero = randint(1,3)
        if numero == 1:
            #long
            patrimonio = patrimonio * (preco_close[i + translacao] / preco_open[i])
            i += translacao
        else:
            if numero == 2:
                #nada
                pass
            else:
                #short
                patrimonio = ((2 * patrimonio) - ((preco_close[i + translacao] / preco_open[i]) * patrimonio))
                i += translacao
    i += 1
    patrimonios.append(patrimonio)
    
subi = 0
desci = 0
subi_muito = 0
desci_muito = 0
subi_absurdamente = 0
desci_absurdamente = 0

parametro_subida_muita = (1 + 0.2) ** (int(2001/365)) #ganhei mais de 20% ao ano.
parametro_subida_extrema = preco_close[-1] / preco_close[0]
parametro_descida_muita = 1 / parametro_subida_muita
parametro_descida_extrema = 1 / parametro_subida_extrema

i = 0

while i < tentativas:
    if patrimonios[i] >= parametro_subida_extrema:
        subi_absurdamente += 1
    else:
        if patrimonios[i] >= parametro_subida_muita:
            subi_muito += 1
        else:
            if patrimonios[i] >= 1:
                subi += 1
            else:
                if patrimonios[i] < 1:
                    desci += 1
                else:
                    if patrimonios[i] <= parametro_descida_muita:
                        desci_muito += 1
                    else:
                        if patrimonios[i] <= parametro_descida_extrema:
                            desci_absurdamente += 1
    i += 1

print(f"subi:{subi}")
print(f"subi muito:{subi_muito}")
print(f"subi absurdamente:{subi_absurdamente}")
print(f"desci:{desci}")
print(f"desci muito:{desci_muito}")
print(f"desci absurdamente{desci_absurdamente}")
