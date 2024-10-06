#vai avaliar volume, reg, medo!
#assim preciso tratar esses dados em 
#um arquivo final de backtest!
from math import fabs

def gera_sinal_venda(ang, vol1, vol2, media, medo, parametro):
    peso = 0
    if fabs(ang) < 10 and medo > 15:
        peso += 20
    elif fabs(ang) < 20 and medo > 15:
        peso += 15
    elif fabs(ang) < 30 and medo > 15:
        peso += 10
    
    if vol1 > (media * 1.5):
        peso += 20
    elif vol1 > (media * 1.4):
        peso += 15
    elif vol1 > (media * 1.3):
        peso += 10

    if vol2 > (media * 1.5):
        peso += parametro 
    elif vol2 > (media * 1.4):
        peso += parametro * (2/3)
    elif vol2 > (media * 1.3):
        peso += parametro * (1/3)

    return peso

def gera_sinal_compra(ang, vol1, vol2, media, medo, parametro):
    peso = 0
    if fabs(ang) < 10 and medo < -15:
        peso += parametro
    elif fabs(ang) < 20 and medo < -15:
        peso += parametro * (2/3)
    elif fabs(ang) < 30 and medo < -15:
        peso += parametro * (1/3)
    
    if vol1 > (media * 1.5):
        peso += parametro 
    elif vol1 > (media * 1.4):
        peso += parametro * (2/3)
    elif vol1 > (media * 1.3):
        peso += parametro * (1/3)

    if vol2 > (media * 1.5):
        peso += parametro 
    elif vol2 > (media * 1.4):
        peso += parametro * (2/3)
    elif vol2 > (media * 1.3):
        peso += parametro * (1/3)

    return peso
