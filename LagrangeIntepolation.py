import numpy as np
import matplotlib.pyplot as plt

# Definindo o polinômio interpolante P(x)
def P(x):
    return (1/4)*(-17*x**3 + 34*x**2 + 49*x - 46)

# Gerando valores de x para a plotagem
x_values = np.linspace(-2, 4, 400)
y_values = P(x_values)

# Pontos fornecidos
points_x = [-1, 1, 2, 3]
points_y = [-11, 5, 13, -13]

# Criando a figura e os eixos
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label='Polinômio P(x)', color='blue')

# Marcando os pontos fornecidos
plt.plot(points_x, points_y, 'ro', label='Pontos fornecidos')

# Adicionando detalhes ao gráfico
plt.title('Polinômio Interpolante de Lagrange')
plt.xlabel('x')
plt.ylabel('P(x)')
plt.legend()
plt.grid(True)

# Mostrando o gráfico
plt.show()
