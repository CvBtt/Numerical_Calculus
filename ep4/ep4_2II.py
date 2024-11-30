import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
from numba import njit, prange

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

# Function to perform simulation per F value
@njit
def simulate_for_F(F, h_transient, transient_steps, h_main, steps_per_period, num_periods, x0, v0):
    # Initial conditions
    ti = 0.0
    xi = x0
    vi = v0
    
    # Transient evolution
    h = h_transient
    for _ in range(transient_steps):
        ti, xi, vi = rk4_step_numba(ti, xi, vi, h, F)
    
    # Arrays to store results
    xi_values = np.empty(num_periods)
    
    # Main evolution
    h = h_main
    for i in range(num_periods):
        # Evolve for one period (steps_per_period steps)
        for _ in range(steps_per_period):
            ti, xi, vi = rk4_step_numba(ti, xi, vi, h, F)
        # Record xi at the end of each period
        xi_values[i] = xi
    
    return xi_values

# Parameters
omega = 1.0
T = 2 * np.pi / omega

# Transient evolution parameters
h_transient = 0.01 * T  # h = 0.01 * 2π/ω
transient_steps = 200000  # Reduced from 200,000 to 100,000

# Main evolution parameters
h_main = 0.001 * T      # h = 0.001 * 2π/ω
steps_per_period = int(T / h_main)  # Should be 1000 steps per period
num_periods = 100        # Reduced from 100 to 50

# Initial conditions
x0 = -0.5
v0 = 0.5

# F values from 0 to 0.35 with step ∆F = 0.0005 (increased from 0.00025)
delta_F = 0.00025
F_values = np.arange(0, 0.35 + delta_F, delta_F)
N_F = len(F_values)

# Preallocate arrays for results
F_list = []
x_poincare_list = []

# Loop over F values (can be parallelized with Numba's prange)
for idx in tqdm(range(N_F), desc="Computing Poincaré sections"):
    F = F_values[idx]
    xi_values = simulate_for_F(F, h_transient, transient_steps, h_main, steps_per_period, num_periods, x0, v0)
    F_list.extend([F] * num_periods)
    x_poincare_list.extend(xi_values)

# Convert lists to arrays
F_list = np.array(F_list)
x_poincare_list = np.array(x_poincare_list)

# Plot the bifurcation diagram
plt.figure(figsize=(12, 8))
plt.scatter(F_list, x_poincare_list, s=0.1, color='black')
plt.xlabel('F')
plt.ylabel('x at Poincaré sections')
plt.title('Diagrama de Bifurcação')
plt.grid(True)
plt.show()