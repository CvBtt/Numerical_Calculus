import numpy as np
import matplotlib.pyplot as plt

# Define the ODE system
def dxdt(t, x, v):
    return v

def dvdt(t, x, v):
    return 0.5 * x * (1 - 4 * x**2)

# Runge-Kutta 4th order method for system of ODEs
def runge_kutta_4_system(t0, x0, v0, h, t_final):
    t = [t0]
    x = [x0]
    v = [v0]
    
    while t[-1] < t_final:
        t_current = t[-1]
        x_current = x[-1]
        v_current = v[-1]
        
        # Compute k1
        k1x = h * dxdt(t_current, x_current, v_current)
        k1v = h * dvdt(t_current, x_current, v_current)
        
        # Compute k2
        k2x = h * dxdt(t_current + h/2, x_current + k1x/2, v_current + k1v/2)
        k2v = h * dvdt(t_current + h/2, x_current + k1x/2, v_current + k1v/2)
        
        # Compute k3
        k3x = h * dxdt(t_current + h/2, x_current + k2x/2, v_current + k2v/2)
        k3v = h * dvdt(t_current + h/2, x_current + k2x/2, v_current + k2v/2)
        
        # Compute k4
        k4x = h * dxdt(t_current + h, x_current + k3x, v_current + k3v)
        k4v = h * dvdt(t_current + h, x_current + k3x, v_current + k3v)
        
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
h = 0.01
t_final = 40.0  # Adjusted to capture the dynamics over a sufficient time

# Initial velocities
v0_values = [0.1, 0.25, 0.5]

# Plotting x'(t) vs x(t) for each initial condition
plt.figure(figsize=(10, 6))

for v0 in v0_values:
    t, x, v = runge_kutta_4_system(t0, x0, v0, h, t_final)
    plt.plot(x, v, label=f"x'(0) = {v0}")

plt.xlabel("x(t)")
plt.ylabel("x'(t)")
plt.title("Plot do x'(t) vs x(t) para velocidades iniciais diferentes")
plt.legend()
plt.grid()
plt.show()
