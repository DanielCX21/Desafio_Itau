import matplotlib.pyplot as plt

import random

import backtest

total = backtest.compras + backtest.vendas

juros_stake = [round(random.uniform(1, 10), 2) for _ in range(len(backtest.dicionario_dados))]

patrimonio_stake = [backtest.patrimonio_inicial]

pos = 0

for i in juros_stake:
    mult = i / (100 * 365)
    mult = 1 + mult
    patrimonio_stake.append(patrimonio_stake[pos] * mult)
    pos += 1

if backtest.patrimonio > patrimonio_stake[-1]:
    print("A estratégia ganhou da pull de USDT")
else:
    print("A estratégia perdeu da pull de USDT")

plt.figure(figsize=(10, 5))
plt.plot(patrimonio_stake, label="StakeUSDT", color="blue")
plt.plot(backtest.patrimonio_contabilizado, label="Estratégia", color="red")
plt.title("Gráfico de comparação")
plt.xlabel("Valor")
plt.ylabel("Tempo")
plt.grid(True)
plt.show()
