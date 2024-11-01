import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import trapezoid

# Constantes
g = 9.81  # Gravidade (m/s²)
l = 1.0   # Comprimento do pêndulo (m)

# Função a ser integrada para o período do pêndulo
def pendulum_integrand(phi, k):
    return 1 / np.sqrt(1 - k**2 * np.sin(phi)**2)

# Calculo do período para diferentes ângulos iniciais θ0
theta0_values = np.linspace(0, np.pi, 10)
T_Galileu = 2 * np.pi * np.sqrt(l / g)
T_values = []

for theta0 in theta0_values:
    k_squared = (1 - np.cos(theta0)) / 2
    phi_values = np.linspace(0, np.pi / 2, 1000)
    integral_value = trapezoid(pendulum_integrand(phi_values, np.sqrt(k_squared)), phi_values)
    T = 4 * np.sqrt(l / g) * integral_value
    T_values.append(T / T_Galileu)

# Tabela de resultados e gráfico
plt.plot(theta0_values, T_values)
plt.xlabel(r"$\theta_0$ (radianos)")
plt.ylabel(r"$T / T_{Galileu}$")
plt.title("Razão do Período do Pêndulo em Função de θ0")
plt.show()
