import numpy as np
import matplotlib.pyplot as plt

# Definindo a função g(x) para o caso b)
def g_b(x):
    return np.sqrt(3 * x - 2)

# Gerando valores de x dentro do domínio válido
x_values = np.linspace(0.67, 3, 400)  # Começa em 2/3
g_values = g_b(x_values)

# Plotando y = g(x) e y = x
plt.figure(figsize=(8, 6))
plt.plot(x_values, g_values, label='g(x) = sqrt(3x - 2)', color='blue')
plt.plot(x_values, x_values, label='y = x', color='red', linestyle='--')

# Destacando o ponto fixo x = 2
plt.plot(2, 2, 'go', label='Ponto fixo x = 2')

# Configurações do gráfico
plt.title('Gráfico de Convergência para o Caso b)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
