import numpy as np
import matplotlib.pyplot as plt

# Definindo a função g(x) para o caso a)
def g_a(x):
    return (x**2 + 2) / 3

# Gerando valores de x dentro do intervalo de interesse
x_values = np.linspace(-2, 2, 400)
g_values = g_a(x_values)

# Plotando y = g(x) e y = x
plt.figure(figsize=(8, 6))
plt.plot(x_values, g_values, label='g(x) = (x² + 2)/3', color='blue')
plt.plot(x_values, x_values, label='y = x', color='red', linestyle='--')

# Destacando o ponto fixo x = 1
plt.plot(1, 1, 'go', label='Ponto fixo x = 1')

# Configurações do gráfico
plt.title('Gráfico de Convergência para o Caso a)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
