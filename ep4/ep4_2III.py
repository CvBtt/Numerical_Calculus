import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
from numba import njit

# Define the ODE system functions using Numba
@njit
def dxdt(t, x, v):
    return v

@njit
def dvdt(t, x, v, F):
    return -0.25 * v + 0.5 * x * (1 - 4 * x**2) + F * np.cos(t)

# RK4 step function optimized with Numba
@njit
def rk4_step_numba(ti, xi, vi, h, F):
    k1x = h * dxdt(ti, xi, vi)
    k1v = h * dvdt(ti, xi, vi, F)
    
    k2x = h * dxdt(ti + h/2, xi + k1x/2, vi + k1v/2)
    k2v = h * dvdt(ti + h/2, xi + k1x/2, vi + k1v/2, F)
    
    k3x = h * dxdt(ti + h/2, xi + k2x/2, vi + k2v/2)
    k3v = h * dvdt(ti + h/2, xi + k2x/2, vi + k2v/2, F)
    
    k4x = h * dxdt(ti + h, xi + k3x, vi + k3v)
    k4v = h * dvdt(ti + h, xi + k3x, vi + k3v, F)
    
    xi_next = xi + (k1x + 2*k2x + 2*k3x + k4x) / 6
    vi_next = vi + (k1v + 2*k2v + 2*k3v + k4v) / 6
    ti_next = ti + h
    
    return ti_next, xi_next, vi_next

# Function to perform simulation
def simulate_system(F, h_transient, transient_steps, h_main, steps_per_period, num_periods, x0, v0):
    # Initial conditions
    ti = 0.0
    xi = x0
    vi = v0
    
    # Transient evolution
    h = h_transient
    for _ in tqdm(range(transient_steps), desc="Transient Evolution"):
        ti, xi, vi = rk4_step_numba(ti, xi, vi, h, F)
    
    # Arrays to store results
    xi_values = np.empty(num_periods)
    vi_values = np.empty(num_periods)
    
    # Main evolution
    h = h_main
    for i in tqdm(range(num_periods), desc="Main Evolution"):
        # Evolve for one period (steps_per_period steps)
        for _ in range(steps_per_period):
            ti, xi, vi = rk4_step_numba(ti, xi, vi, h, F)
        # Record xi and vi at the end of each period
        xi_values[i] = xi
        vi_values[i] = vi
        # Optional: Print the values (if needed)
        # print(f"Period {i+1}, x = {xi}, v = {vi}")
    
    return xi_values, vi_values

# Parameters
omega = 1.0
T = 2 * np.pi / omega

# Transient evolution parameters
h_transient = 0.01 * T  # h = 0.01 * 2π/ω
transient_steps = 100000  # Number of steps for transient evolution

# Main evolution parameters
h_main = 0.001 * T      # h = 0.001 * 2π/ω
steps_per_period = int(T / h_main)  # Should be 1000 steps per period
num_periods = 20000     # i from 1 to 20000

# Initial conditions
x0 = -0.5
v0 = 0.5

# Fixed F value
F = 0.26

# Run the simulation
xi_values, vi_values = simulate_system(F, h_transient, transient_steps, h_main, steps_per_period, num_periods, x0, v0)

# Plotting x'(t) vs x(t)
plt.figure(figsize=(10, 6))
plt.scatter(xi_values, vi_values, s=0.1, color='blue')
plt.xlabel('x(t)')
plt.ylabel('x\'(t)')
plt.title(f'Phase Space Plot for F = {F}')
plt.grid(True)
plt.show()
