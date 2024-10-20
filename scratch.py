import matplotlib.pyplot as plt

colors = ["red", "blue", "pink", "purple"]

x = [1,2,3]
y = [1,2,3]

for i in range(2):
    x = [1,2,3]
    y = [1 + i*i,2 + 2*i*i,3 + 3*i*i]
    plt.plot(x, y, color=colors[i])

# Exibir o gráfico
plt.show()
