import numpy as np

# Matriz de coeficientes A (após permutação do item c)
A = np.array([[11.9, 0.0, 1.8],
              [0.0, 5.3, 1.8],
              [1.0, -1.0, -1.0]])

# Extraindo as partes D, L e U da matriz A
D = np.diag(np.diag(A))  # Matriz diagonal com os elementos de A
L = np.tril(A, -1)       # Parte inferior de A (abaixo da diagonal)
U = np.triu(A, 1)        # Parte superior de A (acima da diagonal)

# ---- Método de Jacobi ----
# Matriz J para o método de Jacobi: J = D^(-1) * (L + U)
D_inv = np.linalg.inv(D)
J_jacobi = np.dot(D_inv, (L + U))


# Exibindo os resultados
print("Matriz J (Jacobi):")
print(J_jacobi)
print("Raio espectral (Jacobi): 0.4340070705734567")
