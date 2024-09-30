import numpy as np

def gauss_elimination(A):
    n = A.shape[0]  # Número de linhas (número de equações)
    
    # Eliminação de Gauss para transformar a matriz em triangular superior
    for i in range(n):
        # Verifica se o pivô é zero. Se for, tenta trocar com outra linha.
        if A[i, i] == 0:
            for j in range(i+1, n):
                if A[j, i] != 0:
                    A[[i, j]] = A[[j, i]]  # Troca as linhas
                    print(f"\nMatriz após trocar as linhas {i+1} e {j+1}:\n{A}")
                    break
        
        # Normaliza a linha atual dividindo pelo pivô
        pivot = A[i, i]
        A[i] = A[i] / pivot
        print(f"\nMatriz após normalizar a linha {i+1} (dividir pelo pivô {pivot}):\n{A}")
        
        # Elimina os elementos abaixo do pivô
        for j in range(i+1, n):
            factor = A[j, i]
            A[j] = A[j] - factor * A[i]
            print(f"\nMatriz após eliminar o elemento abaixo do pivô na linha {j+1}:\n{A}")
    
    print("\nMatriz em forma triangular superior:\n", A)
    
    # Substituição retroativa para eliminar termos acima do pivô e transformar em matriz identidade
    for i in range(n-1, -1, -1):  # Começando da última linha
        for j in range(i-1, -1, -1):  # Elimina os termos acima do pivô
            factor = A[j, i]
            A[j] = A[j] - factor * A[i]
            print(f"\nMatriz após eliminar o elemento acima do pivô na linha {j+1}:\n{A}")
    
    print("\nMatriz final (identidade com resultados):\n", A)
    return A

# Exemplo de uso
A = np.array([[0.0, 5.3, -1.8, 3.1],
              [11.9, 0.0, 1.8, 15.0],
              [1.0, -1.0, -1.0, 0.0]])

print("Matriz original aumentada:\n", A)
gauss_elimination(A)


