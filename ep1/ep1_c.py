import numpy as np
import matplotlib.pyplot as plt

pd.options.display.float_format = '{:.8f}'.format
# Constantes fornecidas
e = 1.602176634e-19  # Carga do elétron (Coulombs)
epsilon_0 = 8.854187817e-12  # Permissividade do vácuo (F/m)
V0 = 1.38e3  # eV
r0 = 0.328  # Angstroms

# Convertendo e^2 / 4πε₀ para eV*Å
constante = e**2 / (4 * np.pi * epsilon_0) * 1e10 / e

# Função de potencial V(r)
def V(r):
    return -constante / r + V0 * np.exp(-r / r0)

# Função de força F(r) = -dV/dr
def F(r):
    return constante / r**2 - V0 / r0 * np.exp(-r / r0)

# Valores de r para plotar
r_values = np.linspace(0.1, 1.5, 400)

# Plotando V(r) e F(r)
plt.figure(figsize=(14, 6))

# Gráfico de V(r)
plt.subplot(1, 2, 1)
plt.plot(r_values, V(r_values), label="V(r)")
plt.xlabel("r (Å)")
plt.ylabel("V(r) (eV)")
plt.title("Potencial V(r) vs r")
plt.legend()

# Gráfico de F(r)
plt.subplot(1, 2, 2)
plt.plot(r_values, F(r_values), label="F(r)", color="orange")
plt.axhline(0, color='black', linewidth=0.5)
plt.xlabel("r (Å)")
plt.ylabel("F(r) (eV/Å)")
plt.title("Força F(r) vs r")
plt.legend()

plt.tight_layout()
plt.show()

# Método das Secantes para encontrar r_eq onde F(r) = 0
def secante(f, r0, r1, tol=1e-5, max_iter=100):
    for _ in range(max_iter):
        f_r0 = f(r0)
        f_r1 = f(r1)
        r2 = r1 - f_r1 * (r1 - r0) / (f_r1 - f_r0)
        if abs(r2 - r1) < tol:
            return r2
        r0, r1 = r1, r2
    return r1

# Encontrando o ponto de equilíbrio r_eq
r_eq = secante(F, 0.3, 0.5)  # Chutes iniciais
print(f"O valor de r_eq encontrado é: {r_eq:.8f} Å")
