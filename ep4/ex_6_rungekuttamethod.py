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

# Método de Runge-Kutta Clássico de quarta ordem
def runge_kutta_lorenz(x0, y0, z0, t0, tf, h):
    t_values = np.arange(t0, tf + h, h)
    n = len(t_values)
    
    # Inicializar arrays para x, y, z
    x = np.zeros(n)
    y = np.zeros(n)
    z = np.zeros(n)
    
    # Condições iniciais
    x[0], y[0], z[0] = x0, y0, z0
    
    # Iteração do método de Runge-Kutta
    for i in range(1, n):
        # k1
        k1_x, k1_y, k1_z = lorenz_derivatives(x[i-1], y[i-1], z[i-1])
        
        # k2
        k2_x, k2_y, k2_z = lorenz_derivatives(
            x[i-1] + h * k1_x / 2, 
            y[i-1] + h * k1_y / 2, 
            z[i-1] + h * k1_z / 2
        )
        
        # k3
        k3_x, k3_y, k3_z = lorenz_derivatives(
            x[i-1] + h * k2_x / 2, 
            y[i-1] + h * k2_y / 2, 
            z[i-1] + h * k2_z / 2
        )
        
        # k4
        k4_x, k4_y, k4_z = lorenz_derivatives(
            x[i-1] + h * k3_x, 
            y[i-1] + h * k3_y, 
            z[i-1] + h * k3_z
        )
        
        # Atualização
        x[i] = x[i-1] + h * (k1_x + 2 * k2_x + 2 * k3_x + k4_x) / 6
        y[i] = y[i-1] + h * (k1_y + 2 * k2_y + 2 * k3_y + k4_y) / 6
        z[i] = z[i-1] + h * (k1_z + 2 * k2_z + 2 * k3_z + k4_z) / 6
    
    # Retornar os valores calculados
    return t_values, x, y, z

# Resolvendo o sistema com o método de Runge-Kutta
t, x, y, z = runge_kutta_lorenz(x0, y0, z0, t0, tf, h)

# Exibindo os resultados em formato de tabela
data = pd.DataFrame({'t': t, 'x': x, 'y': y, 'z': z})
print(data)
