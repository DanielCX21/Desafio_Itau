def gerar_sinal_compra(candle):
    if candle['close'] < candle['open'] * 0.95:
        return 1
    else: 
        return 0
    
def gerar_sinal_venda(candle):
    if candle['close'] > candle['open'] * 1.05:
        return -1
    else:
        return 0
    
def compra(patrimonio, candle, sinal):
    if sinal == 1:
        quantidade = patrimonio / candle['open']
        return quantidade
    else:
        pass


