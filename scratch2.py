import matplotlib.pyplot as plt

# Exemplo de dados (substitua pelos seus dados reais)
datas = [1, 2, 3, 4, 5, 6, 7]
valores = [100, 105, 102, 110, 108, 112, 115]
datas_especificas = [2, 5]

# Criar o gráfico
plt.plot(datas, valores, color="lightgreen", linewidth=3)

# Adiciona linhas limitadas para destacar os pontos de interesse
for data in datas_especificas:
    if data in datas:
        # Encontrar o índice da data e o valor correspondente
        idx = datas.index(data)
        y_value = valores[idx]
        
        # Linha vertical até o ponto
        plt.plot([data, data], [0, y_value], color="red", linestyle="--", linewidth=1.5)
        
        # Linha horizontal até o ponto
        plt.plot([0, data], [y_value, y_value], color="red", linestyle="--", linewidth=1.5)
        
        # Destacar o ponto no gráfico
        plt.scatter(data, y_value, color="black", zorder=5)
        plt.text(data, y_value, f"({data}, {y_value})", fontsize=10, color="black")

# Configurações dos eixos e exibição
plt.xticks(datas, rotation=45)
plt.ylabel('SOL/USD', fontsize=16)
plt.title("Gráfico com destaques em pontos específicos")
plt.show()
