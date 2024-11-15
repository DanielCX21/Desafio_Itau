import matplotlib.pyplot as plt
from datetime import datetime

# Dados de exemplo
datas = [
    datetime(2024, 1, 1), datetime(2024, 1, 2), datetime(2024, 1, 3),
    datetime(2024, 1, 4), datetime(2024, 1, 5), datetime(2024, 1, 6),
    datetime(2024, 1, 7), datetime(2024, 1, 8), datetime(2024, 1, 9),
    datetime(2024, 1, 10)
]
valores = [10, 15, 7, 8, 20, 18, 25, 30, 12, 22]

# Especificar datas a serem exibidas no eixo X
datas_especificas = [
    datetime(2024, 1, 1), datetime(2024, 1, 5), datetime(2024, 1, 10)
]

# Criando o gráfico
plt.figure(figsize=(10, 5))
plt.plot(datas, valores, marker='o')

# Configurando os ticks do eixo X
plt.xticks(datas_especificas, rotation=45)  # Exibe apenas as datas específicas com rotação

# Rotulando e exibindo
plt.xlabel("Datas")
plt.ylabel("Valores")
plt.title("Gráfico com datas específicas no eixo X")
plt.grid()
plt.show()
