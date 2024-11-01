import numpy as np

# Configuração do gerador congruente linear
a = 1103515245
c = 12345
m = 2147483647
Z0 = 11302272  # Coloque aqui seu número USP como semente

# Gerador de números aleatórios linear congruente
def linear_congruential_generator(n, Z0):
    Z = Z0
    random_numbers = []
    for _ in range(n):
        Z = (a * Z + c) % m
        random_numbers.append(Z / m)
    return np.array(random_numbers)

# Função da parábola
def parabola(x):
    return 1 - x**2

# Área usando Monte Carlo
def monte_carlo_area(trials, points_per_trial, Z0):
    areas = []
    for _ in range(trials):
        x_random = linear_congruential_generator(points_per_trial, Z0)
        y_random = linear_congruential_generator(points_per_trial, Z0)
        inside_curve = np.sum(y_random < parabola(x_random))
        area_estimate = inside_curve / points_per_trial
        areas.append(area_estimate)
    return np.mean(areas), np.std(areas), np.std(areas) / np.sqrt(trials)

# Tabela de resultados
trials_values = [2**n for n in range(1, 18)]
results = []

for trials in trials_values:
    mean_area, std_dev, std_error = monte_carlo_area(trials, 100, Z0)
    results.append((trials, mean_area, std_dev, std_error))

# Impressão dos resultados
print("Nt\tIm\tσ\tσm")
for trials, Im, sigma, sigma_m in results:
    print(f"{trials}\t{Im:.5f}\t{sigma:.5f}\t{sigma_m:.5f}")
