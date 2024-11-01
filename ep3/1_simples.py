import numpy as np
import matplotlib.pyplot as plt
def integrand(x):
    return 6 - 6 * x **5
# Método de Simpson
def simpson_integration(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    return h / 3 * (y[0] + 4 * sum(y[1:-1:2]) + 2 * sum(y[2:-2:2]) + y[-1])
# Valor analítico da integral
I_analytical = 5 
# Valores para a tabela e cálculo de erro
p_values = range(1, 26)
errors_single = []
print("p\tN\tI\tErro")
for p in p_values:
    N = 2**p
    I_num_single = np.float32(simpson_integration(integrand, 0, 1, N))
    errors_single.append(abs(I_num_single - I_analytical))
    print(f"{p}\t{N}\t{I_num_single:.8f}\t{errors_single[-1]:.7f}")