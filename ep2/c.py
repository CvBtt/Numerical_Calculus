import numpy as np

def jacobi_method(A, b, epsilon=1e-3, max_iterations=100):
    n = len(b)
    x = np.zeros(n)  # Solução inicial
    x_new = np.zeros(n)
    
    # Armazena os valores de I1, I2, I3 e o erro
    tabela = []
    
    for k in range(max_iterations):
        for i in range(n):
            sum_j = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - sum_j) / A[i][i]
        
        # Calcular o erro de parada
        error = np.max(np.abs(x_new - x))
        tabela.append([k+1] + list(x_new) + [error])
        
        if error < epsilon:
            break
        
        x = np.copy(x_new)  # Atualizar o valor de x
    
    # Imprimir tabela de iterações
    print(f"\n{'k':<4} {'I1':<10} {'I2':<10} {'I3':<10} {'Erro':<10}")
    print("-" * 40)
    for linha in tabela:
        print(f"{linha[0]:<4} {linha[1]:<10.6f} {linha[2]:<10.6f} {linha[3]:<10.6f} {linha[4]:<10.6f}")
    
    return x_new

# Sistema linear após permutar as linhas
A = np.array([[11.9, 0.0, 1.8],  # Linha 2 agora é a primeira
              [0.0, 5.3, -1.8],  # Linha 1 agora é a segunda
              [1.0, -1.0, -1.0]])  # Linha 3 continua

b = np.array([15.0, 3.1, 0.0])  # Termos independentes

# Chamar o método de Jacobi
solucao = jacobi_method(A, b)
print("\nSolução final: ", solucao)
