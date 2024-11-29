import numpy as np
import matplotlib.pyplot as plt

def g(t, y, z):
    return z

def f(t, y, z):
    return -y + t**3 - 3*t**2 + 7*t + 1

def euler(t0, y0, z0, h, t_final):
    t = [np.float32(t0)]
    y = [np.float32(y0)]
    z = [np.float32(z0)]
    
    while t[-1] < t_final:
        t_proximo = np.float32(t[-1] + h)
        y_proximo = np.float32(y[-1] + h * g(t[-1], y[-1], z[-1]))
        z_proximo = np.float32(z[-1] + h * f(t[-1], y[-1], z[-1]))
        
        t.append(t_proximo)
        y.append(y_proximo)
        z.append(z_proximo)
    
    return np.array(t, dtype=np.float32), np.array(y, dtype=np.float32), np.array(z, dtype=np.float32)

def runge_kutta_4(t0, y0, z0, h, t_final):
    t = [np.float32(t0)]
    y = [np.float32(y0)]
    z = [np.float32(z0)]
    
    while t[-1] < t_final:
        t_atual = t[-1]
        y_atual = y[-1]
        z_atual = z[-1]
        
        k1y = np.float32(h * g(t_atual, y_atual, z_atual))
        k1z = np.float32(h * f(t_atual, y_atual, z_atual))
        
        k2y = np.float32(h * g(t_atual + h/2, y_atual + k1y/2, z_atual + k1z/2))
        k2z = np.float32(h * f(t_atual + h/2, y_atual + k1y/2, z_atual + k1z/2))
        
        k3y = np.float32(h * g(t_atual + h/2, y_atual + k2y/2, z_atual + k2z/2))
        k3z = np.float32(h * f(t_atual + h/2, y_atual + k2y/2, z_atual + k2z/2))
        
        k4y = np.float32(h * g(t_atual + h, y_atual + k3y, z_atual + k3z))
        k4z = np.float32(h * f(t_atual + h, y_atual + k3y, z_atual + k3z))
        
        y_proximo = np.float32(y_atual + (k1y + 2*k2y + 2*k3y + k4y) / 6)
        z_proximo = np.float32(z_atual + (k1z + 2*k2z + 2*k3z + k4z) / 6)
        t_proximo = np.float32(t_atual + h)
        
        t.append(t_proximo)
        y.append(y_proximo)
        z.append(z_proximo)
    
    return np.array(t, dtype=np.float32), np.array(y, dtype=np.float32), np.array(z, dtype=np.float32)

def analytical_solution(t):
    return np.float32(t**3 - t)

t0 = np.float32(0)
y0 = np.float32(0)
z0 = np.float32(-1)
h = np.float32(0.01)
t_final = np.float32(5)

t_euler, y_euler, z_euler = euler(t0, y0, z0, h, t_final)

t_rk4, y_rk4, z_rk4 = runge_kutta_4(t0, y0, z0, h, t_final)

# Solução analítica
t_exact = np.linspace(t0, t_final, 1000, dtype=np.float32)
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
print(f"Valor de y(5) usando Euler (double precision): {y_euler[-1]:.8f}")
print(f"Valor de y'(5) usando Euler (double precision): {z_euler[-1]:.8f}")
print(f"Valor de y(5) usando RK4 (double precision): {y_rk4[-1]:.8f}")
print(f"Valor de y'(5) usando RK4 (double precision): {z_rk4[-1]:.8f}")
print(f"Valor exato de y(5) (double precision): {analytical_solution(np.float32(5)):.8f}")
