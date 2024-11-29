import numpy as np
import matplotlib.pyplot as plt

# Define the ODE system
def dxdt(t, x, v):
    return v

def dvdt(t, x, v, gamma):
    return -2 * gamma * v + 0.5 * x * (1 - 4 * x**2)

# Runge-Kutta 4th order method for system of ODEs with damping
def runge_kutta_4_system(t0, x0, v0, h, t_final, gamma):
    t = [t0]
    x = [x0]
    v = [v0]
    
    while t[-1] < t_final:
        t_current = t[-1]
        x_current = x[-1]
        v_current = v[-1]
        
        # Compute k1
        k1x = h * dxdt(t_current, x_current, v_current)
        k1v = h * dvdt(t_current, x_current, v_current, gamma)
        
        # Compute k2
        k2x = h * dxdt(t_current + h/2, x_current + k1x/2, v_current + k1v/2)
        k2v = h * dvdt(t_current + h/2, x_current + k1x/2, v_current + k1v/2, gamma)
        
        # Compute k3
        k3x = h * dxdt(t_current + h/2, x_current + k2x/2, v_current + k2v/2)
        k3v = h * dvdt(t_current + h/2, x_current + k2x/2, v_current + k2v/2, gamma)
        
        # Compute k4
        k4x = h * dxdt(t_current + h, x_current + k3x, v_current + k3v)
        k4v = h * dvdt(t_current + h, x_current + k3x, v_current + k3v, gamma)
        
        # Update x and v
        x_next = x_current + (k1x + 2*k2x + 2*k3x + k4x)/6
        v_next = v_current + (k1v + 2*k2v + 2*k3v + k4v)/6
        t_next = t_current + h
        
        t.append(t_next)
        x.append(x_next)
        v.append(v_next)
        
    return np.array(t), np.array(x), np.array(v)

# Parameters
t0 = 0.0
x0 = -0.5
v0 = 0.5
h = 0.01
t_final = 20.0  # Adjust as needed to capture the dynamics

# Damping coefficients
gamma_values = [0.125, 0.4]  # Corresponding to 2*gamma = 0.25 and 0.8

# Plotting x'(t) vs x(t) for each damping coefficient
plt.figure(figsize=(10, 6))

for gamma in gamma_values:
    t, x, v = runge_kutta_4_system(t0, x0, v0, h, t_final, gamma)
    label = f"2γ = {2*gamma}"
    plt.plot(x, v, label=label)

plt.xlabel("x(t)")
plt.ylabel("x'(t)")
plt.title("Plot of x'(t) vs x(t) for different damping coefficients")
plt.legend()
plt.grid()
plt.show()
