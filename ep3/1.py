import numpy as np
import matplotlib.pyplot as plt

# Função a ser integrada
def integrand(x):
    return 6 - 6 * x ** 5

# Método de Simpson
def simpson_integration(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    return h / 3 * (y[0] + 4 * sum(y[1:-1:2]) + 2 * sum(y[2:-2:2]) + y[-1])

# Valor analítico da integral
I_analytical = 6 - 6 / 6  # Integral conhecida: 5

# Valores para a tabela e cálculo de erro
p_values = range(1, 26)
errors_single = []
errors_double = []

print("p\tN\tI\tErro")
for p in p_values:
    N = 2**p
    I_num_single = np.float32(simpson_integration(integrand, 0, 1, N))
    I_num_double = simpson_integration(integrand, 0, 1, N)
    errors_single.append(abs(I_num_single - I_analytical))
    errors_double.append(abs(I_num_double - I_analytical))
    print(f"{p}\t{N}\t{I_num_double}\t{errors_double[-1]}")

# Substitui valores zero por um valor muito pequeno para evitar log(0)
errors_single = [err if err != 0 else 1e-16 for err in errors_single]
errors_double = [err if err != 0 else 1e-16 for err in errors_double]

# Gráfico log2(erro) vs p com ajustes para visualização
plt.plot(p_values, np.log2(errors_single), label="Precisão Simples", marker='o')
plt.plot(p_values, np.log2(errors_double), label="Precisão Dupla", marker='x')
plt.xlabel("p")
plt.ylabel("log2(erro)")
plt.legend()
plt.title("Erro no Método de Simpson (Precisão Simples e Dupla)")
plt.grid(True)
plt.ylim(bottom=-30)  # Ajusta o limite inferior do eixo y para garantir visibilidade
plt.show()
