import numpy as np
import matplotlib.pyplot as plt

# Funções g(t, y, z) e f(t, y, z) com precisão dupla
def g(t, y, z):
    return z

def f(t, y, z):
    return -y + t**3 - 3*t**2 + 7*t + 1

# Método de Euler com precisão dupla
def euler(t0, y0, z0, h, t_final):
    t = [np.float64(t0)]
    y = [np.float64(y0)]
    z = [np.float64(z0)]
    
    while t[-1] < t_final:
        t_next = np.float64(t[-1] + h)
        y_next = np.float64(y[-1] + h * g(t[-1], y[-1], z[-1]))
        z_next = np.float64(z[-1] + h * f(t[-1], y[-1], z[-1]))
        
        t.append(t_next)
        y.append(y_next)
        z.append(z_next)
    
    return np.array(t, dtype=np.float64), np.array(y, dtype=np.float64), np.array(z, dtype=np.float64)

# Método RK4 com precisão dupla
def runge_kutta_4(t0, y0, z0, h, t_final):
    t = [np.float64(t0)]
    y = [np.float64(y0)]
    z = [np.float64(z0)]
    
    while t[-1] < t_final:
        t_current = t[-1]
        y_current = y[-1]
        z_current = z[-1]
        
        k1y = np.float64(h * g(t_current, y_current, z_current))
        k1z = np.float64(h * f(t_current, y_current, z_current))
        
        k2y = np.float64(h * g(t_current + h/2, y_current + k1y/2, z_current + k1z/2))
        k2z = np.float64(h * f(t_current + h/2, y_current + k1y/2, z_current + k1z/2))
        
        k3y = np.float64(h * g(t_current + h/2, y_current + k2y/2, z_current + k2z/2))
        k3z = np.float64(h * f(t_current + h/2, y_current + k2y/2, z_current + k2z/2))
        
        k4y = np.float64(h * g(t_current + h, y_current + k3y, z_current + k3z))
        k4z = np.float64(h * f(t_current + h, y_current + k3y, z_current + k3z))
        
        y_next = np.float64(y_current + (k1y + 2*k2y + 2*k3y + k4y) / 6)
        z_next = np.float64(z_current + (k1z + 2*k2z + 2*k3z + k4z) / 6)
        t_next = np.float64(t_current + h)
        
        t.append(t_next)
        y.append(y_next)
        z.append(z_next)
    
    return np.array(t, dtype=np.float64), np.array(y, dtype=np.float64), np.array(z, dtype=np.float64)

# Solução analítica com precisão dupla
def analytical_solution(t):
    return np.float64(t**3 - t)

# Parâmetros
t0 = np.float64(0)
y0 = np.float64(0)
z0 = np.float64(-1)
h = np.float64(0.01)
t_final = np.float64(5)

# Resolvendo com Euler
t_euler, y_euler, z_euler = euler(t0, y0, z0, h, t_final)
#print(t_euler, y_euler, z_euler)

# Resolvendo com RK4
t_rk4, y_rk4, z_rk4 = runge_kutta_4(t0, y0, z0, h, t_final)
#print(t_rk4, y_rk4, z_rk4)

# Solução analítica
t_exact = np.linspace(t0, t_final, 1000, dtype=np.float64)
y_exact = analytical_solution(t_exact)
#print(t_exact, y_exact)

# Plotando os resultados
plt.figure(figsize=(10, 6))
plt.plot(t_exact, y_exact, label="Solução Analítica", linestyle="--")
plt.plot(t_euler, y_euler, label="Euler", marker="o", markersize=2, linestyle="-")
plt.plot(t_rk4, y_rk4, label="Runge-Kutta 4ª ordem", marker="s", markersize=2, linestyle="-")
plt.xlabel("t")
plt.ylabel("y(t)")
plt.title("Solução da EDO: Comparação dos Métodos (Double Precision)")
plt.legend()
plt.grid()
plt.show()

# Valores finais
print(f"Valor de y(5) usando Euler (double precision): {y_euler[-1]:.15f}")
print(f"Valor de y'(5) usando Euler (double precision): {z_euler[-1]:.15f}")
print(f"Valor de y(5) usando RK4 (double precision): {y_rk4[-1]:.15f}")
print(f"Valor de y'(5) usando RK4 (double precision): {z_rk4[-1]:.15f}")
print(f"Valor exato de y(5) (double precision): {analytical_solution(np.float64(5)):.15f}")
