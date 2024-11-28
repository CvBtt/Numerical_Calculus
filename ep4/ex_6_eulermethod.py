import numpy as np
import pandas as pd

# Parâmetros do sistema de Lorenz
sigma = 10
beta = 8 / 3
rho = 28

# Condições iniciais
x0, y0, z0 = 1, 1, 1  # Valores iniciais
t0, tf = 0, 2         # Intervalo de tempo
h = 0.01              # Passo de integração

# Funções derivadas
def lorenz_derivatives(x, y, z):
    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - beta * z
    return dx, dy, dz

# Método de Euler
def euler_lorenz(x0, y0, z0, t0, tf, h):
    t_values = np.arange(t0, tf + h, h)
    n = len(t_values)
    
    # Inicializar arrays para x, y, z
    x = np.zeros(n)
    y = np.zeros(n)
    z = np.zeros(n)
    
    # Condições iniciais
    x[0], y[0], z[0] = x0, y0, z0
    
    # Iteração do método de Euler
    for i in range(1, n):
        dx, dy, dz = lorenz_derivatives(x[i-1], y[i-1], z[i-1])
        x[i] = x[i-1] + h * dx
        y[i] = y[i-1] + h * dy
        z[i] = z[i-1] + h * dz
    
    # Retornar os valores calculados
    return t_values, x, y, z

# Resolvendo o sistema com o método de Euler
t, x, y, z = euler_lorenz(x0, y0, z0, t0, tf, h)

# Exibindo os resultados em formato de tabela
data = pd.DataFrame({'t': t, 'x': x, 'y': y, 'z': z})
print(data)
