import math
import sys

def max_factorial(precision='double'):
    if precision == 'float':
        max_value = 3.4e38  # Máximo para precisão simples
    elif precision == 'double':
        max_value = 1.8e308  # Máximo para precisão dupla
    else:
        raise ValueError("A precisão deve ser 'float' ou 'double'.")

    ln_max_value = math.log(max_value)
    ln_factorial = 0
    n = 1

    while True:
        ln_factorial += math.log(n)
        if ln_factorial > ln_max_value:
            break
        n += 1

    return n - 1  # Subtrair 1 porque o último incremento causou o overflow

# Calculando para precisão simples
max_n_float = max_factorial('float')
print(f"O maior n para precisão simples (float) é: {max_n_float}")

# Calculando para precisão dupla
max_n_double = max_factorial('double')
print(f"O maior n para precisão dupla (double) é: {max_n_double}")
